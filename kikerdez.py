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

def read_from_csv(fname):
    '''
    read_from_csv('fovarosok.csv')
    '''
    pairs = []
    with open(fname, 'rt') as f:
        rows = list(csv.reader(f))
        question1 = rows[0][0]
        question2 = rows[0][1]
        for row in rows[1:]:
            pairs.append(Pair(question1, row[0], row[1]))
            pairs.append(Pair(question2, row[1], row[0]))
    return pairs

def main():
    pairs = read_from_csv('data/fovarosok.csv')
    random.shuffle(pairs)
    for pair in pairs:
        while not short_text(pair):
            print('Helytelen.')
        print('Na azért.')

main()
