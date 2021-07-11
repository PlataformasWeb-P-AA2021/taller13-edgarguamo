from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hola Mundo !</p>"


@app.route("/edificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificio/",
            auth=('edgarf', 'pipo-234'))
    edificios = json.loads(r.content)
    return render_template("losedificios.html", edificios=edificios)

@app.route("/departamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=('edgarf', 'pipo-234'))
    datos = json.loads(r.content)
    datos2 = []
    for d in datos:
        datos2.append({'nombre':d['nombre'], 'costo_dept':d['costo_dept'],
        'num_dept':d['num_dept'], 'num_cuarto':d['num_cuarto'],
        'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentos.html", datos=datos2)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('edgarf', 'pipo-234'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio
