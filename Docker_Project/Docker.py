def docker():
    import os
    import Docker_services
    import Docker_Containers
    import Docker_Images
    import Docker_Networks
    import Docker_Volumes
    import Docker_Compose
    x = 0
    while (x != 7) :
        os.system("clear")
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
        print("\t\t\t\t\t\tWELCOME TO DOCKER HELPER GUIDE\n")
        os.system("tput rmul")
        os.system("tput setaf 6")
        print('''
Press 1 : For Docker Services
Press 2 : For Docker Containers
Press 3 : For Docker Images
Press 4 : For Docker Networks
Press 5 : For Docker Volumes
Press 6 : For Docker Compose
Press 7 : To EXIT \n''')
        os.system("tput setaf 3")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 7")
        if ( x == 1 ):
            Docker_services.services()
        elif ( x == 2 ):
            Docker_Containers.containers()
        elif ( x == 3 ):
            Docker_Images.images()
        elif ( x == 4 ):
            Docker_Networks.networks()
        elif ( x == 5 ):
            Docker_Volumes.volumes()
        elif ( x == 6 ):
            Docker_Compose.compose()
        elif ( x == 7 ):
            exit()
docker()
