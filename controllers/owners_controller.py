
from flask import Blueprint, Flask, render_template, request

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
    return render_template('/pets/register_pet.html')


# @owners_blueprint.route('/')
# def owners():
#     owners = owner_repository.select_all()
#     return render_template('index.html')



