# nl = '\n'
# datei = open('chat.txt','a')
# datei.write('Neue Zeile blubb' + nl)

datei = open('chat.txt', 'r')
alles = datei.readline()

print(alles,end='::')
alles = datei.readline()
print(alles,end='::')


# Was willst Du tun?
# r - lies protokoll
# w - schreibe protokoll
