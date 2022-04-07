# -*- coding: utf-8 -*-
'''
This module provides utilities for doing requests.
'''

import requests

import logging
log = logging.getLogger(__name__)

from .uri import is_uri

RETRY_ATTEMPTS = 5
TIMEOUT = 10

def get_resource(url, SSO=None, session=None):
    '''
    Get a single resource. Any object that is represented by a single url,
    without extra parameters.

    :param str url: The url of the resource
    :param str SSO: An OpenAm SSO key
    :param requests.Session session: A session that can be reused.
    :return: Returns a dictionary with data or False if the resource could not
    be reached
    :rtype: dict
    :raises Exception: if the url could not be reached
    :raises ValueError: if the url parameter is not a valid url
    '''

    if not is_uri(url):
        raise ValueError(
            f'{url} is not a valid url'
        )

    if not session:
        session = requests.Session()

    headers = {
        'Accept': 'application/json'
    }
    if SSO:
        headers['OpenAmSSOID'] = SSO

    for i in range(RETRY_ATTEMPTS):  # Try up to RETRY_ATTEMPTS times to get the URI
        # Retry scenarios are: connection errors, timeouts, 5xx status codes
        try:
            response = session.get(url, headers=headers, timeout=TIMEOUT)
            if response.ok:
                return response.json()
            if 400 <= response.status_code < 500:
                return False
            else:
                log.error(
                    f"Problem fetching {url}: "
                    f"{response.status_code} - {response.text}"
                )
        except RequestException as e:
            log.error(
                f"Problem fetching {url}: {e}"
            )
    else:  # When the loop exited without a break, all retries used.
        raise Exception(f'Tried to reach {url} {RETRY_ATTEMPT} times, but failed.')

def get_collection(url, parameters, SSO = None, session=None):
    '''
    Fetch all data from a url until there are no more `next` urls in the Link
    header.

    :param str url: The url of the collecion
    :param dict parameters: A dict of query string parameters
    :param str SSO: An OpenAm SSO key
    :return: Returns a list of resources that form the collection
    :rtype: lst
    '''

    if not session:
        session = requests.Session()

    data = []

    headers = {
        'Accept': 'application/json'
    }
    if SSO:
        headers['OpenAmSSOID'] = SSO

    def _do_query(url, params, headers):
        for i in range(RETRY_ATTEMPTS):  # Try up to RETRY_ATTEMPTS times to get the URI
            # Retry scenarios are: connection errors, timeouts, 5xx status codes
            try:
                response = session.get(url, params=params, headers=headers, timeout=TIMEOUT)
                if response.ok:
                    return response
                if 400 <= response.status_code < 500:
                    log.error(
                        f"Client error, please check your query: "
                        f"{response.status_code} - {response.text}"
                    )
                    # No point in retrying
                    raise Exception(f'Could not exceute query: {response.status_code} - {response.text}')
                else:
                    log.error(
                        f"Problem fetching {url}: "
                        f"{response.status_code} - {response.text}"
                    )
            except RequestException as e:
                log.error(
                    f"Problem fetching {url}: {e}"
                )
        else:  # When the loop exited without a break, all retries used.
            raise Exception(f'Tried to reach {url} {RETRY_ATTEMPT} times, but failed.')

    res = _do_query(url, parameters, headers)

    total = None
    if res.status_code == requests.codes.ok:
        if 'Content-Range' in res.headers:
            total = res.headers['Content-Range'].split('/')[-1]
        else:
            total = 0
        log.debug(f'Planning to get {total} results', total)

    if not total:
        log.info('No results found')
        return []
    else:
        data.extend(res.json())

    while 'next' in res.links:
        res = _do_query(res.links['next']['url'], params={}, headers=headers)
        data.extend(res.json())

    return data
