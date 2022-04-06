from flask import Blueprint
from flask import jsonify, request

from src.api.recipe_ingredient.service import get_all_recipe_ingredients, get_ingredient_id_from_recipe, insert_recipe_ingredient_by_id, \
    delete_recipe_ingredient_by_id

recipe_ingredient_routes = Blueprint(name="recipe-ingredient", import_name=__name__)


@recipe_ingredient_routes.route('/', methods=["GET"])
def get_ingredient_route():
    values = get_all_recipe_ingredients()
    return jsonify(values)


@recipe_ingredient_routes.route('/<recipe_id>/ingredient', methods=["GET"])
def get_ingredient_from_recipe(recipe_id):
    values = get_ingredient_id_from_recipe(recipe_id)
    return jsonify(values)


@recipe_ingredient_routes.route('/', methods=["POST"])
def create_recipe_ingredient_route():
    data = request.get_json()
    print(data)
    recipe_id = data.get("recipe_id")
    ingredient_id = data.get("ingredient_id")
    result = insert_recipe_ingredient_by_id(recipe_id, ingredient_id)
    return jsonify(result)


@recipe_ingredient_routes.route('/', methods=["PUT"])
def update_recipe_ingredient():
    data = request.get_json()
    recipe_id = data.get("recipe_id")
    ingredient_id = data.get("ingredient_id")
    result = insert_recipe_ingredient_by_id(recipe_id, ingredient_id)
    return jsonify(result)


@recipe_ingredient_routes.route('/<recipe_ingredient_id>', methods=["DELETE"])
def delete_recipe_ingredient(recipe_ingredient_id):
    values = delete_recipe_ingredient_by_id(recipe_ingredient_id)
    return jsonify(values)

