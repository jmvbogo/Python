def PlndrmNmbrChckr():
    nmbr=int(input('Enter number:'))
    temp=nmbr
    rev=0

    while(nmbr>0):
        dig=nmbr%10
        rev=rev*10+dig
        nmbr=nmbr//10
    if(temp==rev):
        print('The number is a palindrome!')
    else:
        print('The number is not a palindrome!')

PlndrmNmbrChckr()
