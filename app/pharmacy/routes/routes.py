from app.pharmacy import blp as pharmacy_blp
from flask.views import MethodView
from flask_smorest import abort
from app.schemas import *
from app import db

@pharmacy_blp.route("/")
class AllDrugInventory(MethodView):
    def get(self):
        pass

    def put(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass


@pharmacy_blp.route("/drug/<string:drug_ndc>")
class AllDrugInventory(MethodView):
    def get(self):
        pass

    def put(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass