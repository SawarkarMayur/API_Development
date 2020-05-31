
from user import User

users = [User(1,'mayur','welcome'),
         User(2,'msd','India')]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username,password):
    #check if user exist
    user= username_table.get(username)
    if user and password == user.password:
        return user

def identity(payload):
    user_id= payload['identity']
    return userid_table.get(user_id,None)