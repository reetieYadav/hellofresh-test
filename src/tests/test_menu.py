class TestWeeklyMenu:

    def test_api_key(self, client):
        menu_id = 1
        response = client.get(f"/weeklymenu/{menu_id}")
        assert response.status_code == 401

    def test_menu_by_id(self, client):
        menu_id = 1
        menu_name = "week01"
        headers = {'x-api-key': '123abc'}
        response = client.get(f"/weeklymenu/{menu_id}", headers=headers)
        data = response.get_json()
        assert response.status_code == 200
        assert menu_id == data[0][0]
        assert menu_name == data[0][1]

    def test_post_recipe(self, client):
        # test if menu is created successfully
        headers = {'x-api-key': '123abc'}
        menu = {
            "menu_id": 9999,
            "menu_name": "week02"
        }
        response = client.post("/weeklymenu/", json=menu, headers=headers)
        assert response.status_code == 200

    def test_delete_menu(self, client):
        menu_id = 9999
        headers = {'x-api-key': '123abc'}
        response = client.get(f"/weeklymenu/{menu_id}", headers=headers)
        assert response.status_code == 200

        response = client.delete(f"/weeklymenu/{menu_id}", headers=headers)
        assert response.status_code == 200