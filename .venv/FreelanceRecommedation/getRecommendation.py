import pandas as pd


def find_nearest_freelancer(freelancer_id):
    # Đọc ma trận khoảng cách kỹ năng từ tệp CSV
    hamming_distance_df = pd.read_csv('ProcessData/freelancer_hamming_distance_matrix.csv', index_col=0)

    # Kiểm tra nếu ID freelancer có trong ma trận hay không
    if freelancer_id not in hamming_distance_df.index:
        print(f"ID freelancer {freelancer_id} không tồn tại trong ma trận.")
        return None

    # Lấy hàng của freelancer được yêu cầu
    freelancer_distances = hamming_distance_df.loc[freelancer_id]

    # Bỏ qua khoảng cách với chính freelancer đó (bằng 0) bằng cách loại freelancer_id khỏi tìm kiếm
    freelancer_distances = freelancer_distances[freelancer_distances.index != str(freelancer_id)]

    # Tìm 5 ID freelancer có khoảng cách nhỏ nhất
    nearest_freelancers = freelancer_distances.nsmallest(5)

    # In ra thông tin về 5 freelancer gần nhất
    for id, distance in nearest_freelancers.items():
        print(f"Freelancer gần nhất với ID {freelancer_id} là freelancer có ID {id} với khoảng cách Hamming {distance:.4f}.")

    return nearest_freelancers.index.tolist()  # Trả về danh sách các ID freelancer gần nhất


# Ví dụ sử dụng hàm
nearest_freelancers = find_nearest_freelancer(4)
