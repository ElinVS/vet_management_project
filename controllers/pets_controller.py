
from flask import Blueprint, redirect, render_template, request

from models.pet import Pet
from repositories import pet_repository
from repositories import owner_repository
from repositories import vet_repository
from repositories import note_repository

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
    vet_id = request.form['vet_id']
    owner= owner_repository.select(owner_id)
    vet=vet_repository.select(vet_id)
    pet= Pet(name, species, dob, owner,vet,id)
    pet_repository.save(pet)
    return redirect('/pets/view_all')

@pets_blueprint.route('/pets/view_all')
def view_all_pets():
    pets = pet_repository.select_all()
    owners = owner_repository.select_all()
    return render_template('/pets/view_all.html', all_pets=pets, owners=owners)

@pets_blueprint.route('/pets/<id>', methods=['GET'])
def view_selected_pet(id):
    pet = pet_repository.select(id)
    owner = owner_repository.select(id)
    pets = owner_repository.select_pets_of_owner(owner)
    notes = note_repository.filter_notes_by_pet(pet)
    return render_template('/pets/view_selected.html', pet=pet, owner=owner, pets=pets, notes=notes)

@pets_blueprint.route('/pets/<id>/edit')
def edit_form(id):
    pet = pet_repository.select(id)
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template('/pets/edit_pet.html', pet=pet, owners=owners, vets=vets)

@pets_blueprint.route('/pets/<id>',methods=['POST'])
def update_pet_details(id):
    name = request.form['name']
    species = request.form['species']
    dob = str(request.form['dob'])
    owner_id = request.form['owner_id']
    vet_id=request.form['vet_id']
    owner= owner_repository.select(owner_id)
    vet=vet_repository.select(vet_id)
    update_pet = Pet(name, species, dob, owner, vet, id)
    pet_repository.update(update_pet)
    return redirect(f'/pets/{id}')

@pets_blueprint.route('/pets/<id>/delete', methods=['POST'])
def delete_pet(id):
     pet_repository.delete(id)
     return redirect('/pets/view_all')





