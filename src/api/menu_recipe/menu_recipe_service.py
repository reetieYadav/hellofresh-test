from src.core.dal.database import connection


def get_menu_recipe(menu_recipe_id):
    cur = connection.cursor()
    cur.execute(f"select * from weekly_menu join menu_recipe mr "
                f"on weekly_menu.menu_id = mr.menu_id "
                f"where mr.recipe_id= {menu_recipe_id}")
    result = cur.fetchall()
    return result


def insert_menu_recipe_by_id(menu_id, recipe_id):
    cur = connection.cursor()
    menu_recipe_create_query = f"insert into menu_recipe (menu_id, recipe_id)" \
                               f" values{menu_id, recipe_id}"
    cur.execute(menu_recipe_create_query)
    result = connection.commit()
    cur.close()
    return result


def update_menu_recipe_by_id(recipe_id, menu_id):
    cur = connection.cursor()
    menu_recipe_update_query = f"update menu_recipe set recipe_id= %s where menu_id =%s"
    cur.execute(menu_recipe_update_query, (recipe_id, menu_id))
    result = connection.commit
    return result


def delete_menu_recipe_by_id(menu_recipe_id):
    cur = connection.cursor()
    menu_recipe_delete_query = f"delete from menu_recipe where menu_recipe_id={menu_recipe_id}"
    cur.execute(menu_recipe_delete_query)
    result = connection.commit()
    return result


def get_menu_by_id(menu_id):
    cur = connection.cursor()
    cur.execute(f"select * from recipes r "
                f"where  r.recipe_id in "
                f"(select menu_recipe.recipe_id from menu_recipe where menu_id ={menu_id})")
    result = cur.fetchall()
    return result
