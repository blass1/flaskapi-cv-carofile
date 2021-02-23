# API FLASK: Curriculum Vitae  de BLAS CAROFILE

Poder verla entrando a: https://flaskapi-cv-carofile.herokuapp.com

## ENDPOINTS
En las APIS a las rutas declaradas del navegador se les llama endpoints
~~~
@app.route('/')
~~~
Cada __endpoint__ posee metodos que le permiten ejecutar diferentes acciones. 
GET y POST por ejemplo son para exponer informacion y aceptar informacion del backend.

El __endpoint__ de la ruta __"/curriculum"__ del  navegador ejecuta las funciones que posee internamente, en este caso haciendo un return del json con el cv y la ruta de la foto en la carpeta static.
~~~
@app.route('/curriculum', methods=['GET'])
~~~
En cambio POST permite enviar mensajes a travez del cuerpo del request al endpoint con su metodo POST
~~~
@app.route('/mensajes', methods=['POST'])
~~~


## Test de insomnia con el endpoint mensajes

Si hago un POST desde Insomnia al endpoint sin cargar nada en el body sale un error 400 por el abort de la funcion.

Bad Request
Debe enviar su mensaje en el body del POST.

Siempre deben ser claro la comunicacion de la API con el desarollador para saber exactamente como se realiza la comunicacion.
