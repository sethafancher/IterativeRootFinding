import sys
import math

def func(x):
    return math.sin(x) # change as needed

def sol():
    return math.pi # change as needed

def steffensen():
    # initialization
    errors = []
    x = float(sys.argv[1])
    tol = float(sys.argv[2])
    print("Chosen inputs:")
    print("x_n = " + str(x))
    print("tolerance = " + str(tol) + "\n")
    n = 0
    while(abs(x - sol()) >= tol):
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
        g = ((func(x + func(x))) / func(x)) - 1
        x = x - (func(x)/g)
        n += 1

if __name__ == "__main__":
    steffensen()