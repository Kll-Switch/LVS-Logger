import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#Write your stuff into the Quotation Marks
Username = "Your Username here"  
Password = "Your Password here"  
startUpAscii = ["      |\      _,,,---,,_", "ZZZzz /,`.-'`'    -.  ;-;;,_           I need Chrome browser to work! (or maybe not idk)", "     |,4-  ) )-,_. ,\ (  `'-'", "    '---''(_/--'  `-'\_)  "]
exitAscii = ["         _nnnn_                      ", "        dGGGGMMb     ,"""""""""""""".", "       @p~qp~~qMb    | BYE!         |        ",
              "       M|@||@) M|   _;..............'","       @,----.JM| -'",  "      JS^\__/  qKL", "     dZP        qKRb", "   fZP            SMMb","   HZM            MMMM",
                "   FqM            MMMM", " __|´´ .        | \dS``qML", " |    `.       | `' \Zq", "_)      \.___.,|     .'", "\____   )MMMMMM|   .'", "     `-'       `--' hjm"]
alreadySigned = [
    "Already signed into LVS today :)",
    "      .----.__",
    "     / c  ^  _`;",
    "     |     .--'",
    "      \\   ( ",
    "      /  -.\\ ",
    "     / .   \\  ",
    "    /  \\    |                  Thanks for using my program! Hope you have a great day.",
    "   ;    `-. `. ",
    "   |      /`'.`. ",
    "   |      |   \\ \\ ",
    "   |    __|    `' ",
    "   ;   /   \\ ",
    "  ,'        | ",
    " (_`'---._ /--, ",
    "   `'---._`'---..__ ",
    "       `''''--, ) ",
    "            _.-'`,",
    "             ```` "
]
def startUp(): 
    for line in startUpAscii: 
        print(line)


    Login = input("Do you want to log in? y/n :  ")

    if Login == "y":
        logOn()
    else: sys.exit()


def logOn():
    driver = webdriver.Chrome()
    driver.get("http://service.bfi-kaernten.at/LVS/login.aspx")
    UserTextbox = driver.find_element(by=By.NAME, value="Login1:tbBenutzername")
    UserTextbox.send_keys(Username)

    PasswordTextbox = driver.find_element(by=By.NAME, value="Login1:tbKennwort")
    PasswordTextbox.send_keys(Password)

    SubmitButton = driver.find_element(by=By.NAME, value="Login1:Button1")
    SubmitButton.click()
    if driver.find_element(by=By.NAME, value="_ctl3:Meinstatus2:Button1"):
        SignButton = driver.find_element(by=By.NAME, value="_ctl3:Meinstatus2:Button1")
        SignButton.click()
        for line in exitAscii: 
          print(line)







    if driver.find_element(by=By.ID, value="_ctl3_Meinstatus2_lbStatus"):
        for line in alreadySigned: 
            print(line)


    driver.close()
    input()



if __name__ == "__main__":
    startUp()