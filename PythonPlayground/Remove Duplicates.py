import numpy as np

def RemoveDuplicates():
    nmbrs=np.random.randint(10, size=20)
    doops_removed=list(set(nmbrs))

    print(f'Random list of numbers: \n {nmbrs}')
    print(f'Duplicate numbers removed: \n {doops_removed}')
    

RemoveDuplicates()
