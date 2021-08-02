from fastapi import FastAPI, Depends, Header, status
from fastapi.exceptions import HTTPException

# app = FastAPI(dependencies=[Depends(authenticate_user)])
app = FastAPI()

fake_db = {
    'ffff': {'name': 'Jack', 'age': 33},
    'qwer': {'name': 'John', 'age': 21},
    'asdf': {'name': 'Dick', 'age': 31},
    'zxcv': {'name': 'Melinda', 'age': 64}
}


class User:

    api_key_calls = 0

    @classmethod
    def is_authenticated(cls, api_key: str):
        if api_key in fake_db and cls.api_key_calls <= 100:
            cls.api_key_calls += 1
            return True


def authenticate_user(api_key: str = Header(...)):
    if User.is_authenticated(api_key):
        user = fake_db.get(api_key, {})
        return user

    raise HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        detail='Invalid api key'
    )


@app.get('/blogs')
async def blogs(user: dict = Depends(authenticate_user)):
    return {'blogs': [
        {'blog1': {'body': 'lorem30', 'author': 'anon'}},
        {'blog322': {'body': 'lorem100', 'author': 'Jackson'}}
    ], 'user': user}
