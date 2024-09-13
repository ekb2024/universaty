class WordsFinder:
    tab = (',', '.', '=', '!', '?', ';', ':', ' - ')
    def __init__(self,*args):
        self.file_names = []
        for i in args:
           self.file_names.append(i)
    def get_all_words(self):
        stroka = ''
        all_words = {}
        for i in self.file_names:
            with open(i,encoding='utf-8') as file:
                  for line in file:
                      for n in range(len(WordsFinder.tab)):
                          line = line.lower().replace(WordsFinder.tab[n],'')
                      stroka += line
                      all_words.update({i : stroka.split()})
        return all_words

    def find(self,word):
        new_dect_word = {}
        number_word = 0
        for name_file, words in self.get_all_words().items():
            for i in words:
               number_word += 1
               if word.lower() in i:
                   new_dect_word.update({name_file:number_word})
                   return new_dect_word

    def count(self,word):
        new_dect_word = {}
        x_word = 0
        for name_file, words in self.get_all_words().items():
            for i in words:
                if word.lower() in i:
                    x_word += 1
                    new_dect_word.update({name_file: x_word})
            return new_dect_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('TEXT'))
