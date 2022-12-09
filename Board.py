import subprocess
from sys import platform


class Board:

    def __init__(self):
        self.__matrix = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                         [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                         [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                         [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

    def getPosition(self, x, y, z):
        return self.__matrix[x][y][z]

    def setPosition(self, x, y, z, val):
        self.__matrix[x][y][z] = val

    def findMax(self,level):
        index = [-1, -1, -1]

        # Print Matrix
        boardString = ''
        out = ''

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    
                    boardString += (' ' + str(self.__matrix[i][j][k]))

        print("Before",boardString)

        # Run cpp file

        

        if platform == "linux" or platform == "linux2":
            out = subprocess.run(["./cpp_executables/MinMax_"+str(level)], text=True, input=boardString,
                                 stdout=subprocess.PIPE).stdout
        elif platform == "darwin":
            out = subprocess.run(["./cpp_executables/MinMax_D"+str(level)], text=True, input=boardString,
                                 stdout=subprocess.PIPE).stdout
        elif platform == "win32":
            out = subprocess.run(["./cpp_executables/MinMax_"+str(level)+".exe"], text=True, input=boardString,
                                 stdout=subprocess.PIPE).stdout

        # Take input

        out = out.splitlines()
        index[0] = int(out[0])
        index[1] = int(out[1])
        index[2] = int(out[2])
        # index[3] = int(out[3])

        print("Ye dek",out)
        print("After",boardString)

        return index

    def isEmpty(self):
        for i in range(0, 4):
            for j in range(0, 4):
                for k in range(0, 4):
                  
                    if self.__matrix[i][j][k] == 0:
                        return True
        return False

    def isWin(self, val):

        # To check diagonal lines of the cube

        if self.__matrix[0][0][0] == val & self.__matrix[1][1][1] == val & self.__matrix[2][2][2] == val & self.__matrix[3][3][3] == val:
            return True

        if self.__matrix[0][0][3] == val & self.__matrix[1][1][2] == val & self.__matrix[2][2][1] == val & self.__matrix[3][3][0] == val:
            return True

        if self.__matrix[3][0][0] == val & self.__matrix[2][1][1] == val & self.__matrix[1][2][2] == val & self.__matrix[0][3][3] == val:
            return True

        if self.__matrix[3][0][3] == val & self.__matrix[2][1][2] == val & self.__matrix[1][2][1] == val & self.__matrix[0][3][0] == val:
            return True

        # To check straight lines

        poss = False
        for i in range(0, 4):
            for j in range(0, 4):

                temp = True
                for k in range(0, 4):
                    if self.__matrix[i][j][k] != val:
                        temp = False
                poss |= temp

                temp = True
                for k in range(0, 4):
                    if self.__matrix[i][k][j] != val:
                        temp = False
                poss |= temp

                temp = True
                for k in range(0, 4):
                    if self.__matrix[k][i][j] != val:
                        temp = False
                poss |= temp
                
#                 temp = True
#                 for k in range(0, 4):
#                     if self.__matrix[k][j][i] != val:
#                         temp = False
#                 poss |= temp
                
#                 temp = True
#                 for k in range(0, 4):
#                     if self.__matrix[j][i][k] != val:
#                         temp = False
#                 poss |= temp
                
#                 temp = True
#                 for k in range(0, 4):
#                     if self.__matrix[j][k][i] != val:
#                         temp = False
#                 poss |= temp

        # To check 2D Diagonal lines

        for i in range(0, 4):
            if self.__matrix[0][0][i] == val & self.__matrix[1][1][i] == val & self.__matrix[2][2][i] == val & self.__matrix[3][3][i] == val:
                return True

            if self.__matrix[3][0][i] == val & self.__matrix[2][1][i] == val & self.__matrix[1][2][i] == val & self.__matrix[0][3][i] == val:
                return True

            if self.__matrix[0][i][0] == val & self.__matrix[1][i][1] == val & self.__matrix[2][i][2] == val & self.__matrix[3][i][3] == val:
                return True

            if self.__matrix[3][i][0] == val & self.__matrix[2][i][1] == val & self.__matrix[1][i][2] == val & self.__matrix[0][i][3] == val:
                return True

            if self.__matrix[i][0][0] == val & self.__matrix[i][1][1] == val & self.__matrix[i][2][2] == val & self.__matrix[i][3][3] == val:
                return True

            if self.__matrix[i][3][0] == val & self.__matrix[i][2][1] == val & self.__matrix[i][1][2] == val & self.__matrix[i][0][3] == val:
                return True

        return poss

    def printBoard(self):
        for i in range(0, 4):
            print('Board : ' + str(i + 1))
            print('-------')
            for j in range(0, 4):
                print('|', end='')
                for k in range(0, 4):
                    if self.__matrix[i][j][k] == 0:
                        print(' ', end='|')
                    elif self.__matrix[i][j][k] == 1:
                        print('X', end='|')
                    else:
                        print('O', end='|')

                print()
                print('-------')

            print()
            print()
