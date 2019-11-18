def dagen(d,a):
    dagen = 25
    if d >= 25 :
        if ( d <= 40):
            dagen+= 2
        else:
            dagen+= 5

    if a >= 45:
        if a <= 55:
            dagen+= 1

    if a >= 56:
        if a <= 65:
            dagen+= 2
    return "Vakantie dagen : "+ str(dagen);

print( dagen(int(input("Jaren in dienst : ")) , int(input("Leeftijd : "))))