import random

# Meminta input nomor sample dari user
sample_number = input('Masukkan nomor sample: ')

# Meminta jumlah nomor yang ingin dihasilkan dari user
total_number = int(input('Berapa nomor: '))

# Generate nomor acak berdasarkan sample number dan total number
for i in range(total_number):
  print(str(int(sample_number) + i))

