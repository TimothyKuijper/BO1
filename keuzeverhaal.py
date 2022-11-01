from http.client import CONTINUE
import time

while True:

    print("Welcome to my multiple choise game")
    time.sleep(1)
    print("The rules are simple")
    time.sleep(1)
    print("Only type the letter infront of the answer")
    print("in capital letters then press enter")
    time.sleep(1)
    print("just read the dialog then this wont be hard")
    time.sleep(0.5)
    print("hope you have fun :)")

    time.sleep(2.5)

    #intro

    print("""
*thunder rumbels* 
You wake up sweating like crazy, you look at the clock.
3 am, your dream it was strange it felt like you were dreaming for your entire life and just now woke up.
But its al still the same. Same bed, desk, clock, clothes, everything. 
    """)

    while True:

        time.sleep(3)

        print("""
[A] just try to go back to sleep 
[B] get some water """)

        qi = input("input: ")

        # tekst 1
        if qi == "A":
            print("""
When you wake up again you look back at the clock “11 am”
That’s a more respectable time to wake up. 
You get of bed hop in de shower and start your day. 
Drink some coffee get some work done catch up with friends and family. 
Then you realise you haven’t eaten anything all day.
            """)

            while True:
                time.sleep(3)

                print("""
[A] get groceries 
[B] get fast-food """)

                q1 = input("input: ")

                # tekst 12
                if q1 == "A":
                    print("""
You get on your motorbike and drive to the nearest grocery store. 
On your way there you notice your town is flooded with police, 
you think nothing of it as no one else does. 
You arrive at the grocery store and get your groceries. 
When you step outside there are dozens of police officers outside the store. 
This is getting weird better ask what is going on
                    """)

                    #tekst 3
                    print("""
You approach an officer and ask what is going on.
He tells you that there have been bombs found all over the country
and its crazy you didn’t know that because it was all over the news this morning
– no wonder, my cable is out and my phone was dead this morning – 
you should probably start packing and leave this town as almost everyone is doing.  
When you get back home your phone is charged but It looks like it got blown up by the amount of messages you got.
                    """)

                    while True:
                        time.sleep(3)

                        print("[A] you start packing as much as you can to make a quick escape.")

                        q32 = input("input: ")

                        # tekst 4
                        if q32 == "A":
                            print("""
You throw as much of your stuff into your car and leave, 
you call up your friend who is verry happy to hear your okay 
and urges you to get to the airport as quickly as possible to still make the same flight as him.
                            """)

                            while True:
                                time.sleep(3)

                                print("""
[A] you go as quickly as possible breaking multiple traffic laws in the process 
[B] you go quick but don’t break any laws this could create some serious accidents
                                """)

                                q42 =  input("input: ")

                                # tekst 5
                                if q42 == "A":
                                    print("""
When you get to the airport your friends are already waiting for you. 
You put your stuff on a cart and quickly head to the gate. 
Wait where are we even going? We are going to the Netherlands. 
About 2 hours later you land. It’s the Netherlands so the weather is shit.
                                    """)

                                    while True:
                                        time.sleep(3)

                                        print("""
[A] you take the train to a little town and look for a hotel
[B] you take the train to Amsterdam city centre and forget your problems for a while 
                                        """)

                                        q52 =  input("input: ")
                                                
                                        # tekst 18
                                        if q52 == "A":
                                            print("""
Finally you can rest easy. You lay on bed and fall asleep. 
When you wake up your phone is dead and your stomach is empty you go down to the hotel restaurant and get some breakfast. 
After charging your phone you see it was blown up with messages from friends and family. 
You call a friend tell him your okay in a hotel in the Netherlands.
                                            """)

                                            while True:
                                                time.sleep(3)

                                                print("""
[A] meet up with your friend
[B] stay in your hotel room 
                                                """)

                                                q182 = input("input: ")

                                                # tekst 7
                                                if q182 == "A":
                                                    print("""
You wake up well rested and hop on into the shower, 
feeling refreshed you meet up with your friends and start making a plan on how to continue from this point forward. 
Together you decide to first all call your parents to make sure they are okay. 
You call your mom and she tells you that she and your dad are all okay they took a plane to Germany and will come over to the Netherlands to reunite. 
You should probably start making some money if you want this new life in the Netherlands to work.
                                                    """)

                                                    while True:
                                                        time.sleep(3)

                                                        print("""
[A] search for a job online
[B] you don’t want to think about that right now 
                                                        """)

                                                        q72 =  input("input: ")

                                                        # tekst 8
                                                        if q72 == "A":
                                                            print("""
You go online and find a good job, you apply, go to a solicitation and get hired. 
It looks like things are getting back on track. 
You apply for a citizenship, get a lone, buy a house and try living life again. 
Your parents are in the Netherlands now and your friends are also starting to get their life together again.
                                                            """)

                                                            time.sleep(7)

                                                            print("YOU DID IT!!")
                                                            print("congratulations, you won the game, you got the good ending")
                                                            print("there are actualy 4 more endings, can you get them all?")
                                                            time.sleep(10)
                                                            quit()

                                                        # tekst 22
                                                        if q72 == "B":
                                                            print("""
You speak with your mom and dad about what to do now you discus all kinds of possibilities
but finally decide to all live together in the Netherlands. 
Your parents will come to Netherlands and buy a house together.
                                                            """)

                                                            print("euyyy, you beat the game")
                                                            print("well you didnt get the intended ending")
                                                            print("but atleast you got a good one")
                                                            print("congrats")
                                                            print("there are actualy 4 more endings, can you get them all?")
                                                            time.sleep(10)
                                                            quit()  

                                                        else:
                                                            continue

                                                # tekst 19
                                                if q182 == "B":
                                                    print("""
you stay in your hotel room to hide from the truth that is your new life here in the Netherlands,
you can’t believe you actually had to abandon your home country. You fall into a depression spending your last money on the hotel room. 
When you have nothing left you live on the streets begging for small amounts of cash from tourist. 
You cant keep this up for long though. Not much later you get sick and die on the streets of Amsterdam.
                                                    """)

                                                    time.sleep(7)

                                                    print("ohw, you really messed up didn`t you?")
                                                    print("well i guess thats one way to do it")
                                                    print("you lost")
                                                    time.sleep(1)
                                                    print("there are actualy 4 more endings, can you get them all?")
                                                    time.sleep(10)
                                                    quit()

                                                else:
                                                    continue
                                    


                                        # tekst 6
                                        if q52 == "B":
                                            print("""
You wonder around Amsterdam for a while get a hotel right outside the city and just chill, 
you talk with your friends about what happened and catch up on the news from your home country,
1/3 of the bombs have exploded. A lot of them have been found by bomb squads,
but a lot of them haven’t been found.
                                            """)

                                            while True:
                                                time.sleep(3)

                                                print("[A] go to bed its been a crazy day and you deserve it")

                                                q62 =  input("input: ")

                                                # tekst 7
                                                if q62 == "A":
                                                    print("""
You wake up well rested and hop on into the shower, 
feeling refreshed you meet up with your friends and start making a plan on how to continue from this point forward. 
Together you decide to first all call your parents to make sure they are okay. 
You call your mom and she tells you that she and your dad are all okay they took a plane to Germany and will come over to the Netherlands to reunite. 
You should probably start making some money if you want this new life in the Netherlands to work.
                                                    """)

                                                    while True:
                                                        time.sleep(3)

                                                        print("""
[A] search for a job online
[B] you don’t want to think about that right now
                                                        """)

                                                        q73 =  input("input: ")

                                                        # tekst 8
                                                        if q73 == "A":
                                                            print("""
You go online and find a good job, you apply, go to a solicitation and get hired. 
It looks like things are getting back on track. 
You apply for a citizenship, get a lone, buy a house and try living life again. 
Your parents are in the Netherlands now and your friends are also starting to get their life together again.
                                                            """)

                                                            time.sleep(10)

                                                            print("YOU DID IT!!")
                                                            print("congratulations, you won the game, you got the good ending")
                                                            print("there are actualy 4 more endings, can you get them all?")
                                                            time.sleep(10)
                                                            quit()


                                                        # tekst 22
                                                        if q73 == "B":
                                                            print("""
you speak with your mom and dad about what to do now you discus all kinds of possibilities
but finally decide to all live together in the Netherlands. 
Your parents will come to Netherlands and buy a house together.
                                                            """)

                                                            print("euyyy, you beat the game")
                                                            print("well you didnt get the intended ending")
                                                            print("but atleast you got a good one")
                                                            print("congrats")
                                                            print("there are actualy 4 more endings, can you get them all?")
                                                            time.sleep(10)
                                                            quit()

                                                else:
                                                    continue        
                                        else:
                                            continue
                                else:
                                    continue            
                        else:
                            continue                
                else:
                    continue    

                # tekst 2
                if q1 == "B":
                    print("""
You get on your motorbike and drive to the nearest subway to get a nice sandwich. 
On your way there you notice your town is flooded with police, 
you think nothing of it as no one else does. 
You arrive at the subway get your sandwich and start driving back. 
On your way back you notice even more police now.
                    """)

                    while True:
                        time.sleep(3)

                        print("""
[A] what the hell is happening. Ask a police officer what is going on
[B] probably just some crazy guy on the loose. Just go home 
                        """)

                        q2 = input("input: ")

                        # tekst 3
                        if q2 == "A":
                            print("""
You approach an officer and ask what is going on.
He tells you that there have been bombs found all over the country
and its crazy you didn’t know that because it was all over the news this morning
– no wonder, my cable is out and my phone was dead this morning – 
you should probably start packing and leave this town as almost everyone is doing.  
When you get back home your phone is charged but It looks like it got blown up by the amount of messages you got.
                            """)

                            while True:
                                time.sleep(3)

                                print("[A] you start packing as much as you can to make a quick escape.")

                                q3 = input("input: ")

                                # tekst 4
                                if q3 == "A":
                                    print("""
you throw as much of your stuff into your car and leave, 
you call up your friend who is verry happy to hear your okay 
and urges you to get to the airport as quickly as possible to still make the same flight as him.
                                    """)

                                    while True:
                                        time.sleep(3)

                                        print("""
[A] you go as quickly as possible breaking multiple traffic laws in the process 
[B] you go quick but don’t break any laws this could create some serious accidents
                                        """)

                                        q4 =  input("input: ")

                                        # tekst 5
                                        if q4 == "A":
                                            print("""
When you get to the airport your friends are already waiting for you. 
You put your stuff on a cart and quickly head to the gate. 
Wait where are we even going? We are going to the Netherlands. 
About 2 hours later you land. It’s the Netherlands so the weather is shit.
                                            """)

                                            while True:
                                                time.sleep(3)

                                                print("""
[A] you take the train to a little town and look for a hotel
[B] you take the train to Amsterdam city centre and forget your problems for a while 
                                                """)

                                                q5 =  input("input: ")
                                                
                                                # tekst 18
                                                if q5 == "A":
                                                    print("""
Finally you can rest easy. You lay on bed and fall asleep. 
When you wake up your phone is dead and your stomach is empty you go down to the hotel restaurant and get some breakfast. 
After charging your phone you see it was blown up with messages from friends and family. 
You call a friend tell him your okay in a hotel in the Netherlands.
                                                    """)

                                                    while True:
                                                        time.sleep(3)

                                                        print("""
[A] meet up with your friend
[B] stay in your hotel room 
                                                        """)

                                                        q18 = input("input: ")

                                                        # tekst 7
                                                        if q18 == "A":
                                                            print("""                                                           
 You wake up well rested and hop on into the shower, 
feeling refreshed you meet up with your friends and start making a plan on how to continue from this point forward. 
Together you decide to first all call your parents to make sure they are okay. 
You call your mom and she tells you that she and your dad are all okay they took a plane to Germany and will come over to the Netherlands to reunite. 
You should probably start making some money if you want this new life in the Netherlands to work.
                                                            """)

                                                            while True:
                                                                time.sleep(3)

                                                                print("""
[A] search for a job online
[B] you don’t want to think about that right now 
                                                                """)

                                                                q72 =  input("input: ")

                                                                # tekst 8
                                                                if q72 == "A":
                                                                    print("""
You go online and find a good job, you apply, go to a solicitation and get hired. 
It looks like things are getting back on track. 
You apply for a citizenship, get a lone, buy a house and try living life again. 
Your parents are in the Netherlands now and your friends are also starting to get their life together again.                                                                   
                                                                    """)

                                                                    time.sleep(7)

                                                                    print("YOU DID IT!!")
                                                                    print("congratulations, you won the game, you got the good ending")
                                                                    print("there are actualy 4 more endings, can you get them all?")
                                                                    time.sleep(10)
                                                                    quit()

                                                                # tekst 22
                                                                if q72 == "B":
                                                                    print("""
You speak with your mom and dad about what to do now you discus all kinds of possibilities
but finally decide to all live together in the Netherlands. 
Your parents will come to Netherlands and buy a house together.
                                                                    """)

                                                                    print("euyyy, you beat the game")
                                                                    print("well you didnt get the intended ending")
                                                                    print("but atleast you got a good one")
                                                                    print("congrats")
                                                                    print("there are actualy 4 more endings, can you get them all?")
                                                                    time.sleep(10)
                                                                    quit()
                                                                else:
                                                                    continue
                                                        # tekst 19
                                                        if q18 == "B":
                                                            print("""
you stay in your hotel room to hide from the truth that is your new life here in the Netherlands,
you can’t believe you actually had to abandon your home country. You fall into a depression spending your last money on the hotel room. 
When you have nothing left you live on the streets begging for small amounts of cash from tourist. 
You cant keep this up for long though. Not much later you get sick and die on the streets of Amsterdam.
                                                            """)

                                                            time.sleep(7)

                                                            print("ohw, you really messed up didn`t you?")
                                                            print("well i guess thats one way to do it")
                                                            print("you lost")
                                                            time.sleep(1)
                                                            print("there are actualy 4 more endings, can you get them all?")
                                                            time.sleep(10)
                                                            quit()

                                                # tekst 6
                                                if q5 == "B":
                                                    print("""
You wonder around Amsterdam for a while get a hotel right outside the city and just chill, 
you talk with your friends about what happened and catch up on the news from your home country,
1/3 of the bombs have exploded. A lot of them have been found by bomb squads,
but a lot of them haven’t been found.
                                                    """)

                                                    while True:
                                                        time.sleep(3)

                                                        print("[A] go to bed its been a crazy day and you deserve it")

                                                        q6 =  input("input: ")

                                                        # tekst 7
                                                        if q6 == "A":
                                                            print("""
You wake up well rested and hop on into the shower, 
feeling refreshed you meet up with your friends and start making a plan on how to continue from this point forward. 
Together you decide to first all call your parents to make sure they are okay. 
You call your mom and she tells you that she and your dad are all okay they took a plane to Germany and will come over to the Netherlands to reunite. 
You should probably start making some money if you want this new life in the Netherlands to work.
                                                            """)

                                                            while True:
                                                                time.sleep(3)

                                                                print("""
[A] search for a job online
[B] you don’t want to think about that right now 
                                                                """)

                                                                q7 =  input("input: ")

                                                                # tekst 8
                                                                if q7 == "A":
                                                                    print("""
You go online and find a good job, you apply, go to a solicitation and get hired. 
It looks like things are getting back on track. 
You apply for a citizenship, get a lone, buy a house and try living life again. 
Your parents are in the Netherlands now and your friends are also starting to get their life together again.
                                                                    """)

                                                                    time.sleep(10)

                                                                    print("YOU DID IT!!")
                                                                    print("congratulations, you won the game, you got the good ending")
                                                                    print("there are actualy 4 more endings, can you get them all?")
                                                                    time.sleep(10)
                                                                    quit()

                                                                # tekst 22
                                                                if q7 == "B":
                                                                    print("""
you speak with your mom and dad about what to do now you discus all kinds of possibilities
but finally decide to all live together in the Netherlands. 
Your parents will come to Netherlands and buy a house together.
                                                                    """)

                                                                    print("euyyy, you beat the game")
                                                                    print("well you didnt get the intended ending")
                                                                    print("but atleast you got a good one")
                                                                    print("congrats")
                                                                    print("there are actualy 4 more endings, can you get them all?")
                                                                    time.sleep(10)
                                                                    quit()

                                                                else:
                                                                    continue

                                                        else:
                                                            continue
                                                
                                                else:
                                                    continue
                                        
                                        # tekst 17
                                        if q4 == "B":
                                            print("""
when you arrive at the airport you try calling your friend but goes to voicemail immediately. 
That’s not a good sign you look everywhere but cant find him. 
He sent his flight details to you so you ask someone at the front desk when and from where the plane was leaving, 
she tells you that plane already left. This is bad you look where his flight went, The Netherlands. 
You get a ticket for the next flight there and get to the gate. 1 hour later and you finally board your plane. 
Now just fall asleep for the coming 2 hours and wake up in a different country. 
When you arrive you take a train to Amsterdam city centre and call your friend.
                                            """)
                                        
                                            # tekst 6
                                            print("""
You wonder around Amsterdam for a while get a hotel right outside the city and just chill, 
you talk with your friends about what happened and catch up on the news from your home country,
1/3 of the bombs have exploded. A lot of them have been found by bomb squads,
but a lot of them haven’t been found.
                                            """)

                                            while True:
                                                time.sleep(3)

                                                print("[A] go to bed its been a crazy day and you deserve it")

                                                q6 =  input("input: ")

                                                # tekst 7
                                                if q6 == "A":
                                                    print("""
you wake up well rested and hop on into the shower, 
feeling refreshed you meet up with your friends and start making a plan on how to continue from this point forward. 
Together you decide to first all call your parents to make sure they are okay. 
You call your mom and she tells you that she and your dad are all okay they took a plane to Germany and will come over to the Netherlands to reunite. 
You should probably start making some money if you want this new life in the Netherlands to work.
                                                    """)

                                                    while True:
                                                        time.sleep(3)

                                                        print("""
[A] search for a job online
[B] you don’t want to think about that right now 
                                                        """)

                                                        q7 =  input("input: ")

                                                        # tekst 8
                                                        if q7 == "A":
                                                            print("""
You go online and find a good job, you apply, go to a solicitation and get hired. 
It looks like things are getting back on track. 
You apply for a citizenship, get a lone, buy a house and try living life again.
your parents are in the Netherlands now and your friends are also starting to get their life together again.
                                                            """)

                                                            time.sleep(10)

                                                            print("YOU DID IT!!")
                                                            print("congratulations, you won the game, you got the good ending")
                                                            print("there are actualy 4 more endings, can you get them all?")
                                                            time.sleep(10)
                                                            quit()

                                                        # tekst 22
                                                        if q7 == "B":
                                                            print("""
You speak with your mom and dad about what to do now you discus all kinds of possibilities
but finally decide to all live together in the Netherlands. 
Your parents will come to Netherlands and buy a house together.
                                                            """)

                                                            print("euyyy, you beat the game")
                                                            print("well you didnt get the intended ending")
                                                            print("but atleast you got a good one")
                                                            print("congrats")
                                                            print("there are actualy 4 more endings, can you get them all?")
                                                            time.sleep(10)
                                                            quit()

                                                        else:
                                                            continue
                                                else:
                                                    continue
                                        else:
                                            continue                                                                      
                                else:
                                    continue                              

                        # tekst 13
                        if q2 == "B":
                            print("""
Back home you turn on the tv to relax. 
When you change the channel you see its all just the news, 
what the hell is this I just want to watch some braindead shit. 
When you give up and just watch the news you see that there is a good reason,
bombs have been found all over the city and everyone needs to evacuate the country. 
That’s why there where so many authorities out there.
                            """)

                            while True:
                                time.sleep(3)

                                print("""
[A] you start packing your stuff and drive straight to the airport 
[B] you stay at home for now and see how this plays out
                                """)

                                q13 = input("input: ")
                                
                                # tekst 5
                                if q13 == "A":
                                    print("""
When you get to the airport your friends are already waiting for you. 
You put your stuff on a cart and quickly head to the gate. 
Wait where are we even going? We are going to the Netherlands. 
About 2 hours later you land. It’s the Netherlands so the weather is shit.
                                    """)

                                    while True:
                                        time.sleep(3)

                                        print("""
[A] you take the train to a little town and look for a hotel
[B] you take the train to Amsterdam city centre and forget your problems for a while 
                                        """)

                                        q5 =  input("input: ")
                                                
                                        # tekst 18
                                        if q5 == "A":
                                            print("""
Finally you can rest easy. You lay on bed and fall asleep. 
When you wake up your phone is dead and your stomach is empty you go down to the hotel restaurant and get some breakfast. 
After charging your phone you see it was blown up with messages from friends and family. 
You call a friend tell him your okay in a hotel in the Netherlands.
                                            """)

                                            while True:
                                                time.sleep(3)

                                                print("""
[A] meet up with your friend
[B] stay in your hotel room 
                                                """)

                                                q18 = input("input: ")

                                                # tekst 7
                                                if q18 == "A":
                                                    print("""
You wake up well rested and hop on into the shower, 
feeling refreshed you meet up with your friends and start making a plan on how to continue from this point forward. 
Together you decide to first all call your parents to make sure they are okay. 
You call your mom and she tells you that she and your dad are all okay they took a plane to Germany and will come over to the Netherlands to reunite. 
You should probably start making some money if you want this new life in the Netherlands to work.
                                                    """)

                                                    while True:
                                                        time.sleep(3)

                                                        print("""
[A] search for a job online
[B] you don’t want to think about that right now 
                                                        """)

                                                        q72 =  input("input: ")

                                                        # tekst 8
                                                        if q72 == "A":
                                                            print("""
You go online and find a good job, you apply, go to a solicitation and get hired. 
It looks like things are getting back on track. 
You apply for a citizenship, get a lone, buy a house and try living life again. 
Your parents are in the Netherlands now and your friends are also starting to get their life together again.
                                                            """)

                                                            time.sleep(7)

                                                            print("YOU DID IT!!")
                                                            print("congratulations, you won the game, you got the good ending")
                                                            print("there are actualy 4 more endings, can you get them all?")
                                                            time.sleep(10)
                                                            quit()

                                                        # tekst 22
                                                        if q72 == "B":
                                                            print("""
You speak with your mom and dad about what to do now you discus all kinds of possibilitie
but finally decide to all live together in the Netherlands. 
Your parents will come to Netherlands and buy a house together.
                                                            """)

                                                            print("euyyy, you beat the game")
                                                            print("well you didnt get the intended ending")
                                                            print("but atleast you got a good one")
                                                            print("congrats")
                                                            print("there are actualy 4 more endings, can you get them all?")
                                                            time.sleep(10)
                                                            quit()
                                                        else:
                                                            continue
                                                # tekst 19
                                                if q18 == "B":
                                                    print("""
you stay in your hotel room to hide from the truth that is your new life here in the Netherlands,
you can’t believe you actually had to abandon your home country. You fall into a depression spending your last money on the hotel room. 
When you have nothing left you live on the streets begging for small amounts of cash from tourist. 
You cant keep this up for long though. Not much later you get sick and die on the streets of Amsterdam.
                                                    """)

                                                    time.sleep(7)

                                                    print("ohw, you really messed up didn`t you?")
                                                    print("well i guess thats one way to do it")
                                                    print("you lost")
                                                    time.sleep(1)
                                                    print("there are actualy 4 more endings, can you get them all?")
                                                    time.sleep(10)
                                                    quit()
                                                
                                                else:
                                                    continue
                                        else:
                                            continue
                                # tekst 14
                                if q13 == "B":
                                    print("""
You turn off the tv and start playing games and make some food. 
After a while your friends call you to ask if your okay and where you are. 
You tell them your fine and just chilling at home, 
they don’t understand how your so calm and urge you to come to airport to get out of here.
                                    """)

                                    while True:
                                        time.sleep(3)
                                        
                                        print("""
[A] you comply and pack your stuff to leave for the airport
[B] you shake it off and tell them as long as your in your house you are save """)

                                        q14 = input("input: ")

                                        # tekst 5
                                        if q14 == "A":
                                            print("""
When you get to the airport your friends are already waiting for you. 
You put your stuff on a cart and quickly head to the gate. 
Wait where are we even going? We are going to the Netherlands. 
About 2 hours later you land. It’s the Netherlands so the weather is shit.
                                            """)

                                            while True:
                                                time.sleep(3)

                                                print("""
[A] you take the train to a little town and look for a hotel
[B] you take the train to Amsterdam city centre and forget your problems for a while 
                                                """)

                                                q5 =  input("input: ")
                                                
                                                # tekst 18
                                                if q5 == "A":
                                                    print("""
Finally you can rest easy. You lay on bed and fall asleep. 
When you wake up your phone is dead and your stomach is empty you go down to the hotel restaurant and get some breakfast. 
After charging your phone you see it was blown up with messages from friends and family. 
You call a friend tell him your okay in a hotel in the Netherlands.
                                                    """)

                                                    while True:
                                                        time.sleep(3)

                                                        print("""
[A] meet up with your friend
[B] stay in your hotel room 
                                                        """)

                                                        q18 = input("input: ")

                                                        # tekst 7
                                                        if q18 == "A":
                                                            print("""
You wake up well rested and hop on into the shower, 
feeling refreshed you meet up with your friends and start making a plan on how to continue from this point forward. 
Together you decide to first all call your parents to make sure they are okay. 
You call your mom and she tells you that she and your dad are all okay they took a plane to Germany and will come over to the Netherlands to reunite. 
You should probably start making some money if you want this new life in the Netherlands to work.
                                                            """)

                                                            while True:
                                                                time.sleep(3)

                                                                print("""
[A] search for a job onlin
[B] you don’t want to think about that right now 
                                                                """)

                                                                q72 =  input("input: ")

                                                                # tekst 8
                                                                if q72 == "A":
                                                                    print("""
You go online and find a good job, you apply, go to a solicitation and get hired. 
It looks like things are getting back on track. 
You apply for a citizenship, get a lone, buy a house and try living life again. 
Your parents are in the Netherlands now and your friends are also starting to get their life together again.
                                                                    """)

                                                                    time.sleep(7)

                                                                    print("YOU DID IT!!")
                                                                    print("congratulations, you won the game, you got the good ending")
                                                                    print("there are actualy 4 more endings, can you get them all?")
                                                                    time.sleep(10)
                                                                    quit()

                                                                # tekst 22
                                                                if q72 == "B":
                                                                    print("""
You speak with your mom and dad about what to do now you discus all kinds of possibilities
but finally decide to all live together in the Netherlands. 
Your parents will come to Netherlands and buy a house together.
                                                                    """)

                                                                    print("euyyy, you beat the game")
                                                                    print("well you didnt get the intended ending")
                                                                    print("but atleast you got a good one")
                                                                    print("congrats")
                                                                    print("there are actualy 4 more endings, can you get them all?")
                                                                    time.sleep(10)
                                                                    quit()
                                                                else:
                                                                    continue
                                                        # tekst 19
                                                        if q18 == "B":
                                                            print("""
you stay in your hotel room to hide from the truth that is your new life here in the Netherlands,
you can’t believe you actually had to abandon your home country. You fall into a depression spending your last money on the hotel room. 
When you have nothing left you live on the streets begging for small amounts of cash from tourist. 
You cant keep this up for long though. Not much later you get sick and die on the streets of Amsterdam.
                                                            """)

                                                            time.sleep(7)

                                                            print("ohw, you really messed up didn`t you?")
                                                            print("well i guess thats one way to do it")
                                                            print("you lost")
                                                            time.sleep(1)
                                                            print("there are actualy 4 more endings, can you get them all?")
                                                            time.sleep(10)
                                                            quit()        
                                                        else:
                                                            continue
                                                else:
                                                    continue        
                                        # tekst 15
                                        if q14 == "B":
                                            print("""
You wish them good luck with finding a new life somewhere else and go back to your game. 
You  keep a low profile and survive on the groceries you got earlier. 
After 2 days of doing nothing and staying inside someone knocks on your door. 
You are hesitant to answer
                                            """)

                                            while True:
                                                time.sleep(3)

                                                print("""
[A] answer the door 
[B] keep silent and wait for them to pass
                                                """)

                                                q15 = input("input: ")

                                                # tekst 16
                                                if q15 == "A":
                                                    print("""
When you open the door 2 shocked police officers stand on your driveway in disbelieve you are still there. 
they tell you that you have 15 minutes to pack your stuff or they will take you with them by force. 
You grab your stuff and go with the police officers, they take you to a military airport. 
When you arrive there are about 2 dozen more people waiting there. 
Someone who is definitely in charge tells you you will be flown out to the Netherlands to start a new life there because this country became unhabitable. 
About 2 hours later you step foot in your new home
                                                    """)

                                                    # tekst 6
                                                    print("""
You wonder around Amsterdam for a while get a hotel right outside the city and just chill, 
you talk with your friends about what happened and catch up on the news from your home country,
1/3 of the bombs have exploded. A lot of them have been found by bomb squads,
but a lot of them haven’t been found.
                                                    """)

                                                    while True:
                                                        time.sleep(3)

                                                        print("[A] go to bed its been a crazy day and you deserve it")

                                                        q6 =  input("input: ")

                                                        # tekst 7
                                                        if q6 == "A":
                                                            print("""
You wake up well rested and hop on into the shower, 
feeling refreshed you meet up with your friends and start making a plan on how to continue from this point forward. 
Together you decide to first all call your parents to make sure they are okay. 
You call your mom and she tells you that she and your dad are all okay they took a plane to Germany and will come over to the Netherlands to reunite. 
You should probably start making some money if you want this new life in the Netherlands to work.
                                                            """)

                                                            while True:
                                                                time.sleep(3)

                                                                print("""
[A] search for a job online
[B] you don’t want to think about that right now 
                                                                """)

                                                                q7 =  input("input: ")

                                                                # tekst 8
                                                                if q7 == "A":
                                                                    print("""
You go online and find a good job, you apply, go to a solicitation and get hired. 
It looks like things are getting back on track. 
You apply for a citizenship, get a lone, buy a house and try living life again. 
your parents are in the Netherlands now and your friends are also starting to get their life together again.
                                                                    """)

                                                                    time.sleep(10)

                                                                    print("YOU DID IT!!")
                                                                    print("congratulations, you won the game, you got the good ending")
                                                                    print("there are actualy 4 more endings, can you get them all?")
                                                                    time.sleep(10)
                                                                    quit()

                                                                # tekst 22
                                                                if q7 == "B":
                                                                    print("""
You speak with your mom and dad about what to do now you discus all kinds of possibilities
but finally decide to all live together in the Netherlands. 
Your parents will come to Netherlands and buy a house together.
                                                                    """)

                                                                    print("euyyy, you beat the game")
                                                                    print("well you didnt get the intended ending")
                                                                    print("but atleast you got a good one")
                                                                    print("congrats")
                                                                    print("there are actualy 4 more endings, can you get them all?")
                                                                    time.sleep(10)
                                                                    quit()

                                                                else:
                                                                    continue
                                                        else:
                                                            continue


                                                # tekst 20
                                                if q15 == "B":
                                                    print("""
the knocking stops a few seconds later you hear footsteps drawing away from the door
and you see them walk to the neighbour. 
You release your breath and realise you hold it that entire time. 
You go back to watching some tv eating some snacks and overall just chilling. 
a few days go by and your food is running out. 
There is no one in the city anymore because everyone fled the country all of a sudden.
                                                    """)

                                                    while True:
                                                        time.sleep(3)

                                                        print("[A] go outside to scavenge food")

                                                        q20 = input("input: ")

                                                        # tekst 21
                                                        if q20 == "A":
                                                            print("""
You grab some supplies in case you need to defend yourself for all you know its mayhem out there. 
You gear up grab a baseball bat and a golfing stick and get out there. 
It’s a sunny and warm day you get on your motorcycle and head to the grocery store. 
When you get to the grocery store there is no one there obviously but this means you can grab whatever you want. 
On your way back you decide to take a detour and look around the city as it is. 
While driving home you get tackled by something and fall of your motorcycle and get ready to fight whatever it is that took you down 
but you don’t see anything.
When you want to take a better look all of a sudden you get jumped by multiple people they look beaten up and like they where shot back to the stone age. 
You try to overcome them but they’re with to many and rip you apart.
                                                            """)

                                                            print("oof, not a nice way to go")
                                                            print("i mean you died horribly")
                                                            print("this is the worst one out there")
                                                            time.sleep(2)
                                                            print("there are actualy 4 more endings, can you get them all?")
                                                            time.sleep(10)
                                                            quit()
                                                        else:
                                                            continue
                                                else:
                                                    continue
                                        else:
                                            continue        
                                else:
                                    continue    
                        
                        else:
                            continue
                else:
                    continue

        # tekst 9
        if qi == "B":
            print("""
You get out of bed and walk to the bathroom to get some water. 
When you lay in bed you scroll on your phone for a bit when you hear a big explosion, 
you jump out of bed and look out the window you see ashes flying everywhere and hear people screaming 
you rush outside to get a better look at what happened 
police are already arriving when you step out the front door.
            """)

            while True:
                time.sleep(3)

                print("""
[A] you rush back inside to the safety of your home
[B] your curious and start walking towards the scene 
                """)

                q9 =  input("input: ")

                # tekst 10
                if q9 == "A":
                    print("""
Back inside you turn on the news to see that there have been bombs found all over the country
and a lot of them have already claimed victims. 
you call up your friends who are already packing to leave you agree and start packing.
Bags packed you get in your car and drive to the airport. 
You have no time to lose
                    """)

                    print("""
When you get to the airport your friends are already waiting for you. 
You put your stuff on a cart and quickly head to the gate. 
Wait where are we even going? We are going to the Netherlands. 
About 2 hours later you land. It’s the Netherlands so the weather is shit.
                    """)

                    while True:
                        time.sleep(3)

                        print("""
[A] you take the train to a little town and look for a hotel
[B] you take the train to Amsterdam city centre and forget your problems for a while
                         """)

                        q5 =  input("input: ")
                                                
                        # tekst 18
                        if q5 == "A":
                            print("""
Finally you can rest easy. You lay on bed and fall asleep. 
When you wake up your phone is dead and your stomach is empty you go down to the hotel restaurant and get some breakfast. 
After charging your phone you see it was blown up with messages from friends and family. 
You call a friend tell him your okay in a hotel in the Netherlands.
                            """)

                            while True:
                                time.sleep(3)

                                print("""
[A] meet up with your friend
[B] stay in your hotel room 
                                """)

                                q18 = input("input: ")

                                # tekst 7
                                if q18 == "A":
                                    print("""
You wake up well rested and hop on into the shower, 
feeling refreshed you meet up with your friends and start making a plan on how to continue from this point forward. 
Together you decide to first all call your parents to make sure they are okay. 
You call your mom and she tells you that she and your dad are all okay they took a plane to Germany and will come over to the Netherlands to reunite. 
You should probably start making some money if you want this new life in the Netherlands to work.
                                    """)

                                    while True:
                                        time.sleep(3)

                                        print("""
                                        [A] search for a job online
                                        [B] you don’t want to think about that right now 
                                        """)

                                        q72 =  input("input: ")

                                        # tekst 8
                                        if q72 == "A":
                                            print("""
You go online and find a good job, you apply, go to a solicitation and get hired. 
It looks like things are getting back on track. 
You apply for a citizenship, get a lone, buy a house and try living life again. 
Your parents are in the Netherlands now and your friends are also starting to get their life together again.
                                        """)

                                            time.sleep(7)

                                            print("YOU DID IT!!")
                                            print("congratulations, you won the game, you got the good ending")
                                            print("there are actualy 4 more endings, can you get them all?")
                                            time.sleep(10)
                                            quit()

                                            # tekst 22
                                        if q72 == "B":
                                            print("""
You speak with your mom and dad about what to do now you discus all kinds of possibilities
but finally decide to all live together in the Netherlands. 
Your parents will come to Netherlands and buy a house together.
                                        """)

                                            print("euyyy, you beat the game")
                                            print("well you didnt get the intended ending")
                                            print("but atleast you got a good one")
                                            print("congrats")
                                            print("there are actualy 4 more endings, can you get them all?")
                                            time.sleep(10)
                                            quit()
                                        else:
                                            continue
                                # tekst 19
                                if q18 == "B":
                                    print("""
you stay in your hotel room to hide from the truth that is your new life here in the Netherlands,
you can’t believe you actually had to abandon your home country. You fall into a depression spending your last money on the hotel room. 
When you have nothing left you live on the streets begging for small amounts of cash from tourist. 
You cant keep this up for long though. Not much later you get sick and die on the streets of Amsterdam.
                                    """)

                                    time.sleep(7)

                                    print("ohw, you really messed up didn`t you?")
                                    print("well i guess thats one way to do it")
                                    print("you lost")
                                    time.sleep(1)
                                    print("there are actualy 4 more endings, can you get them all?")
                                    time.sleep(10)
                                    quit()                    
                                else:
                                    continue
                        else:
                            continue    
                # tekst 11
                if q9 == "B":
                    print("""
you walk towards where the explosion was and try to talk to an officer who is already looking very alert,  
when you approach him you ask him what just happened, 
he tells you there are bombs hidden all over the country and should get back inside to pack your stuff and flee the country. 
You are shocked with what you hear and run back home. Just before you walk up your drive way you hear a click and explode.
                    """) 

                    print("wow, impresive you got the fastest ending possible")
                    print("i mean your dead so you kinda lost")
                    print("but hey, at least you where fast right")
                    print("there are actualy 4 more endings, can you get them all?")
                    quit()

                else:
                    continue
        else:
            continue




