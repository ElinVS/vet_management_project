from db.run_sql import run_sql
from models.pet import Pet
from models.owner import Owner

import repositories.owner_repository as owner_repository

def save(pet):
    sql = "INSERT INTO pets (name, species, dob, owner_id, treatment_notes) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.species, pet.dob, pet.owner.id, pet.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id


def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for result in results:
        owner = owner_repository.select(result["owner_id"])
        pet = Pet(result["name"], result["species"],result["dob"], owner, result["treatment_notes"], result["id"])
        pets.append(pet)
    return pets

def select(id):
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    owner = owner_repository.select(result["owner_id"])
    pet = Pet(result["name"], result["species"],result["dob"], owner, result["treatment_notes"], result["id"])
    return pet


def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(pet):
    sql = "UPDATE pets SET (name, species, dob, owner_id, treatment_notes) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.species, pet.dob, pet.owner.id, pet.treatment_notes, pet.id]
    run_sql(sql, values)