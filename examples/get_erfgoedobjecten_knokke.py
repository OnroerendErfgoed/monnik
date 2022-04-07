# -*- coding: utf-8 -*-

from monnik.core import get_collection

INVENTARIS_URL = 'https://inventaris.onroerenderfgoed.be'
ERFGOEDOBJECTEN_URL = INVENTARIS_URL + '/erfgoedobjecten'

knokke = get_collection(
    ERFGOEDOBJECTEN_URL,
    {
        'gemeente': 31043,
        'deelgemeente': '31043A'
    }
)

for eob in knokke:
    print(f'* {eob["id"]}: {eob["naam"]}')
    print(f'  {eob["locatie_samenvatting"]}')
