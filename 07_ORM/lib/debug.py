#!/usr/bin/env python3

from owner import Owner, CONN as owner_conn, CURSOR as owner_cursor
from pet import Pet, CONN as pet_conn, CURSOR as pet_cursor
from vet import Veterinarian, CONN as vet_conn, CURSOR as vet_cursor
from datetime import datetime
# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()
Veterinarian.drop_table(vet_conn, vet_cursor)
Veterinarian.create_table()
matteo = Veterinarian.create("Matteo", "Immunology", "San Diego")
# Veterinarian.find_by("name", "Matteo")
Pet.drop_table(pet_conn, pet_cursor)
Pet.create_table()
spot = Pet.create("spot", "dog", "chihuahua", "feisty", matteo.id, datetime.now())
lily = Pet.create("lily", "dog", "pit bull", "feisty", None, datetime.now())

import ipdb; ipdb.set_trace()
