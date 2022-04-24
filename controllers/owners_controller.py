from flask import Blueprint, Flask

from models.owner import Owner


owners_blueprint = Blueprint("owners", __name__)