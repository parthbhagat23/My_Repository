#****************************************************************
#Name: Parth Bhagat
#Student Number: A00218451
#
#ANA1001 Mid Term Project
#****************************************************************
#

#importing libraries and declaring and defining variables
import time
import sys
health = 100
money = 235
pistol = 22
handcuff = 1
choice = "z"
cigarette = 0
user_choice = " "
#creating function for loading screen
def loading():
    time.sleep(2)
    print("Loading game......1%")
    time.sleep(2)
    print("7%")
    time.sleep(2)
    print("53%")
    time.sleep(0.3)
    print("98%")
    time.sleep(0.2)
    print("100%")
    time.sleep(2)
    print("Launching......")
    time.sleep(1)
    print("""
       ▄███████▄    ▄████████    ▄████████    ▄████████ ███▄▄▄▄    ▄██████▄   ▄█     ▄████████
      ███    ███   ███    ███   ███    ███   ███    ███ ███▀▀▀██▄ ███    ███ ███    ███    ███
      ███    ███   ███    ███   ███    ███   ███    ███ ███   ███ ███    ███ ███▌   ███    ███
      ███    ███   ███    ███  ▄███▄▄▄▄██▀   ███    ███ ███   ███ ███    ███ ███▌   ███    ███
    ▀█████████▀  ▀███████████ ▀▀███▀▀▀▀▀   ▀███████████ ███   ███ ███    ███ ███▌ ▀███████████
      ███          ███    ███ ▀███████████   ███    ███ ███   ███ ███    ███ ███    ███    ███
      ███          ███    ███   ███    ███   ███    ███ ███   ███ ███    ███ ███    ███    ███
     ▄████▀        ███    █▀    ███    ███   ███    █▀   ▀█   █▀   ▀██████▀  █▀     ███    █▀
                                ███    ███
    """)

    time.sleep(5)
    intro()

