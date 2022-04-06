from flask import Blueprint
from flask import jsonify, request

from src.api.ingredients.ingredients_service import get_all_ingredients, get_ingredient_by_id, insert_ingredient_by_id \
    , delete_ingredient_by_id, update_ingredient_by_id

ingredients_routes = Blueprint(name="ingredients", import_name=__name__)


@ingredients_routes.route('/', methods=["GET"])
def get_all_ingredient_route():
    values = get_all_ingredients()
    return jsonify(values)


@ingredients_routes.route('/', methods=["POST"])
def create_ingredients_route():
    data = request.get_json()
    ingredient_id = data.get("ingredient_id")
    ingredient_name = data.get("ingredient_name")
    values = insert_ingredient_by_id(ingredient_id, ingredient_name)
    return jsonify(values)


@ingredients_routes.route('/', methods=["PUT"])
def update_ingredient_route():
    data = request.get_json()
    ingredient_name = data.get("ingredient_name")
    ingredient_id = data.get("ingredient_id")
    values = update_ingredient_by_id(ingredient_name, ingredient_id)
    return jsonify(values)


@ingredients_routes.route('/<ingredient_id>', methods=["GET"])
def get_ingredient_by_id_route(ingredient_id):
    values = get_ingredient_by_id(ingredient_id)
    return jsonify(values)


@ingredients_routes.route('/<ingredient_id>', methods=["DELETE"])
def delete_ingredient_route(ingredient_id):
    values = delete_ingredient_by_id(ingredient_id)
    return jsonify(values)
