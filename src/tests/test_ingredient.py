import pytest


class TestIngredients:
    def test_api_key(self, client):
        # test if response is returned as unauthorized when no token is passed
        ingredient_id = 1
        response = client.get(f"/ingredients/{ingredient_id}")
        data = response.get_json()
        assert response.status_code == 401

    def test_get_ingredient(self, client):
        # test if recipe is listed successfully
        ingredient_id = 1
        headers = {'x-api-key': '123abc'}
        response = client.get(f"/ingredients/{ingredient_id}", headers=headers)
        assert response.status_code == 200

    def test_ut_get_ingredient(self, client):
        # test if recipe metadata is same as the one passed in the response
        headers = {'x-api-key': '123abc'}
        recipe_id_expected = 1
        recipe_name_expected = 'Garlic'
        response = client.get(f"/ingredients/{recipe_id_expected}", headers=headers)
        data = response.get_json()
        ingredient_id = data[0][0]
        ingredient_name = data[0][1]
        assert ingredient_id == recipe_id_expected
        assert ingredient_name == recipe_name_expected

    # negative tetsing
    def test_post_ingredient_with_exception(self, client):
        headers = {'x-api-key': '123abc'}
        with pytest.raises(Exception):
            response = client.post("/ingredients/", data={}, headers=headers)

    def test_post_ingredient(self, client):
        # test if recipe is created successfully
        headers = {'x-api-key': '123abc'}
        ingredient = {
            "ingredient_id": 999998,
            "ingredient_name": "jeera"
        }
        response = client.post("/ingredients/", json=ingredient, headers=headers)
        assert response.status_code == 200

    def test_delete_ingredient(self, client):
        # test if recipe is deleted successfully
        headers = {'x-api-key': '123abc'}
        ingredient_id = 999998
        response = client.delete(f"/ingredients/{ingredient_id}", headers=headers)
        assert response.status_code == 200

        # test if recipe and its metadata is actually deleted from database
        response = client.get(f"/ingredients/{ingredient_id}", headers=headers)
        assert response.status_code == 200
        assert response.get_json() == []
