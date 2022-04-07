# -*- coding: utf-8 -*-
'''
This module provides utilities for working with :term:`URIs <URI>`.
'''

import rfc3987

def is_uri(uri):
    '''
    Check if a string is a valid URI according to rfc3987

    :param string uri:
    :rtype: boolean
    '''
    if uri is None:
        return False
    return rfc3987.match(str(uri), rule='URI')

def get_id(uri):
    '''
    Splits the id from a standard Onroerend Erfgoed :term:`URI`

    :param string uri: A standard Onroerend Erfgoed :term:`URI`
    :rtype: string
    '''
    return uri.split('/')[-1]
