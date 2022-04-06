from src.core.dal.database import connection


def get_review_for_menu():
    cur = connection.cursor()
    cur.execute()
    result = cur.fetchall()
    return result


def get_review_for_recipe():
    cur = connection.cursor()
    cur.execute()
    result = cur.fetchall()
    return result
