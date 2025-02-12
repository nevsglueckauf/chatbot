import re
import random


class ChatBot_Gen_One:

  command_end = ['quit']
  
  welcome = 'Guten Tag, ich heisse'

  user_name = 'Nadja'
  au =  r' [ich heisse | mein Name ist] (.*)'

  regex_action = [{'regex': r'Mir geht es nicht gut',
                 'answer': ['Es tut mir leid zu hören, dass es dir nicht gut geht. Möchtest du darüber sprechen?',
                            'Wenn du irgendetwas brauchst oder ich dir helfen kann, lass es mich wissen.',
                            'Ich bin für dich da, egal was du brauchst. Manchmal kann es helfen, einfach mit jemandem zu reden.']
                  },
                  {'regex': r'Ich (.*) gern',
                 'answer': ['Das klingt interessant. Erzähl mir mehr über {0}n',
                            'Welche Ziele hast du beim {0}n',
                            'Wie kann ich dir helfen, wenn du {0}n möchtest']
                  },
                  {'regex': r'Mein Hobby ist (.*)',
                 'answer': ['Das klingt interessant. Erzähl mir mehr vom {0}.',
                            'Welche Ziele hast du beim {0}?',
                            'Wie kann ich dir helfen, wenn du {0} möchtest?']
                  },
                  {'regex': r'Ich habe vor (.*)',
                 'answer': ['Schön, dass du {0} möchtest',
                            'Wonach suchst du, wenn du {0} möchtest',
                            'Wie kann ich dir helfen, wenn du {0} möchtest']
                  },
                  {'regex': r'Ich möchte (.*)',
                 'answer': ['Schön, dass du {0} möchtest',
                            'Wonach suchst du, wenn du {0} möchtest',
                            'Wie kann ich dir helfen, wenn du {0} möchtest']
                  },
                  {'regex': r'Ich heisse (.*)',
                 'answer': ['Schön, dass du da bist, {0}!',
                            'Wonach suchst du, {0}?',
                            'Wie kann ich dir helfen, {0}?']
                  },
                  {'regex': r'Ich brauche (.*)',
                   'answer': ['Warum brauchst du {0}?',
                              'Würde {0} dir denn wirklich helfen?',
                              'Bist du sicher, dass du {0} brauchst?']
                  },
                  {'regex': r'Ich will (.*)',
                   'answer': ['Warum möchtest du {0}?',
                              'Was erhoffst du dir von {0}?',
                              'Gibt es einen bestimmten Grund, warum du {0} willst?']
                  },
                  #{'regex': r'[Mm]ein(.*) (.*)',
                   #'answer': ['Warum denkst Du, dass dein{0}?',
                              #'Wie beeinflusst es dein Leben, dass dein{0}?',
                              #'Hast du mit jemandem daüber gesprochen, dass dein{0}?']
                  #},
                  {'regex': r'Ich wünsche mir (.*)',
                   'answer': ['Warum wünschst du dir {0}?',
                         'Würde {0} dir denn wirklich helfen?',
                         'Bist du sicher, dass du {0} brauchst?',
                         'Dabei wünsche ich dir viel Erfolg!']
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
                              'Chuck Norris hält seine eigenen Elfmeter',
                              'Welche Sportler reden am wenigsten? Tennisspieler! Drei Sätze und dann ist Schluss!'
                              '']

                  },
                  {'regex': r'Erzähle mir von (.*)',
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
                   'answer': ['Auf Wiedersehen, {0}',
                              'Bye, bye, {0}',
                              'Bis zum nächsten Mal, {0}']
                  },
                  {'regex': r'[A-Za-z0-9_-](.*)',
                   'answer': ['Das habe ich nicht so recht verstanden ...',
                              'Magst Du das bitte anders formulieren?',
                              'Ach komm - es ist auch für mich spät']
                  }]
  
  def __init__(self, name = 'Dr. Seltsam'):
    print(self.welcome, name, ' Wie ist dein Name?')
  

  def read(self, user_input):
    for item in self.regex_action:
      answer_given = False
      
      #regex = re.compile(item['regex'], re.I)
      #mtc = re.search(item['regex'], user_input, re.I)
      
      regex = re.compile(item['regex'], re.I)
      mtc = regex.search(user_input)
      
      if mtc:
          text = ' '.join(mtc.groups())
          print('Bot:', item['answer'][random.randrange(0, len(item['answer']))].format(text))
          answer_given = True
          break
      
  
    
    

  def run(self):
    phrase = ''
    while not phrase.lower() in self.command_end:
      phrase = input('User: ')
      self.read(phrase)
      
v = ChatBot_Gen_One('ChatBot 2025.')
v.run()