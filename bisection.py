import sys
import math

def func(x):
    return math.sin(x) # change as needed

def sol():
    return math.pi # change as needed

def bisection():
    # initialization
    errors = []
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    tol = float(sys.argv[3])
    print("Chosen inputs:")
    print("a = " + str(a))
    print("b = " + str(b))
    print("tolerance = " + str(tol) + "\n")
    x = a
    n = 0
    while (abs(x - sol()) >= tol):
        # print information
        print("n = " + str(n))
        print("x_n = " + str(x))
        error = abs(x - sol())
        print("e_n = " + str(abs(x - sol())))
        if (not len(errors) == 0):
            print("e_n / e_(n-1) = " + str(error / errors[n - 1]))
            print("e_n / e_(n-1) = " + str(error / (errors[n - 1])**2))
            print("e_n / e_(n-1) = " + str(error / (errors[n - 1])**3) + "\n")
        else:
            print()
        errors.append(error)
        # Perform algorithm
        x = (a+b)/2
        if (func(x)*func(a) < 0):
            b = x
        else:
            a = x
        n += 1

if __name__ == "__main__":
    bisection()