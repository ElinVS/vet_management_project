from flask import Blueprint, Flask, redirect, render_template, request

from models.note import Note
from models.pet import Pet
from models.owner import Owner
from models.vet import Vet
from repositories import pet_repository
from repositories import owner_repository
from repositories import vet_repository

notes_blueprint = Blueprint("notes",__name__)