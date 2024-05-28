from modulofarmacia.generadorturnos import generador_turno_farmacia, generador_turno_dermatologia, \
    generador_turno_perfumeria
from modulofarmacia import utilidades


def main():
    menu = ["Farmacia", "Dermatologia", "Cosmetologia", "Salir"]
    indicaciones = f"*** BIENVENIDO A LA FARMACIA - LA POMADA DE LA ABUELA ***\n" \
                   f"Seleccione el departamento y se le asignará un turno:"
    seleccion = 0

    while seleccion != len(menu):

        seleccion = utilidades.seleccion_opcion_match(menu, indicaciones)
        match seleccion:
            case 1:
                generador_turno_farmacia()
            case 2:
                generador_turno_dermatologia()
            case 3:
                generador_turno_perfumeria()
            case 4:
                print("Gracias por su compra, vuelva pronto.")


main()
