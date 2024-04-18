def tim_hoc_sinh_theo_diem(dsdiem, dsten, diem_min, diem_max):
    dshs = []
    for i in range(len(dsdiem)):  # Duyệt qua từng học sinh trong danh sách
        if diem_min <= dsdiem[i] <= diem_max:  # Kiểm tra nếu điểm của học sinh nằm trong khoảng đã nhập
            dshs.append(dsten[i])  # Thêm tên của học sinh vào danh sách
    return dshs

def hien_thi_dshs(dshs):
    if dshs:  # Nếu danh sách không rỗng
        print("Danh sách học sinh có điểm trong khoảng đã nhập:")
        for ten in dshs:  # Duyệt qua từng học sinh trong danh sách và hiển thị tên của họ
            print(ten)
    else:  # Nếu danh sách rỗng
        print("Không có học sinh nào có điểm trong khoảng đã nhập.")

dsdiem = [5.6, 7.4, 7.8, 8.4, 8.9, 9.5]
dsten = ["Sơn", "Huyền", "Nam", "Hùng", "Hương", "Hà"]

dsdiem_ds, dsten_ds = zip(*sorted(zip(dsdiem, dsten)))

diem_min = float(input("Nhập điểm thấp nhất trong khoảng: "))
diem_max = float(input("Nhập điểm cao nhất trong khoảng: "))
    
dshs = tim_hoc_sinh_theo_diem(dsdiem_ds, dsten_ds, diem_min, diem_max)
hien_thi_dshs(dshs)
