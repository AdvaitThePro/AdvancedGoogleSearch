from time import sleep
import sys

print("""

 ________  ________  ___      ___ ________  ________   ________  _______   ________         
|\   __  \|\   ___ \|\  \    /  /|\   __  \|\   ___  \|\   ____\|\  ___ \ |\   ___ \        
\ \  \|\  \ \  \_|\ \ \  \  /  / | \  \|\  \ \  \\ \  \ \  \___|\ \   __/|\ \  \_|\ \       
 \ \   __  \ \  \ \\ \ \  \/  / / \ \   __  \ \  \\ \  \ \  \    \ \  \_|/_\ \  \ \\ \      
  \ \  \ \  \ \  \_\\ \ \    / /   \ \  \ \  \ \  \\ \  \ \  \____\ \  \_|\ \ \  \_\\ \     
   \ \__\ \__\ \_______\ \__/ /     \ \__\ \__\ \__\\ \__\ \_______\ \_______\ \_______\    
    \|__|\|__|\|_______|\|__|/       \|__|\|__|\|__| \|__|\|_______|\|_______|\|_______|    
                                                                                            
                                                                                            
                                                                                            
 ________  ________  ________  ________  ___       _______                                  
|\   ____\|\   __  \|\   __  \|\   ____\|\  \     |\  ___ \                                 
\ \  \___|\ \  \|\  \ \  \|\  \ \  \___|\ \  \    \ \   __/|                                
 \ \  \  __\ \  \\\  \ \  \\\  \ \  \  __\ \  \    \ \  \_|/__                              
  \ \  \|\  \ \  \\\  \ \  \\\  \ \  \|\  \ \  \____\ \  \_|\ \                             
   \ \_______\ \_______\ \_______\ \_______\ \_______\ \_______\                            
    \|_______|\|_______|\|_______|\|_______|\|_______|\|_______|                            
                                                                                            
                                                                                            
                                                                                            
 ________  _______   ________  ________  ________  ___  ___                                 
|\   ____\|\  ___ \ |\   __  \|\   __  \|\   ____\|\  \|\  \                                
\ \  \___|\ \   __/|\ \  \|\  \ \  \|\  \ \  \___|\ \  \\\  \                               
 \ \_____  \ \  \_|/_\ \   __  \ \   _  _\ \  \    \ \   __  \                              
  \|____|\  \ \  \_|\ \ \  \ \  \ \  \\  \\ \  \____\ \  \ \  \                             
    ____\_\  \ \_______\ \__\ \__\ \__\\ _\\ \_______\ \__\ \__\                            
   |\_________\|_______|\|__|\|__|\|__|\|__|\|_______|\|__|\|__|                            
   \|_________|                                                                             
                                                                                                                                 
""")
sleep(2)
get_data = True
ext = False
while get_data:
    print("""                                                                                                
Welcome to Advanced Google Search!

Select your Search category:
[1] Calculations
[2] Quick Data Conversion
[3] Currency Conversion
[4] Distance from one area to another
[5] Hotels
[6] Events
[7] Time in another area
[8] Customer support information
[9] Translate
[10] Stocks
[11] Sunrise in local time
[12] Your IP Address
[13] Holiday Dates
[14] Coding Docs      
[15] Exit Advanced Google Search
""")
    
    try:
        opt = int(input("Enter your search type: "))
        if opt > 15 or opt < 0:
            print("Invalid number. Please try again")
            sleep(3)
        elif opt == 15:
            print("Exiting Advanced Google Search......")
            sleep(3)
            get_data = False
            exit()
        else:
            print("Option captured!")
            get_data = False
    except:
        if get_data == True:
            print("Your input is not a number. Please try again.")
            sleep(3)


if opt == 1:
    print("""
 ________  ________  ___       ________  ___  ___  ___       ________  _________  ___  ________  ________   ________      
|\   ____\|\   __  \|\  \     |\   ____\|\  \|\  \|\  \     |\   __  \|\___   ___\\  \|\   __  \|\   ___  \|\   ____\     
\ \  \___|\ \  \|\  \ \  \    \ \  \___|\ \  \\\  \ \  \    \ \  \|\  \|___ \  \_\ \  \ \  \|\  \ \  \\ \  \ \  \___|_    
 \ \  \    \ \   __  \ \  \    \ \  \    \ \  \\\  \ \  \    \ \   __  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \ \_____  \   
  \ \  \____\ \  \ \  \ \  \____\ \  \____\ \  \\\  \ \  \____\ \  \ \  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \|____|\  \  
   \ \_______\ \__\ \__\ \_______\ \_______\ \_______\ \_______\ \__\ \__\   \ \__\ \ \__\ \_______\ \__\\ \__\____\_\  \ 
    \|_______|\|__|\|__|\|_______|\|_______|\|_______|\|_______|\|__|\|__|    \|__|  \|__|\|_______|\|__| \|__|\_________\
                                                                                                              \|_________|
                                                                                                
        """)
    try:
        x = int(input("Enter value of x: "))
        operator = int(input("""
Operator Directory:
[1] Addition
[2] Division
[3] Multiplication
[4] Subtraction
[5] Power
[6] Modulus
Enter operator number: """))
  
        y = int(input("Enter value of y: "))
    except:
        sys.exit("ValueError: Non-Integer type input. Please relaunch Advanced Google Search")

    if operator == 1:
        print(f"{str(x)} + {str(y)} = {str(x + y)}")
    elif operator == 2:
        print(f"{str(x)} ÷ {str(y)} = {str(x / y)}")
    elif operator == 3:
        print(f"{str(x)} × {str(y)} = {str(x * y)}")
    elif operator == 4:
        print(f"{str(x)} - {str(y)} = {str(x - y)}")
    elif operator == 5:
        print(f"{str(x)} ** {str(y)} = {str(x ** y)}")
    elif operator == 6:
        print(f"{str(x)} % {str(y)} = {str(x % y)}")
    else:
        sys.exit("Internal Error: Operator index out of range. Please relaunch Advanced Google Search")
    