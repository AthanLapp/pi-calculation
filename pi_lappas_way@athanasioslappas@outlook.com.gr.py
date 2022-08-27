pi=0
#For distance 0 
size=100000
accuracypi=28*size
for i in range(0,accuracypi):
    pi=i+i
print("pi with set accuracy = '?'-> to", pi*accuracypi/(2*accuracypi)/(9*size))
