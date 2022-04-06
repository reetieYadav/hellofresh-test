from flask import Blueprint
from flask import jsonify, request

from src.api.menu.menu_service import get_weekly_menu_by_id, insert_weekly_menu_by_id, update_weekly_menu_by_id, delete_weekly_menu_by_id
weekly_menu_routes = Blueprint(name="weeklymenu", import_name=__name__)



@weekly_menu_routes.route('/<menu_id>', methods=["GET"])
def get_weekly_menu_id(menu_id):
    values = get_weekly_menu_by_id(menu_id)
    return jsonify(values)


@weekly_menu_routes.route('/', methods=["POST"])
def create_menu_route():
    data = request.get_json()
    print(data)
    menu_id = data.get("menu_id")
    menu_name = data.get("menu_name")
    result = insert_weekly_menu_by_id(menu_id, menu_name)
    return jsonify(result)


@weekly_menu_routes.route('/', methods=["PUT"])
def update_menu():
    data = request.get_json()
    menu_name = data.get("menu_name")
    menu_id = data.get("menu_id")
    result = update_weekly_menu_by_id(menu_name, menu_id)
    return jsonify(result)


@weekly_menu_routes.route('/<menu_id>', methods=["DELETE"])
def delete_menu(menu_id):
    values = delete_weekly_menu_by_id(menu_id)
    return jsonify(values)


# @weekly_menu_routes.route('/<menu_name>/recipe', methods=["GET"])
# def get_recipe_id_by_menu_recipe_route(menu_name):
#     values = get_recipes_by_menu_name(menu_name)
#     return jsonify(values)
