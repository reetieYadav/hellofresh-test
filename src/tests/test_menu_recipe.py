class TestMenuRecipe:

    def test_api_key(self, client):
        menu_recipe_id = 1
        response = client.get(f"/menu-recipe/{menu_recipe_id}")
        assert response.status_code == 401

    def test_menu_recipe_by_id(self, client):
        menu_recipe_id = 1
        menu_id = 1
        recipe_id = 1
        headers = {'x-api-key': '123abc'}
        response = client.get(f"/menu-recipe/{menu_recipe_id}", headers=headers)
        data = response.get_json()
        assert response.status_code == 200
        assert menu_recipe_id == data[0][0]
        assert menu_id == data[0][2]
        assert recipe_id == data[0][3]

    def test_post_menu_recipe(self, client):
        # test if menu is created successfully
        headers = {'x-api-key': '123abc'}
        menu_recipe = {
            "menu_id": 1,
            "recipe_id": 4
        }
        response = client.post("/menu-recipe/", json=menu_recipe, headers=headers)
        assert response.status_code == 200

    def test_delete_menu_recipe(self, client):
        menu_id = '4'
        headers = {'x-api-key': '123abc'}
        response = client.get(f"/menu-recipe/{menu_id}", headers=headers)
        assert response.status_code == 200

        response = client.delete(f"/menu-recipe/{menu_id}", headers=headers)
        assert response.status_code == 200
