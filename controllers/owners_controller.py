import re
from flask import Blueprint, Flask, render_template

from models.owner import Owner
from repositories import owner_repository


owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route('/')
def owners():
    owners = owner_repository.select_all()
    return render_template('index.html', owners =owners)