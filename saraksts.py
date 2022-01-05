def izdruka (daudzums, sar1):
    for elementi in range(0,daudzums):
        print(sar1[elementi])
    #return 0

sar1=[1,2,3,3,4,4,5,5,6,7,8,9,10]
daudzums=int(input("Norādiet daudzumu\n"))
rez = izdruka(daudzums, sar1)
print(rez)

