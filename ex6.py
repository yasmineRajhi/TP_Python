import random
ADN =["A","C","G","T"]
def ex6(ADN):
    for i in ADN:
        return(random.choices(ADN,k=12))
print(ex6(ADN))