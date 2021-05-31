import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nOk, vamos ha hacer el registro en el sistema")

        nombre=input("¿Cual es tu nombre?")
        apellidos=input("¿cuales osn tus apellidos?")
        email=input("Introduce tu email")
        password=input("Introduce una contraseña")

        usuario=modelo.Usuario(nombre,apellidos,email,password)
        registro=usuario.registrar()

        if registro[0]>=1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")

    
    
    def login(self):
        print("\nOk, Identificate en el sistema")
        
        try:
            email=input("Introduce tu email")
            password=input("Introduce una contraseña")

            usuario=modelo.Usuario('','',email,password)

            login=usuario.identificar()

            if email==login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(self)
        
        except Exception as e:
            #print(type(e))
            print(type(e).__name__)
            print("Login incorrecto intentalo mas tarde")

    
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponiobles:

        - Crear notas (crear)
        - Mostar notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
       
        """)

        accion= input("¿Que desea hacer?")
        hazEl= notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            #print("prueba")
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar()
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"\nHasta pronto {usuario[1]}")
            exit()

    

        


    
    