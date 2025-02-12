import re

txt = 'Pyromane Peter sagt: Hallo Python im All Pythonschlange' #raw String --> für Regex 
#      
#print(txt[6:6+len('Python')])       

# Sonderzeichen in re \b -> boundary -> Wortgrenze
#                     \w -> word     -> Wort
matches = re.findall(r'\bPyth\w+\b', txt, re.I)
print(matches)

# Funktion addiere -> 2 Zahlen a,b





class RechnerKlasse():
    def addiere(self, a, b): # Methode
        return a+b

    def moo(self):
        print('Muh')


rechner = RechnerKlasse()
x = rechner.addiere(55, 102)
print(x)
rechner.moo()