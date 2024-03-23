def tinhGiaVe(height):
    if 1 <= height and height <= 300:
        if height <= 130: print ("Gia ve: 20000")
        elif height > 130: print("Gia ve: 30000")
    else:
        print("Error")
        
print("Nhap chieu cao: ")
a =int(input())
tinhGiaVe(a)