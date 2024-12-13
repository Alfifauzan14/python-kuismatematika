nama = input("Masukkan Nama Kamu: ")
poin = 0
chance = 5

print("Halo " +nama, ", selamat datang di game Quis")
print("Jawablah soal yang muncul di layar, Jawaban yang benar akan mendapatkan poin")
input("(ENTER)")


while chance > 0:
    if poin < 75:
        print("Dapatkan poin tertinggi dan menangkan hadiah menarik")
        print("Kamu punya", chance, "kesempatan")
        input("(ENTER)")
        mulai = input("Kamu siap? (Ya/Tidak): ")

        if mulai == "Ya":
            poin -= poin
            chance -= 1
            print("Jawablah, soal nomor 1")
            print("1). Berapakah hasil dari 4 * 3 ?")
            ans1 = input("Jawaban : ")
            if ans1 == "12":
                poin += 25
                print("Selamat Kamu mendapat 25 poin, poin Kamu", poin)
                input("(ENTER)")
            else:
                print("Maaf jawaban Kamu salah, poin Kamu", poin)
                input("(ENTER)")
            
            print("Berikutnya, soal nomor 2")
            print("2). Berapa hasil 50/5 ?")
            ans2 = input("Jawaban: ")
            if ans2 == "10":
                poin += 25
                print("Selamat Kamu mendapat 25 poin, poin Kamu", poin)
                input("(ENTER)")
            else:
                print("Maaf jawaban Kamu salah, poin Kamu", poin)
                input("(ENTER)")

            print("Berikutnya, soal nomor 3")
            print("3). Berapa hasil 80 * 4 ?")
            ans3 = input("Jawaban: ")
            if ans3 == "400":
                poin += 25
                print("Selamat Kamu mendapat 25 poin, poin Kamu", poin)
                input("(ENTER)")
            else:
                print("Maaf jawaban Kamu salah, poin Kamu", poin)
                input("(ENTER)")

            print("Terakhir, soal nomor 4")
            print("4). Berapa hasil 21 * 4 ?")
            ans4 = input("Jawaban: ")
            if ans4 == "84":
                poin += 25
                print("Selamat Kamu mendapat 25 poin, poin Kamu", poin)
                input("(ENTER)")
            else:
                print("Maaf jawaban Kamu salah, poin Kamu", poin)
                input("(ENTER)")
        elif mulai == "Tidak":
            break
        else:
            print("silahkan jawab pertanyaan ini")
            input("(ENTER)")
    else:
        print("Selamat " +nama, "Kamu mendapatkan ", poin,"Poin")
        if poin >= 75:
            print("Selamat Kamu Menang")
            input("(ENTER)")
            break
        else: 
            print("Maaf Kamu Gagal")
            input("(ENTER)")
            break

print("Terimakasih :D!")