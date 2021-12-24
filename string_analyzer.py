from string import punctuation
class Analyzer:
    def __init__(self,s):
        for c in punctuation:
            s=s.replace(c,'')
            s=s.lower()
            self.words=s.split()
    def number_of_words(self):
        return len(self.words)
    def starts_with(self,s):
        return len([words for words in self.words if words[:len(s)]==s])
    def number_with_length(self, n):
        return len([w for w in self.words if len(w)==n])
s = 'is this the classroom?,hopefu;;y!!! helo boys:::/.'
analyzer = Analyzer(s)
print(analyzer.words)
print('Number of words:', analyzer.number_of_words())
print('Number of words starting with "c":', analyzer.starts_with('c'))
print('Number of 4-letter words:', analyzer.number_with_length(4))
