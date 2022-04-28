# -*- coding: utf-8 -*-
'''
This module provides easy access to resources
'''

import logging
log = logging.getLogger(__name__)

import requests

from monnik.core import get_resource

from monnik.uri import is_uri

HOSTS = {
    'uri': 'https://id.erfgoed.net',
    'inventaris': 'https://inventaris.onroerenderfgoed.be'
}

URI_TEMPLATES = {
    'erfgoedobject': HOSTS["uri"] + '/erfgoedobjecten/{identifier}',
    'aanduidingsobject': HOSTS["uri"] + '/aanduidingsobjecten/{identifier}',
    'waarneming': HOSTS["uri"] + '/waarnemingen/{identifier}',
    'thema': HOSTS["uri"] + '/persoon/{identifier}',
    'gebeurtenis': HOSTS["uri"] + '/persoon/{identifier}',
    'persoon': HOSTS["uri"] + '/persoon/{identifier}',
}

URL_TEMPLATES = {
    'erfgoedobject': HOSTS['inventaris'] + '/erfgoedobjecten/{identifier}',
    'aanduidingsobject': HOSTS['inventaris'] + '/aanduidingsobjecten/{identifier}',
    'waarneming': HOSTS['inventaris'] + '/waarnemingen/{identifier}',
    'thema': HOSTS['inventaris'] + '/thema/{identifier}',
    'gebeurtenis': HOSTS['inventaris'] + '/gebeurtenis{identifier}',
    'persoon': HOSTS['inventaris'] + '/persoon/{identifier}',
}

class Monnik:

    session = None

    def __init__(self, session = None):
        if not session:
            session = requests.Session()
        self.session = session

    def _get_resource(self, identifier, resourcetype):
        if not is_uri(identifier):
            identifier = URI_TEMPLATES[resourcetype].format(identifier=identifier)
        return get_resource(identifier, session = self.session)

    def get_erfgoedobject(self, identifier):
        return self._get_resource(identifier, 'erfgoedobject')

    def get_aanduidingsobject(self, identifier):
        return self._get_resource(identifier, 'aanduidingsobject')

    def get_waarneming(self, identifier):
        return self._get_resource(identifier, 'waarneming')

    def get_thema(self, identifier):
        return self._get_resource(identifier, 'thema')

    def get_gebeurtenis(self, identifier):
        return self._get_resource(identifier, 'gebeurtenis')

    def get_persoon(self, identifier):
        return self._get_resource(identifier, 'persoon')
