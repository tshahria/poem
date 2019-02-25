import requests


noun = input("enter a noun \n")

adjective = requests.get('https://api.datamuse.com//words?rel_jjb=' + (requests.get('https://api.datamuse.com/words?rel_rhy=' + noun).json()[0]['word'])).json()[0]['word']

rhyme = requests.get('https://api.datamuse.com/words?rel_rhy='+ adjective).json()[0]['word']
result = [[noun,adjective,rhyme]]

for i in range(3):
    curr = []

    nouns = requests.get('https://api.datamuse.com/words?ml=' +result[-1][0]).json()

    newNoun = nouns[0]['word']

    adjectives = requests.get('https://api.datamuse.com//words?rel_jjb=' + newNoun).json()
    newAdjective = adjectives[0]['word']

    newRhyme = requests.get('https://api.datamuse.com/words?rel_rhy=' + newAdjective).json()[0]['word']
    result.append([newNoun,newAdjective,rhyme])


for arr in result:
    print(' '.join(arr) +'\n')

