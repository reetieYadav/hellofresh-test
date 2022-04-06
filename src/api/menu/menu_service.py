from src.core.dal.database import connection


def get_weekly_menu_by_id(menu_id):
    cur = connection.cursor()
    cur.execute(f"select * from weekly_menu where menu_id={menu_id}")
    result = cur.fetchall()
    return result


def insert_weekly_menu_by_id(menu_id, menu_name):
    cur = connection.cursor()
    menu_create_query = f"insert into weekly_menu (menu_id, menu_name) values{menu_id, menu_name}"
    print(menu_create_query)
    cur.execute(menu_create_query)
    result = connection.commit()
    count = cur.rowcount
    print(count, "Record Updated successfully ")
    cur.close()
    return result


def update_weekly_menu_by_id(menu_name, menu_id):
    cur = connection.cursor()
    menu_update_query = f"update weekly_menu set menu_name= %s where menu_id =%s"
    cur.execute(menu_update_query, (menu_name, menu_id))
    result = connection.commit()
    return result


def delete_weekly_menu_by_id(menu_id):
    cur = connection.cursor()
    menu_delete_query = f"delete from weekly_menu where menu_id={menu_id}"
    cur.execute(menu_delete_query)
    result = connection.commit()
    return result


# def get_recipes_by_menu_name(menu_name):
#     cur = connection.cursor()
#     cur.execute(f"SELECT recipe_id FROM weekly_menu WHERE menu_name='{menu_name}'")
#     result = cur.fetchall()
#     return result
