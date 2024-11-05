import pandas as pd
import numpy as np
from scipy.spatial.distance import hamming


def calculate_hamming_distance_matrix():
    # Đọc ma trận kỹ năng của freelancer từ tệp CSV
    skill_matrix = pd.read_csv('ProcessData/freelancer_skill_matrix.csv', index_col=0)

    # Lấy danh sách ID Freelancer
    freelancer_ids = skill_matrix.index.tolist()

    # Chuyển đổi ma trận kỹ năng thành các vector kỹ năng (bỏ qua ID Freelancer)
    skill_vectors = skill_matrix.values

    # Khởi tạo ma trận kết quả khoảng cách Hamming
    hamming_distance_matrix = np.zeros((len(skill_vectors), len(skill_vectors)))

    # Tính khoảng cách Hamming giữa các vector kỹ năng của từng cặp freelancer
    for i in range(len(skill_vectors)):
        for j in range(len(skill_vectors)):
            # Tính khoảng cách Hamming giữa vector i và j
            hamming_distance = hamming(skill_vectors[i], skill_vectors[j])
            # Lưu kết quả vào ma trận
            hamming_distance_matrix[i, j] = hamming_distance

    # Chuyển ma trận khoảng cách thành DataFrame để dễ đọc và ghi ra CSV
    hamming_distance_df = pd.DataFrame(hamming_distance_matrix, index=freelancer_ids, columns=freelancer_ids)

    # Đường dẫn lưu ma trận khoảng cách Hamming
    output_path = 'ProcessData/freelancer_hamming_distance_matrix.csv'

    # Xuất ma trận khoảng cách ra tệp CSV mới
    hamming_distance_df.to_csv(output_path)

    print(
        "Ma trận khoảng cách Hamming của freelancer đã được tạo và lưu vào freelancer_hamming_distance_matrix.csv trong thư mục 'ProcessData'.")


# Gọi hàm để thực hiện quá trình tính toán
calculate_hamming_distance_matrix()
