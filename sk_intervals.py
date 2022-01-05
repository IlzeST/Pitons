def noteiktIntervalu(d1, d2, sk):
    rezultats="Nepieder intervālam"
    if sk>=d1 and sk<=d2:
        rezultats="Pieder intervālam"
    return rezultats


d1=int(input("Ievadiet intervāla sākumu!\n"))
d2=int(input("Ievadiet intervāla beigas!\n"))
sk=int(input("Ievadiet skaitli!\n"))

rez=noteiktIntervalu(d1,d2,sk)
print(rez)