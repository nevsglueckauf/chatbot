import re
import random
import os

class ChatBot_Gen_One:

  command_end = ['stop', 'quit', 'end', 'exit']
  regex_action = [{'r': r"Ich brauche (.*)",
                   'a': ["Warum brauchst du {0}?",
                        "Würde {0} dir denn wirklich helfen?",
                        "Bist du sicher, dass du {0} brauchst?"]
                  },
                  {'r': r"Ich will (.*)",
                   'a': ["Warum möchtest du {0}?",
                         "Was erhoffst du dir von {0}?",
                         "Gibt es einen bestimmten Grund, warum du {0} willst?"]
                  },
                  {'r': r"[Mm]ein (.*) (.*)",
                   'a': ["Warum denkst Du, dass dein {0}?",
                         "Wie beeinflusst dein {0}  dein Leben?",
                         "Hast du mit jemandem daüber gesprochen, dass dein {0} ?"]
                  },
                  {'r': r"Ich brauche (.*)",
                   'a': ["Warum brauchst du {0}?",
                         "Würde {0} dir denn wirklich helfen?",
                         "Bist du sicher, dass du {0} brauchst?"]
                  },
                  {'r': r"Kannst du (.*)?", 
                   'a': ["Ich kann {0} gerne versuchen!",
                         "Das kann ich leider nicht machen!",
                         "Kannst du nicht selbst {0}?"]
                  },
                  {'r': r"Wie geht es dir?",
                    'a': ["Danke. Mir geht es gut und dir?",
                          "Sehr gut, danke. Und wie läuft's bei dir?",
                          "Ich kann nicht klagen. Was ist mit dir?"]
                  },
                  {'r': r"[Ee]rzaehle mir (?:einen|einen weiteren) Witz",
                    'a':["Natürlich! Hier ist ein Witz für dich: Warum hat der Kühlschrank den Laptop nicht bezahlt? Weil er schon eine eigene Rechnung hatte!",
                          "Klar, hier ist einer: Was macht ein Clown im Büro? Faxen!",
                          "Warum hat der Mathematiker eine Brille? Weil er mit Zahlen jongliert!",
                          "Was ist grün und läuft durch den Wald? Eine Rudel Gurken!"]

                  },
                  {'r': r"Erzaehle mir von (.*)",
                   'a': ["Gerne erzähle ich dir mehr über {0}. Was interessiert dich daran?",
                         "Was möchtest du über {0} wissen?",
                         "Ich kann dir einige Informationen über {0} geben."]
                  },
                  {'r': r"^[A-Za-z0-9_-]*$",
                   'a': ['Das habe ich nicht so recht verstanden ..',
                         'Magst Du das bitte anders formulieren?']
                  }
  ]
  
  def __init__(self):
    prcommand = 'cls' if os.name.startswith('nt') else 'clear'
    os.system(prcommand)

  

  def read(self, user_input):
    for item in self.regex_action:
      answer_given = False
      regex = re.compile(item['r'], re.I)
      mtc = regex.search(user_input)
      if mtc != None:
          print(item['a'][random.randrange(0, len(item['a']))].format(' '.join(mtc.groups())))
          answer_given = True
          break
      
         

  def run(self):
    foo = ''
    while not foo.lower() in self.command_end:
      foo = input('|')
      self.read(foo)
      
    print ('bye, bye')
    
v = ChatBot_Gen_One()
v.run()