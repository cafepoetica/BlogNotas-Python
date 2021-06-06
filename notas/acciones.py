import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"ok {usuario[1]}, vamos ha crear una nueva nota")
        titulo = input("\nIntroduce el titulo de la nota")
        descripcion = input("\nIntroduce el contenido de tu nota")

        nota = modelo.Nota(usuario[0], titulo, descripcion)

        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        else:
            print("La nota no se ha guardado, lo siento!!!! ")

    def mostrar(self, usuario):
        print(f" \nok, {usuario[1]}, estas son tus notas: ")

        nota = modelo.nota(usuario[0], "", "")

        notas = nota.listar()

        for nota in notas:
            print("\n···························")
            print(nota[2])
            print(nota[3])

    def borrar(self, usuario):

        print(f"| ok, {usuario[1]}, vamos ha borrar")

        titulo = input("Introduce el titulo de la nota que desea borrar")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota {nota.titulo}")
        else:
            print("No se ha borrado la nota")
