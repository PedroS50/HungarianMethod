from math import inf

def mPrint(matrix):
    for x in matrix:
        print(x)
    print()

def hungarianMethod(matrix):
    originalMatrix = []
    for i in range(0, len(matrix)):
        originalMatrix.append([])
        for col in matrix[i]:
            originalMatrix[i].append(col)

    print("Initial matrix:")
    mPrint(matrix)
    ##################################################
    # Step1
    for index in range(0, len(matrix)):
        lineMin = min(matrix[index])
        matrix[index] = [elem - lineMin for elem in matrix[index]]

    print("Matrix after step 1:")
    mPrint(matrix)
    ##################################################

    ##################################################
    # Step2
    for index in range(0, len(matrix)):
        columnMin = min([row[index] for row in matrix])
        for x in matrix:
            x[index] -= columnMin

    print("Matrix after step 2:")
    mPrint(matrix)
    ##################################################

    ##################################################
    # Step3
    #matrix= [ [0,0,0,1], [3,0,4,1], [9,4,0,0], [1,0,1,7] ]
    #matrix= [ [0,1,0,1], [2,0,3,0], [9,5,0,0], [0,0,0,6] ]

    while (True):
        rowLines = []
        columnLines = []
        cLinesDict = dict()
        rLinesDict = dict()
        
        #while (True):
        for totalZeros in range(len(matrix), 0, -1):
            columnFlag = True
            rowFlag = True
            while (columnFlag or rowFlag):
                # Check columns
                maxZeros = 0
                cLinesDict = dict()
                columnFlag = False
            
                for index in range(0, len(matrix)):
                    # If the index is already in columnLines, no need to repeat the process
                    if index in columnLines:
                        continue
                    
                    column = [row[index] for row in matrix]
                    nZeros = column.count(0)
                    #   If there are 0's in the line
                    if nZeros > 0: 
                        # For each member of column
                        for e in range(0, len(column)):
                            # If that zero is already being covered by a rowLine, it isn't considered for calculating the solution
                            if column[e] == 0 and e in rowLines:
                                nZeros-=1
                    
                    if nZeros != totalZeros:
                        continue
                    columnFlag = True

                    if nZeros > maxZeros:
                        cLinesDict[index] = nZeros
                        maxZeros = nZeros

                # Check rows
                maxZeros = 0
                rLinesDict = dict()
                rowFlag = False
            
                for index in range(0, len(matrix)):
                    if index in rowLines:
                        continue
                    row = matrix[index]
                    nZeros = row.count(0)

                    if nZeros > 0:
                        for e in range(0, len(row)):
                            if row[e] == 0 and e in columnLines:
                                nZeros-=1

                    if nZeros != totalZeros:
                        continue
                    rowFlag = True

                    if nZeros > maxZeros:
                        rLinesDict[index] = nZeros
                        maxZeros = nZeros

                cSum = sum(cLinesDict.values())
                rSum = sum(rLinesDict.values())
                if (cSum > rSum):
                    for coll in cLinesDict.keys():
                        columnLines.append(coll) 
                else:
                    for roww in rLinesDict.keys():
                        rowLines.append(roww)
                #print(columnLines)
                #print(rowLines)
                #print()

            # Check if all zeros are covered
            #complete = True
            #for r in range(0, len(matrix)):
            #    for c in range(0, len(matrix)):
            #        if matrix[r][c] == 0 and (r not in rowLines and c not in columnLines):
            #            complete = False
                        #mPrint(matrix)
                        #print(r, " in ", rowLines)
                        #print(r not in rowLines)
                        #print(rowLines)
                        #print(columnLines)
                        #print(r,",",c)
                        #print()

            #if (complete):
            #    break
            #print(columnLines)
            #print(rowLines)

        if len(rowLines) + len(columnLines) == len(matrix):
            break

        ##################################################
        # Step4

        # Create auxiliar matrix
        auxMatrix = []
        for i in range(0, len(matrix)):
            auxMatrix.append([])
            for col in matrix[i]:
                auxMatrix[i].append(col)

        rowLines.sort(reverse=True)
        columnLines.sort(reverse=True)
        # Remove all lines that are rows
        if rowLines != []:
            for r in rowLines:
                auxMatrix.pop(r)

        # Remove all lines that are columns
        if columnLines != []:
            for line in auxMatrix:
                for col in columnLines:
                    line.pop(col)

        # Retrieve the minimum value from all "open" matrix elements
        matrixMin = inf
        for row in auxMatrix:
            if min(row) < matrixMin:
                matrixMin = min(row)

        # Subtract minimum value from all "open" matrix elements and add minimum value to all matrix elements intersect by 2 lines
        for r in range(0, len(matrix)):
            for c in range(0, len(matrix)):
                if r not in rowLines and c not in columnLines:
                    matrix[r][c] -= matrixMin
                if r in rowLines and c in columnLines:
                    matrix[r][c] += matrixMin
        ##################################################
    print("Optimal matrix: ")
    mPrint(matrix)
    ##################################################
    '''
    ##################################################
    # Step5
    totalCost = 0

    while (True):
        assignMin = inf
        minCoord = (-1, -1)
        for r in range(0, len(matrix)):
            for c in range(0, len(matrix)):
                if matrix[r][c] < assignMin:
                    assignMin = matrix[r][c]
                    minCoord = (r, c)
        totalCost += originalMatrix[ minCoord[0], minCoord[1] ]
    '''

        
    ##################################################
if __name__ == "__main__":
    matrix = [ [4,2,5,7], [8,3,10,8], [12,5,4,5], [6,3,7,14] ]
    hungarianMethod(matrix)