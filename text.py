import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
key = 0
flashlight = 0

required = ("\nYou can only choose option A, B, or C\n") #Cutting down on duplication
required2 = ("\nYou can only choose option A or B\n")

print("""Welcome to another day at Hopkinton High School. Life can be boring and
mundane but we still have our fun. What would you like to do next?\n\n""")

def intro():
    choice = input("Would you like an official tour?\n >>> ")
    time.sleep(1) #this just means you are including a pause
    print("\n")
    if choice in yes:
        print("Great! We'll start in the C wing.\n")
    elif choice in no:
        print ("\n Fine, I guess you can just wander around "
        "\n\nBut don't be shocked for when you get lost")
        raise SystemExit

def do_next():
  print ("""After taking the tour, you are now an expert at navigating the halls
  of HHS, but are looking to do some more exploring. Do you: """)
  time.sleep(1)
  choice2 = input("""
    A. Join the ongoing gym class
    B. Try to friends in the cafeteria
    C. Choose to explore the town instead\n
    >>> """)
  print("\n")
  if choice2 in answer_A:
        print("Dodgeball sounds fun.")
  elif choice2 in answer_B:
        print("Wonder what everyone's having for lunch.\n")
        raise SystemExit
  elif choice2 in answer_C:
        print ("\n Ok See you soon.\n")
        raise SystemExit
  else:
        print(required)
        time.sleep(0.5)
        do_next()

def gymclass():
    print("""  \nThere are 3 gym classes going on. Do you choose:""")
    time.sleep(1)
    choice3 = input("""
    A. Mr. Miller's volleyball game
    B. MR Sanborn's dodgeball game
    C. Mrs. Maillet's RAD class\n
    >>> """)
    print("\n")
    if choice3 in answer_A:
          print("Bump! Set! Spike!\n")
          time.sleep(0.5)
          key()
    elif choice3 in answer_B:
          print("""Just don't get hit!\n""")
          raise SystemExit
    elif choice3 in answer_C:
          print("SHHHHH can't talk about it!\n")
          time.sleep(1)
          terrestrial()
          raise SystemExit
    else:
          print(required)
          time.sleep(1)
          gymclass()


def cafeteria():
    print("""You walk into the cafeteria expecting to see a lunch or at least
    a study going on but...\n""")
    time.sleep(0.75)
    print("""No one is there!.\n""")
    time.sleep(0.75)
    print("""You look around and can't find a single soul.\n""")
    time.sleep(0.75)
    print("""or worse... no food!\n""")
    time.sleep(0.75)

def doors():
    print("""Somehow, some way you manage to break through the cafeteria doors
    and call over a lunch lady so you can check out your pop-tart\n""")

def people():
    print("""But when you walk out, the cafteria is packed! Strange? I thought so.\n""")

#This is where you call all the functions so they run
intro()
do_next()
gymclass()
cafeteria()
