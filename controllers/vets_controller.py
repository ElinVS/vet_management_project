from flask import Blueprint, Flask, redirect, render_template, request, redirect

from models.pet import Pet
from models.owner import Owner
from models.vet import Vet
from repositories import pet_repository
from repositories import owner_repository
from repositories import vet_repository


vets_blueprint = Blueprint("vets", __name__)


@vets_blueprint.route('/vets')
def vets_page():
    return render_template('vets/view.html')

@vets_blueprint.route('/vets/register_vet')
def register_vet_form():
    return render_template('vets/register_vet.html')

@vets_blueprint.route('/vets/veterinarians')
def view_veterinarians():
    vets = vet_repository.select_all()
    return render_template('/vets/veterinarians.html', vets=vets)

@vets_blueprint.route("/vets/veterinarians", methods=['POST'])
def register_new_vet():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    speciality = request.form['speciality']
    vet_object = Vet(first_name, last_name,speciality)
    vet_repository.save(vet_object)
    return redirect('/vets/veterinarians')

@vets_blueprint.route('/vets/<id>', methods=['GET'])
def view_selected_vet(id):
    
    vet = vet_repository.select(id)
    print(vet)
    pets = vet_repository.select_pets_of_vet(vet)
    print(pets)
    return render_template('/vets/view_selected.html', vet=vet,pets=pets)