#initializing loop and creating functions that are essentially different levels in the game along with print and if statements and inputs and choices from the user.
#at the end of each function is calling for the next function(level)
#all the functions have variables declared as global except the first and last oness
while user_choice.title() != "Quit":
    def intro():
      print("You are Yendis Shiropa, an infamous detective from Surbury, Canada with a dark past.\n")
      time.sleep(3)
      print("One day you were driving through a scarcely populated forest area to visit a friend when you suddenly heard a gunshot from a nearby mansion along the road.\n")
      time.sleep(5)
      print("Being a detective, you couldn't help it and decided to check out what's going on, with there being no signals inside the forest at that point of time you decided to go in alone without calling for any backup.\n")
      time.sleep(5)
      print("You get out of your car and enter the Mansion from the front door which you find open.\n")
      time.sleep(3)
      mansion_hall()


    def mansion_hall():
      global choice, money, health, handcuff, pistol, cigarette
      print(f"Your stats are: Health {health}\tMoney \t{money}\n\t Items: Pistol {pistol}\tHandcuffs {handcuff}\n")
      time.sleep(4)
      print("You are inside the Mansion Hall.\n")
      time.sleep(2)
      print("You realize there's dead silence inside the mansion.\n")
      time.sleep(2)
      print("You observe there are many big paintings put at display on the walls and there are many doors leading to other rooms connected through the hall.The mansion has multiple floors and there's a staircase leading to the first floor.\n")
      time.sleep(5)
      print("Your gut feel is telling you whatever happened, happened on the upper floor.\n")
      time.sleep(2)
      while choice.upper() != "Y":
        choice = input("Take the staircase up the first floor? Y/N_\n")
        if choice.upper() == "Y":
          print("You start climbing the stairs slowly without making any footstep noise and reach outside the master bedroom.")
          time.sleep(3)
          print("You find the bedroom's entrance open and walk in slowly")
          time.sleep(3)
          masterbedroom()
        else:
          print("You can't find out what has happened if you don't leave the Mansion Hall!")
          time.sleep(3)

    def masterbedroom():
      global choice, money, health, handcuff, pistol, cigarette
      print(f"Your stats are: Health {health}\tMoney \t{money}\n\t Items: Pistol {pistol}\tHandcuffs {handcuff}\n")
      time.sleep(2)

      print("You are inside the bedroom now.\n")
      time.sleep(1)

      print("There's an antique styled bed, the room has a colour style of red with red bedsheet and curtains. There's a study desk beside the window in the room which is closed from the inside.\n")
      time.sleep(3)

      print("You look around and find nothing, but there's a smell.\n")
      time.sleep(2)

      print("You look down and find a burning cigarette lying down on the floor.\n")
      time.sleep(2)


      while choice.upper() != "A":
        print("What do you do now?\n A: Pick up the cigarette to inspect it.\n B: Keep searching the room for more evidence.\n C: Leave the room and search other parts of the mansion.\n")

        choice = input("\n")
        print("\n")
        if choice.upper() == "A":
          print("You pick up the cigarette and look at it.\n")
          time.sleep(2)

          print("Upon closer inspection you realize that it was lit just a few seconds before you entered the room!\n")
          time.sleep(2)

          print("This means the suspect must be inside the room hiding somewhere!\n")
          time.sleep(2)

          print("Just when you are about to turn and search you get sucker punched from behind!\n")
          time.sleep(2)

          print("For a second you lose consciousness and fall down.....\n")
          time.sleep(2)

          print("It takes you a few seconds to gain back your balance\n")
          time.sleep(2)

          print("Just as you get up you realize the person who punched you is running down the staircase.\n")
          time.sleep(2)


          choice = "z"
          choice = input("What do you do now?\n A: Pull out your gun and shoot him.\n B: Chase after him.\n C: Tell him to stop running away.\n")
          print("\n")

          if choice.upper() == "A":
            health = health - 40
            print(f"You take a shot at him but miss, he shoots back immediately and injures you but the bullet is not inside your body. You loose 40 health. Your health is now {health}.\n")
            time.sleep(3)

            pistol = pistol - 1
            print("He keeps running, you shoot again and graze him on the right leg.\n")
            time.sleep(2)

            pistol = pistol - 1
            print("You chase after him and exit the mansion.\n")
            time.sleep(2)

            forest()

          elif choice.upper() == "B":
            print("You chase after him but he's too fast and runs away.\n ")
            exit()

          elif choice.upper() == "C":
            print("You Tell him to stop running but he doesn't listen and runs away!\n")
            exit()
          else:
            print("You took too much time to decide and lost the suspect!\n")
            exit()

        elif choice.upper() == "B":
          print("You search but find nothing.\n")

        elif choice.upper() == "C":
          print("You can't leave the room, whatever happened, happened in that room only!\n")

    def forest():
      print("You are now in the forest!\n")
      time.sleep(2)

      global choice, money, health, handcuff, pistol, cigarette
      print(f"Your stats are: Health {health}\tMoney \t{money}\n\t Items: Pistol {pistol}\tHandcuffs {handcuff}\n")
      time.sleep(2)

      print("\n")
      print("You can see the suspect running away. There's not much time before he is too far away from you but he's bleeding from your gunshot wound and limping.\n\n")
      time.sleep(3)

      print("What do you do?\nA: Shoot him again to stop him?\nB: Chase him\nC: Tell him to stop again or you'll shoot?")
      choice = input("\n")
      if choice.upper() == "A":
        print("You shoot him and injure him critically because of which he dies.")
        exit()
      elif choice.upper() == "B":
        print("You start chasing him, he sees you following him and closing the gap very fast.\n")
        time.sleep(2)

        print("He panicks and starts running frantically, accidentally dashes in a tree, hits his head and passes out.\n")
        time.sleep(2)

        print("You reach near him with your gun pointed at him and realize he's unconscious.\n")
        time.sleep(2)

        print("You look at his face but it's covered in blood.\n")
        print("You cuff him and look at his face again. He looks somewhat familiar to you.\n")
        time.sleep(2)

        handcuff = handcuff - 1
        print("You check him for any IDs and find nothing but a gun.\n")
        time.sleep(2)

        print("He's bleeding out you must take him to a hospital or he'll die from bloodloss.\n")
        time.sleep(2)

        choice = input("Take him to a hospital? Y/N_\n")
        if choice.upper() == "Y":
          print("You leave him at a hospital with guards assigned incase he tries to run away and return to your office at the police station.")
          #
          policestation()
        else:
          print("He died due to blood loss.")
          exit()
      elif choice.upper() == "C":
        print("It was pointless to tell him to stop at this point of time. He got away!")
        exit()


    def policestation():
      global choice, money, health, handcuff, pistol, cigarette
      print(f"Your stats are: Health {health}\tMoney \t{money}\n\t Items: Pistol {pistol}\tHandcuffs {handcuff}\n")
      time.sleep(3)

      print("You are at your office now. It's a big cabin with 2 windows at the back. There's a desk with a telephone along with a cabinet full of files and folders.\n")
      time.sleep(2)

      print("Suddenly there's a knock on the cabin's door. A middle aged man comes in and sits down. It's Charlie, your old colleague and friend.\n")
      time.sleep(2)

      print("Charlie: I heard you messed up that guy Yendis, didn't have to be so harsh on that poor lad.\n")
      time.sleep(2)

      print("Yendis: Yeah!? Well, I wasn't. Dude sucker punched me and then started running away. Couldn't think much and shot at him like an idiot without any warning and he shot me back. Only difference is I missed at first.\n")
      time.sleep(3)

      print("Charlie: That's suspension if it gets in the report.\n")
      print("Yendis: Yeah, I know. Nevermind that did you find anything at the crimescene?\n")
      time.sleep(2)

      print("Charlie: You said you heard a gunshot there right?\n")
      print("Yendis: Yeah.\n")
      time.sleep(2)

      print("Charlie: Well, we didn't find any body there, nor was there any empty shell of that gunshot in the bedroom you were talking about.\n")
      time.sleep(2)

      print("Yensid: What!?\n")
      time.sleep(2)

      print("Charlie: But we did find those bullet shells that were fired at you and the weapon that was used to fire them. We've sent them to the forensics to find out more and we are searching for the owner of the weapon as we speak. That was a tranquilizer gun by the way.\n")
      time.sleep(5)

      print("Yendis: Good!\n")
      time.sleep(2)

      print("Charlie: Here, I got you something from the store.\n")
      time.sleep(2)

      print("Yendis: You didn't have to but thank you, lemme pay you for this one atleast. I am in your debt, for all these treats  you give me.(Haha.....) \n")
      time.sleep(2)

      print("Charlie: You don't have to pay me anything man.\n")
      choice = input("Pay anyways? Y/N_\n")
      for x in range(1,2):
        if choice.upper() == "Y":
          money = money - 5
          print(f"You have now ${money}.\n\n")
        else:
          continue

      print("Your office telephone starts to ring all of a sudden. You pick it up.\n")
      time.sleep(2)

      print("Doctor Hendricks: Hello! Am I speaking to Detective Yendis!?\n")
      time.sleep(2)

      print("Yendis: Yes, you sound panicked, what's wrong doctor?\n")
      time.sleep(2)

      print("Doctor Hendricks: Detective the suspect has run away! He got out at night when the guards were asleep!\n")
      time.sleep(2)

      print("Yendis: How irresposible can you all be!?\n")
      time.sleep(2)

      print("Damnit!(Cuts call)\n")
      time.sleep(2)

      print("Charlie: What's wrong Yendis?\n")
      time.sleep(2)

      print("Yendis: That guy ran away from the hospital and we have no leads as to why he did what he did.\n")
      time.sleep(2)

      print("Charlie: Oh well! We do have a lead now, when you were on the call I got a fax, this is the address the weapon is registered to and the name of the owner is some Disney.\n")
      time.sleep(3)

      print("Yendis: What kind of a name is Disney? Nevermind, this is a great news. I'll leave immediately and search that address. Hopefully , we'll find out more about this Disney guy.\n")
      time.sleep(3)

      choice = input("Eat the snack before leaving? Don't forget you have to hurry up or you might lose important leads. Y/N_\n")
      for y in range(1,2):
        if choice.upper() == "Y":
          health = 100
          print(f"Your health is now {health}.")
        else:
          continue
      address()
    print("\n")

    def address():
      global choice, money, health, handcuff, pistol, cigarette
      print(f"Your stats are: Health {health}\tMoney \t{money}\n\t Items: Pistol {pistol}\tHandcuffs {handcuff}\n")
      time.sleep(2)

      print("You reach the address Charlie got you. An eerie feeling starts to linger inside you. Something about the house you are about to enter doesn't sit tight with you.\n")
      time.sleep(3)

      print("You pick the front door lock and Ignoring everything enter the house anyways.\n")
      time.sleep(2)

      print("The house has just one room with attached kitchen and washroom.\n")
      time.sleep(2)

      print("There just one large cabinet in the house and one table. You don't see anything of value around and move towards the table.\n")
      time.sleep(2)

      print("When you look at the unique design of the table you start feeling terrified of something that even you don't know.\n")
      time.sleep(2)

      print("That eerie feel inside starts to weigh heavy and you can't think straight anymore.\n")
      time.sleep(2)

      print("You turn around to get out of that house and immediately realize there's someone hiding inside the cabinet. It's dark around you but something tells you that it's the suspect on the run.\n")
      time.sleep(3)

      print("You walk towards the cabinet and just as you were about to open it, the man inside the cabinet jumped out and attacked you with a knife.\n")
      time.sleep(2)

      health = health - 90
      if health < 0:
        print("You were too injured to put up a fight and died.")
        exit()
      else:
        print(f"You got severely injured by that attack but kicked down the attacker.\n Health is critical at {health}")
        print("\n")
      choice = input("What do you do now?\n A: You run away to save yourself and call for backup.\n B: Get into a fist fight with the attacker.\n C: Pull out your gun and shoot the attacker.\n")
      if choice.upper() == "A":
        print("You run outside of the house to protect yourself from the attacker.\n")
        time.sleep(2)

        print("The attacker follows you outside.\n")
        time.sleep(2)

        print("You get to your car but can't find the keys to open it.\n")
        time.sleep(2)

        print("The attacker catches up to you and stabs you multiple times which kills you on the spot.\n")
        exit()
      elif choice.upper() == "B":
        print("You get into a fist fight with the attacker.\n")
        time.sleep(2)

        print("You punch him in the face but he's unaffected by that and attacks you with the knife.\n")
        time.sleep(2)

        print("You are successfully able to avoid his attack but he is persistent and keeps swinging his knife at you.\n")
        time.sleep(2)

        print("He eventually gets and stabs you multiple times which kills you on the spot.\n")
        exit()
      elif choice.upper() == "C":
        print("You immediately pull out your gun and shoot the attacker before he's able to get up.\n")
        time.sleep(2)

      print("You turn on the lights to look at the attacker's face and just as you look at his face you start to freak out and loose consciousness.\n")
      time.sleep(2)

      print("The attacker looks just like you!\n")
      time.sleep(2)

      print("Suddenly, you are overcome with flashbacks of memories you don't recall.\n")
      time.sleep(2)

      print("Places you've never been to and people you've never met!\n")
      time.sleep(2)

      print("In the flashbacks you realize that the place you are at is infact your home!\n")
      time.sleep(2)

      print("This makes no sense and was too much for you to handle and you pass out.\n")
      time.sleep(2)

      asylum()

    def asylum():
      money = 0
      health = 100
      handcuff = 0
      pistol = 0
      cigarette = 0
      print(f"Your stats are: Health {health}\tMoney \t{money}\n")
      time.sleep(2)

      print("You wake up in a strait-jacket at an Asylum. You are in a room which has a hospital bed and a urinal with a washbasin. The room has been painted white from the inside. There's a steel door with a very small window in front of you, you look outside and see similar doors around the corridor. Confused and baffled you start screaming and asking for help.\n")
      time.sleep(5)

      print("Suddenly, a man appears wearing a guard uniform. It's Charlie!\n")
      time.sleep(2)

      print("Yendis: Charlie what the hell is going on here? Why am I in a strait-jacket at an asylum? And why are you wearing a guard uniform?\n")
      time.sleep(2)

      print("Mike: There you go again with your everyday non-sense. I've told you the same exact thing for the past 7 years and I'll do the same today also. MY NAME IS NOT CHARLIE!!!\n")
      time.sleep(2)

      print("Yendis: Is this some sort of a joke? If it is then I'm not enjoying it! I am Yendis and you are Charlie.\n")
      time.sleep(2)

      print("Mike: To hell with your Yendis and Charlie crap man. Every damn day you start screaming and do this same thing again and again.\n")
      time.sleep(2)

      print("(He takes out a nameplate from the door and shows it to you.....)\n")
      time.sleep(2)

      print("Mike: Look at this plate! What does it say? It says SIDNEY SHAPIRO! That's what your name is and will ever be till ya breathin' ,Just like I'll be Mike! Now, stop with your nonsense or I'll have to ask doctor Hendricks to put you on sedatives again!\n")
      time.sleep(3)

      print("(He starts walking away from your door, but you have others things in mind. As he moves away a few steps you start to pretend like you are going mad and start hitting your head in the door. Mike rushes to stop you and opens the door but you......)\n")
      time.sleep(3)

      choice = input("\nA: Suddenly stop and grab hold of his collars and ask him why is he doing what he's doing?\nB: Suddenly attack him and snatch his tranquilizer pistol along with a cigarette and a cheap lighter while holding him hostage to get out of the Asylum.\nC: Do nothing and go back to your bed.\n")
      if choice.upper() == "A":
        print("He pushes you back and shoots you with his tranquilizer gun.")
        exit()
      elif choice.upper() == "B":
        print("As you get out of the asylum you shoot Mike with his gun and he gets paralyzed while you run away inside the forest.")
        cigarette = 1
        pistol = 4
        print(f"Your stats are: Health {health}\tMoney \t{money}\n\t Items: Pistol {pistol}\tCigarette {cigarette}\n")
        time.sleep(2)


        print("While running away from the asylum you loose track of your way and end up at a mansion inside the forest.\n")
        time.sleep(2)

        print("You enter the mansion and realize it's empty and un-inhabited.\n")
        time.sleep(2)

        print("There's left over old furniture all of which is red in colour.\n")
        time.sleep(2)

        print("You enter a bedroom after climbing the staircase in the hall.\n")
        time.sleep(2)

        print("As soon as you light the cigarette you hear someone coming up slowly and quitely.....\n")
        time.sleep(2)

        print("Without making a noise you hide behind the door but drop the cigarette on the foor.\n")
        time.sleep(2)

        print("A suspicious man comes inside the room and starts looking around, by chance he notices the cigarette lying on the ground.\n")
        time.sleep(2)

        print("You realize this is a good opportunity to get out of this bind you are stuck in.\n")
        time.sleep(2)

        choice = input("You: \nA: Sneak behind him and sucker punch him so as to run away.\nB: Sneak out of the room and run away while he's not looking in your direction.")
        if choice.upper() == "A":
          print("You repeat the cycle and are stuck in an endless loop.")
          exit()
        elif choice.upper() == "B":
          print("So, you tried to break the cycle. Something different must have happened. Which you probably will never find out, or you will? Who knows.\n\n")
          print("GAME OVER!/YOU WON!")
          user_choice = input("To quit the game enter quit, To continue enter anything._\t")
          if user_choice.title() == "Quit":
            sys.exit()
          else:
            loading()
      elif choice.upper() == "C":
        print("You stay stuck inside the Asylum forever.")
        exit()

    def exit():
        global user_choice
        for x in range(1,2):
            print("GAME OVER!")
            user_choice = input("To quit the game enter quit, To continue enter anything._\t\ny")
            if user_choice.title() == "Quit":
                sys.exit()
            else:
                loading()
    loading()

