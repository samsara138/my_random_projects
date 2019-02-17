#external modual:PyKeyboard
import time
from pykeyboard import PyKeyboard

#count down to give time for user to move his cursour
def count_down(second):
    for i in range(second,0,-1):
        print("count down: "+ str(i))
        time.sleep(1)

#inputing number through keyboard giving a range of number
def crackA(start,end):
    key = PyKeyboard()
    for i in range(start,end):
        temp = [str(x) for x in str(i)]
        for number in temp:
            key.tap_key(str(number))
        key.tap_key('\r')
        key.tap_key('\r')

#inputing password through keyboard giving a wordlist
def crackB(passlist):
    key = PyKeyboard()
    for i in passlist:
        temp = list(i)
        for letter in temp:
            key.tap_key(str(letter))
        key.tap_key('\r')
        key.tap_key('\r')

#read passlist from file
def InList(InFileHandle):
    passlist = []
    with open(InFileHandle,'r') as file:
        for line in file:
            passlist.append(line[:-1])
    return passlist

def main():
    print("start of program")
    print("winrar cracker")
    print("while counting down, left click cracking place")
    print("select a method to import wordlist")
    choice = int(input("(1)number range (2)txt file: "))
    if(choice == 1):
        start = int(input("input start of range: "))
        end = int(input("input end of range: "))+1
        count_down(3)
        crackA(start,end)

    elif(choice == 2):
        file_name = str(input("input the name of wordlist: "))
        list = InList(file_name)
        count_down(3)
        crackB(list)
    else:
        print("error input")
    print("job done")

if __name__ == "__main__":
    main()
