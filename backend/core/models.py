import numpy as np

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
        pendiente2 = ecuacion(t0 + intervalo/2, presente + (intervalo/2) * pendiente, *args)
        pendiente3 = ecuacion(t0 + intervalo/2, presente + (intervalo/2) * pendiente2, *args)
        pendiente4 = ecuacion(t0 + intervalo/2, presente + (intervalo) * pendiente3, *args)
        presente = presente + (intervalo/6) * (pendiente + 2*pendiente2 + 2*pendiente3 + pendiente4)
        t0 += intervalo
        if t0 >= tf:
            break
    futuros = np.array(futuros)
    tiempos = np.array(tiempos)
    return tiempos, futuros
