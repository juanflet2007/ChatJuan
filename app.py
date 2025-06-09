from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

respuestas = {
    "hola": "¡Hola! ¿Cómo estás?",
    "adios": "¡Hasta luego! Que tengas un buen día.",
    "gracias": "De nada, ¡estoy aquí para ayudar!",
    "como estas": "Estoy bien, gracias por preguntar. ¿Y tú?",
    "que puedes hacer": "Puedo responder a saludos básicos y mantener una conversación simple.",
    "que es python": "Python es un lenguaje de programación interpretado, de alto nivel y multipropósito. Es conocido por su sintaxis clara y legible.",
    "que es flask": "Flask es un microframework para Python que se utiliza para desarrollar aplicaciones web. Es ligero y fácil de usar.",
    "como crear una función en javascript": "En JavaScript, una función se crea así:\n\nfunction nombreFuncion(parametros) {\n  // código\n}",
    "diferencia entre list y tuple": "En Python:\n- Listas: mutables, se definen con []\n- Tuplas: inmutables, se definen con ()",
    "que es un bucle for": "Un bucle for permite repetir un bloque de código un número determinado de veces. En Python:\n\nfor i in range(5):\n  print(i)",
    "que es html": "HTML (HyperText Markup Language) es el lenguaje estándar para crear páginas web. Define la estructura del contenido.",
    "que es css": "CSS (Cascading Style Sheets) es un lenguaje que describe cómo se deben mostrar los elementos HTML en la pantalla.",
    "como centrar un div": "Puedes centrar un div con CSS de varias formas:\n\n1. Con márgenes automáticos:\ndiv {\n  width: 200px;\n  margin: 0 auto;\n}\n\n2. Con Flexbox:\nbody {\n  display: flex;\n  justify-content: center;\n}",
    "que es una api": "Una API (Application Programming Interface) es un conjunto de reglas que permite que diferentes aplicaciones se comuniquen entre sí.",
    "que es git": "Git es un sistema de control de versiones distribuido que permite gestionar cambios en el código fuente durante el desarrollo de software.",
    "que es poo": "POO (Programación Orientada a Objetos) es un paradigma de programación basado en objetos que contienen datos y métodos. Sus pilares son: encapsulamiento, herencia, polimorfismo y abstracción.",
    "como instalar flask": "Para instalar Flask en Python:\n\n1. Asegúrate de tener Python instalado\n2. Ejecuta en tu terminal:\npip install flask",
    "que es javascript": "JavaScript es un lenguaje de programación interpretado que se usa principalmente para añadir interactividad a las páginas web.",
    "que es un framework": "Un framework es una estructura base que proporciona funcionalidades genéricas para facilitar el desarrollo de software.",
    "default": "No estoy seguro de cómo responder a eso. ¿Puedes reformular tu pregunta?"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message').lower()  
    if user_message:
        messages.append({'sender': 'user', 'text': user_message})
        
        bot_response = respuestas.get(user_message, respuestas['default'])
        
        for key in respuestas:
            if key in user_message and key != 'default':
                bot_response = respuestas[key]
                break
        
        messages.append({'sender': 'bot', 'text': bot_response})
        
        return jsonify({'status': 'success', 'messages': messages})
    return jsonify({'status': 'error'})

@app.route('/get_messages')
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)