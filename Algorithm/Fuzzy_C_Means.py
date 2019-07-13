# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def getMatriksU(clusterNum, dataSize):
    for i in range(dataSize):
        row = clusterNum
        for j in range(clusterNum):
            row[j] = random.randdouble(1,101)
    matrixU.add(row)
    return matrixU