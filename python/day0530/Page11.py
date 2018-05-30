import threading, time

def a(start, end):
    for _ in range(start, end):
        print("a : " , _)
        time.sleep(0.5)
def b(start, end):
    for _ in range(start, end):
        print("b : ", _)
        time.sleep(1)

t1 = threading.Thread(target = a, args = (1, 10))
t1.start()
t2 = threading.Thread(target = b, args = (1, 5))
t2.start()
# t3 - threading.Thread(target = c, args = )
