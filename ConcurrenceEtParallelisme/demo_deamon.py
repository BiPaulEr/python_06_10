from threading import Thread
import time, threading
def printer(caractere, temps_att):
    for i in range(0, 10):
        print(caractere, flush = True, end='')
        time.sleep(temps_att)

t1 = Thread(target=printer, args=("*", 1), name="JAck")
t1.start()
t2 = Thread(target=printer,  args=("$", 2), daemon=True)
t2.start()
print("end")