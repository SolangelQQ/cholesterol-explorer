from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy

app = Flask(__name__)
CORS(app)



def colesterol(t, C, cn, k1, k2, E):
    dCdt = (cn - C) * k1 + E * k2
    return dCdt

    
def euler(t0, tf, presente, ecuacion, intervalo, *args):
    futuros = []
    tiempos = []
    while True:
        futuros.append(presente)
        tiempos.append(t0)
        if (t0 + intervalo) > tf:
            intervalo = tf - t0
        pendiente = ecuacion(t0, presente, *args)
        pendiente2= ecuacion(t0 + intervalo/2, presente + (intervalo/2) * pendiente, *args)
        pendiente3 = ecuacion(t0 + intervalo/2, presente + (intervalo/2) * pendiente2, *args)
        pendiente4 = ecuacion(t0 + intervalo/2, presente + (intervalo) * pendiente3, *args)
        presente = presente + (intervalo/6) * (pendiente + 2*pendiente2 + 2*pendiente3 + pendiente4)
        t0 += intervalo
        if t0 >= tf:
            break
    futuros = numpy.array(futuros)
    tiempos = numpy.array(tiempos)
    return tiempos, futuros


@app.route('/')
def hello_world():
    return jsonify(message="¡Hola desde el backend en Python!")

@app.route('/sumar', methods=['POST'])
def sumar():
    try:
        data = request.get_json()
        tf = float(data.get('tf', 0))
        presente = float(data.get('presente', 0))

        t0 = 0
        cn = 200
        k1 = 0.1
        k2 = 0.1
        E = 400
        dt = 0.01

        tiempos, futuros = euler(t0, tf, presente, colesterol, dt, cn, k1, k2, E)
        resultado = {'tiempos': tiempos.tolist(), 'futuros': futuros.tolist()}

        return jsonify(resultado=resultado)
    except ValueError:
        return jsonify(error="Los datos proporcionados no son números válidos"), 400



if __name__ == '__main__':
    app.run(debug=True)
