def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

# Check
print(paper_doll('hello'))

# Check
print(paper_doll('mississippi'))
