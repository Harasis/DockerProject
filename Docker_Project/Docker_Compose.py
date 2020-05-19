def compose():
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
        print("\t\t\t\t\t\tWELCOME TO DOCKER COMPOSE MANAGEMENT\n")
        os.system("tput setaf 6")
        os.system("tput rmul")
        print('''
Press 1 : To open the compose file
Press 2 : To show the content of compose file
Press 3 : To run docker compose to start
Press 4 : To run docker compose to stop 
Press 5 : To GO BACK to Main Menu
Press 6 : To EXIT\n''')
        os.system("tput setaf 3")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 7")

        if ( x == 1 ):
            os.system("vim docker-compose.yml")
        elif ( x == 2 ):
            os.system("cat docker-compose.yml")
        elif ( x == 3 ):
            os.system("docker-compose up -d")
        elif ( x == 4 ):
            os.system("docker-compose stop")
        elif ( x == 5 ):
            Docker.docker()
        elif ( x == 6 ):
            exit()
        os.system("tput setaf 3")
        y=input("\n\nEnter to continue.......")
