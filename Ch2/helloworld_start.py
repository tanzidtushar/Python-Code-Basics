#
# Example file for HelloWorld
#
def inc(a,b=1):
    return(a+b)
a=inc(1)
a=inc(a,a)
print(a)
def main():
    print("Hello world")
    name = input("What is your name?")
    print("Nice to meet you, ",name) 


if __name__ == "__main__":
    main()