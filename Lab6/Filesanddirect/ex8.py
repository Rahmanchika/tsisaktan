import os

path = "C:/Users/pc/Documents/aktantsis/Lab6/Filesanddirect/atoz/Z.txt"

if os.access(path, os.F_OK):
    os.remove(path)