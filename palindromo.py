pal=str(input("palavra: ")).lower().replace(" ","")
pal2=pal[::-1]
if pal2 == pal:
    print("palindromo")
else:
    print("não")