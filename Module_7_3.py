class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = dict()
        for file in self.file_names:
            with open(file, "r", encoding="utf-8") as f:
                string = f.read().lower()
                symbol = (',', '.', '=', '!', '?', ';', ':', ' - ')
                for s in symbol:
                    string = string.replace(s, "")
                all_words[file] = string.split()
        return all_words

    def find(self, word):
        dict_words = self.get_all_words()
        counter = 0
        for key in dict_words:
            for slovo in dict_words[key]:
                counter += 1
                if slovo.lower() == word.lower():
                    return {key: counter}

    def count(self,word):
        dict_words = self.get_all_words()
        counter = 0
        for key in dict_words:
            for slovo in dict_words[key]:
                if slovo.lower() == word.lower():
                    counter += 1
            return {key: counter}
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
