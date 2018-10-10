from nltk.tokenize import sent_tokenize, word_tokenize

example_text = input("Enter a Sentence:\n")

sentence_list = sent_tokenize(example_text)
word_list = word_tokenize(example_text)

print("\nThe sentence is...")
for s in sentence_list:
    print(s)

print("\nThe words are...")
for w in word_list:
    print(w)
