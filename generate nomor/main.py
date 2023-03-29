import random
import phonenumbers
from phonenumbers import carrier,geocoder, timezone

# Meminta input dari user
provider = input("Masukkan provider: ")
daerah = input("Masukkan daerah: ")
jumlah_nomor = int(input("Masukkan jumlah nomor: "))

# Generate nomor berdasarkan provider dan daerah
for i in range(jumlah_nomor):
    mobileNo = phonenumbers.parse("+62" + provider + "-" + daerah + str(random.randint(1000000, 9999999)))
    print(mobileNo)

    # Timezone dari nomor mobile
    print(timezone.time_zones_for_number(mobileNo))

    # Carrier dari nomor mobile
    print(carrier.name_for_number(mobileNo, "en"))

    # Informasi daerah dari nomor mobile
    print(geocoder.description_for_number(mobileNo, "en"))

    # Penyedia layanan
    print("Penyedia Layanan: ", phonenumbers.is_possible_number(mobileNo))

    # Nomor yang valid
    print("Nomor yang valid: ", phonenumbers.is_valid_number(mobileNo))