import numpy as np

def gss(f, xl, xu, tol=1e-5):
    y1 = f(xl)
    yu = f(xu)

    I = xu - xl
    gr = (np.sqrt(5) - 1) / 2
    xa = xu - gr * I
    xb = xl - gr * I
    ya = f(xa)
    yb = f(xb)

    while(abs(xb - xl) >= tol*(abs(xa) + abs(xu))):
        if ya > yb:
            xl = xa
            yl = ya
            xa = xb
            ya = yb
            I = gr * I
            xb = xl + gr * I
            yb = f(xb)
        else:
            xu = xb
            yu = yb
            xb = xa
            yb = ya
            I = gr * I
            xa = xu - gr * I
            ya = f(xa)

    if (ya > yb):
        ymin = yb
        xmin = xb
    else:
        ymin = ya
        xmin = xa

    return xmin, ymin