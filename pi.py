calculation_limit = 10000000
start=3
i=1
cont=0
pre=+1
while(i<calculation_limit):
    cont=(i+1)*(i+2)*(i+3)
    start=start+4/cont*pre
    pre=pre*-1
    i=i+2
    print(start)
print(start)