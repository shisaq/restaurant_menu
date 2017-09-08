from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base

engine = create_engine('sqlite:///chineserestaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()
