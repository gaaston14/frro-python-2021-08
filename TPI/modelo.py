
import db
from sqlalchemy import Column, Integer, String, Float

class Usuarios(db.Base):
    __tablename__ = 'usuario'
    usuario = Column(String(10), nullable=False, primary_key=True)
    contraseña = Column(String(10))
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
    def __repr__(self):
        return f'usuario({self.usuario}, {self.contraseña})'
    def __str__(self):
        return self.usuario
class cliente(db.Base):
    __tablename__= 'cliente'
    dni = Column (Integer , nullable=False, primary_key=True)
    nombre = Column(String(20), nullable=False)
    apellido = Column(String(20), nullable=False)
    direccion = Column(String(20), nullable=False)
    telefono = Column(Integer, nullable=False)
    def __init__(self, dni, nombre, apellido,direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
    def __repr__(self):
        return f'usuario({self.dni}, {self.nombre}, {self.apellido}, {self.direccion}, , {self.telefono})'
    def __str__(self):
        return self.dni
class mesa(db.Base):
    __tablename__= 'mesa'
    idmesa = Column (Integer , nullable=False, primary_key=True)
    descripcion = Column(String(20), nullable=False)
    def __init__(self, idmesa, descripcion):
        self.idmesa = idmesa
        self.descripcion = descripcion
    def __repr__(self):
        return f'usuario({self.idmesa}, {self.descripcion})'
    def __str__(self):
        return self.idmesa