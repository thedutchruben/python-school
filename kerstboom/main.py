import colorama;
size = int(input("Voer de grote : "));
for aantal in range(0,int(input("voer het aan tal bomen in"))):
    for i in range(1, size):print((int(size - i) * " ") + (("#" * i) * 2))
    for i in range(0, 2): print(int(size-1) * " " + "**");