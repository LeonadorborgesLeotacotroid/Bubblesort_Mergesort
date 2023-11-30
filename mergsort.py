def CrearSubArreglo(A, inIzq, inDer):
    return A[inIzq:inDer]

def Merge(A, p, q, r):
    Izq = CrearSubArreglo(A, p, q)
    Der = CrearSubArreglo(A, q, r)
    i = 0
    j = 0
    for k in range(p, r):
        if (j >= len(Der)) or (i < len(Izq) and Izq[i] < Der[j]):
            A[k] = Izq[i]
            i += 1
        else:
            A[k] = Der[j]
            j += 1

def MergeSort(A, p, r):
    if r - p > 1:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q, r)
        Merge(A, p, q, r)

if __name__ == "__main__":
    A = [15, 67, 8, 16, 44, 27, 12, 35]
    print("Lista original:", A)

    MergeSort(A, 0, len(A))
    print("Lista ordenada:", A)
