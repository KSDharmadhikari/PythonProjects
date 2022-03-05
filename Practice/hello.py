import math

def Hello(name):
    print("Hello " + name)
    print(f'Hello {name}')

def sqrt(num):
    print(type(math.sqrt(num)))

def whileLoop(count):
    while count <= 10:
        print(f"Hello, I am in a loop for {count} times")
        count += 1



if __name__=="__main__":
    Hello("6")
    sqrt(4)
    whileLoop(1)