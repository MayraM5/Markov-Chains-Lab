"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # file = open("green-eggs.txt")
    # text_as_str = ''

    # for line in file:
    #     line = line.rstrip()
    #     text_as_str += line + ' '

    # return text_as_str #file of file_path as one long string'
    
    file = open("green-eggs.txt").read()
    return file

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    
    # words = open_and_read_file(text_string).split()
    words = text_string.split()

    chains = {}
   

    for i in range(len(words) -2):
        key = (words[i], words[i+1])

        if key in chains:
            chains[key].append(words[i+2])
        else:
            chains[key] = [words[i + 2],]    

    return chains            

def make_text(chains):
    """Return text from chains."""

    words = []

    key = choice(list(chains)) #take keys from chains{}, convert it into list
    words.extend(key)

    while key in chains:
        value = chains[key]
        next_word = choice(value)
        words.append(next_word)
        key = (key[1], next_word) #<----if this is false it will stop
    
    
    return ' '.join(words)

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
