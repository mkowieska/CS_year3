import math

#dodawanie macierzy,
def dodanie_m(matrix1, matrix2): #Dodaje dwie macierze.
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Macierze musza byc tego samego rozmiaru.")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result #list of lists: Macierz będąca wynikiem dodawania.

#dodawanie stałej do macierzy,
def dodanie_stalej_do_m(matrix, constant):
    result = []
    for row in matrix:
        new_row = [element + constant for element in row]
        result.append(new_row)
    return result

#mnożenie macierzy,
def mnozenie_m(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Liczba kolumn pierwszej macierzy musi byc rowna liczbie wierszy drugiej")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            value = 0
            for k in range(len(matrix2)):
                value += matrix1[i][k] * matrix2[k][j]
            row.append(value)
        result.append(row)
    return result #Macierz będąca wynikiem mnożenia.

#mnożenie macierzy przez skalar,
def mnozenie_m_przez_skalar(matrix, scalar):
    result = []
    for row in matrix:
        new_row = [element * scalar for element in row]
        result.append(new_row)
    return result

#iloczyn Hadamarda (iloczyn po współrzędnych),
def iloczyn_hadamarda(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Macierze musza byc tego samego rozmiaru")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] * matrix2[i][j])
        result.append(row)
    return result

#iloczyn Kroneckera (iloczyn prosty).
def iloczyn_kroneckera(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            new_row = [element * matrix1[i][j] for element in matrix2]
            row.extend(new_row)
        result.extend([row] * len(matrix2))
    return result

