# Check if a name is in a sentence

'''
Write a script that given a sentence and a word it will tell
if the word is included in the sentence and how many time it 
appears in the sentence.
'''

# Output example:

#   ```sh
#   Please insert a sentence: this is a test
#   Please insert the word to search: test
#   The word test is included in the sentence
#   ```

def word_in_sentence(sentence, word):
 
  # Convert sentence to lower case to make search case insensitive
  sentence = sentence.lower()
  word = word.lower()

  # Split the sentence into words
  words = sentence.split()


  # Count the occurences
  word_count = words.count(word)

  # Check if word is in a sentence and how many times it appears

  if word_count > 0:
   return f"The word '{word}' is included in the sentence and it appears '{word_count}' times. "
  else:
   return f"The word '{word}' is not included in the sentence"


sentence = input("Please insert a sentence: ")
word = input("Please insert a word: ")

result = word_in_sentence(sentence, word)
print(result)