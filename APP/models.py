from sqlalchemy import Column, Integer, String, Text
from APP.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)


class Foods(Base):
    __tablename__ = 'foods'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    num = Column(String(50), unique=True)
    prices = Column(String(120), unique=True)
    img = Column(String(500))

    def __init__(self, name=None, num=None, prices=None, text=None,img=None):
        self.name = name
        self.num = num
        self.prices = prices
        self.text = text
        self.img = img

    def __repr__(self):
        return '<Food %r>' % (self.name)


class CartFood(Base):
    __tablename__ = 'cartfood'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    num = Column(String(50), unique=True)
    prices = Column(String(120), unique=True)
    text = Column(Text)
    img = Column(String(500))
    def __init__(self, id=None, name=None, num=None,img=None,prices=None, text=None):
        self.id = id
        self.name = name
        self.num = num
        self.img = img
        self.prices = prices
        self.text = text


    def __repr__(self):
        return '<CartFood %r%s>' % (self.name,self.prices)
