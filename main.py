import os
import sys
print("      |\      _,,,---,,_")
print("ZZZzz /,`.-'`'    -.  ;-;;,_           I need Chrome browser to work!")
print("     |,4-  ) )-,_. ,\ (  `'-'")
print("    '---''(_/--'  `-'\_)  ")

Username = "supleo"
Password = "Kddioso_s11"

Login = input("Do you want to log in? y/n :  ")

if Login == "y":
    pass
else: sys.exit()

try:        
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import pandas as pd
    import platform
except ImportError as e:
    print("Import Error ({e}), now importing some packages that need to be installed. If pip isn't installed, please install it \n")
    os.system('cmd /k "pip install selenium"')
    os.system('cmd /k "pip install platform"')
    os.system('cmd /k "pip install panda"')
if not platform.system() == "Windows": print("You are not using Windows, Errors may occure")

driver = webdriver.Chrome()
driver.get("http://service.bfi-kaernten.at/LVS/login.aspx")
UserTextbox = driver.find_element(by=By.NAME, value="Login1:tbBenutzername")
UserTextbox.send_keys(Username)

PasswordTextbox = driver.find_element(by=By.NAME, value="Login1:tbKennwort")
PasswordTextbox.send_keys(Password)

SubmitButton = driver.find_element(by=By.NAME, value="Login1:Button1")
SubmitButton.click()

if driver.find_element(by=By.ID, value="_ct13_Meinstatus2_ddStatus"):
    SignButton = driver.find_element(by=By.ID, value="_ct13_Meinstatus2_ddStatus")
    SignButton.click()
print("         _nnnn_                      ")
print("        dGGGGMMb     ,"""""""""""""".")
print("       @p~qp~~qMb    | BYE! |        ")
print("       M|@||@) M|   _;..............'")
print("       @,----.JM| -'")
print("      JS^\__/  qKL")
print("     dZP        qKRb")
print("    dZP          qKKb")
print("   fZP            SMMb")
print("   HZM            MMMM")
print("   FqM            MMMM")
print(" __|´´ .        | \dS``qML")
print(" |    `.       | `' \Zq")
print("_)      \.___.,|     .'")
print("\____   )MMMMMM|   .'")
print("     `-'       `--' hjm")







if driver.find_element(by=By.ID, value="_ctl3_Meinstatus2_lbStatus"):
    print("Already signed into LVS today :)") 
    print("      .----.__")
    print("     / c  ^  _`;")
    print("     |     .--'")
    print("      \   ( ")
    print("      /  -.\ ")
    print("     / .   \  ")
    print("    /  \    |                  Thanks for using my program! Hope you have a great day.")
    print("   ;    `-. `. ")
    print("   |      /`'.`. ")
    print("   |      |   \ \ ")
    print("   |    __|    `' ")
    print("   ;   /   \ ")
    print("  ,'        | ")
    print(" (_`'---._ /--, ")
    print("   `'---._`'---..__ ")
    print("       `''''--, ) ")
    print("            _.-'`,` ")
    print("             ```` ")
