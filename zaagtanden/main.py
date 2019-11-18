def tanden(l, r, t):
    for i in range(r, 0):
        print(t* l)
        t-=1;



tanden(input("Voer het letter in die je wil zien : "), int(input("Aantal regels: ")), int(input("Aantal tanden: ")))