from flask_smorest import Blueprint

blp = Blueprint('Pharmacy', __name__, description="Operations on Pharmacy Drug Inventory", url_prefix="/pharmacy")

from app.pharmacy.routes import routes