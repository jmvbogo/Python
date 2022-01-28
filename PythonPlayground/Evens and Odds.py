import numpy as np
import sys

def EvensOdds():
    option=int(input('''Check for Even and Odds:
    1.) Run random numbers
    2.) Exit program
    Choice: '''))
    
    if option==1:
        nmbrs=np.random.randint(100, size=500)

        even=[n for n in nmbrs if n%2==0]
        odd=[n for n in nmbrs if n%2!=0]
        
        print('Even numbers: \n', even)
        print('Odd numbers: \n',odd)
        print('\n')
        
        return True
    elif option==2:
        sys.exit()
    else:
        print('*Please enter the correct choice*')

def main():
    while True:
        EvensOdds()
        
main()
