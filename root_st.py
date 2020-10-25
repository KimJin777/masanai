a = int(input("a"))
b = int(input("b"))
c = int(input("c"))

def root_solve(a, b, c):
    x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)

    print(x1, x2)
    return x1, x2


aa = root_solve(a,b,c)

# for i in aa:
print(aa)