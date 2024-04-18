def tinh_tong_uoc(n):
    tong = 1  
    for i in range(2, n):
        if n % i == 0:
            tong += i
    return tong
def dem_so_phong_phu(L, R):
    dem = 0
    for so in range(L, R + 1):
        if tinh_tong_uoc(so) > so:
            dem += 1
    return dem
ket_qua = dem_so_phong_phu(L, R)

with open("PHONGPHU.INP", "r") as f:
    L, R = map(int, f.readline().split())
with open("PHONGPHU.OUT", "w") as f:
    f.write(str(ket_qua))
