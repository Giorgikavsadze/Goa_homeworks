# 6) Write a function that takes a sentence, a word, and an index, and inserts the word into the sentence at the given index.

def bigger_sentence(sentence,word,ind):
    new=sentence.split("")
    new.insert(ind,word)
    result= "".join(new)
    print(result)

bigger_sentence("hello there","hi",1)