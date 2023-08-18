from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/inicial')
def nivel_inicial():
    return render_template('sitio/inicial.html')

@app.route('/contacto')
def contacto():
    return render_template('sitio/contacto.html')

@app.route('/comunicado')
def comunicado():
    return render_template('sitio/comunicado.html')

@app.get('/img/<imagen>')
def imagenes(imagen):
    return send_from_directory(os.path.join("templates/sitio/img"), imagen)

@app.get('/css/<archivocss>')
def css_link(archivocss):
    return send_from_directory(os.path.join("templates/sitio/css"), archivocss)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)