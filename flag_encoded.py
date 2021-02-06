from base64 import *


file_path = "path to encoded flag goes here"
file =open(file_path, "r+")
file = str(file.readlines())
file = file[2:-2]

for x in range(5):
    file = b16decode(file)
for x in range(5):
    file = b32decode(file)
for x in range(5):
    file = b64decode(file)


print(file)