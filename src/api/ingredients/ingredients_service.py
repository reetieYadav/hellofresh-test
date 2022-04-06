from src.core.dal.database import connection


def get_all_ingredients():
    cur = connection.cursor()
    cur.execute(f"select * from ingredients")
    result = cur.fetchall()
    return result


def get_ingredient_by_id(ingredient_id):
    cur = connection.cursor()
    cur.execute(f"select * from ingredients where ingredient_id={ingredient_id}")
    result = cur.fetchall()
    return result


def insert_ingredient_by_id(ingredient_id, ingredient_name):
    cur = connection.cursor()
    cur.execute(
        f"insert into ingredients (ingredient_id, ingredient_name) values{ingredient_id, ingredient_name}")
    result = connection.commit()
    return result


def update_ingredient_by_id(ingredient_name, ingredient_id):
    cur = connection.cursor()
    cur.execute(f"update ingredients set ingredient_name='{ingredient_name}' where ingredient_id={ingredient_id}")
    result = connection.commit()
    return result


def delete_ingredient_by_id(ingredient_id):
    cur = connection.cursor()
    cur.execute(f"delete from ingredients where ingredient_id={ingredient_id}")
    result = connection.commit()
    return result
