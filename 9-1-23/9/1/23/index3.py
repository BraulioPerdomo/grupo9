from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    from leerConfiguracion import velocidadDeParpadeo
    return render_template('configuracion.html', velocidad = velocidadDeParpadeo)

@app.route('/formanombre', methods=['POST'])
def prueba1():
    if request.method =='GET':
        nombre = request.args['nombre']
    else:
        nombre = request.args['nombre']
    return render_template('index3.html', nombre=nombre)

if __name__ == '__main__':
    app.run (debug=True, port=80, host='0.0.0.0')