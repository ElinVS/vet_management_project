from flask import Blueprint, Flask, redirect, render_template, request

from models.note import Note
from models.pet import Pet
from models.owner import Owner
from models.vet import Vet
from repositories import note_repository
from repositories import pet_repository
from repositories import owner_repository
from repositories import vet_repository

notes_blueprint = Blueprint("notes",__name__)

@notes_blueprint.route('/notes/add_note')
def add_note_form():
    return render_template('notes/add_note.html')

@notes_blueprint.route("/pets/<id>", methods=['POST'])
def add_new_note():
    note = request.form['note']
    pet= pet_repository.select(id)
    new_note = Note(note, pet, id)
    note_repository.save(new_note)
    return redirect(f'/pets/{id}')
