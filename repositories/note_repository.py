from db.run_sql import run_sql
from models.note import Note
from models.pet import Pet

import repositories.pet_repository as pet_repository


def save(note):
    sql = "INSERT INTO notes (note, pet_id) VALUES (%s,%s) RETURNING id"
    values = [note.note, note.pet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    note.id = id


def filter_notes_by_pet(pet):
    notes = []

    sql = "SELECT notes.* FROM notes INNER JOIN pets on notes.pet_id = pets.id WHERE pets.id = %s"
    values = [pet.id]
    results = run_sql(sql,values)

    for result in results:
        pet = pet_repository.select(result["pet_id"])

        note_object = Note(result['note'],pet, result['id'])
        notes.append(note_object)

    return reversed(notes)

    

