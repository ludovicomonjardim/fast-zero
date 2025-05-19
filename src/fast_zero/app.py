from http import HTTPStatus
# from http.client import HTTPException

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()
database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    print('🔄 Reload executado!')
    return {'message': 'Olá, mundo!!'}


@app.post('/user/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@app.get('/user/', response_model=UserList)
def read_user():
    """
    Retorna todos os usuários cadastrados.
    """
    return {'users': database}


@app.put('/user/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    """
    Atualiza um usuário existente.
    """

    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado')

    user_with_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id
    return user_with_id

@app.delete('/user/{user_id}', response_model=Message)
def delete_user(user_id: int):
    """
    Deleta um usuário existente.
    """

    if user_id < 1 or user_id > len(database):
        # Verifica se o usuário existe
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado')

    user = database[user_id - 1]

    # Exclui o usuário do banco de dados
    del database[user_id - 1]

    return {'message': f'Usuário {user.username} deletado com sucesso!'}

@app.get('/user/{user_id}', response_model=UserPublic)
def read_user_by_id(user_id: int):
    """
    Retorna um usuário específico.
    """

    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado')

    return database[user_id - 1]



"""
Operação     HTTP
CRUD
--------------------
Create       POST       Envia dados para o servidor
Read         GET        Pede dados do servidor
Update       PUT        Envia dados para o servidor
Delete       DELETE     Envia IDs para o servidor
"""
