def networks():
    import os
    import Docker
    x = 0
    while x != 7 :
        os.system("clear")
        os.system("tput setf 4")
        os.system("tput setaf 2")
        os.system("tput bold")
        print('''
        \t\t\t\t######     ########  ########  ##   ##  ########  ########
        \t\t\t\t##   ###   ##    ##  ##        ##  ##   ##        ##    ##
        \t\t\t\t##    ###  ##    ##  ##        ## ##    ##        ##    ##
        \t\t\t\t##    ###  ##    ##  ##        ####     #####     ########
        \t\t\t\t##    ###  ##    ##  ##        ## ##    ##        ##  ##  
        \t\t\t\t##   ###   ##    ##  ##        ##  ##   ##        ##   ## 
        \t\t\t\t######     ########  ########  ##   ##  ########  ##    ##
        \n\n''')
        os.system("tput setaf 4")
        os.system("tput smul")
        print("\t\t\t\t\t\tWELCOME TO DOCKER NETWORK MANAGEMENT\n")
        os.system("tput setaf 6")
        os.system("tput rmul")
        print('''
Press 1 : To create a Network
Press 2 : To show the list of all Network
Press 3 : To inspect a Network
Press 4 : To remove a Network
Press 5 : To show IP routing table
Press 6 : To GO BACK to Main Menu
Press 7 : To EXIT\n''')
        os.system("tput setaf 3")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 7")

        if ( x == 1 ):
            name=input("Enter the name of Network : ")
            os.system("docker network create {}".format(name))
            print("Network created successfully")
        elif ( x == 2 ):
            print("List of docker Networks..... \n")
            os.system("docker network ls")
        elif ( x == 3 ):
            name=input("Enter the name of Network : ")
            os.system("docker network inspect {}".format(name))
        elif ( x == 4 ):
            name=input("Enter the name of Network : ")
            os.system("docker network rm -f {}".format(name))
            print("Network removed successfully")
        elif ( x == 5 ):
            os.system("route -n")
        elif ( x == 6 ):
            Docker.docker()
        elif ( x == 7 ):
            exit()
        os.system("tput setaf 3")
        y=input("\n\nEnter to continue.......")
