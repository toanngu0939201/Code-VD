def NhapDL(filename):
    try:
        with open(filename, encoding="UTF-8") as f:
            Tenhs = []
            Diemhs = []
            for line in f:
                L = line.strip().split()
                if len(L) == 2:
                    Tenhs.append(L[0])
                    Diemhs.append(float(L[1]))
                else:
                    print("Dòng không đúng định dạng:", line)
        return Tenhs, Diemhs
    except FileNotFoundError:
        print("Không tìm thấy tệp", filename)
        return [], []

def TimDiemTheoTen(Tenhs, Diemhs, ten):
    for i in range(len(Tenhs)):
        if Tenhs[i] == ten:
            return Diemhs[i]
    return None

filename = "data.inp"
Tenhs, Diemhs = NhapDL(filename)

if Tenhs and Diemhs:
    ten_can_tim = input("Nhập tên học sinh cần tra cứu điểm: ")
    diem = TimDiemTheoTen(Tenhs, Diemhs, ten_can_tim)
    if diem is not None:
        print(f"Điểm của học sinh {ten_can_tim}: {diem}")
    else:
        print(f"Không tìm thấy thông tin cho học sinh {ten_can_tim}")
