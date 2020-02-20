from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username) # pretazuje da li je user regitrovan u bazi - tabela users
    if user and user.password == password:
        return user
    
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)