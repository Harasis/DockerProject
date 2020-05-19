def volumes():
    import os
    import Docker
    x = 0
    while x != 6 :
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
        print("\t\t\t\t\t\tWELCOME TO DOCKER VOLUME MANAGEMENT\n")
        os.system("tput setaf 6")
        os.system("tput rmul")
        print('''
Press 1 : To create a Volume
Press 2 : To show the list of all Volume
Press 3 : To inspect a Volume
Press 4 : To remove a Volume
Press 5 : To GO BACK to Main Menu
Press 6 : To EXIT\n''')
        os.system("tput setaf 3")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 7")

        if ( x == 1 ):
            name=input("Enter the name of Volume : ")
            os.system("docker volume create {}".format(name))
            print("Volume created successfully")
        elif ( x == 2 ):
            print("List of docker Volumes..... \n")
            os.system("docker volume ls")
        elif ( x == 3 ):
            name=input("Enter the name of Volume : ")
            os.system("docker volume inspect {}".format(name))
        elif ( x == 4 ):
            name=input("enter the name of Volume : ")
            os.system("docker volume rm {}".format(name))
        elif ( x == 5 ):
            Docker.docker()
        elif ( x == 6 ):
            exit()
        os.system("tput setaf 3")
        y=input("\n\nEnter to continue.......")
