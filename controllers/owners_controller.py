
from flask import Blueprint, redirect, render_template, request

from models.owner import Owner
from repositories import owner_repository

owners_blueprint = Blueprint("owners", __name__)


@owners_blueprint.route('/owners/register_owner')
def register_new_owner_form():
    return render_template('/owners/register_owner.html')

@owners_blueprint.route("/pets/register_pet", methods=['POST'])
def register_new_owner():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    adress = request.form['adress']
    postcode = request.form['postcode']
    owner_object = Owner(first_name, last_name, email, phone_number, adress, postcode, registered= True)
    owner_repository.save(owner_object)
    return redirect('/pets/register_pet')


@owners_blueprint.route('/owners/<id>/edit/pet/<pet_id>')
def edit_form(id, pet_id):
    owner = owner_repository.select(id)
    return render_template('/owners/edit_owner.html', owner=owner, pet_id = pet_id)


@owners_blueprint.route('/owners/<id>/edit',methods=['POST'])
def update_owner_details(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    adress = request.form['adress']
    postcode = request.form['postcode']
    pet_id = request.form['pet-id']
    registered = True
    update_owner = Owner(first_name, last_name, email,phone_number, adress, postcode, registered, id)
    owner_repository.update(update_owner)
    return redirect(f'/pets/{pet_id}')


@owners_blueprint.route("/owners/<id>/delete", methods=["POST"])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect('/pets/view_all')
