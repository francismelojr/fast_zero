def test_root_retorna_200_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Francisco',
            'email': 'francisco@exemplo.com',
            'password': 'senha123',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'username': 'Francisco',
        'email': 'francisco@exemplo.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'Francisco',
                'email': 'francisco@exemplo.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Lucas',
            'email': 'lucas@email.com',
            'password': 'novasenha123',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'username': 'Lucas',
        'email': 'lucas@email.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'Usuário deletado'}
