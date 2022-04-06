from src.core.dal.database import connection


def get_all_recipe():
    # Creating a cursor object using the cursor() method
    cur = connection.cursor()
    # execute a statement
    # under execute we write query. it can be multiple.  like --: (query1, query2)
    cur.execute("SELECT * FROM public.users")
    cur.close()
    result = cur.fetchall()
    return result


def get_recipe_by_id(recipe_id):
    cur = connection.cursor()
    cur.execute(f"select * from public.recipes where recipe_id={recipe_id}")
    result = cur.fetchall()
    cur.close()
    return result


def delete_recipe_by_id(recipe_id):
    cur = connection.cursor()
    cur.execute(f"delete from public.recipes where recipe_id={recipe_id}")
    result = connection.commit()
    count = cur.rowcount
    cur.close()
    print(count, "deleted successfully ")
    return result


def update_recipe_by_id(recipe_name, recipe_id):
    cur = connection.cursor()
    sql_update_query = "UPDATE public.recipes SET recipe_name = %s  WHERE recipe_id = %s"
    cur.execute(sql_update_query, (recipe_name, recipe_id))
    result = connection.commit()
    count = cur.rowcount
    cur.close()
    print(count, "Record Updated successfully ")
    return result


def insert_recipe_by_id(recipe_name, description):
    cur = connection.cursor()
    query = f"INSERT INTO public.recipes (recipe_name, description) VALUES{recipe_name, description}"
    cur.execute(query)
    result = connection.commit()
    cur.close()
    return result
