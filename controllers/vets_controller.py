from flask import Blueprint, redirect, render_template, request, redirect

from models.vet import Vet
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
    pets = vet_repository.select_pets_of_vet(vet)
    return render_template('/vets/view_selected.html', vet=vet,pets=pets)

@vets_blueprint.route('/vets/<id>/edit')
def edit_form(id):
    vet = vet_repository.select(id)
    return render_template('/vets/edit_vet.html', vet=vet)

@vets_blueprint.route('/vets/<id>',methods=['POST'])
def update_vet_details(id):
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    speciality = request.form['speciality']
    
    update_vet = Vet(first_name, last_name, speciality, id)
    vet_repository.update(update_vet)
    return redirect(f'/vets/{id}')

@vets_blueprint.route('/vets/<id>/delete', methods=['POST'])
def delete_vet(id):
     vet_repository.delete(id)
     return redirect('/vets/veterinarians')

