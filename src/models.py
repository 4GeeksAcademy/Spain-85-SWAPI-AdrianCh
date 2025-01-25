from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, ForeignKey

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String(120), nullable=False)
    password = mapped_column(String(80))
    favorites = relationship("Favorite", back_populates="user")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            
        }

class Planet(db.Model):
    __tablename__ = 'planet'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    climate = mapped_column(String(30), nullable=False)
    population = mapped_column(Integer, nullable=False)
    terrain = mapped_column(String(30), nullable=False)
    
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "terrain": self.terrain,
        }
    
class Character(db.Model):
    __tablename__ = 'character'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    species = mapped_column(String(30), nullable=False)
    gender = mapped_column(String(30), nullable=False)
    homeworld = relationship("Planet")
    homeworld_id = mapped_column(Integer, ForeignKey('planet.id'), nullable=False)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "gender": self.gender,
            # "homeworld": self.homeworld,
            # "homeworld_id": self.homeworld_id
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = mapped_column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = mapped_column(Integer, ForeignKey('character.id'), nullable=True)

    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet")
    character = relationship("Character")