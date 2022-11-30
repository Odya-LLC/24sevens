from flask import Blueprint, jsonify
from app import db
from app.models import Products
api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/ping")
def ping():
    print(db.session.bind)
    return "Pong!"

@api_bp.route("/products")
def products():
    pr = Products.query.all()
    return jsonify([p.to_dict() for p in pr])
