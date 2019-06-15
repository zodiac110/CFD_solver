from Packages import *


def FACTORIAL (n):
    fact = 1
    for i in range(n):
        fact = fact*(i+1)
    return (fact)


def FD_GEN (stencil,order):

    accuracy = stencil.size - 1
    # semi = (accuracy/2)
    D = np.zeros(accuracy+1)
    D[order] = FACTORIAL(order)
    S = np.zeros([accuracy+1,accuracy+1])
    for i in range(accuracy+1):
        S[i] = stencil**i
    if((np.linalg.det(S))==0):
        print("[FD.FORMULA_GEN] : singular matrix formed for stencil\n",stencil,"\n\n",S)
        formula = np.zeros_like(D)
    else:
        formula = np.linalg.solve(S,D)
    return(formula)


def STENCIL_GEN (size,accuracy,bc_type):

    semi = int(accuracy/2)
    stencil = np.zeros([size,accuracy+1])

    for i in range(size):

        if (i<semi):
            if (bc_type[0] == "one-sided"):
                stencil[i] = np.arange(0,accuracy+1)
            elif (bc_type[0] == "periodic"):
                stencil[i] = np.arange(i-semi,i+semi+1)
            elif (bc_type[0] == "reflect-even"):
                stencil[i] = np.pad(np.arange(0,i+semi+1),(semi-i,0),'reflect')
            elif (bc_type[0] == "symmetric-even"):
                stencil[i] = np.pad(np.arange(0,i+semi+1),(semi-i,0),'symmetric')
            elif (bc_type[0] == "edge"):
                stencil[i] = np.pad(np.arange(0,i+semi+1),(semi-i,0),'edge')

        elif (i>=size-semi):
            if (bc_type[1] == "one-sided"):
                stencil[i] = np.arange(size-accuracy-1,size)
            elif (bc_type[1] == "periodic"):
                stencil[i] = np.arange(i-size-semi,i-size+semi+1)
            elif (bc_type[1] == "reflect-even"):
                stencil[i] = np.pad(np.arange(i-size-semi,0),(0,semi-size+i+1),'reflect')
            elif (bc_type[1] == "symmetric-even"):
                stencil[i] = np.pad(np.arange(i-size-semi,0),(0,semi-size+i+1),'symmetric')
            elif (bc_type[1] == "edge"):
                stencil[i] = np.pad(np.arange(i-size-semi,0),(0,semi-size+i+1),'edge')

        else:
            stencil[i] = np.arange(i-semi,i+semi+1)

    return(stencil.astype(int))


def FORMULA_GEN (size,accuracy,order,bc_type):

    semi = int(accuracy/2)
    formula = np.zeros([size,accuracy+1])

    for i in range(size):

        if (i<semi):
            if (bc_type[0] == "one-sided"):
                formula[i] = FD_GEN(np.arange(-i,accuracy-i+1),order)
            else:
                formula[i] = FD_GEN(np.arange(-semi,semi+1),order)

        elif (i>=size-semi):
            if (bc_type[1] == "one-sided"):
                formula[i] = FD_GEN(np.arange(-(accuracy+1)+(size-i),(size-i)),order)
            else:
                formula[i] = FD_GEN(np.arange(-semi,semi+1),order)

        else:
            formula[i] = FD_GEN(np.arange(-semi,semi+1),order)

    return(formula)


def MD_GEN (formula,bc_type):

    accuracy = formula.shape[1]-1
    size = formula.shape[0]
    semi = int(accuracy/2)
    id_d = np.zeros_like(formula)

    for i in range(size):

        if (i<semi):
            if (bc_type[0] == "one-sided"):
                id_d[i][i] = 1
            else:
                id_d[i][semi] = 1

        elif (i>=size-semi):
            if (bc_type[1] == "one-sided"):
                id_d[i][i-size] = 1
            else:
                id_d[i][semi] = 1

        else:
            id_d[i][semi] = 1

    # print(id_m)

    id_m = 1-id_d

    multiplier = id_m*formula
    divider = id_d*formula

    return(multiplier,divider)


def DS ():

    return(ds)

