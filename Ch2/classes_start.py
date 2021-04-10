#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print("myclass method1")

    def method2(self,anyShit):
        print("myClass method2: "+anyShit)

class anotherClass(myClass):
    def method1(self):
        # myClass.method1(self)
        print("anotherClass method1")

    def method2(self,anyShit):
        print("anotherClass method2 ")
    



def main():
    c=myClass()
    c.method1()
    c.method2("this is a fucking string baby")

    c2=anotherClass()
    c2.method1()
    c2.method2("yo motherfuckers")


if __name__ == "__main__":
    main()
