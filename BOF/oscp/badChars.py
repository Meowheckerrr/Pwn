
#print()




charArray = []
for x in range(1, 256):
    charArray.append(f"\\x + {:02x}.format(x)")
print(charArray)

