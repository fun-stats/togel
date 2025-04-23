'''
Analisis Probabilistik Hasil Togel Hongkong Pool Berdasarkan Simulasi Monte Carlo
https://hongkongpools.com/
'''

import random
import csv
from collections import Counter

# Jumlah iterasi simulasi Monte Carlo
jumlah_iterasi = 10
jumlah_angka_per_iterasi = 500_000
top_n = 20

# Data historis tahun 2025
data_asli = [
    "5760", "0279", "9006", "0141", "6393", "2704", "5386",
    "8962", "4578", "3045", "2953", "6474", "9781", "7268",
    "9773", "8336", "5046", "6293", "0682", "3900", "2763",
    "3572", "7344", "2576", "9097", "5282", "4689", "0893",
    "7610", "7402", "6964", "2301", "8565", "8648", "3056",
    "0174", "9220", "3858", "9081", "0676", "4705", "0541",
    "8224", "0194", "3116", "1042", "0491", "2879", "9665",
    "6901", "5216", "1695", "8506", "4492", "7583", "2300",
    "9064", "6848", "0919", "5171", "8785", "1422", "4360",
    "6584", "5958", "3074", "1808", "7796", "3573", "5180",
    "6364", "8496", "9619", "1765", "0305", "4802", "1537",
    "7188", "2067", "9378", "3424", "4964", "0540", "4056",
    "9793", "6255", "3723", "8437", "0516", "4931", "1834",
    "9182", "5223", "6818", "2591", "7532", "1065", "8482",
    "3976", "7020", "9150", "1744", "5807", "0373", "6213",
    "8961", "4645", "9761", "6627", "8941", "3832", "2196",
    "7680", "2766", "4308"
]

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
