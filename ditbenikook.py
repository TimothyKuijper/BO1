from re import A
import time

print("hai ik ben tim")
time.sleep(1)
print("hoe heet jij")
naam = input("vul hier je naam in: ")
print("leuk je te leren kennen", naam,)
time.sleep(1)

while True:

    print("ik heb vroeger allemaal verschillende soorten sport gedaan, wat  voor sport heb ik gedaan")
    time.sleep(1)
    print("a- voetbal en kravmaga")
    time.sleep(1)
    print("b- voetbal en tennis")
    time.sleep(1)
    print("c- tennis en kravmaga")
    q1 = input("type alleen de kleine letter van de vraag en druk daarna op enter>")


    time.sleep(0.5)


    if q1 == "a":
        print("ja dat klopt, lekker gedaan")
        q1 == "C"
        break
    elif q1 == "b":
        print("ik heb spijt van voetbal maar fuck tennis broer")
        time.sleep(1)
        continue
    elif q1 == "c":
        print("kravmaga klopt maar fuck tennis broer")
        time.sleep(1)
        continue
    else :
        continue

    
while True:

    time.sleep(0.5)

    print("vanaf het moment dat het kan ben ik al aan het werk. waar werk ik nu?")
    time.sleep(1)
    print("a- ober in een restaurant in castricum")
    time.sleep(1)
    print("b- thuisbezorgd in amsterdam")
    time.sleep(1)
    print("c- schoonmaker op een school")
    q2 = input("type alleen de kleine letter van de vraag en druk daarna op enter>")

    time.sleep(0.5)

    if q2 == "a":
        print("nee horeca werk is niks voor mij.")
        time.sleep(1)
        continue
    elif q2 == "b":
        print("ja dat klopt.")
        q2 == "C"
        break
    elif q2 == "c":
        print("doe normaal jij denkt ik ga de hele dag schoon staan maken")
        time.sleep(1)
        continue
    else :
        continue

time.sleep(0.5)

print("je gaaat lekker, nog 1 vraag en dan ben je klaar")

while True :

    time.sleep(1)
    print("wat zijn mijn hobbies")
    time.sleep(1)
    print("a- gamen en vissen")
    time.sleep(1)
    print("b- gamen en beunen")
    time.sleep(1)
    print("c- beunen en vissen")
    time.sleep(1)
    q3 = input("type alleen de kleine letter van de vraag en druk daarna op enter>")

    time.sleep(0.5)


    if q3 == "a":
        print("oei, met gamen zit je goed maar vissen vindt ik zo fucking saai")
        continue
    elif q3 == "b":
        print("jaja jij snapt het, gamen is gewoon leuk")
        print("en knutselen aan brommers is gewoon geweldig")
        q3 == "C"
        time.sleep(1)
        break
    elif q3 == "c":
        print("oei, kijk beunen heb je zeker gelijk in")
        print("maar vissen is gewoon zo fucking saai")
        time.sleep(1)
        continue
    else :
        continue

time.sleep(2)

if q1 or q2 or q3 == "C":
    print("jij had er iniedergeval 1 goed")

else:
    print("wow, jij  kent mij dus helemaal niet")
time.sleep(5)

