from flask import Flask, request, render_template, redirect


app = Flask(__name__)

@app.route('/')
def index():
    import leerConfiguracion
    return render_template('configuracion.html', velocidad = leerConfiguracion.velocidadDeParpadeo)

@app.route('/grabarConfiguracion', methods=['POST'])
def grabarconfiguracion():
    velocidad = request.form['velocidad']
    import leerConfiguracion
    leerConfiguracion.velocidadDeParpadeo = velocidad
    leerConfiguracion.grabarConfiguracion()
    return redirect("/")

if __name__ == '__main__':
    app.run (debug=True, port=80, host='0.0.0.0')