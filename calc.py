import time
import sys

def main():
    def add(x, y):
        return x + y
    def min(x, y):
        return x - y
    def divide(x, y):
        return x / y
    def multiply(x, y):
        return x * y

    nRestart = ["restart", "r"]
    quit = ["quit", "q"]

    num1 = float(input("\nnum1: "))
    num2 = float(input("num2: "))

    choise = input("\n1.add, 2.min, 3.divide, 4.multiply, 5.exit: ")
    if choise == '1':
        print("\n",num1, "+", num2, "=", add(num1, num2))
        restart = input("\nRestart program or quit: ").lower()
        if restart in nRestart:
            print("\nwait 2sec...")
            time.sleep(2)
            main()
        elif restart in quit:
            def quitSystem():
                sys.exit()
            quitSystem()
    if choise == '2':
        print("\n",num1, "-", num2, "=", min(num1, num2))
        restart = input("\nRestart program or quit: ").lower()
        if restart in nRestart:
            print("\nwait 2sec...")
            time.sleep(2)
            main()
        elif restart in quit:
            def quitSystem():
                sys.exit()
            quitSystem()
    if choise == '3':
        print("\n",num1, "/", num2, "=", divide(num1, num2))
        restart = input("\nRestart program or quit: ").lower()
        if restart in nRestart:
            print("\nwait 2sec...")
            time.sleep(2)
            main()
        elif restart in quit:
            def quitSystem():
                sys.exit()
            quitSystem()       
    if choise == '4':
        print("\n",num1, "*", num2, "=", multiply(num1, num2))
        restart = input("\nRestart program or quit: ").lower()
        if restart in nRestart:
            print("\nwait 2sec...")
            time.sleep(2)
            main()
        elif restart in quit:
            def quitSystem():
                sys.exit()
            quitSystem()
    if choise == '5':
        def quitSystem():
            sys.exit()
        quitSystem()
main()
