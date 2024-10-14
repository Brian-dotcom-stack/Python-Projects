# Remove extra spaces between words

"""
Given the following sentence, find a way to remove all the extra
spaces and print the same sentence with just one space between words.

paragraph = "Argentina wins football  world cup 2022  in a nail biting final  match
that  led to  a spectacular penalty  shootout.  Football  lovers across  the world hailed 
it as one  of the memorable matches ."
"""

def remove_extra_spaces(paragraph):

 # Split the paragraph into words and rejoin them with a single space
 clean_paragraph = ' '.join(paragraph.split())
 return clean_paragraph


# Given paragraph

paragraph = """Argentina wins football  world cup 2022  in a nail biting final  match
that  led to  a spectacular penalty  shootout.  Football  lovers across  the world hailed 
it as one  of the memorable matches ."""

# Call the function and print result

clean_paragraph = remove_extra_spaces(paragraph)
print(clean_paragraph)