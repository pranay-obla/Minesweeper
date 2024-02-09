import time
import random

mines=list()
reveal=[[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9]]
numbers=list()
GG=0
r=0
c=0
count=0
print("WELCOME TO MINESWEEPER!!")
print()
time.sleep(1.5)

def Numbers():
    global numbers
    numbers=list()
    for i in range (1,9):
        a=list()
        for j in range(1,9):
            if mines[i][j]==1:
                a.append(9)
            else:
                count=0
                if mines[i+1][j+1]==1:
                    count+=1
                if mines[i+1][j]==1:
                    count+=1
                if mines[i+1][j-1]==1:
                    count+=1
                if mines[i][j+1]==1:
                    count+=1
                if mines[i][j-1]==1:
                    count+=1
                if mines[i-1][j]==1:
                    count+=1
                if mines[i-1][j+1]==1:
                    count+=1
                if mines[i-1][j-1]==1:
                    count+=1
                a.append(count)
        numbers.append(a)

def Home_Screen():
    while True:
        print("HOME SCREEN :")
        print("1.Instructions")
        print("2.Play the game")
        ch=input("Select your option :\n")
        try:
            ch=int(ch)
        except:
            pass
        if ch==1:
            print('''
                             INSTRUCTIONS
 - You will be given an 8 x 8 board
 - You must then select a square to be opened
 - The first square will never be a mine
 - There will be around 10-13 mines in the whole board
 - If you open a mine, you will lose the game
 - Once you open all the squares without a mine, then you win the game
 - A square contains the number of mines it is touching (including diagonally)
 - Example Square - c4 , a1 , a8 , h1 , h8''')
            print()
            print()
            ch11=input("Enter anything to go back:  ")
            print()
        elif ch==2:
            break
        else:
            print("Enter valid option \n")

def Board_Display():
    global reveal
    global r
    global GG
    for k in range(8):    
        for i in range(8):
            for j in range(8):
                if reveal[i][j]==0:
                    if (i-1)>=0 and (j-1)>=0:
                        reveal[i-1][j-1]=numbers[i-1][j-1]
                    if (i-1)>=0 and (j)>=0:
                        reveal[i-1][j]=numbers[i-1][j]
                    if (i-1)>=0 and (j+1)<=7:
                        reveal[i-1][j+1]=numbers[i-1][j+1]
                    if (i)>=0 and (j-1)>=0:
                        reveal[i][j-1]=numbers[i][j-1]
                    if (i)>=0 and (j+1)<=7:
                        reveal[i][j+1]=numbers[i][j+1]
                    if (i+1)<=7 and (j-1)>=0:
                        reveal[i+1][j-1]=numbers[i+1][j-1]
                    if (i+1)<=7 and (j)>=0:
                        reveal[i+1][j]=numbers[i+1][j]
                    if (i+1)<=7 and (j+1)<=7:
                        reveal[i+1][j+1]=numbers[i+1][j+1]                
    print("       ",end="")
    for i in range(8):
        print(i+1, end ="    ")
    print()
    print()
    print()
    for i in range(1,9):
        print(chr(64+i) , end="      ")
        for j in range(1,9):
            if reveal[i-1][j-1]==9:
                print("\u25A0" , end="    ")
            elif reveal[i-1][j-1]==0:
                print(chr(927) , end="    ")
            else :
                print(reveal[i-1][j-1],end="    ")
        print()
        totalm=0
        for i in range(1,9):
            for j in range(1,9):
                if mines[i][j]==1:
                    totalm+=1
        print()
    if yy==2:
        print("Total Mines:  ",totalm)
        print()
        
def Mines_Randomizer():
    global mines
    mines=list()
    mines.append([9,9,9,9,9,9,9,9,9,9])
    for i in range(1,9):
        a=list()
        a.append(9)
        for j in range(1,9):
            if random.randint(0,7)==1:
                a.append(1)
            else:
                a.append(0)
        a.append(9)
        mines.append(a)
    mines.append([9,9,9,9,9,9,9,9,9,9])
    totalm=0
    for i in range(1,9):
        for j in range(1,9):
            if mines[i][j]==1:
                totalm+=1
    while totalm<10:
        for i in range (1,9):
            for j in range (1,9):
                if mines[i][j]==0 and random.randint(0,25)==1:
                    mines[i][j]=1
        totalm=0
        for i in range(1,9):
            for j in range(1,9):
                if mines[i][j]==1:
                    totalm+=1   
