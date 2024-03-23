def tinhGiaVe(height):
    ans = ""
    if 1 <= height and height <= 300:
        if height <= 130: 
            ans += "20000"
        elif height > 130: 
            ans += "30000"
    else:
        ans += "Error"
    return ans 
        
print("Nhap chieu cao: ")
a =int(input())
print("Gia ve: " + tinhGiaVe(a))