print("===masukkan koordinat====")
x = int(input("masukkan nilai x: "))
y = int(input("masukkan nilai y: "))
info = f"koordinat {x},{y} berada pada kuadran: "
if x > 0 and y > 0:
    print(info + "I")
elif x < 0 and y > 0:
    print(info + "II")
elif x < 0 and y < 0:
    print(info + "III")
elif x > 0 and y < 0:
    print(info + "IV")
else:
    pass
print()
