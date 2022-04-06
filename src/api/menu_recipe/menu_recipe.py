from flask import Blueprint
from flask import jsonify, request

from src.api.menu_recipe.menu_recipe_service import get_menu_recipe, get_menu_by_id, insert_menu_recipe_by_id, \
    delete_menu_recipe_by_id, update_menu_recipe_by_id

menu_recipe_routes = Blueprint(name="menu-recipe", import_name=__name__)


@menu_recipe_routes.route('/<menu_recipe_id>', methods=["GET"])
def get_menu_recipe_id(menu_recipe_id):
    values = get_menu_recipe(menu_recipe_id)
    return jsonify(values)


@menu_recipe_routes.route('/<menu_id>/recipes', methods=["GET"])
def get_recipe_from_menu(menu_id):
    values = get_menu_by_id(menu_id)
    return jsonify(values)


@menu_recipe_routes.route('/', methods=["POST"])
def create_menu_recipe_route():
    data = request.get_json()
    menu_id = data.get("menu_id")
    recipe_id = data.get("recipe_id")
    result = insert_menu_recipe_by_id(menu_id, recipe_id)
    return jsonify(result)


@menu_recipe_routes.route('/', methods=["PUT"])
def update_menu_recipe():
    data = request.get_json()
    recipe_id = data.get("recipe_id")
    menu_id_ = data.get("menu_id")
    result = update_menu_recipe_by_id(recipe_id, menu_id_)
    return jsonify(result)


@menu_recipe_routes.route('/<menu_recipe_id>', methods=["DELETE"])
def delete_menu_recipe(menu_recipe_id):
    values = delete_menu_recipe_by_id(menu_recipe_id)
    return jsonify(values)
