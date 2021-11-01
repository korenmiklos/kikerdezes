import csv
import random
import sys
from Levenshtein import jaro_winkler

class Pair:
    def __init__(self, question, prompt, answer):
        self.question = question
        self.prompt = prompt
        self.answer = answer
        self.ask = self.question.format(self.prompt)

def equals(text1, text2):
    return jaro_winkler(text1.lower(), text2.lower()) > 0.95

def short_text(pair):
    answer = input(pair.ask)
    return equals(answer, pair.answer)

def read_from_csv(fname, question1, question2):
    '''
    read_from_csv('fovarosok.csv', 'Mi {} fővárosa? ', 'Minek a fővárosa {}? ')
    '''
    pairs = []
    with open(fname, 'rt') as f:
        for row in csv.reader(f):
            pairs.append(Pair(question1, row[0], row[1]))
            pairs.append(Pair(question2, row[1], row[0]))
    return pairs

def main():
    pairs = read_from_csv('data/fovarosok.csv', 'Mi {} fővárosa? ', 'Minek a fővárosa {}? ')
    random.shuffle(pairs)
    for pair in pairs:
        while not short_text(pair):
            print('Helytelen.')
        print('Na azért.')

main()
