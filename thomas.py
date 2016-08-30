import numpy as np

def tridiagonal(md, ud, ld, b):

    N = md.size
    
    x = np.empty_like(b)

    for i in range(1, N):
        # We remove de lower diagonal and upper one remains
        # equal.
        # Starting the indexing in 1 we preserve md[0]
        # and b[1].
        md[i] = md[i] - (ld[i - 1] * ud[i - 1]) / md[i - 1]

        b[i] = b[i] - (b[i - 1] * ld[i]) / md[i - 1]

    # Solving

    x[-1] = b[-1] / md[-1]
        
    for i in range(N - 2, -1, -1):

        x[i] = (b[i] - ud[i] * x[i + 1]) / md[i]
        
    return x
