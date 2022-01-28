#pip install speedtest-cli
import speedtest
import sys

def internet_speed_checker():
    st=speedtest.Speedtest()

    option=int(input('''Internet Speed Checker:
    1.) Download speed
    2.) Upload Speed
    3.) Ping
    4.) All
    5.) Quit Program 
    Choice: '''))
    print('\n')

    if option==1:
        print('*Testing Download Speed*')
        print('Download Speed: ',st.download(),'\n')
        return True
    elif option==2:
        print('*Testing Upload Speed*')
        print('Upload speed: ',st.upload(),'\n')
        return True
    elif option==3:
        print('*Checking Server*')
        servername=[]
        st.get_servers(servername)
        print('*Testing Ping*')
        print('Ping: ',st.results.ping,'\n')
        return True
    elif option==4:
        print('*Testing Download Speed*')
        print('Download Speed: ',st.download(),'\n')
        print('*Testing Upload Speed*')
        print('Upload speed: ',st.upload(),'\n')
        print('*Checking Server*')
        servername=[]
        st.get_servers(servername)
        print('*Testing Ping*')
        print('Ping: ',st.results.ping,'\n')
        return True
    elif option==5:
        sys.exit()
    else:
        print('*Please enter the correct choice*')


def main():
    while True:
        internet_speed_checker()

main()
