
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
class material(db.Base):
    __tablename__= 'material'
    codigo = Column (Integer , nullable=False, primary_key=True)
    descripcion = Column(String(20), nullable=False)
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
    def __repr__(self):
        return f'usuario({self.codigo}, {self.descripcion})'
    def __str__(self):
        return self.codigo
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