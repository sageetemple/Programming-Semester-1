
def loan(r, p, n, t):
    return(p*((1+(r/n))**(n*t))/(t*12))

r=float(input("Interest rate: "))
p=float(input("Starting monies: "))
n=float(input("Number of times compounded per year: "))
t=float(input("Life of loan: "))

print("Your payment is $","{:5.2f}".format(loan(r, p, n, t)))



