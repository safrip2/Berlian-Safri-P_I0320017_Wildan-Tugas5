print("\t\tSelamat Datang")
print("masukkan nilai untuk ditambahkan.")
print("masukkan 0 untuk berhenti")
nama = input("masukkan nama anda: ")
a = 1
s = 0
count = 0
while a != 0:
    print("total nilai saat ini adalah", s)
    a = float(input("nilai: "))
    s = s + a
    count = count + 1
print("nilai total adalah =", s)
print(f"nilai rata-rata adalah {s / (count -1)}")
rata2 = s / (count -1)
if rata2 >= 85:
    print(f"Halo {nama}! Grade anda adalah A")
elif rata2 >= 80 and rata2 <= 84:
    print(f"Halo {nama}! Grade anda adalah A-")
elif rata2 >= 75 and rata2 <= 79:
    print(f"Halo {nama}! Grade anda adalah B+")
elif rata2 >= 70 and rata2 <= 74:
    print(f"Halo {nama}! Grade anda adalah B")
elif rata2 >= 65 and rata2 <= 69:
    print(f"Halo {nama}! Grade anda adalah C+")
elif rata2 >= 60 and rata2 <= 64:
    print(f"Halo {nama}! Grade anda adalah C")
else:
    print(f"Halo {nama}! Grade anda adalah E")
