from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.types import TypeDecorator, Unicode

Base = declarative_base()

# decode Chinese charactors to database
class CoerceUTF8(TypeDecorator):
    """Safely coerce Python bytestrings to Unicode
    before passing off to the database."""

    impl = Unicode

    def process_bind_param(self, value, dialect):
        if isinstance(value, str):
            value = value.decode('utf-8')
        return value

class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(CoerceUTF8, nullable = False)
    id = Column(Integer, primary_key = True)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }

class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(CoerceUTF8, nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    price = Column(String(8))
    description = Column(CoerceUTF8(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course
        }

engine = create_engine('sqlite:///chineserestaurantmenu.db')
Base.metadata.create_all(engine)
