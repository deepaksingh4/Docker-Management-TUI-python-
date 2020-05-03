import os
import webbrowser
        
def intro():
    os.system("clear")
    os.system("tput setaf 1")
    print("\t\t\t\t\tDOCKER MANAGEMENT TUI ")
    os.system("tput setaf 7")    
    print("\t\t\t------------------------------------------------------------------")
    os.system("tput setaf 2")
    print("\t\t\t\t#################     MENU    ####################")
    os.system("tput setaf 7")
    print("\t\t\t\tA Docker Project by : Aishwary Madiwale, Deepak Singh")
    
  
def dockerinstall():
    os.system("sudo apt-get remove docker docker-engine docker.io")
    os.system("sudo apt install docker.io")
    os.system("sudo systemctl start docker")
    os.system("sudo systemctl enable docker")


def dockdelt():
    os.system("tput setaf 1")
    print(" Warning!!!!!! this action will remove docker from you system  and all the data assciated with it ")
    os.system("tput setaf 7")
    os.system("yum remove docker-ce")
    os.system("rm -rf /var/lib/docker")	

def deletedock():
    print("Enter the name or pid of the docker image that u want to delete")
    dockerid=input()
    os.system("docker image  rm -f {}".format(dockerid))


def dockimg():
    os.system("docker images")

def activeimg():
    os.system("docker ps")
    print("Would you like to stop the docker images??")
    os.system("tput setaf 1")
    print("Stopping images would result into abortion of all the processes")
    os.system("tput setaf 7")
    x=input("Would You Like To stop the containers ?? : Y= Yes , N= No")
    if x == 'yes' or x == 'y':
      print("please wait while we are stopping all the containers")
      os.system("docker container stop $(docker container ls -aq)")
    elif x == 'no' or x == 'n':
      print("Process Aborted")

def wordpress():
    os.system("docker-compose up -d")
    print("Type 'localhost:8000' in preffered browser to access this wordpress site")

def image():
    print("Enter the name of os that you want to download")
    osname=input()
    print("Please Wait while the image is being downloaded")
    os.system("sudo docker pull {}".format(osname)) 

def dockmonitor():
    os.system("npm install -g dockly")
    os.system("dockly")

def dockver():
    os.system("sudo docker --version")

def dockcontstart() :
	os.system("docker images")
	print("Enter the name for your container ")
	conname=input()
	print("Enter the name of the image you want to use for the container")
	imagename=input()
	print("Do You want the container to be run in background yes or no")
	option=input()
	if option == 'yes' or option == 'y':
		print("Please wait while we are launching the container ")
		os.system("docker container run -dit --name {} {}".format(conname,imagename))
	

		success=os.system("docker container  ls | grep {}".format(conname))
		if success != ' ' :
			print("Container has been launched")
		else :
			print("Error in launching container")
	elif option == 'no' or option == 'n':
		os.system("docker container run -it --name {} {}".format(conname,imagename))    
    

# start of the program
intro()

while True:
    intro()
    print("\tMenu")
    print("\t1. Install Docker")
    print("\t2. Download Docker Images")
    print("\t3. Set up a Wordpress server & Emby Media Server: ")
    print("\t4. Pull up Docker monitor")
    print("\t5. Delete docker images")
    print("\t6. Start a docker container")
    print("\t7. Check Docker Version")
    print("\t8. Check all Docker Images")
    print("\t9. Delete Docker ??")
    print("\t10. Check Active Containers ?")
    print("\t11. Exit TUI")
    print("\tSelect Your Option (1-11) ")
    m = int(input())
    if m == 1:
        dockerinstall()
    elif m == 2:
        image()
    elif m == 3:
        wordpress()
    elif m == 4:
        dockmonitor()
    elif m == 5:
        deletedock()
    elif m == 6:
        dockcontstart()
    elif m == 7:
        dockver()
    elif m == 8:
        dockimg()
    elif m == 9:
        dockdelt()
    elif m == 10:
        activeimg()
    elif m == 11:
        exit(0)
    else :
        print("Inavlid Input")
	
    input("Press Enter to Continue")
    os.system("clear")    
   
    
