def split(t, l):
    l-=3
    text = ""
    for s in t.split():
        if l-len(s) >= 0:
            text += (s + " ")
            l-=len(s)
        else:
            l = 0

    text += "..."
    print(text)

split(input("Voer hier je title in : "), int(input("voer hier je maximale lengte in : ")))