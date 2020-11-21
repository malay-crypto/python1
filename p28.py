class Customer:
    def __init__(m,n,a):
        m.name=n
        m.age=a


    def show(p):
        print(p.name)
        print(p.age)

c1=Customer(100,20)
print(c1.name)
print(c1.age)
c1.show()