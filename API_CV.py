from flask import Flask, jsonify, request, abort

app = Flask(__name__)
# Para que muestre el json en una forma mas agradable
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def index():
    info = {
        "mensaje" : "Bienvenido a la API del curriculum vitae de Blas Carofile",
        "acciones" : [
            "GET /curriculum",
            "POST /mensajes"
        ]
    }
    # Con esta funcion de flask transformamos el diccionario de python en json
    return jsonify(info)

""" El metodo GET en HTTP y en el protocolo REST se utiliza para envie informacion """
@app.route('/curriculum', methods=['GET'])
def cv():

    # Generamos el link de la foto utilizado la host url del metodo request
    url_imagen = request.host_url + "static/foto.jpeg"
    
    # Creo el diccionario (Clave-Valor) que se enviara en el GET
    cv = {
        "apellido_nombre" : "CAROFILE Blas Alfonso",
        "domicilio" : "Villa Urquiza(CABA), Argentina",
        "experiencia" : [{
            "posicion" : "Responsable Informático de la Inspectoría General",
            "lugar" : "Ministerio de Defensa, Fuerza Aérea Argentina",
            "desde" : "01/2010",
            "hasta" : "Actualidad",
            "descripcion" : """ Encargado del mantenimiento preventivo y correctivo de 38 puestos de trabajo tanto en software como hardware. Coordinación de tareas relacionadas a la telefonía, servidores, seguridad de la información e infraestructura de redes. Asesoramiento tecnológico en las áreas Administrativas , Control de gestión y Direcciones de Inspecciones.
            """
        },{
            "posicion" : "Diseñador de Autocad y presupuestos de instalaciones industriales",
            "lugar" : "B.P Instalaciones",
            "desde" : "12-2008",
            "hasta" : "01-2010",
            "descripcion" : """Área de presupuestos de instalaciones industriales y comerciales de ventilación, aire acondicionado y sistemas termomecánicos. Diseño de instalaciones utilizando AUTOCAD.
            """
        }],
        "educacion" : [{
            "nivel" : "Terciario",
            "titulo" : "Técnico Superior en Análisis de Sistemas",
            "institucion" : "Instituto Universitario ESBA - Barrio Norte"
        },{
            "nivel" : "Secundario Técnico",
            "titulo" : "Técnico Mecánico con especialización en automatización y robótica",
            "institucion" : "Instituto Politécnico Modelo"
        }],
        "hobbies" : ["Programacion", "Desarrollo", "Ciencia"],
        "tecnologias" : [{
            "S.O" : "Linux (Ubuntu) + Windows",
            "Control de versiones" : "Git + GitHub",
            "web" : "HTML + CSS + BOOSTRAP",
            "Python3 Frameworks" : """ Flask + Extensions(SQLAlchemy + Brcrypt + Mail + WTForms). Django (ORM + Sqlite3 / PostgreSQL), Django REST Framework""",
            "Python3 Librerias" : "Pillow - OS - PyGame - Tkinter - OpenCV - Pandas - Matplotlib - gTTS - request",
            "Entornos V" : "VirtualEnv",
            "Otros breves conocimientos de lenguajes" : "Kotlin, Java, C#(.Net), JS"
        }],
        "contacto" : {
            "linkedin" : "linkedin.com/in/carofile",
            "github" : "github.com/blass1"
        },
        "foto" : url_imagen
    }
    # Con esta funcion de flask transformamos el diccionario  o estructura de datos de python en json (JavaScript Object Notation)
    return jsonify(cv)


""" Con POST envio informacion a la api en el body del mensaje usando Insomnia
"""
@app.route('/mensajes', methods=['POST'])
def contacto():
    # Creo el mensaje con la data del "body" enviada a travez del request
    mensaje = request.get_data()
    # Si no envia nada en el request utilizo la excepcion 400 (bad request) y llamada abort, le personalizo un mensaje.
    if not mensaje:
        abort(400, description="Debe enviar su mensaje en el body del POST.")
    print("MESAJE DE CONTACTO: " + str(mensaje))
    return "Gracias por su mensaje! (*.~)"

# Si la subimos en modo productivo hay que desactivar el debug
if __name__ == '__main__':
    #app.run(debug=True)
    app.run()