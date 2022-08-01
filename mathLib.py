# Libreria personal matematica
# Sara Paguaga 20634

def mm(m1, m2):

        l_M1 = len(m1)
        l_M1_in, l_M2_in = len(m1[0]), len(m2[0])
        matrixR = []

        for rM1 in range(l_M1):
            new = []
            for cM2 in range(l_M2_in):
                new.append(sum(m1[rM1][rM2] * m2[rM2][cM2] for rM2 in range(l_M1_in)))
            matrixR = matrixR + [new]

        return matrixR