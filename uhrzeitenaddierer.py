def uhrzeit_minuten_addieren(stunden, minuten, summand):
  #In der Klammer steht die Menge, die die Variable "uhrzeit_minuten_addieren" enthält
  
    if minuten+summand >= 60:
      #wenn diese Minuten den dazugerechneten Minuten(Summand) über 60 oder 60 betragen, soll das folgende ausgeführt werden
      stunden=stunden+1
#bei den Stunden soll plus eins gerechnet werden
      minuten=minuten-60
      #und bei den Minuten soll minus 60 gerechnet werden, damit die Minuten wieder bei null stehen(neue Stunde)

    print(str(stunden)+":"+str(minuten+summand))
#Der Output soll sein: die Stunden(oben im Programm ist stunden eine Variable) dann ein Doppelpunkt("" da es nichts ausrechnen soll) und rechts vom Doppelpunkt sollen die Minuten mit dem dazugerechneten Summand stehen.

uhrzeit_minuten_addieren(17,32,8)
uhrzeit_minuten_addieren(17,58,20)
#Diese oberen zwei sollen mit dem obrigen Code gerechnet werden.
