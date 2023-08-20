from sys import *
from random import randint
a = [
    "L","l",
    "Z","z",
    "Y","y",
    "S","s",
    "O","o",
    "F","f",
    "T","t",
    "W","w",
    "A","a",
    "R","r",
    "E","e",
    "?","=",
    "*","@",
]
ra = 10
if len(argv) > 1:
    ra = int(argv[1])
for i in range(ra):
    print(a[randint(0,25)],end="")
