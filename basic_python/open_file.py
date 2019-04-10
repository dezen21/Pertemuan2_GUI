myfile = open("perangkat.txt")
content = myfile.read()
myfile.close()
print(content)
print()

filegw = open("prodi.txt")
konten = filegw.read()
filegw.close()
print(konten)
print()

pins = {"Lisa","Jennie","Rose","Ji-Soo"}
for pin in pins:
print(pin)
fileane = open("fruit.txt")
con = fileane.read()
fileane.close()
