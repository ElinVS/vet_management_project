from db.run_sql import run_sql
from models.pet import Pet
from models.owner import Owner
from models.vet import Vet

import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository



def save(pet):
    sql = "INSERT INTO pets (name, species, dob, owner_id, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.species, pet.dob, pet.owner.id, pet.treatment_notes, pet.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id


def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for result in results:
        owner = owner_repository.select(result["owner_id"])
        vet = vet_repository.select(result["vet_id"])
        pet = Pet(result["name"], result["species"],result["dob"], owner, result["treatment_notes"],vet, result["id"])
        pets.append(pet)
    return pets

def select(id):
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    owner = owner_repository.select(result["owner_id"])
    vet = vet_repository.select(result["vet_id"])
    pet = Pet(result["name"], result["species"],result["dob"], owner, result["treatment_notes"],vet, result["id"])
    return pet


def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(pet):
    sql = "UPDATE pets SET (name, species, dob, owner_id, treatment_notes, vet_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.species, pet.dob, pet.owner.id, pet.treatment_notes, pet.vet.id, pet.id]
    run_sql(sql, values)


# def save_notes():
#     sql = 
