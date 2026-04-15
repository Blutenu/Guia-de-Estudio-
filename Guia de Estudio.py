import random
import pyfiglet

from preguntas_de_quimica import banco_preguntas  
from preguntas_de_quimica import titulo_Prubeba_doc

titulo = pyfiglet.figlet_format("PRUEBA DE ESTUDIO", font="slant")
print(titulo)
class estilo:
    NEGRITA = '\033[1m'
    FIN = '\033[0m'
print(f"{estilo.NEGRITA}Tema:{estilo.FIN} {titulo_Prubeba_doc}\n")
# Función para limpiar texto (quitar tildes y poner en minúsculas)
def normalizar(texto):
    reemplazos = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u")]
    texto = texto.lower().strip()
    for original, nuevo in reemplazos:
        texto = texto.replace(original, nuevo)
    return texto

preguntas_pendientes = list(banco_preguntas)

print(f"{estilo.NEGRITA}--- PRUEBA DE ESTUDIO (DATOS EXTERNOS) ---{estilo.FIN}\n")

while True:
    if not preguntas_pendientes:
        print(f"\n{estilo.NEGRITA}--- ¡Ronda completada! Reiniciando... ---{estilo.FIN}\n")
        preguntas_pendientes = list(banco_preguntas)

    pregunta_actual = random.choice(preguntas_pendientes)
    print(f"{estilo.NEGRITA}Pregunta:{estilo.FIN} {pregunta_actual['pregunta']}")

    # --- ENTRADA ---
    if pregunta_actual["tipo"] == "multiple":
        for i, opt in enumerate(pregunta_actual["opciones"], 1):
            print(f"  {i}) {opt}")
        entrada = input("Tu respuesta (número o nombre): ")
        if entrada.isdigit() and int(entrada) <= len(pregunta_actual["opciones"]):
            entrada = pregunta_actual["opciones"][int(entrada)-1]
    
    elif pregunta_actual["tipo"] == "enumeracion":
        print("  (Escribe los elementos separados por comas)")
        entrada_raw = input("Respuestas: ")
        entrada = [normalizar(item) for item in entrada_raw.split(",")]
    else:
        entrada = input("Respuesta: ")

    if isinstance(entrada, str) and normalizar(entrada) == "salir": break

    # --- VALIDACIÓN ---
    es_correcto = False
    if pregunta_actual["tipo"] == "enumeracion":
        correctas_norm = [normalizar(c) for c in pregunta_actual["correcta"]]
        if sorted(entrada) == sorted(correctas_norm):
            es_correcto = True
    else:
        if normalizar(entrada) == normalizar(pregunta_actual["correcta"]):
            es_correcto = True

    # --- RESULTADO ---
    if es_correcto:
        print(f"✅ {estilo.NEGRITA}¡Correcto!{estilo.FIN}")
        preguntas_pendientes.remove(pregunta_actual)
    else:
        solucion = ", ".join(pregunta_actual["correcta"]) if isinstance(pregunta_actual["correcta"], list) else pregunta_actual["correcta"]
        print(f"❌ Incorrecto. Era: {estilo.NEGRITA}{solucion}{estilo.FIN}")

    print(f"(Faltan {len(preguntas_pendientes)} preguntas)\n" + "-"*30)