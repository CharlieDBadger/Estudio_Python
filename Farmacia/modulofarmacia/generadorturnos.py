from . import generador_de_numeros_infinito, anotacion_texto_espera, anotacion_texto_espera_dummie

__generador_numero_generico__ = generador_de_numeros_infinito()
__generador_numero_farmacia__ = generador_de_numeros_infinito()
__generador_numero_perfumeria__ = generador_de_numeros_infinito()
__generador_numero_dermatologia__ = generador_de_numeros_infinito()

@anotacion_texto_espera_dummie
def generador_turno_dummie(letra):
    return f"{letra}-{next(__generador_numero_generico__)}"


@anotacion_texto_espera
def generador_turno_generico():
    return f"G-{next(__generador_numero_generico__)}"


@anotacion_texto_espera
def generador_turno_farmacia():
    return f"F-{next(__generador_numero_farmacia__)}"


@anotacion_texto_espera
def generador_turno_perfumeria():
    return f"P-{next(__generador_numero_perfumeria__)}"


@anotacion_texto_espera
def generador_turno_dermatologia():
    return f"D-{next(__generador_numero_dermatologia__)}"
