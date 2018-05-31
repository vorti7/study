import time, threading

def f(num):
    on_air = True
    while on_air:
        num += 1
        print("a num : ", num)
        time.sleep(0.5)
        if num>10:
            on_air = False


t1 = threading.Thread(target=f, args=(1,))
t1.setDaemon(True)#if Daemon thread thread will stop before finish their work
t1.start()
print("end")
