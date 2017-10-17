class Lexicon(object):

    def scan(self,stuff):
        self.stuff = stuff
        self.words = stuff.split()
        pairs = []
        lexicon = [('direction', 'north', 'south', 'east', 'west'),('verb', 'go', 'kill', 'eat'),('nouns', 'princess', 'bear')]

        for word in self.words:

            if word in lexicon[0]:
                pairs.append(('direction', word))
            elif word in lexicon[1]:
                pairs.append(('verb', word))
            elif word in lexicon[2]:
                pairs.append(('nouns', word))
            else: 
                pairs.append(('error', word))

        print pairs


