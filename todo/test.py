import requests


def login():
    login_url = 'http://localhost:8000/api/users/login/'
    data = {
        'username': 'admin',
        'password': 'admin'
    }
    response = requests.post(login_url, data=data).json()
    return response['access']


token = login()


def get_todos(with_token=True):
    todos_url = 'http://localhost:8000/api/main/todos/'
    headers = dict()
    if with_token:
        headers = {
            'Authorization': f'Bearer {token}'
        }
    response = requests.get(todos_url, headers=headers).json()
    return response


print(get_todos())
print(get_todos(with_token=False))