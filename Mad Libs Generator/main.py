import random

noun = input('Please enter a noun: ')
verb = input('Please enter a verb: ')
adjective = input('Please enter an adjective: ')
adverb = input('Please enter an adverb: ')

phraseList = ['He said ADVERB as he jumped into his convertible NOUN and VERB with his ADJECTIVE wife.',
              'He VERB ADVERB towards ADJECTIVE NOUN.',
              'The ADJECTIVE NOUN who VERB the person ran away ADVERB.']

def replace(phrase, part, word):
    pos = phrase.find(part)
    str = phrase[0:pos] + word + phrase[pos + len(part):]
    return str

def chooseRandomPhrase(phraseList):
    randomPhraseNumber = random.randint(0,len(phraseList) - 1)
    return phraseList[randomPhraseNumber]


def madlibs(phraseList,noun,verb,adjective,adverb):
    randomPhrase = chooseRandomPhrase(phraseList)

    randomPhrase = replace(randomPhrase, 'NOUN', noun.lower())
    randomPhrase = replace(randomPhrase, 'ADVERB', adverb.lower())
    randomPhrase = replace(randomPhrase, 'VERB', verb.lower())
    randomPhrase = replace(randomPhrase, 'ADJECTIVE', adjective.lower())
    return randomPhrase

print(madlibs(phraseList,noun,verb,adjective,adverb))

