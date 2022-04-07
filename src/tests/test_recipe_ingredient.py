class TestRecipeIngredients:
    def test_api_key(self, client):
        # test if response is returned as unauthorized when no token is passed
        recipe_id = 1
        response = client.get(f"/recipe-ingredient/{recipe_id}/ingredient")
        data = response.get_json()
        assert response.status_code == 401

    def test_get_ingredient_from_recipe_id(self, client):
        # test if recipe is listed successfully
        recipe_id = 1
        headers = {'x-api-key': '123abc'}
        response = client.get(f"/recipe-ingredient/{recipe_id}/ingredient", headers=headers)
        data = response.get_json()
        print(data)
        print(data[0][0])
        assert response.status_code == 200

        ingredient_id = data[1][0]
        response = client.get(f"/ingredients/{ingredient_id}", headers=headers)
        print(response.get_json())
        assert response.status_code == 200

    def test_get_recipe_ingredient(self, client):
        # test if recipe is listed successfully
        recipe_id = 1
        headers = {'x-api-key': '123abc'}
        response = client.get(f"/recipe-ingredient/", headers=headers)
        print(response.get_json())
        assert response.status_code == 200

    def test_post_recipe_ingredient(self, client):
        # test if menu is created successfully
        headers = {'x-api-key': '123abc'}
        recipe_ingredient = {"recipe_id": 2, "ingredient_id": 5}
        response = client.post("/recipe-ingredient/", json=recipe_ingredient, headers=headers)
        assert response.status_code == 200

    def test_delete_recipe_ingredient(self, client):
        recipe_ingredient_id = '4'
        headers = {'x-api-key': '123abc'}
        response = client.delete(f"/recipe-ingredient/{recipe_ingredient_id}", headers=headers)
        assert response.status_code == 200

    def test_get_ingredient_ids_from_recipe(self, client):
        recipe_id = 1
        headers = {'x-api-key': '123abc'}
        response = client.get(f"/recipe-ingredient/{recipe_id}/ingredient", headers=headers)
        data = response.get_json()
        print(data)
        assert response.status_code == 200
