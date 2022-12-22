from flask import Blueprint, request, send_from_directory, redirect
from flask_cors import CORS
import os
from sqlalchemy import update

from bdd import Session
from middlewares import auth
from flask_uploads import UploadSet, ALL
from models.Accounts import Accounts

profile = Blueprint('profile', __name__)
session = Session()

CORS(profile, supports_credentials=True)

BASE_URL = '/api/'

images = UploadSet('images', ALL)


@profile.get(BASE_URL + '/profile')
def get_informations():
    try:
        # On récupère l'utilisateur
        user = auth.authenticate(request)
        # On retourne nom et prénom de l'utilisateur
        return {'email': user.email, 'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name}
    except Exception as e:
        return {'message': str(e)}, 500


@profile.get(BASE_URL + '/profile/picture')
def picture():
    try:
        # On récupère l'utilisateur
        user = auth.authenticate(request)
        # On récupère la liste des fichiers contenu dans le dossier images
        files = os.listdir('static/images/profile')
        # On récupère le nom de l'image de l'utilisateur
        image_name = [file for file in files if file.split('.')[0] == user.username]
        if image_name:
            # On retourne l'image
            return send_from_directory('static/images/profile', image_name[0])
        else:
            # On retourne l'image par défaut
            return send_from_directory('static/images/profile', 'default_photo.jpg')
    except Exception as e:
        print(e)
        return {'message': str(e)}, 500

@profile.patch(BASE_URL + '/profile')
def modify_profile():
    try:
        user = auth.authenticate(request)
        #image = request.files['file']
        body = request.form
        username = body['username']
        profile = session.query(Accounts).filter_by(username=user.username).first()
        profile.username = username 
        session.add(profile)
        session.commit()
        return {'message': 'change done'}
    except Exception as e:
        return {'message': str(e)}, 500

@profile.patch(BASE_URL + '/personnal_info')
def modify_info():
    try:
        user = auth.authenticate(request)
        body = request.form
        first_name = body['first_name']
        last_name = body['last_name']
        profile = session.query(Accounts).filter_by(username=user.username).first()
        profile.first_name = first_name
        profile.last_name = last_name 
        session.add(profile)
        session.commit()
        return {'message': 'change done'}
    except Exception as e:
        return {'message': str(e)}, 500
    