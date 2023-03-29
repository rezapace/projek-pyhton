import phonenumbers
from phonenumbers import carrier,geocoder, timezone

# Memasukkan nomor telepon dalam format internasional
mobileNo = input("Masukkan nomor mobile dengan kode negara: ")
mobileNo = phonenumbers.parse(mobileNo)

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