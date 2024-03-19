# Pet Attributes:
# name: TEXT
# species: TEXT
# breed: TEXT
# temperament: TEXT

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3
from sqlite3 import IntegrityError
from helper import Helper
from datetime import datetime
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect('./resources.db')

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

class Pet(Helper):
    all = {}

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    def __init__(self, name, species, breed, temperament, veterinarian_id, created_at, updated_at=None, id=None):
        self.name, self.species, self.breed, self.temperament, self.veterinarian_id, self.created_at, self.updated_at, self.id = (
            name,
            species,
            breed,
            temperament,
            veterinarian_id,
            created_at, 
            updated_at,
            id,
        )

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist
    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    f"""
                    CREATE TABLE IF NOT EXISTS {cls.pascal_to_camel_plural()} (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        species TEXT,
                        breed TEXT,
                        temperament TEXT,
                        veterinarian_id INTEGER,
                        created_at DATETIME,
                        updated_at DATETIME,
                        FOREIGN KEY (veterinarian_id) REFERENCES veterinarians(id)
                    );
                """
                )
            # CONN.commit()
        except IntegrityError as e:
            # CONN.rollback()
            return e

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
    # @classmethod
    # def drop_table(cls):
    #     try:
    #         with CONN:
    #             CURSOR.execute(
    #                 f"""
    #                     DROP TABLE IF EXISTS {cls.pascal_to_camel_plural()};
    #                 """
    #             )
    #         # CONN.commit()
    #     except Exception as e:
    #         # CONN.rollback()
    #         return e

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB
    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    f"""
                        INSERT INTO {type(self).pascal_to_camel_plural()} 
                        (name, species, breed, temperament, veterinarian_id, created_at) 
                        VALUES 
                        (?, ?, ?, ?, ?, ?);
                    """,
                    (
                        self.name,
                        self.species,
                        self.breed,
                        self.temperament,
                        self.veterinarian_id, 
                        self.created_at,
                    ),
                )
                self.id = CURSOR.lastrowid
                # all[self.id] = self
            # CONN.commit()
        except Exception as e:
            # CONN.rollback()
            return e

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    @classmethod
    def create(cls, name, species, breed, temperament, veterinarian_id, created_at):
        new_pet = cls(name, species, breed, temperament, veterinarian_id, created_at)
        new_pet.save()
        return new_pet

    # ✅ 6. Add "update" Instance Method to Update the db based on its Attributes
    def update(self):
        try:
            with CONN:
                CURSOR.execute(
                    f"""
                        UPDATE {type(self).pascal_to_camel_plural()} 
                        SET name=?, species=?, breed=?, temperament=?, veterinarian_id=?, updated_at=?
                        WHERE 
                        id = ?;
                    """,
                    (
                        self.name,
                        self.species,
                        self.breed,
                        self.temperament,
                        self.veterinarian_id,
                        self.updated_at,
                        self.id,
                    ),
                )
                all[self.id] = self
                return self
            # CONN.commit()
        except Exception as e:
            # CONN.rollback()
            return e
    # ✅ 7. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB
    @classmethod
    def new_from_db(cls, row_of_data):
        return cls(
            row_of_data[1],
            row_of_data[2],
            row_of_data[3],
            row_of_data[4],
            row_of_data[5],
            row_of_data[6],
            row_of_data[7],
            row_of_data[0],
        )

    # ✅ 8. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def get_all(cls):
        try:
            with CONN:
                result = CURSOR.execute(f"SELECT * FROM {cls.pascal_to_camel_plural()}")
                rows = result.fetchall()
                return [cls.new_from_db(row) for row in rows]
        except Exception as e:
            return e
    # ✅ 9. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB

    # If No "pet" Found, return "None"

    # ✅ 10. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

    # If No "pet" Found, return "None"

    # ✅ 11. Add "find_or_create_by" Class Method to:

    #  Find and Retrieve "pet" Instance w/ All Attributes

    # If No "pet" Found, Create New "pet" Instance w/ All Attributes
