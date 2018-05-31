from TestClass import *

if __name__ == "__main__":
    c1 = CountThread("java", 1, 20, 0.7)
    c1.start()
    print("main end")
