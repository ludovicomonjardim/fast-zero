from http import HTTPStatus


def test_read_root_retorna_ok_e_ola_mundo(fix_client):
    response = fix_client.get('/') # Act (Ação)
    assert response.status_code == HTTPStatus.OK # Assert (Verificação)
    assert response.json() == {'message': 'Olá, mundo!!'}


def test_create_user_retorna_usuario_criado(fix_client):
    response = fix_client.post('/user/',
                           json={
                                'username': 'ludovico',
                                'email': 'teste@teste.com',
                                'password': '123456'
                           }
                           ) # Act (Ação)
    assert response.status_code == HTTPStatus.CREATED # Assert (Verificação)
    assert response.json() == {
        'id': 1,
        'username': 'ludovico',
        'email': 'teste@teste.com'}

def test_read_user_retorna_lista_de_usuarios(fix_client):
    response = fix_client.get('/user/') # Act (Ação)
    assert response.status_code == HTTPStatus.OK # Assert (Verificação)
    assert (response.json() ==
                            {'users':
                                [
                                    {
                                    'id': 1,
                                    'username': 'ludovico',
                                    'email': 'teste@teste.com'
                                    }
                                ]
                            })

def test_update_user_retorna_usuario_atualizado(fix_client):
    response = fix_client.put('/user/1', json={'username': 'ludovico',
                 'email': 'ludo@example.com',
                 'password': '123456',
                 'id': 1,}) # Act (Ação)
    assert response.json() == {'username': 'ludovico',
                 'email': 'ludo@example.com',
                 'id': 1,} # Assert (Verificação)

def test_update_user_retorna_erro_usuario_nao_encontrado(fix_client):
    response = fix_client.put('/user/2', json={'username': 'ludovico',
                 'email': 'ludo@example.com',
                 'password': '123456',
                 'id': 2,}) # Act (Ação)
    assert response.status_code == HTTPStatus.NOT_FOUND # Assert (Verificação)
    assert response.json() == {'detail': 'Usuário não encontrado'} # Assert (Verificação)

def test_delete_user_retorna_usuario_deletado(fix_client):
    response = fix_client.delete('/user/1') # Act (Ação)
    assert response.status_code == HTTPStatus.OK # Assert (Verificação)
    assert response.json() == {'message': 'Usuário ludovico deletado com sucesso!'}

def test_delete_user_retorna_erro_usuario_nao_encontrado(fix_client):
    response = fix_client.delete('/user/2') # Act (Ação)
    assert response.status_code == HTTPStatus.NOT_FOUND # Assert (Verificação)
    assert response.json() == {'detail': 'Usuário não encontrado'} # Assert (Verificação)

def test_read_user_por_id_retorna_usuario_especifico(fix_client):
    # Arrange: cria o usuário antes de buscar
    fix_client.post('/user/', json={
        'username': 'ludovico',
        'email': 'ludo@example.com',
        'password': '123456'
    })

    # Act
    response = fix_client.get('/user/1')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'ludovico',
        'email': 'ludo@example.com'
    }


def test_read_user_por_id_retorna_usuario_nao_encontrado_erro(fix_client):
    response = fix_client.get('/user/2') # Act (Ação)
    assert response.status_code == HTTPStatus.NOT_FOUND # Assert (Verificação)
    assert response.json() == {'detail': 'Usuário não encontrado'} # Assert (Verificação)