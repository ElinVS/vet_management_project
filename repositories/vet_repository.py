from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet

import repositories.owner_repository as owner_repository

def save(vet):
    sql = "INSERT INTO vets (first_name, last_name, speciality) VALUES (%s, %s, %s) RETURNING id"
    values = [vet.first_name, vet.last_name, vet.speciality]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id

def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for result in results:
        vet = Vet(result["first_name"], result["last_name"],result["speciality"],result["id"])
        vets.append(vet)
    return vets

def select(id):
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    vet = Vet(result["first_name"], result["last_name"], result["speciality"],result["id"])
    return vet


def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(vet):
    sql = "UPDATE vets SET (first_name, last_name, speciality) = (%s, %s, %s)  WHERE id = %s"
    values = [vet.first_name, vet.last_name, vet.speciality, vet.id]
    run_sql(sql, values)


def select_pets_of_vet(vet):
    pets = []
    sql = "SELECT pets.* FROM pets INNER JOIN vets ON pets.vet_id = vets.id WHERE vets.id= %s"
    values = [vet.id]
    results = run_sql(sql, values)

    for result in results:
        owner = owner_repository.select(result["owner_id"])
       
        
        pet_object = Pet(result['name'], result['species'], result['dob'], owner, vet, result['id'])
        pets.append(pet_object)
    return pets



