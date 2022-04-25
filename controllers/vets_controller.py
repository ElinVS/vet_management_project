from flask import Blueprint, Flask, render_template, request

from models.pet import Pet
from models.owner import Owner
from models.vet import Vet
from repositories import pet_repository
from repositories import owner_repository
from repositories import vet_repository


vets_blueprint = Blueprint("vets", __name__)