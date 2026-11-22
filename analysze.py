def welcomeuser():
    print("Welcome to Text-analysis-tool, i will mine and analyze a body of text from a file you give me")
# Get username
def getusername():
     # print message to prompt user to enter username

    usernamefrominput = input("\nTo, begin please enter your user name\n")
    return usernamefrominput

#greet the user

def greetuser(name):
    
    print('Hello, ' + name)

welcomeuser()
username = getusername()
greetuser(username)
