import usuarios.conexion as conexion
import datetime
import hashlib

#Conexion a la BBDD
connect= conexion.conectar()
database= connect[0]
cursor= connect[1]


class Usuario:
    
    def __init__(self,nombre, apellidos, email, password):
        self.nombre=nombre
        self.apellidos=apellidos
        self.email=email
        self.password=password

    def registrar(self):

        #cifrar contraseña
        cifrado=hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))


        fecha=datetime.datetime.now()
        sql="INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s);"
        usuario=(self.nombre, self.apellidos, self.email,cifrado.hexdigest(), fecha)


        #Capturamos errores
        try:
            cursor.execute(sql,usuario)
            database.commit()

            result= [cursor.rowcount, self]
        except: result=[0,self]
        return result
        

    def identificar(self):
        # Consulta de comprobacion en la bbdd
        sql="SELECT * FROM usuarios WHERE email=%s AND password=%s;"

        #cifrar contraseña
        cifrado=hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        # datos para la consulta
        usuario=(self.email,cifrado.hexdigest())

        cursor.execute(sql,usuario)
        result=cursor.fetchone()
        return result
