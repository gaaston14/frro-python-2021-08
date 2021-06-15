from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import db
import modelo
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import TwoLineListItem
import hashlib as hl

class login(MDScreen):
    def verifica(self):
        for i in db.session.query(modelo.Usuarios).all():
            if i.usuario == hl.md5(str(self.ids.user.text).encode('utf-8')).hexdigest() or self.ids.pw.text == '':
                self.ids.label.text = 'Usuario ya existente o no valido'
                return False
        return True
    def registrar(self):
        if self.verifica():
            obj = modelo.Usuarios(hl.md5(str(self.ids.user.text).encode('utf-8')).hexdigest(), hl.md5(str(self.ids.pw.text).encode('utf-8')).hexdigest())
            db.session.add(obj)
            db.session.commit()
            self.ids.label.text = 'nuevo usuario registrado'
    def consultar(self):
        b = db.session.query(modelo.Usuarios).all()
        for i in b:
            if (i.usuario == hl.md5(str(self.ids.user.text).encode('utf-8')).hexdigest()) and (i.contraseña == hl.md5(str(self.ids.pw.text).encode('utf-8')).hexdigest()):
                self.ids.label.text = 'logeo exitoso'
                return True
        else:
            self.ids.label.text = 'Contraseña o usuario incorrecto'
class menu(MDScreen):
    def on_start(self):
        a = db.session.query(modelo.mesa).all()
        for j in a:
            self.ids.contenedor.add_widget(
                TwoLineListItem(text=f"Mesa {j.idmesa}",
                                secondary_text=f"Estado {j.descripcion}")
            )



class Myapp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(login(name='login'))
        sm.add_widget(menu(name='menu'))
        return sm
Myapp().run()
