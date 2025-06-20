
from colorama import init, Fore, Style
from rich.console import Console
import os
import sys
import time

#VARIABLE
greetings=Fore.BLACK+"Happy brithday to [yourname] !!"
console=Console()

#DEFINE SECTION
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#START SECTION
console.print("[green]================[green]")
console.print("[bold][green][YOUR TITLE][green][bold]" )
console.print("[green]================[green]")
time.sleep(2)
print('insert the correct code to open.')
time.sleep(2)
code=input("insert: ")

#EXECUTE SECTION 
if code=="[YOUR CODE]" : #<-- This is important
    console.print("[green]The code is correct[green]")
    time.sleep(2)
    clear_terminal()
    time.sleep(0.5)#<-- You can change this if you want
    for word in greetings:
     sys.stdout.write(word)
     sys.stdout.flush()
     time.sleep(0.15) #<-- You can change this if you want
else :
    print("The code is incorrect")
    print("Please try again.")



# for word in greetings:
#     sys.stdout.write(word)
#     sys.stdout.flush()
#     time.sleep(0.15) #<-- You can change this if you want

#END-note
##Please to be responsible if you want to edit or add something, don't add e.g malware, spyware, etc.
##casscode