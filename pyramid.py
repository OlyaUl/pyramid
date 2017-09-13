#! env bin/python
# codding = utf-8
import random
from random import random

if __name__ == "__main__":

    def tri():
        n = 7
        a = []
        for i in range(n):
            b = []
            for j in range(i+1):
                b.append(int(random() * 11))
            a.append(b)
        return a

    triangle1 = tri()
    print(triangle1)


    def pyramid(triangle):
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    print(pyramid(triangle1))
