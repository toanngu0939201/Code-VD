filename = "data.inp"
def NhapDL(filename):
    Tenhs = []
    Diemhs = []
    try:
        with open(filename, encoding="UTF-8") as f:
            for line in f:
                L = line.strip().split()
                if len(L) == 2:
                    Tenhs.append(L[0])
                    Diemhs.append(float(L[1]))
                else:
                    print("Dòng không đúng định dạng:", line)
    except FileNotFoundError:
        print("Không tìm thấy tệp", filename)
    except Exception as e:
        print("Đã xảy ra lỗi:", e)
    return Tenhs, Diemhs

filename = "data.inp"
Tenhs, Diemhs = NhapDL(filename)
for i in range(len(Tenhs)):
    print(Tenhs[i], Diemhs[i])
