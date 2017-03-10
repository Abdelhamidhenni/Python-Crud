from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import datetime

db = SqliteExtDatabase('my_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    email = CharField()
    password = CharField()
# create table
User.create_table(True)

#MODEL Token
class Token(BaseModel):
    token = CharField()
    user_id = CharField()
Token.create_table(True)
#MODEL Transaction
class Trans(BaseModel):
    user_emeteur = CharField()
    user_recepteur = CharField()
    amount = CharField()
Trans.create_table(True)
# connect db
db.connect()

