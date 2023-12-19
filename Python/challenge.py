## Implement the add_prefix_un() function that takes word as a parameter and returns a new un prefixed word:
# Define Prefix as function
def add_prefix_un(word):
    return "un" + word
# declare the variable and print the function
word = "happy"
prefixed_word = add_prefix_un(word)
print(prefixed_word)  
### Implement the make_word_groups(<vocab_words>) function that takes a vocab_words as a parameter in the following form: [<prefix>, <word_1>, <word_2> .... <word_n>], and returns a string with the prefix applied to each word that looks like: '<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'.
##Define make_word_group
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    word_groups = " :: ".join([prefix] + prefixed_words)
    return word_groups
# using the function with prefix words
#with prefix 'en'
vocab_words = ['en', 'close', 'joy', 'lighten']
word_groups = make_word_groups(vocab_words)
print(word_groups)
# with prefix 'pre'
vocab_words = ['pre', 'serve', 'dispose', 'position']
word_groups = make_word_groups(vocab_words)
print(word_groups)
# with prefix 'auto'
vocab_words = ['auto', 'didactic', 'graph', 'mate']
word_groups = make_word_groups(vocab_words)
print(word_groups)
# with prefix 'inter'
vocab_words = ['inter', 'twine', 'connected', 'dependent']
word_groups = make_word_groups(vocab_words)
print(word_groups)
### Remove suffix from a word
### Implement the remove_suffix_ness(<word>) function that takes in a word str, and returns the root word without the ness suffix.
# Define suffix ness word
def remove_suffix_ness(word):
    if word.endswith("ness"):
        if word[-5] == "i":
            return word[:-5] + "y"
        else:
            return word[:-4]
    return word
# Remove suffix ness in the word heaviness, sadness
word = "heaviness"
root_word = remove_suffix_ness(word)
print(root_word)
word = "sadness"
root_word = remove_suffix_ness(word)
print(root_word)
### Implement the adjective_to_verb(<sentence>, <index>) function that takes two parameters. A sentence using the vocabulary word, and the index of the word, once that sentence is split apart. The function should return the extracted adjective as a verb.
def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index]
    
    if adjective.endswith("y"):
        verb = adjective[:-1] + "en"
        
    else:
        verb = adjective.strip(".") + "en"       
    
    return verb

sentence = 'I need to make that bright.'
index = -1
verb = adjective_to_verb(sentence, index)
print(verb)  
sentence = 'It got dark as the sun set.'
index = 2
verb = adjective_to_verb(sentence, index)
print(verb)  





