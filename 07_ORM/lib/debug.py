#!/usr/bin/env python3

from owner import Owner, CONN as owner_conn, CURSOR as owner_cursor
from pet import Pet, CONN as pet_conn, CURSOR as pet_cursor
from vet import Veterinarian, CONN as vet_conn, CURSOR as vet_cursor

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

Pet.drop_table()
Pet.create_table()
spot = Pet("spot", "dog", "chihuahua", "feisty")
spot.save()

Veterinarian.drop_table()
Veterinarian.create_table()
matteo = Veterinarian("Matteo", "Immunology", "San Diego")
matteo.save()

import ipdb; ipdb.set_trace()
