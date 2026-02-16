from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Float, Date
from db import Base, engine

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    telegram_id = Column(Integer, unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f'User ID {self.id} - {self.username}'

class Name(Base):
    __tablename__ = 'names'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f'Name {self.id} - {self.name}'

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'User country {self.id} - {self.name}'

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f'User city {self.id} - {self.name}'

class Language(Base):
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f'User language {self.id} - {self.name}'

class CurrencyRate(Base):
    __tablename__ = 'currency_rates'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)  # date of value
    rate = Column(Float, nullable=False)  # value

    def __repr__(self):
        return f'Rate {self.id} -  {self.date}, {self.rate}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
