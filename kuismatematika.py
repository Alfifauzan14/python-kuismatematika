import random
import time

def tampilkan_menu():
    print("="*30)
    print(" \tKuis Matematika!")
    print("="*30)
    print("1. Mulai Kuis")
    print("2. Keluar")
    print("="*30)

def soal_matematika():
    # List soal yang akan di-generate
    soal = [
        ("Berapa 5 + 3?", 8),
        ("Berapa 12 - 4?", 8),
        ("Berapa 6 x 7?", 42),
        ("Berapa 16 ÷ 4?", 4),
        ("Berapa 9 + 6?", 15),
        ("Berapa 15 - 7?", 8),
        ("Berapa 8 x 9?", 72),
        ("Berapa 24 ÷ 6?", 4)
    ]
    
    random.shuffle(soal)  # Mengacak urutan soal
    
    skor = 0
    kesempatan = 3  # Jumlah kesempatan untuk menjawab soal
    
    total_soal = len(soal)
    
    print("\nKuis Dimulai! Jawablah soal-soal berikut dengan benar.")
    time.sleep(1)  # Delay untuk memberikan efek dramatis

    # Menampilkan soal dan memeriksa jawaban
    for i, (pertanyaan, jawaban_benar) in enumerate(soal):
        if kesempatan == 0:
            print("\nAnda telah kehabisan kesempatan. Kuis selesai!")
            break
        
        print(f"\nSoal {i+1}: {pertanyaan}")
        print(f"Sisa Kesempatan: {kesempatan}")
        try:
            jawaban = int(input("Jawaban: "))
            
            if jawaban == jawaban_benar:
                print("Jawaban Anda Benar!\n")
                skor += 10  # Poin yang didapatkan jika jawaban benar
            else:
                print(f"Jawaban Anda Salah. Jawaban yang benar adalah {jawaban_benar}.\n")
                kesempatan -= 1  # Mengurangi kesempatan jika jawabannya salah
                
        except ValueError:
            print("Harap masukkan angka yang valid.\n")
            kesempatan -= 1  # Mengurangi kesempatan jika terjadi input tidak valid
    
    print(f"\nKuis selesai! Anda mendapatkan {skor} poin dengan {kesempatan} kesempatan tersisa.")

def main():
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1/2): "))
            
            if pilihan == 1:
                soal_matematika()
            elif pilihan == 2:
                print("\nTerima kasih telah bermain! Sampai jumpa lagi.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
        except ValueError:
            print("Harap masukkan angka yang valid.")

if __name__ == "__main__": main()