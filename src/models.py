import os
import sys
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.orm import mapped_column

Base = declarative_base()

# Tabla Usuario
class Usuario(Base):
    __tablename__ = 'usuario'

    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String(120), unique=True, nullable=False)
    password = mapped_column(String(80), nullable=False)
    nombre = mapped_column(String(80), nullable=False)
    apellido = mapped_column(String(80), nullable=False)

    favoritos = relationship('Favorito', back_populates='usuario')  #back_populates conecta bidireccionalmente la tabla favoritos con el usuario en est caso

# Tabla Planeta
class Planeta(Base):
    __tablename__ = 'planeta'

    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(120), unique=True, nullable=False)
    clima = mapped_column(String(80))
    terreno = mapped_column(String(80))
    poblacion = mapped_column(String(80))

    favoritos = relationship('Favorito', back_populates='planeta')

# Tabla Personaje
class Personaje(Base):
    __tablename__ = 'personaje'

    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(120), unique=True, nullable=False)
    especie = mapped_column(String(80))
    genero = mapped_column(String(80))
    altura = mapped_column(String(80))

    favoritos = relationship('Favorito', back_populates='personaje')

# Tabla Favorito (intermedia)
class Favorito(Base):
    __tablename__ = 'favorito'
    #foreign_key hace que esta tabla dependa del resto, no puedes tener un favorito de una id que no exista x ejemplo
    id = mapped_column(Integer, primary_key=True)
    usuario_id = mapped_column(Integer, ForeignKey('usuario.id'))
    planeta_id = mapped_column(Integer, ForeignKey('planeta.id'), nullable=True)
    personaje_id = mapped_column(Integer, ForeignKey('personaje.id'), nullable=True)

    usuario = relationship('Usuario', back_populates='favoritos')
    planeta = relationship('Planeta', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')

# Generar el diagrama
def generate_schema_diagram():
    from eralchemy2 import render_er
    render_er('sqlite:///database.db', 'diagram.png')

if __name__ == "__main__":
    # Crear el esquema de la base de datos
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)

    # Generar el diagrama
    generate_schema_diagram()
