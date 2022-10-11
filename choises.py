from re import A
import time

print("hai ik ben tim")
time.sleep(1)
print("hoe heet jij")
naam = input("vul hier je naam in: ")
print("leuk je te leren kennen", naam,)
time.sleep(1.5)
print("het is zonnig weer dus wat trek je aan")
time.sleep(1.5)
print("a- een kortebroek, met een shirt en vest.")
time.sleep(1.5)
print("b- een korte broek met hoge schoenen en een dikke jas")
time.sleep(1.5)
print("c- een lange broek met shirt, trui en jas")
q1 = input("type alleen de kleine letter van de vraag en druk daarna op enter")


time.sleep(1.5)

if q1 == "a":
    print("doe normaal je gaat je toch niet zo warm kleden")
elif q1 == "b":
    print("nee joh, ben je gek")
    quit 
elif q1 == "c":
    print("doe normaal je gaat je toch niet zo warm kleden")
    quit 
    

time.sleep(0.5)

print("okay, nu ff een ontbijtje maken. wat gaan we eten")
time.sleep(1.5)
print("a- een dikke lap vlees van de BBQ")
time.sleep(1.5)
print("b- een broodje met pindakaas en hagelslag")
time.sleep(1.5)
print("c- je eet geen ontbijt")
q2 = input("type alleen de kleine letter van de vraag en druk daarna op enter")

time.sleep(0.5)

if q2 == "a":
    print("nee joh, ben je gek") 
elif q2 == "b":
    print("ja dat is wel het best in de ochtend")
elif q2 == "c":
    print("nee joh, ben je gek")

    time.sleep(0.5)

print("je gaaat lekker, nog 1 vraag en dan ben je klaar")
time.sleep(1.5)
print("nu de grote vraag, hoe gaan we naar station")
time.sleep(1.5)
print("a- je stapt op de fiets")
time.sleep(1.5)
print("b- de bus is lekker makkelijk")
time.sleep(1.5)
print("c- jij gaat ff een stukje lopen")
time.sleep(1.5)
q3 = input("type alleen de kleine letter van de vraag en druk daarna op enter")

time.sleep(0.5)
print("trick question, het was allemaal goedgeweest")

if q3 == "a":
    print("maar jij bent wel lekker sportief maar niet te ingewikkeld")
elif q3 == "b":
    print("maar toch doe je me aan mezelf denken gewoon geen zin,")
    print("ik snap het wel ik doe het zelf ook altijd")
elif q3 == "c":
    print("maar jij gaat gewoon op volledig eigen kracht")
    print("doe je goed")

print("lekker gedaan bedankt voor het spelen :)")

