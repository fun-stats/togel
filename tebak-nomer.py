'''
Analisis Probabilistik Hasil Togel Hongkong Pool Berdasarkan Simulasi Monte Carlo
https://hongkongpools.com/
'''

import random
import csv
from collections import Counter

# Jumlah iterasi simulasi Monte Carlo
jumlah_iterasi = 100
jumlah_angka_per_iterasi = 100_000
top_n = 20

# Data historis 10 hari terakhir (pastikan dalam bentuk string 4 digit)
data_asli = ["1943", "3627", "0076", "4121", "2738", "3889", "5966", "1297", "9246", "7689", # <= 4 digit awal
            "4308", "2766", "7680", "2196", "3832", "8941", "6627", "9761", "4645", "8961"] # <= 4 digit akhir

# Variabel untuk menyimpan jumlah kemenangan
jumlah_win = 0

# Siapkan file CSV untuk menyimpan hasil top_angka
with open('top_angka.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Iterasi', 'Top Angka'])  # Menulis header

    # Jalankan simulasi sebanyak jumlah_iterasi
    for iterasi in range(jumlah_iterasi):
        # Simulasikan 100.000 angka acak
        hasil_simulasi = [str(random.randint(0, 9999)).zfill(4) for _ in range(jumlah_angka_per_iterasi)]
        frekuensi = Counter(hasil_simulasi)
        top_angka = [angka for angka, _ in frekuensi.most_common(top_n)]
        
        # Simpan hasil top_angka ke file CSV
        writer.writerow([iterasi + 1, ', '.join(top_angka)])

        # Cek apakah ada angka yang cocok dengan data historis dalam top 20
        cocokan_historis = [(angka, jumlah) for angka, jumlah in zip(top_angka, [frekuensi[angka] for angka in top_angka]) if angka in data_asli]
        
        # Jika ada angka yang cocok, hitung sebagai kemenangan
        if cocokan_historis:
            print(f"Iterasi {iterasi + 1} - Cocokan Historis: {cocokan_historis}")
            jumlah_win += 1

# Hitung winrate
winrate = (jumlah_win / jumlah_iterasi) * 100

# Tampilkan hasil
print(f"Jumlah iterasi dengan angka yang cocok: {jumlah_win} dari {jumlah_iterasi} iterasi.")
print(f"Winrate: {winrate}%")
