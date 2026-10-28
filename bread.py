print()
print("hey buddy, we makeing bread today in this overly fancy bakery")
print()
mc = input("whats your name rq before we start - ")
print()

Game_running = True
room = "dry ing"
attempts = 0

while Game_running:
    if room == "dry ing":
        print("alright twin, so we dig in the pantry for some thing to make the bread, and we find some dry stuff? we have flour(1) dirt (2) and salt (3) what do we put in?")
        x = input("this is ur answer, 1/2/3 :- ")
        if x == "1":
            print("GOOD JOBBB, you got that right! its a start, we just plan to have flour as the dry stuff here btw")
            room = "trick"
        elif x == "2":
            print("uhh, i doubt dirt would make good bread")
            attempts += 1
            room = "dry ing"
        else:
            print("yeah.... try again ")
            attempts += 1
            room = "dry ing"

    elif room == "trick":
        print("alright now that thats done, what more can we add to the bread? (1) eggs, (2)dry inactive yeast (3)we leave it be")
        y = input("this is ur answer, 1/2/3 :- ")
        if y == "3":
            print("good, best we dont mess this up and make it overloaded, now onto the wet stuff")
            room = "wet ing"
        elif y == "2":
            print("uhhh, we gotta activate the yeast first, we gotta take more flour, start over")
            attempts += 1
            room = "dry ing"
        else:
            print("well eggs aint a bad choise, but its really not the choise for this, itll reduce the shelf life, plus eggs are a wet ingredient and not a dry one")
            attempts += 1
            room = "dry ing"

    elif room == "wet ing":
        print("ooh now we doing the wet stuff, what do we put here (1) water (2) we take yeast out to activate with sugar (3)wet ingredients are for weaklings, we gonna do this dry to the core")
        z = input("this is ur answer, 1/2/3 :- ")
        if z == "2":
            print(" nice, thats the stuff that makes the bread go fuwp. right choise btw, now we get to prepping the yeast")
            room = "hot"
        elif z == "1":
            print("uhh you should not have put water, we gotta make the yeast first unless you want a brick, and if you do, your in the wrong place, lets retry")
            attempts += 1
            room = "dry ing"
        else:
            print("no we arnt")
            attempts += 1
            room = "dry ing"

    elif room == "hot":
        print("okayyyy we got far heh, didnt think wed do so well " + mc + ", lets keep at it >~<, now for the yeast")
        print("do weeeeee")
        print("(1) shoot eletricity through the yeast to bring it to life")
        print("(2)give it a niceee warm sugar water bath with just a bit of water thats not too hot")
        print("(or 3) drop em in boiling water")
        a = input("this is ur answer, 1/2/3 :- ")
        if a == "2":
            print("ooh, answers 2 twice in a row, we may be on a roll, anyhow good, you can handle life as insignificat as yeast. did you know yeast is actually a fungus, yeah like mushrooms, and so are some antibactrials you take")
            room = "bread life"
        elif a == "1":
            print("oooh close but not quite, its a tad too shocking for them and we gotta run form a yeast monster now")
            attempts += 1
            room = "dry ing"
        else:
            print("why would you do that,that yeast had a family you monster")
            attempts += 1
            room = "dry ing"

    elif room == "bread life":
        print("okayyy, now that we have alive yeast, what do we dooo? oh yeah we mix it with our dry ingredients, with a tad more waterrr, and make a dough outta it heh, now we rise it, tell me friend " + mc + " how long do you rekon we let this dough floof up")
        print("(1) idk like 4-9 hours, or we just put it and sleep the night")
        print("(2) give it 4 months so we get monster bread")
        print("(3) 20 minutes and well be fineeee")
        b = input("this is ur answer, 1/2/3 :- ")
        if b == "1":
            print("ooh, now we god nice fat bread, lets bake it, i preheated it for u")
            room = "burnt bread"
        elif b == "2":
            print("ooooh i like the sprit and paitence, but thats gonna give you monster stinky moldy smelly evil bread of doom dispair and sickness. lets try again")
            attempts += 1
            room = "dry ing"
        else:
            print("paticence is a very important virtue, try again")
            attempts += 1
            room = "dry ing"

    elif room == "burnt bread":
        print("final strech, and also i relaised we got no more flour so its the last batch, how many hours do we bake it, 1, 2, or 3")
        c = input("this is ur answer, 1/2/3 :- ")
        if c == "1":
            print("welp, i dont know how it happend so fast but it burnt as soon as it got in, like the oven was as hot as the sun, jeez")
            room = "end stuff"
        elif c == "2":
            print("uhh, we tried but the oven was hot, too hot, burnt it")
            room = "end stuff"
        else:
            print("burnt it somehow, its burnt bread")
            room = "end stuff"

    elif room == "end stuff":
        print("good job at this, you made burnt bread, me that is, in " + str(attempts) + " attempts. pretty easy right, bye bye and have a good day")
        Game_running = False