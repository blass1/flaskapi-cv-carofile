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
    url_imagen = request.host_url + "static/foto.jpg"
    
    # Creo el diccionario (Clave-Valor) que se enviara en el GET
    cv = {
        "nombre" : "Blas Alfonso",
        "apellido" : "Carofile",
        "domicilio" : "Villa Urquiza(CABA), Argentina",
        # Puedo enviar una lista que contiene otros diccionarios internamente
        "experiencia" : [{
            "posicion" : "RIO",
            "lugar" : "FAA",
            "desde" : "01/2010",
            "hasta" : "Actualidad",
            "descripcion" : "Una pija"
        }],
        "educacion" : {
            "nivel" : "Terciario",
            "titulo" : "Analista de sistemas",
            "institucion" : "ESBA"
        },
        "intereses" : ["Python", "Desarrollo", "Games"],
        "contacto" : {
            "linkedin" : "linkedin.com/in/carofile",
            "github" : "github.com/blass1"
        },
        "foto" : url_imagen
    }
    # Con esta funcion de flask transformamos el diccionario  o estructura de datos de python en json (JavaScript Object Notation)
    return jsonify(cv)


""" Con POST envio informacion a la api, se la envio en el body del mensaje usando Insomnia
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