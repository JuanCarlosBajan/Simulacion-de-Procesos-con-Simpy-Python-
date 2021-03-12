import simpy
import random


random.seed(10)

def Process(env,name, Ram,cpu, memoria, instrucciones, redIns, tiempoEspera, TiempoTotal):
    cc =0 
    run = True
    tiempoInterno = tiempoEspera
    yield env.timeout(tiempoEspera)
    print("Iniciando proceso %s, entrando a lista ready. %s" % (name, env.now))
    pivoteTiempo = env.now
    while run == True:
        yield Ram.get(memoria)
        tiempoInterno = tiempoInterno + env.now-pivoteTiempo +1
        while instrucciones > 0:
            pivoteTiempo = env.now
            with cpu.request() as req:
                yield req
                tiempoInterno = tiempoInterno + env.now-pivoteTiempo +1