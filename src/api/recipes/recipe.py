from flask import Blueprint
from flask import jsonify, request

from src.api.recipes.recipeService import delete_recipe_by_id, get_recipe_by_id, insert_recipe_by_id, \
    update_recipe_by_id

recipe_routes = Blueprint(name="recipes", import_name=__name__)


@recipe_routes.route('/<recipe_id>', methods=["GET"])
def get_recipe_route(recipe_id):
    values = get_recipe_by_id(recipe_id)
    return jsonify(values)


@recipe_routes.route('/', methods=["POST"])
def create_recipe_route():
    data = request.get_json()  # json object
    recipe_name = data.get("recipe_name")  # read property from json object
    description = data.get("description")  # read property from json object
    result = insert_recipe_by_id(recipe_name, description)
    return jsonify(result)


@recipe_routes.route('/', methods=["PUT"])
def update_recipe_route():
    data = request.get_json()  # json object
    recipe_name = data.get("recipe_name")  # read property from json object
    _id = data.get("recipe_id")  # read property from json object
    result = update_recipe_by_id(recipe_name, _id)
    return jsonify(result)


@recipe_routes.route('/<recipe_id>', methods=["DELETE"])
def delete_recipe_route(recipe_id):
    # print(recipe_id)
    values = delete_recipe_by_id(recipe_id)
    return jsonify(values)
