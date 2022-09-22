abecedario = []
for x in range(ord('a'), ord('a')+26):
    abecedario.append(chr(x))
    
print(abecedario)
del abecedario[3-1::3]
print(abecedario)