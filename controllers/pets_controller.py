
from flask import Blueprint, Flask, render_template, request

from models.pet import Pet
from models.owner import Owner
from models.vet import Vet
from repositories import pet_repository
from repositories import owner_repository
from repositories import vet_repository


pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route('/pets/register_pet')
def register_new_pet_form():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template('/pets/register_pet.html', owners=owners, vets=vets)


@pets_blueprint.route("/pets/view_all", methods=['POST'])
def register_new_pet():
    name = request.form['name']
    species = request.form['species']
    dob = str(request.form['dob'])
    owner_id = request.form['owner_id']
    owners = owner_repository.select_all()
    owner= owner_repository.select(owner_id)
    pet= Pet(name, species, dob, owner, treatment_notes=False)
    pet_repository.save(pet)
    return render_template('/pets/view_all.html', owners=owners )


@pets_blueprint.route('/pets/view_all')
def view_all_pets():
    pets = pet_repository.select_all()
    owners = owner_repository.select_all()
    return render_template('/pets/view_all.html', all_pets=pets, owners=owners)

@pets_blueprint.route('/pets/<id>', methods=['POST'])
def view_selected_pet(id):
    pet = pet_repository.select(id)
    return render_template('/pets/view_selected.html', pet=pet)

