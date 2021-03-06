from db.run_sql import run_sql
from models.owner import Owner
from models.pet import Pet

import repositories.vet_repository as vet_repository


def save(owner):
    sql = "INSERT INTO owners (first_name, last_name, email, phone_number, adress, postcode, registered) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [owner.first_name, owner.last_name, owner.email, owner.phone_number, owner.adress, owner.postcode, owner.registered]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id




def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for result in results:
        owner = Owner(result["first_name"], result["last_name"],result["email"], result["phone_number"], result["adress"], result["postcode"], result["registered"],result["id"])
        owners.append(owner)
    return owners

def select(id):
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    owner = Owner(result["first_name"], result["last_name"],result["email"], result["phone_number"], result["adress"], result["postcode"], result["registered"],result["id"])
    return owner


def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(owner):
    sql = "UPDATE owners SET (first_name, last_name, email, phone_number, adress, postcode, registered) = (%s, %s, %s, %s, %s, %s, %s)  WHERE id = %s"
    values = [owner.first_name, owner.last_name, owner.email, owner.phone_number, owner.adress, owner.postcode, owner.registered, owner.id]
    run_sql(sql, values)

def select_pets_of_owner(owner):
    pets = []
    sql = "SELECT pets.* FROM pets INNER JOIN owners ON pets.owner_id = owners.id WHERE owners.id = %s"
    values = [owner.id]
    results = run_sql(sql, values)

    for result in results:
        vet = vet_repository.select(result["vet_id"])
        pet_object = Pet(result['name'], result['species'], result['dob'], owner, vet, result['id'])
        pets.append(pet_object)
    return pets
        
