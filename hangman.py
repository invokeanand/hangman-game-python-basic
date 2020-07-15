# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

sleep(1) 
clear()
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print ("************************************")
print ("Let's play Hangman - Movie Version!")
movie="HAIDER"
movie=movie.upper()
length = len(movie)
print ("Movie Length-->",length)
print(" ")
print(" ")
print(" ")
print(" ")
print ("************************************")


def _create_a_list(len, value, pos, _list):
    _temp=[]
    j = 0
    for i in range(0, len):
        
        if i==pos[j]:
            _list[i] = value
            j = j+1
            #_list.append(value)
        elif _list[i] == "_":
            #_list.append("_")
            
            _list[i] = '_';
    _temp = _list        
    return _temp
        
_chances = 8
_blanks=["_"]*length  

#_blanks = _create_a_list(length, "a", -1, _blanks)
win_flag = "N"


for turn in range(0, _chances):
    
    _guess=input("Enter a letter or you can guess the entire word:")
    _guess=_guess.upper()
    if len(_guess) > 1:
        if str(_guess) == str(movie):
            print ("answer is:", movie)
            print ("You Win!")
            win_flag = "Y"
            break
    elif len(_guess) == 1:
        pos=[0]*length
        k = 0
        for j in range(0, length):
            if movie[j] == _guess:
                pos[k] = j
                k = k +1 
        
        #pos =movie.find(_guess)
        if k == 0:
            print ("Letter not present")
            pos[0] = -1
            _blanks = _create_a_list(length, _guess, pos , _blanks)
            _temp = _blanks
        else:
            _blanks = _create_a_list(length, _guess, pos , _blanks)
    if turn == _chances -2:
        print ("Last chance...")
        sleep(2)
    sleep(1) 
    clear()
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print ("************************************")
    print(" ")
    print(" ")
    print(" ")
    print(" ")    
    print (_blanks)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print ("************************************")
if win_flag != "Y":
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print ("You Lose! HAHAHAHAH.....")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print ("************************************")

