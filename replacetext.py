def replacetext(filename, newtext, oldtext):
    with open(filename, 'r+') as file:
        text = file.read()
        i = text.index(oldtext)
        file.seek(0)
        file.write(text[:i] + newtext + text[i + len(oldtext):])