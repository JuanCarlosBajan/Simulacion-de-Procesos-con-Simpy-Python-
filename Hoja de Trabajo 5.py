import simpy
import random


random.seed(10)

def Process(env,name, Ram,cpu, memoria, instrucciones, redIns, tiempoEspera, TiempoTotal):
    cc =0 
    run = True
    tiempoInterno = tiempoEspera