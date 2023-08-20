from typing import List
from collections import defaultdict


#O(N) space complexity
#O(M * (k * log k)) time complexity
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        #store sentences and theor frequencies in adictionary where key=starting char
        self.prefix_map = defaultdict(list)
        self.input_str = "" #iniialise input str

        #populate dict with sentences and their frequencies
        for i, sentence in enumerate(sentences):
            self.prefix_map[sentence[0]].append((-times[i], sentence)) #use -ve for sorting later

    def input(self, c:str) -> List[str]:
        #if input is completed, add curr str to dict with frequency = 0
        if c == "#":
            self.prefix_map[self.input_str[0]].append((0, self.input_str))
            self.input_str = "" #reset str
            return []

        self.input_str += c #update input str
        suggestions = self.prefix_map[self.input_str[0]] #get suggestions for curr prefix
        suggestions.sort() #sort suggestions by frequency (-ve value)

        result = []
        count = 0

        for freq, sentence in suggestions:
            if sentence.startswith(self.input_str):
                result.append(sentence)
                count += 1
            if count == 3:
                break

        return result # return autocomplete suggestion
    

sentences = ["i love you", "island", "ironman", "i love coding"]
times = [5,3,2,2]
autocomplete = AutocompleteSystem(sentences, times)

print(autocomplete.input("i"))
print(autocomplete.input(" "))
print(autocomplete.input("a"))
print(autocomplete.input("h"))

print(autocomplete.input("i"))
