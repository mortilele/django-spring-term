import requests


def test_register():
    data = {
        'username': 'alik2',
        'password': 'alik',
        'first_name': 'Alik',
        'last_name': 'Akhmetov'
    }

    register_url = 'http://localhost:8000/auth/register/'
    response = requests.post(register_url, data=data)
    return response.json()


def test_login(username):
    data = {
        'username': username,
        'password': 'alik'
    }

    login_url = 'http://localhost:8000/auth/login/'

    token = requests.post(login_url, data=data).json()['access']
    return token


def test_admin_permission(token):
    HEADERS = {
        'Authorization': f'Bearer {token}'
    }

    journals_url = 'http://localhost:8000/journals/'

    data = {
        'name': 'POST',
        'price': 1234.00,
        'description': 'POST description',
        'type': 2
    }
    # CREATE
    response = requests.post(journals_url, data=data, headers=HEADERS).json()

    if 'id' in response:
        journal_id = response['id']
        detail_url = f'{journals_url}{journal_id}/'

        # UPDATE
        data['name'] = 'POST UPDATED'
        response = requests.put(detail_url, data=data, headers=HEADERS)
        print(response.json())

        # DELETE
        print(requests.delete(detail_url, headers=HEADERS))


# test_register()
token = test_login('alik2')  # Guest role
test_admin_permission(token)
token = test_login('alik')  # Admin role
test_admin_permission(token)
