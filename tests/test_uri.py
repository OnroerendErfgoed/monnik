# -*- coding: utf-8 -*-

from monnik.uri import (
    is_uri,
    get_id
)

class TestIsUri:

    def test_None(self):
        assert not is_uri(None)

    def test_url(self):
        assert is_uri('https://id.erfgoed.net/thesauri/erfgoedtypes/1')
        assert is_uri('https://thesaurus.erfgoed.net/conceptschemes/erfgoedtypes/1')

    def test_urn(self):
        assert is_uri('urn:x-skosprovider:typologie')
        assert is_uri('urn:x-skosprovider:typologie:1')

    def test_get_id(self):
        assert '1' == get_id('https://id.erfgoed.net/thesauri/erfgoedtypes/1')
        assert '1' == get_id('https://thesaurus.erfgoed.net/conceptschemes/erfgoedtypes/1')
        assert 'wortel' == get_id('https://id.erfgoed.net/thesauri/voedseltypes/wortel')
