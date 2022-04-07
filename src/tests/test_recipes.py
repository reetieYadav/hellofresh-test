import pytest


class TestRecipes:
    def test_api_key(self, client):
        # test if response is returned as unauthorized when no token is passed
        recipe_id = 1
        response = client.get(f"/recipes/{recipe_id}")
        assert response.status_code == 401

    def test_get_recipe(self, client):
        # test if recipe is listed successfully
        recipe_id = 1
        headers = {'x-api-key': '123abc'}
        response = client.get(f"/recipes/{recipe_id}", headers=headers)
        assert response.status_code == 200

    def test_ut_get_recipe(self, client):
        # test if recipe metadata is same as the one passed in the response
        headers = {'x-api-key': '123abc'}
        recipe_id_expected = 1
        recipe_name_expected = 'Grilled Vegetable Salad'
        response = client.get(f"/recipes/{recipe_id_expected}", headers=headers)
        data = response.get_json()
        recipe_id = data[0][0]
        recipe_name = data[0][1]
        assert recipe_id == recipe_id_expected
        assert recipe_name == recipe_name_expected

    # negative tetsing
    def test_post_recipe_with_exception(self, client):
        headers = {'x-api-key': '123abc'}
        with pytest.raises(Exception):
            client.post("/recipes/", data={}, headers=headers)

    def test_post_recipe(self, client):
        # test if recipe is created successfully
        headers = {'x-api-key': '123abc'}
        recipe = {
            "recipe_name": "salad",
            "description": "anything"
        }
        response = client.post("/recipes/", json=recipe, headers=headers)
        assert response.status_code == 200

    def test_delete_recipe(self, client):
        # test if recipe is deleted successfully
        headers = {'x-api-key': '123abc'}
        recipe_id = 7
        response = client.delete(f"/recipes/{recipe_id}", headers=headers)
        assert response.status_code == 200

        # test if recipe and its metadata is actually deleted from database
        response = client.get(f"/recipes/{recipe_id}", headers=headers)
        assert response.status_code == 200