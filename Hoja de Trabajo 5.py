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
                yield env.timeout(1)
                instrucciones = instrucciones- redIns

                des = random.randint(1,2)

                if(des == 1):
                    print('Enviando proceso %s a cola de espera por %s segundos. Tiempo Actual: %s ( Ocupando %s megas de memoria)' % (name, tiempoEspera, env.now, memoria))
                    yield env.timeout(3)
                    tiempoInterno = tiempoInterno + 1
                else:
                    c = 0
                    print('Proceso %s, enviando a procesar %s instrucciones mas. Tiempo acatual: %s ( Ocupando %s megas de memoria)' % (name, redIns, env.now, memoria))
        print('Proceso %s exitoso, finalizando en tiempo: %s' % (name, env.now))
        Ram.put(memoria)
        run = False
    print("Le tomo %s segundos a %s terminar el proceso." %(tiempoInterno,name))
    TiempoTotal.put(tiempoInterno)
            



env = simpy.Environment()
Ram = simpy.Container(env, init=100,capacity=100)
TiempoTotal = simpy.Container(env,capacity=1000000000000000000)
cpu = simpy.Resource(env, capacity= 2)

procesos = 200



for i in range(procesos):
    env.process(Process(env, i+1,Ram,cpu,random.randint(1,10),random.randint(1,10),3, round(random.expovariate(1/10) + 1), TiempoTotal))

env.run()
print(TiempoTotal.level/procesos)
