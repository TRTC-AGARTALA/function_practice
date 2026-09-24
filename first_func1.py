def sum(a,b):
    sum=a+b
    return sum
def simple_intrest(p,r,t):
    SI=(p*r*t)/100
#function inside function SI
    def greet():
        print("good day")
    #function inside function greet    
        def hello():
            print("Hello Everyone!")
        hello()
    greet()
    return SI        
print(sum(2,3))
P=float(input("Enter the value of principle amount:"))
R=float(input("Enter the value of rate:"))
T=float(input("Enter the value of time:"))
print("the simple intrest is",simple_intrest(P,R,T))