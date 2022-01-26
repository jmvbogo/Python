import numpy as np

def EvensOdds():
    nmbrs=np.random.randint(100, size=500)

    even=[n for n in nmbrs if n%2==0]
    odd=[n for n in nmbrs if n%2!=0]
    
    print('Even numbers: \n', even)
    print('Odd numbers: \n',odd)
    
EvensOdds()
