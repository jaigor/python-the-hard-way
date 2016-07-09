# tuples of different types of words
# directions to move somewhere
directions = [('direction', 'north'),
              ('direction', 'south'),
              ('direction', 'east'),
              ('direction', 'west'),
              ('direction', 'down'),
              ('direction', 'up'),
              ('direction', 'left'),
              ('direction', 'right'),
              ('direction', 'back')]

# verbs to do something
verbs = [('verb', 'go'),
         ('verb', 'stop'),
         ('verb', 'kill'),
         ('verb', 'eat'),]

# stops words
stops = [('stop', 'the'),
         ('stop', 'in'),
         ('stop', 'of'),
         ('stop', 'from'),
         ('stop', 'at'),
         ('stop', 'it')]

# nouns to do reference things
nouns = [('noun', 'door'),
         ('noun', 'bear'),
         ('noun', 'princess'),
         ('noun', 'cabinet')]

# scans the words (inputs) sent by the user
def scan(inputs):
    # splits all the strings separated by a blank space
    words = inputs.split()
    # list used to save the words found
    found_words = []

    # iterates in each separate word
    for word in words:
        found = False

        # looks in every tuple list if exits the word looked for
        for direction in directions:
            if direction[1] == word.lower(): # converts all strings to lowercase
                found_words.append(direction)
                found = True

        for verb in verbs:
            if verb[1] == word.lower():
                found_words.append(verb)
                found = True

        for stop in stops:
            if stop[1] == word.lower():
                found_words.append(stop)
                found = True

        for noun in nouns:
            if noun[1] == word.lower():
                found_words.append(noun)
                found = True

        if len(word) >= 0 and len(word) <= 9:
            number = convert_number(word)
            if number != None:
                found_words.append(('number', number))
                found = True

        if found == False:
           found_words.append(('error', word))

    return found_words


# converts the string s into an integer or None
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None