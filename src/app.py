from flask import Flask

from src.api.ingredients.ingredients import ingredients_routes
from src.api.menu.menu import weekly_menu_routes
from src.api.menu_recipe.menu_recipe import menu_recipe_routes
from src.api.recipes.recipe import recipe_routes
from src.api.recipe_ingredient.route import  recipe_ingredient_routes
from src.middleware.authentication import Authentication


def register_blueprints(app_):
    app_.register_blueprint(recipe_routes, url_prefix="/recipes")
    app_.register_blueprint(weekly_menu_routes, url_prefix="/weeklymenu")
    app_.register_blueprint(menu_recipe_routes, url_prefix="/menu-recipe")
    app_.register_blueprint(ingredients_routes, url_prefix="/ingredients")
    app_.register_blueprint(recipe_ingredient_routes, url_prefix="/recipe-ingredient")


def create_app():
    app_ = Flask(__name__)
    app_.wsgi_app = Authentication(app_.wsgi_app)
    register_blueprints(app_)
    return app_


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
