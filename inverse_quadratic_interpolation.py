import sys
import math

def func(x):
    return math.sin(x) # change as needed

def sol():
    return math.pi # change as needed

def inverse_quadratic_interpolation():
    # initialization
    errors = []
    x0 = float(sys.argv[1])
    x1 = float(sys.argv[2])
    x2 = float(sys.argv[3])
    tol = float(sys.argv[4])
    x = x2
    n = 0
    print("Chosen inputs:")
    print("x0 = " + str(x0))
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))
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
        fx0 = func(x0)
        fx1 = func(x1)
        fx2 = func(x2)
        L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
        L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
        L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
        x = L0 + L1 + L2
        x0, x1, x2 = x, x0, x1
        n += 1

if __name__ == "__main__":
    inverse_quadratic_interpolation()