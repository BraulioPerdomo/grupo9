from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    strUsuario = request.form['usuario']
    strPassword = request.form['password']
    if (strUsuario=='Braulio' and strPassword== 'password'):
        return render_template("inicio.html", strNombre=strUsuario)
    else:
        return render_template("login.html", strError="Usuario o Contraseña incorecta")

@app.route('/led')
def led():
    accion = request.args['accion']
    
    return render_template("led.html")

if __name__ == '__main__':
    app.run (debug=True, port=80, host='0.0.0.0')