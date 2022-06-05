s = input("Bitte gib einen beliebigen Satz ein: ")                      # String(-Variable) für Nutzerinput wird erstellt
s = s.replace(" ","").lower()                                           #Anpassen des Strings zur effizienteren Nutzung

#Dicionary zur Zerlegung des Strings in einzelne Schlüssel-Zeichen
dict_zerlegung = {} 
for i in s:                                                             #for-Schleife durchläuft jedes einzelne Zeichen des Strings 
    if i in dict_zerlegung: 
        dict_zerlegung[i] += 1                                          #falls ein Eintrag bereits vorliegt wird der Betrag / Wert erhöht
    else: 
        dict_zerlegung[i] = 1                                           # falls es noch nicht vorlag, wird es mit dem Wert 1 angelegt

#Liste der Schlüssel der 3 höchsten Werte
liste = []
for _ in range(3):                                                      #3 Mal durchschlaufen, da man die 3 höchsten Schlüssel erhalten möchte
    liste.append(max(dict_zerlegung, key=dict_zerlegung.get))           #Liste wird der aktuelle Schlüssel des höhsten Wertes angehangen
    del dict_zerlegung[max(dict_zerlegung, key=dict_zerlegung.get)]     #der aktuell höchste Schlüssel-Wert-Eintrag wird gelöscht, um im nächsten Durchlauf einen neuen maximalen Wert, bzw. Schlüssel zu erhalten

#Ausgabe
print("Die drei häufigsten Zeichen sind " + liste[0] + ", " + liste[1] + " und " + liste[2]+ ".")