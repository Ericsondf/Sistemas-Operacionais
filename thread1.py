import threading 
import time       


def imprime_1_a_10():
    #números de 1 até 10
    for i in range(1, 11):
        print(f"{threading.current_thread().name} -> {i}")  
        #valor atual
        
        time.sleep(0.5)

# Função que será executada pela Thread-2
def imprime_50_a_60():
    #números de 50 até 60
    for i in range(50, 61):
        print(f"{threading.current_thread().name} -> {i}")
        
        time.sleep(0.5)  

# deferir o parametro
t1 = threading.Thread(target=imprime_1_a_10, name="Thread-1")
t2 = threading.Thread(target=imprime_50_a_60, name="Thread-2")


t1.start()
t2.start()


t1.join()
t2.join()

print("Execução finalizada!")  