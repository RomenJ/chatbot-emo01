import random

def chatbot_emocional():
    print("Hola, soy tu chatbot de apoyo emocional. En primer lugar dime tu nombre")
    nombre= input("Nombre: ").lower()
    print("¿Cómo te sientes", nombre," ?")
    while True:
        respuesta = input("Tú: ").lower()
        respuesta = limpiar_entrada(respuesta)
        
        if "triste" in respuesta in respuesta or "depresion" in respuesta or "negro" in respuesta:
            print("Chatbot: Lamento escuchar que te sientes triste. Podrías realizar el siguiente test para ver tus niveles de presión: https://www.psicologia-online.com/test-de-depresion-de-beck-4098.html Mucho ánimo", nombre)
        elif "feliz" in respuesta:
            print("Chatbot: ¡Eso suena genial! ¿Qué te hace sentir feliz ",nombre,"?")  
        elif "enojado"  in respuesta or "cabreado" in respuesta or "mosqueado" in respuesta:
            print("Chatbot: Entiendo que puedas estar enojado. ¿Qué pasó", nombre,"?")
        elif "sauron"  in respuesta or "legolas" in respuesta or "arwen" in respuesta:
            print("Chatbot: No me vengas con tus frikadas ", nombre,". Ese no es el tema y lo sabes")      
        elif "miedo" in respuesta or "ansiedad" in respuesta or "panico" in respuesta:
            print("Chatbot: El miedo y la ansiedad son emocionales naturales. Vamos a revisar tu estado de ansiedad. Puedes realizar el siguiente test. http://espectroautista.info/GAD7-es.html. Si tus puntuaciones son altas no dudes en consultarme. ", nombre,".")
        elif "adiós" in respuesta or "salir" in respuesta:
            print("Chatbot: Siempre estoy aquí si necesitas hablar.",nombre," ¡Cuídate!")
            break
        else:
            print("Chatbot: Cuéntame más sobre eso",nombre,".")

def limpiar_entrada(texto):
    # Función para limpiar la entrada de texto de caracteres no deseados
    caracteres_no_deseados = [",", ".", "!", "?", "¿", "¡", "(", ")", ";", ":"]
    for caracter in caracteres_no_deseados:
        texto = texto.replace(caracter, "")
    return texto

if __name__ == "__main__":
    chatbot_emocional()