def Choice():
    global r
    global c
    global d
    global i1
    global j1
    print()
    if (d==1):
        r=i1+1
        c=j1+1
    else:
        while(True):
            cell=input("Select Square :   \n")
            if(len(cell)==2 and cell[0].isalpha() and cell[1].isdigit()):
                r=ord(cell[0].upper())-64
                c=(cell[1])
                try:
                    c=int(c)
                    if 0<=r<=8 and 0<=c<=8:
                        break
                    else:
                        print("Enter valid coordinates \n")
                except:
                    print("Enter valid coordinates \n")
                    break
            else:
                print("Enter valid coordinates \n")
def Result():
    global mines
    global count
    global reveal
    global r
    global c
    global GG
    if mines[r][c]==1:
        GG=1
        print("YOU LOOOOSE!!!!!")
    else :
        reveal[r-1][c-1]=numbers[r-1][c-1]

def Lose():
    global reveal
    global mines
    time.sleep(2)
    print("       ",end="")
    for i in range(8):
        print(i+1, end ="    ")
    print()
    print()    
    for i in range(1,9):
        print(chr(64+i) , end="      ")
        for j in range(1,9):
            if mines[i][j]==1:
                print(chr(1147),end="    ")
                continue
            if reveal[i-1][j-1]==9:
                print("\u25A0" , end="    ")
            elif reveal[i-1][j-1]==0:
                print(chr(927) , end="    ")
            else :
                print(reveal[i-1][j-1],end="    ")
        print()
        print()
    print()
    print()
    time.sleep(2)
    print('''
                        ,--.!,
                     __/   -*-
                   ,d08b.  '|`
                   0088MM     
                   `9MMP'     ''')
    time.sleep(2)
    print('''
                  _ ._  _ , _ ._
                (_ ' ( `  )_  .__)
              ( (  (    )   `)  ) _)
             (__ (_   (_ . _) _) ,__)
                 `~~`\ ' . /`~~`
                      |   |
                      /   \\
        _____________/_ __ \\_____________ ''')

def win():
    print("YOU WINNN!!!")
    for i in range(1,9):
        print(chr(64+i) , end="      ")
        for j in range(1,9):
            if mines[i][j]==1:
                print(chr(1147),end="    ")
                continue
            if reveal[i-1][j-1]==9:
                print("\u25A0" , end="    ")
            elif reveal[i-1][j-1]==0:
                print(chr(927) , end="    ")
            else :
                print(reveal[i-1][j-1],end="    ")
        print()
        print()
        
    print('''
                         $$$$$$$$$$$$$$$$$$$$
                       $$$$$$$$$$$$$$$$$$$$$$$$$$$
                    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$         $$   $$$$$
    $$$$$$        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$$$$$$$$
 $$ $$$$$$      $$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$       $$$$$$$$
 $$$$$$$$$     $$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$    $$$$$$$$
   $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  $$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$
     $$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$$
    $$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$$
    $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$$$$$$$$$
  $$$$       $$$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$      $$$$
             $$$$$     $$$$$$$$$$$$$$$$$$$$$$$$$         $$$
               $$$$          $$$$$$$$$$$$$$$           $$$$
                $$$$$                                $$$$$
                 $$$$$$      $$$$$$$$$$$$$$        $$$$$
                   $$$$$$$$     $$$$$$$$$$$$$   $$$$$$$
                      $$$$$$$$$$$  $$$$$$$$$$$$$$$$$
                         $$$$$$$$$$$$$$$$$$$$$$
                                 $$$$$$$$$$$$$$$
                                     $$$$$$$$$$$$
                                      $$$$$$$$$$$
                                       $$$$$$$$
''')
    time.sleep(1)
    print('''

                            YOU ARE TRULY A GENIUS!!!!''')


#main        
Home_Screen()
print()
d=1
time.sleep(1)
print("HERE IS YOUR BOARD  :  ")
time.sleep(1)
print()
Mines_Randomizer()
Numbers()
yy=1
Board_Display()
while(True):
    str1=input("Select Square(Example--c4)  :   \n")
    if (len(str1)==2 and str1[0].isalpha() and str1[1].isdigit()):
        i1=(ord(str1[0].upper())-65)
        j1=(str1[1])
        try:
            j1=int(j1)-1
            if 0<=i1<=7 and 0<=j1<=7:
                break
            else:
                print("Enter valid coordinates \n")
        except:
            print("Enter valid coordinates \n")
            break       
    else:
        print("Enter valid coordinates \n")
while(True):
    if numbers[i1][j1]!=0:
        Mines_Randomizer()
        Numbers()
    else:
        break
yy=2
Choice()
Result()
Board_Display()
d=2
while GG!=1:
    Choice()
    Result()
    Board_Display()
    count=0
    i=0
    j=0
    ch=0 
    if (reveal==numbers):
        GG=0
        break
if GG==0:
    time.sleep(2)
    print()
    print()
    win()
    
else:
    print()
    print()
    Lose()
