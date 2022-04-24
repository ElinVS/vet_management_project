from db.run_sql import run_sql
from models.owner import Owner

def save(owner):
    sql = "INSERT INTO owners (first_name) VALUES (%s) RETURNING id"
    values = [owner.first_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id


def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)