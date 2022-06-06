from distutils.command.install_egg_info import to_filename
from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas
from fastapi import status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "bxZNcjdjhxdsbsxzhjcbdshucdbxzkjcbdjbcxbkjzxcb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)
        return token_data
    except JWTError as e:
        print(e)
        raise credentials_exception
    except AssertionError as e:
        print(e)


def get_current_user(token: str = Depends(oauth2scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    return verify_access_token(token, credentials_exception)
