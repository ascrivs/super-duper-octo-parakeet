from app.pharmacy import blp as pharmacy_blp
from flask.views import MethodView
from flask_smorest import abort
from app.schemas import *
from app import db

@pharmacy_blp.route("/")
class DrugInventory(MethodView):
    def get(self):
        pass

    def put(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass