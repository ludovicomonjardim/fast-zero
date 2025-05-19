from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    """
    Base class for all messages.
    """

    message: str


class UserSchema(BaseModel):
    """
    User schema for user data validation.
    """

    username: str
    email: EmailStr
    password: str


class UserDB(UserSchema):
    id: int


class UserPublic(BaseModel):
    """
    User schema for public user data.
    """

    id: int
    username: str
    email: EmailStr


class UserList(BaseModel):
    """
    User schema for a list of users.
    """

    users: list[UserPublic]
