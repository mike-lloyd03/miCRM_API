from flask import json
from flask_restful import Resource

from app.models import Contact

class ContactResource(Resource):
    def get(self):
        # return 'yup'
        return {'data': str(Contact.query.all())}

    def post(self):
