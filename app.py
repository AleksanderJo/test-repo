from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from db import db
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # moze da bude bilo koji sem "sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose' #mora biti dugo i komplikoano
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all() # alchemy stvara tabele za importe koje vidi i koji imaju inicijalizacije u sebi, pa za svaku tabelu koju zelim da imamo u bazi mora da navedemo u importu

jwt = JWT(app, authenticate, identity) # autentifikacioni token

api.add_resource(StoreList, '/stores') # svaku stranicu treba inicijalizovati kao resurs
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__': #provera sluzi da ne pokrece aplikaciju pri importu ove skripte u druge, vec samo ako je ova skripta main.
    db.init_app(app)
    app.run(port=5000, debug=True)





