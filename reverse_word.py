def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    # Joining the reversed list of words into a string
    reversed_text = ' '.join(reverse_word_list)
    return reversed_text

# Calling the function
print(master_yoda('i am home'))
