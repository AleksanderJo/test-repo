from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    items = db.relationship('ItemModel', lazy='dynamic') # lazy='dynamic' >>> self.items onda postaje query builder pa more .all()
    
    def __init__(self, name):
        self.name = name
        
    def json(self):
        return {"name": self.name, "items": [item.json() for item in self.items.all()]}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1 # moze i .filter_by(id=1) # vraca ItemModel objekat
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()