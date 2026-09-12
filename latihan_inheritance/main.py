from player import Kicker, Keeper

player = input("Masukkan nama penendang: ")
stat = int(input("Masukkkan nilai stat shootingnya: "))
player1 = Kicker(player, stat)
player = input("Masukkan nama kiper: ")
stat = int(input("Masukkkan nilai stat tangkapannya: "))
player2 = Keeper(player, stat)

totalTendangan = 0
while player1.stamina > 0 and player2.stamina > 0:
    print(f"\n=> tendangan ke-{totalTendangan + 1}")
    player1.menendang(player2)
    totalTendangan += 1
    pilihan = input("Apakah ingin lanjut menendang (y/t): ")

    if pilihan == "y":
        continue
    elif pilihan == "t":
        break

print(f"\n- sisa stamina \n\t{player1.name}: {player1.stamina}\n\t{player2.name}: {player2.stamina}")
print(f"|total tendangan: {totalTendangan}|jumlah gol: {Kicker.getJumlahGol()}|jumlah tepisan: {Keeper.getJumlahTepisan()}|")