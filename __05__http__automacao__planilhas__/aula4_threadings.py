from time import sleep 
from threading import Thread, Lock

class MyCustonThread(Thread):
    
    def __init__(self, tempo, texto):
        self._tempo = tempo
        self._texto = texto
        
        super().__init__()
        
    def run(self):
        sleep(self._tempo)
        print(self._texto)
        
t1 = MyCustonThread(texto= 'Thread 1', tempo= 2)
t1.start()
t2 = MyCustonThread(texto= 'Thread 2', tempo= 5)
t2.start()
t3 = MyCustonThread(texto= 'Thread 3', tempo= 11)
t3.start()

for i in range(15):
    print(i)
    sleep(1)

# ----------- Usando a própria classe Thread -----------
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)
    
t = Thread(target= vai_demorar, args=('Olá paralelo !!', 6))
t.start()

while t.is_alive():
    print('Esperando a Thread.')
    sleep(1)

# ----------- Controlando paralelismo com condição -----------
class Ingressos:
    def __init__(self, estoque: int):
        self.estoque = estoque
        # Nosso cadeado
        self.lock = Lock()

    def comprar(self, quantidade: int):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')
        
        self.lock.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque) 