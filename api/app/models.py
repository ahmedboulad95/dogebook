from app import db

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

class YourModel(BaseModel):
    ___tablename__ = 'my_table'

class User(BaseModel):
    __tablename__ = 'User'

class Post(BaseModel):
    __tablename__ = 'Post'

class Reaction(BaseModel):
    __tablename__ = 'Reaction'
    