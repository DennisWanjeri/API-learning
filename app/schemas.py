from pydantic import BaseModel


class PostModel(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostModel):
    pass


class Post(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True
