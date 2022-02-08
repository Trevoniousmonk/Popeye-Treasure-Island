print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You're in the jungle. How spooky!")
print("The path to the right is clear. Grunting noises are coming from the path to the left.") 
choice1 = input("Which way do you go, left or right?")
left_or_right = choice1.lower()

if left_or_right == "right":
  print('''
  uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
''')
  print("As you walk down the path you slip on a banana peel and crack open your skull. Too bad, game over!")

if left_or_right == "left":
  print('''            .--------------------------------------------.
           ( DO YOU KNOW HOW HARD IT IS TO DRAW AN OKAPI? )
          //'--------------------------------------------'
         /      , _.-~~-.__            __.,----.
      (';    __( )         ~~~'--..--~~         '.
(    . \"..-'  ')|                     .       \  '.
 \\. |\.'                    ;       .  ;       ;   ;
  \ \'"   /9)                 '       .  ;           ;
   ; )           )    (        '       .  ;     '    .
    )    _  __.-'-._   ;       '       . ,     /\    ;
    '-'"'--'      ; "-. '.    '            _.-(  ".  (
                  ;    \,)    )--,..----';'    >  ;   .
                   \   ( |   /           (    /   .   ;
     ,   ,          )  | ; .(      .    , )  /     \  ;
,;'-PjP;.';.-.;._,;/;,;)/;.;.);.;,,;,;,,;/;;,),;.,/,;.).,;,

  
''')
  print("It's an okapi! You climb onto its back. Hold on to your butt!")
  print("You arrive at a lake and bid farewell to your new friend.")
  print("In the middle of the lake is an island.")
  choice2 = input("You can either swim or wait. What do you do?")
  swim_or_wait = choice2.lower()

  if swim_or_wait == "swim":
    print('''
                        _.--._
                _.-'(//|(\'-._
            _.-'(\)))(\\\\((|\'-._
        _.-')/)/)\((|\))/(/\()\\(/'-._
     .-'/))/))(\\))\)//)\\)))(/))\)(\\'-.
    /')/)\(/\)\))/\(/|)\))/((||\/)\)\)\\'\
    \((\\(/((\///)))/(\\(/)\\\\\)\)\))\))/
     V )/.-.__(/|_/|' ' ' |\_|)/__.-. ))V
       | |    | |_/| ' ' '|\_| |    | |
       | |    | |_/|' '  '|\_| |    | |
       | '-.__| |_/| ' ' '|\_| |__.-' |
       |        |_/|'  ' '|\_|        |
       |_       |_/| ' ' '|\_|       _|
       ||'-._   |_/|______|\_|   _.-'||
       ||    '-.|_/<      >\_|.-'    ||
       ||      ||\__________/||      ||
       ||      || \________/ ||      ||
       ||      ||  \______/  ||      ||
   LGB ||      ||  |______|  ||      ||
               ||  |______|  ||
               ||  |______|  ||
 ''')
    print("You decide to take a dive into the water, despite your better judgement.")
    print("Today, your better judgement was wrong. You made it to the island!")
    print("There is a bamboo hut with 3 doors. One red, one yellow and one blue.")
    choice3 = input("Which colour do you choose?")
    door_choice = choice3.lower()

    if door_choice == "red":                            
      print("Applesauce?! Oh no! GAME OVER!")
    if door_choice == "yellow":
      print("You found the treasure! Ahoy! Spend it wisely, lucky.")
    else:
      print("It's a room full of fish! GAME OVER! But take some with you as you go.")





  if swim_or_wait == "wait":
    print('''
          !
    T            ....Well-l-l-l-!
   O   _._
  O . (_{})   ...Blow me down..Sweet Pea!
 T. . .\__\
   \|/c- o       that's not me spinach...
    U--=U-
      (_,_)   ...it's SPAM! ...Uk Uk Uk Uk...
    ^_(/\)_^
   /\   o  /\              /\
  / /|  o |\ \            |/\|
 <  \|  o |/  >           |\/|
  \ W\  o | W/        ******/           YUK!
   \  \_o_|  \       =========           /
    ))))   ))))      |      /|          ~
    |   | |          |______/|        c")@/\ __
____\   @ @__________| SPAM /|__________~/     \____.
    /  _/ /_         |_______|            \  \/   ) \___..
   / /(  )  )        |      /|          =(/ /(   / ____)/D;
   ==-=== ==         =========          =( /--\______)/D;
   ''')
    print("Popeye appears out of the jungle. OH NO! Too bad, GAME OVER!")