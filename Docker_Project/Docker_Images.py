def images():
    import os
    import Docker
    x = 0
    while x != 9 :
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
        print("\t\t\t\t\t\tWELCOME TO DOCKER IMAGES MANAGEMENT\n")
        os.system("tput setaf 6")
        os.system("tput rmul")
        print('''
Press 1 : To install a new Image
Press 2 : To upload a image
Press 3 : To show the list of all Images
Press 4 : To delete a Image
Press 5 : To rename a Image
Press 6 : To commit a Image from Container
Press 7 : To inspect a Image
Press 8 : To GO BACK to Main Menu
Press 9 : To EXIT\n''')
        os.system("tput setaf 3")
        x = int(input("Enter your choices : "))
        os.system("tput setaf 7")

        if ( x == 1 ):
            name=input("enter the name of image : ")
            os.system("docker pull {}".format(name))
            print("image installed successfully")
        elif ( x == 3 ):
            print("\nDocker images..... \n")
            os.system("docker images")
        elif ( x == 2 ):
            name=input("enter the name of image : ")
            os.system("docker push {}".format(name))
        elif ( x == 4 ):
            name=input("enter the name of image : ")
            os.system("docker rmi {}".format(name))
            print("image removed successfully")
        elif ( x == 5 ):
            name=input("enter the name of image : ")
            namei=input("enter the new name of image : ")
            os.system("docker tag {} {}".format(name,namei))
            print("image renamed successfully")
        elif ( x == 6 ):
            name=input("enter the name of container : ")
            namei=input("enter the name of image : ")
            os.system("docker commit {} {}".format(name,namei))
            print("image created successfully")
        elif ( x == 7 ):
            name=input("enter the name of image : ")
            os.system("docker image inspect {}".format(name))
        elif ( x == 8 ):
            Docker.docker()
        elif ( x == 9 ):
            exit()
        os.system("tput setaf 3")
        y=input("\n\nEnter to continue.......")
