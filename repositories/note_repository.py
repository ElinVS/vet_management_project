from db.run_sql import run_sql
from models.note import Note
from models.pet import Pet


def save(note):
    sql = "INSERT INTO notes (note, pet_id) VALUES (%s,%s) RETURNING id"
    values = [note.note, note.pet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    note.id = id
