from os import system, name  
from time import sleep  
 
def clear():  
 
 if name == 'nt':  # for windows
    system('cls')  
 else:  
    system('clear')  