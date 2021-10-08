Getal = 25
Vraag = 'ja'
AantalKansen = 1
Score = 0


while Vraag == "ja" and AantalKansen <=10:
    VraagGetal = int(input("Raad het getal "))
    AantalKansen = AantalKansen + 1
    WarmKoud = Getal - VraagGetal
    if VraagGetal > Getal:
        print ("lager")
    elif VraagGetal < Getal:
        print ("Hoger")

        if WarmKoud <= 50 and WarmKoud > 20:
            print ("Je bent warm")
        elif WarmKoud <= 20:
            print ("Je bent heel warm")

    if VraagGetal == Getal:
        print ("Je hebt het getal geraden")
        Vraag = 'nee'
        Score = Score + 1
        print ("Je score is" , Score)
    elif AantalKansen >= 11:
        print ("Je kansen zijn op en je hebt het getal niet geraden")
        print ("Je score is" , Score)

Opnieuw = input("Wil je opnieuw ja of nee? ")
if Opnieuw == "ja":
    Vraag = 'ja'
    AantalKansen = 1
elif Opnieuw == "nee":
    print ("Je bent gestopt je score was", Score)