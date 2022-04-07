# -*- coding: utf-8 -*-

from monnik.core import (
    get_resource
)

import pytest

class TestGetResource:

    def test_invalid_url_none(self):
        with pytest.raises(ValueError):
            get_resource(None)

    def test_invalid_url_id(self):
        with pytest.raises(ValueError):
            get_resource(5)

    def test_invalid_url_str(self):
        with pytest.raises(ValueError):
            get_resource('vijf')
