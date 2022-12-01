import sys
import math

def func(x):
    return math.sin(x) # change as needed

def sol():
    return math.pi # change as needed

def secant():
    # initialization
    errors = []
    x0 = float(sys.argv[1])
    x1 = float(sys.argv[2])
    tol = float(sys.argv[3])
    n = 0
    x = x1
    print("Chosen inputs:")
    print("x_0 = " + str(x0))
    print("x_1 = " + str(x1))
    print("tolerance = " + str(tol) + "\n")
    while abs(x - sol()) >= tol:
        # print information
        print("n = " + str(n))
        print("x_n = " + str(x))
        error = abs(x - sol())
        print("e_n = " + str(abs(x - sol())))
        if (not len(errors) == 0):
            print("e_n / e_(n-1) = " + str(error / errors[n - 1]))
            print("e_n / e_(n-1)^2 = " + str(error / (errors[n - 1])**2))
            print("e_n / e_(n-1)^3 = " + str(error / (errors[n - 1])**3) + "\n")
        else:
            print()
        errors.append(error)
        # perform algorithm
        x = x1 - func(x1) * ((x1 - x0)/(func(x1)- func(x0)))
        x0 = x1
        x1 = x
        n += 1
    print("x_n = " + str(x))
 
if __name__ == "__main__":
    secant()