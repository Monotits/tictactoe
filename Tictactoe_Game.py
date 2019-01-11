print(" *** XOX - Tictactoe Game *** ")
print("      1   |   2   |   3\n"
      "      4   |   5   |   6\n"
      "      7   |   8   |   9\n")

import random

tictactoe = []
kullanıcı = []
bilgisayar = []
kazanan=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
varsa_kullanıcı=[]
varsa_bilgisayar=[]
xox=open("tictactoe.txt", "w+")
xox.write(" | | \n"
          " | | \n"
          " | | \n")
xox.close()

def tic():

    # Kullanıcı Bölümü
    while True:
        try:
            a = int(input("Bir Sayı Giriniz: "))
            if 0 >= a or a >= 10:
                print("Lütfen 1 ile 9 arasında bir sayı giriniz..")
            elif 0 < a < 10:
                if a in tictactoe:
                    print(a, "hücresi dolu lütfen farklı bir sayı seçin!")
                    continue
                else:
                    tictactoe.append(a)
                    kullanıcı.append(a)
                    with open("tictactoe.txt", "r+", encoding="utf-8") as xox:
                        if a == 1:
                            xox.seek(0)
                            xox.write("X")
                        elif a==2:
                            xox.seek(2)
                            xox.write("X")
                        elif a==3:
                            xox.seek(4)
                            xox.write("X")
                        elif a==4:
                            xox.seek(6)
                            xox.write("X")
                        elif a==5:
                            xox.seek(8)
                            xox.write("X")
                        elif a==6:
                            xox.seek(10)
                            xox.write("X")
                        elif a==7:
                            xox.seek(12)
                            xox.write("X")
                        elif a==8:
                            xox.seek(14)
                            xox.write("X")
                        elif a==9:
                            xox.seek(16)
                            xox.write("X")
                        break
        except:
            print("Lütfen tam sayı (1-9 Arasında) giriniz..")

    # Bilgisayar Bölümü
    while True:
        if 5 not in tictactoe:
            tictactoe.append(5)
            bilgisayar.append(5)
            with open("tictactoe.txt", "r+", encoding="utf-8") as xox:
                if 5 in tictactoe:
                    xox.seek(8)
                    xox.write("O")
                    break
        else:
            rastgele = [random.randint(1, 9) for i in range(1)]
            b = int(rastgele[0])
            if b in tictactoe:
                if len(tictactoe) ==9:
                    break
            else:
                tictactoe.append(b)
                bilgisayar.append(b)
                with open("tictactoe.txt", "r+", encoding="utf-8") as xox:
                    if b == 1:
                        xox.seek(0)
                        xox.write("O")
                    elif b == 2:
                        xox.seek(2)
                        xox.write("O")
                    elif b == 3:
                        xox.seek(4)
                        xox.write("O")
                    elif b == 4:
                        xox.seek(6)
                        xox.write("O")
                    elif b == 6:
                        xox.seek(10)
                        xox.write("O")
                    elif b == 7:
                        xox.seek(12)
                        xox.write("O")
                    elif b == 8:
                        xox.seek(14)
                        xox.write("O")
                    elif b == 9:
                        xox.seek(16)
                        xox.write("O")
                    break

def oyuncu1():
    a = [(x,y,z) for x in kullanıcı for y in kullanıcı for z in kullanıcı if x != y and x != z and y != z]
    for i in a:
        for j in kazanan:
            if i==j:
                varsa_kullanıcı.append(i)
                return True


def oyuncu2():
    b = [(x,y,z) for x in bilgisayar for y in bilgisayar for z in bilgisayar if x != y and x != z and y != z]
    for i in b:
        for j in kazanan:
            if i==j:
                varsa_bilgisayar.append(i)
                return True

while len(tictactoe) <=9 :
    if oyuncu1():
        print(kullanıcı)
        print(bilgisayar)
        print(" *** Tebrikler Kazandınız! *** ")
        with open("tictactoe.txt", "r", encoding="utf-8") as xox:
            for i in xox:
                print(i,end="")
        break

    elif oyuncu2():
        print(kullanıcı)
        print(bilgisayar)
        print(" *** Kaybettin! *** ")
        with open("tictactoe.txt", "r", encoding="utf-8") as xox:
            for i in xox:
                print(i,end="")
        break
    else:
        tic()