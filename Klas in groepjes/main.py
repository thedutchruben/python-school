import random;
todoNameList = [
    "Ruben de Roos",
    "Charlotte Vermeulen",
    "Ruben Scheepstra",
    "Thomas de Boer",
    "Erik Veenstra",
    "Robbin Mulder",
    "Jorrit Tjepkema",
    "Lars Volbeda",
    "Lars Bosscher",
    "Carlo van der Wal",
    "Dimitri Westerveld",
    "Martha De Vries",
    "Siebe Witteveen",
    "Sytze Dalstra",
    "Colin Feringa",
    "Jorrit de Haan",
    "Jelle Komrij",
    "Jonathan Naberman",
    "Jesper Schreuder",
    "Hylke Storteboom"
]


def split(l,n):
    random.shuffle(todoNameList)
    for i in range(0,len(l),n):
        yield l[i:i+n]


print(list(split(todoNameList,int(input("Grote van de groepjes : ")))))