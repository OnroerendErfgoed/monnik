# -*- coding: utf-8 -*-

from monnik.core import get_resource

EINDVERSLAG_URI = 'https://id.erfgoed.net/archeologie/eindverslagen/1814'

mal_ade_staats = get_resource(
    EINDVERSLAG_URI
)

print(mal_ade_staats)
