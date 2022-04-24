from db.run_sql import run_sql
from models.pet import Pet
from models.owner import Owner

import repositories.owner_repository as owner_repository

def save(pet):
    sql = "INSERT INTO pets (name, species, dob,owner_id, treatment_notes) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.species, pet.dob, pet.owner.id, pet.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id