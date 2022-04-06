from src.core.dal.database import connection


def get_all_recipe_ingredients():
    # Creating a cursor object using the cursor() method
    cur = connection.cursor()
    # execute a statement
    # under execute we write query. it can be multiple.  like --: (query1, query2)
    cur.execute("SELECT * FROM recipe_ingredient")
    result = cur.fetchall()
    cur.close()
    return result


def get_ingredient_id_from_recipe(recipe_id):
    cur = connection.cursor()
    cur.execute(f"select ingredient_id from recipe_ingredient where recipe_id = {recipe_id}")
    result = cur.fetchall()
    cur.close()
    return result


def insert_recipe_ingredient_by_id(recipe_id, ingredient_id):
    cur = connection.cursor()
    recipe_ingredient_create_query = f"insert into recipe_ingredient (recipe_id, ingredient_id) values{recipe_id, ingredient_id}"
    cur.execute(recipe_ingredient_create_query)
    result = connection.commit()
    count = cur.rowcount
    print(count, "Record Updated successfully ")
    cur.close()
    return result


def update_recipe_ingredient_by_id(recipe_id, ingredient_id):
    cur = connection.cursor()
    recipe_ingredient_update_query = f"update recipe_ingredient set ingredient_id= %s where recipe_id =%s"
    cur.execute(recipe_ingredient_update_query, (recipe_id, ingredient_id))
    result = connection.commit()
    return result


def delete_recipe_ingredient_by_id(recipe_ingredient_id):
    cur = connection.cursor()
    recipe_ingredient_delete_query = f"delete from recipe_ingredient where recipe_ingredient_id={recipe_ingredient_id}"
    cur.execute(recipe_ingredient_delete_query)
    result = connection.commit()
    return result


def get_recipe_id(recipe_id):
    cur = connection.cursor()
    cur.execute(f"SELECT recipe_id FROM recipe_ingredient WHERE recipe_id='{recipe_id}'")
    result = cur.fetchall()
    return result




