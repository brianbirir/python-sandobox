from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context

DB = SQLAlchemy()

# base model
class BaseModel(DB.Model):
    '''Base data model for all objects'''
    __abstract__ = True

    id = DB.Column(DB.Integer, primary_key=True)
    created_at = DB.Column(DB.DateTime, default=DB.func.current_timestamp())
    modified_at = DB.Column(DB.DateTime, default=DB.func.current_timestamp(), onupdate=DB.func.current_timestamp())

    def __repr__(self):
        '''Define a base way to print models'''
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })


# user model extends base model
class User(BaseModel):

    __tablename__ = 'users'
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(45), index=True)
    password_hash = DB.Column(DB.String(128))

    def hash_password(self, password):

        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):

        return pwd_context.verify(password, self.password_hash)