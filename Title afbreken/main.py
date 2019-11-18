def split(textInput, length):
    length -= 3
    text = ""
    for s in textInput.split():
        if length - len(s) >= 0:
            text += (s + " ")
            length -= len(s)
        else:
            length = 0

    text += "..."
    print(text)


split(input("Voer hier je title in : "), int(input("voer hier je maximale lengte in : ")))
