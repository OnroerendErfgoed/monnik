# -*- coding: utf-8 -*-

from monnik.monnik import Monnik

amandus = Monnik()

abdij = amandus.get_erfgoedobject(19148)

print(f'{abdij["id"]}: {abdij["naam"]}')
print(f'{abdij["locatie_samenvatting"]}')
print
print(f'{abdij["korte_beschrijving"]}')
