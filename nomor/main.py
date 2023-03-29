import random

# daftar kode area untuk setiap provinsi/wilayah
area_codes = {
    "Jabodetabek": list(range(10, 15)),
    "Jawa Barat": list(range(15, 33)),
    "Jawa Tengah": list(range(33, 39)),
    "Jawa Timur": list(range(39, 44)),
    "Bali": list(range(44, 48)),
    "Kalimantan": list(range(48, 60)),
    "Sumatera Utara": list(range(60, 69)),
    "Sumatera Tengah": list(range(69, 75)),
    "Sumatera Selatan": list(range(75, 87)),
    "Sulawesi": list(range(87, 97)),
    "Papua dan Maluku": list(range(97, 100))
}

# daftar kode awal untuk setiap operator
operator_codes = {
    "Simpati": ["0813", "0821"],
    "AS": ["0852", "0853", "0851"],
    "Loop": ["0822"],
    "By.U": ["0851"],
    "Halo": ["0811", "0812"],
    "IM3": ["0857", "0856"],
    "XL Axiata": ["0817", "0818", "0819", "0859", "0877", "0878"],
    "AXIS": ["0813", "0832", "0833", "0838"],
    "Smartfren": ["0881", "0882", "0883", "0884", "0885", "0886", "0887", "0888", "0889"]
}

# fungsi untuk menghasilkan nomor telepon acak berdasarkan daerah dan operator tertentu
def generate_phone_number(area, operator):
    area_code = random.choice(area_codes[area])
    operator_code = random.choice(operator_codes[operator])
    last_four_digits = ''.join(random.choices('0123456789', k=4))
    return f"{operator_code}{area_code}{last_four_digits}"

# meminta input dari pengguna
num_of_numbers = int(input("Masukkan jumlah nomor telepon yang ingin dihasilkan: "))
area = input("Masukkan nama provinsi atau wilayah: ")
operator = input("Masukkan nama operator: ")

# menghasilkan nomor telepon acak sejumlah yang diminta pengguna
for i in range(num_of_numbers):
    print(generate_phone_number(area, operator))
