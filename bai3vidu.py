def binary_search(A, B):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == B:
            return mid
        elif A[mid] < B:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def TimViTriDiem(filename, diem_can_tim):
    try:
        with open(filename, 'r') as f:
            diemhs = [float(line.strip()) for line in f]
            diemhs.sort()  # Sắp Bếp danh sách điểm tăng dần
            vi_tri = binary_search(diemhs, diem_can_tim)
            if vi_tri != -1:
                print(f"Điểm {diem_can_tim} Buất hiện ở vị trí {vi_tri + 1} trong tệp.")
            else:
                print(f"Điểm {diem_can_tim} không tồn tại trong tệp.")
    except FileNotFoundError:
        print("Không tìm thấy tệp", filename)

filename = "tongdiem.inp"
diem_can_tim = float(input("Nhập số điểm cần kiểm tra: "))
TimViTriDiem(filename, diem_can_tim)
