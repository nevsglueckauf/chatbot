
class ChatBot:
    pass # Platzhalter; "tue nix" --> um korrekte Syntax einzuhalten

    bot_name = ''
    language = 'DE' # Datenattribut
    welcome = 'Guten Tag, ich heisse'
    your_name = 'Und wie heisst Du?'
    answer_bot = 'Dummyantwort'
    quit = 'stop'
    question = 'Und weiter? '
    answer = ''

    #####

    known_names = ['Nadja', 'Andrei', 'Manuel', 'Sven', 'Jakob']

    #####

    user_name = ''
    # Attribut -> Methoden / Funktionen

    # __NAME__ --> double underscore --> 
    def __init__(self, name):
        self.bot_name = name


    def run(self):
        print(self.welcome, self.bot_name, self.your_name)
     
        while self.answer.lower() != self.quit:
            self.answer = input(self.question)
            self.split_words(self.answer)
            self.bot_says()

    def bot_says(self):
        print(self.answer_bot)

    def split_words(self, sentence: str): 
        # Ich heisse nämlich Sven -> ['ich',  'heisse', 'Sven', 'nämlich' ]
        tmp = sentence.split()
        
        self.clean(tmp)
        self.is_known(tmp)
        print(tmp)
        exit()

    def clean(self, words: list):
        for word in words:
            #print(word)
            pass
    
    def is_known(self, words: list):
        for word in words:
            if word in self.known_names:
                self.user_name = word
       


Maja = ChatBot('Bine')

Maja.run()
