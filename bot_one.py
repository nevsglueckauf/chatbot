import re
import random

class ChatBot_Gen_One:

  command_end = ['quit']
  
  welcome = 'Guten Tag, mein Name ist'
  
  #   "Ich brauche (.*)",
  regex_action = [{'regex': r'Ich brauche (\w+)',
                   'answer': ['Warum brauchst du {0}?',
                              'Würde {0} dir denn wirklich helfen?',
                              'Bist du sicher, dass du {0} brauchst?']
                  },
                  {'regex': r'Ich will (.*)',
                   'answer': ['Warum möchtest du {0}?',
                              'Was erhoffst du dir von {0}?',
                              'Gibt es einen bestimmten Grund, warum du {0} willst?']
                  },
                  {
                   'regex': r'Ich heiße(.*)',
                   'answer': ['Hallo {0}',
                              'Guten Tag {0}',
                              'Nett dich kennzulernen {0}',
                              'Endlich lerne ich dich mal kennen, {0} - ich habe schon so viel gehört über dich'
                              ]
                  },
                  {'regex': r'[Mm]ein(.*) (.*)',
                   'answer': ['Warum denkst Du, dass dein{0}?',
                              'Wie beeinflusst es dein Leben, dass dein{0}?',
                              'Hast du mit jemandem daüber gesprochen, dass dein{0} ?']
                  },
                  {'regex': r'Ich brauche (.*)',
                   'answer': ['Warum brauchst du {0}?',
                              'Würde {0} dir denn wirklich helfen?',
                              'Bist du sicher, dass du {0} brauchst?']
                  },
                  {'regex': r'Kannst du (.*)?', 
                   'answer': ['Ich kann {0} gerne versuchen!',
                              'Das kann ich leider nicht machen!',
                              'Kannst du nicht selbst {0}?']
                  },
                  {'regex': r'Wie geht es dir',
                    'answer': ['Danke. Mir geht es gut und dir?',
                               'Sehr gut, danke. Und wie läuft es bei dir?',
                               'Ich kann nicht klagen. Was ist mit dir?',
                               'Bestens. Und dir?']
                  },
                  {'regex': r'[Ee]rzähle mir (?:einen|einen weiteren) Witz',
                   'answer':['Kommt ein Pferd in die Kneipe, fragt der Wirt: warum so ein langes Gesicht?',
                               'Ich wollte Spiderman anrufen, aber er hat gerade kein Netz',
                              'Wissenschaftler haben herausgefunden... – und sind wieder hineingegangen.']
                  },
                  {'regex': r'erzähle mir von (.*)',
                   'answer': ['Gerne erzähle ich dir mehr über {0}. Was interessiert dich daran?',
                              'Was möchtest du über {0} wissen?',
                              'Ich kann dir einige Informationen über {0} geben.']
                  },
               
                  {'regex': r'Mir geht es gut(.*)',
                   'answer': ['Das freut mich.',
                              'Das hört man gerne',
                              'Sehr schön. Wo waren wir...?',
                              'Erzähle mir mehr..'
                             ]
                  },
                  {'regex': r'quit',
                   'answer': ['Auf Wiedersehen ..',
                              'Bye, bye!',
                              'Bis zum nächsten Mal']
                  },
                  
                  {'regex': r'[A-Za-z0-9_-](.*)',
                   'answer': ['Das habe ich nicht so recht verstanden ..',
                              'Magst Du das bitte anders formulieren?',
                              'Ach komm es - ist auch für mich spät']
                  }]
  
  def __init__(self, name = 'Dr. Seltsam'):
    print(self.welcome, name)
  

  def read(self, user_input):
    for item in self.regex_action:
      answer_given = False
      
      #regex = re.compile(item['regex'], re.I)
      #mtc = re.search(item['regex'], user_input, re.I)
      
      #regex = re.compile(item['regex'], re.I)
      mtc = re.search(item['regex'], user_input, re.I)
      
      if mtc:
          #print('Bot::', mtc)
          print('Bot::', item['answer'][random.randrange(0, len(item['answer']))].format(' '.join(mtc.groups())))
          answer_given = True
          break
   
  def run(self):
    phrase = ''
    while not phrase.lower() in self.command_end:
      phrase = input('User::')
      self.read(phrase)
      
  def read_file(self):
    pass

  def write_line(self, line):
    pass
    
v = ChatBot_Gen_One('ChatBot 2025')
v.run()