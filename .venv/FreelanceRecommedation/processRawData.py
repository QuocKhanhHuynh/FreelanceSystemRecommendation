import pandas as pd
import os

def processRawData():
    # Đọc dữ liệu từ các tệp CSV
    freelancer_ky_nang = pd.read_csv('Data/freelancer_ky_nang.csv')
    ky_nang = pd.read_csv('Data/ky_nang.csv')

    # Tạo bảng pivot với ID Freelancer là hàng, ID Kỹ năng là cột, và giá trị là 1 nếu có kỹ năng
    pivot_table = freelancer_ky_nang.pivot_table(index='ID Freelancer',
                                                 columns='ID Kỹ năng',
                                                 aggfunc='size',
                                                 fill_value=0)

    # Đảm bảo tất cả các kỹ năng từ bảng ky_nang có trong cột của pivot_table
    for skill_id in ky_nang['ID']:
        if skill_id not in pivot_table.columns:
            pivot_table[skill_id] = 0  # Thêm cột kỹ năng mới và gán giá trị 0 cho tất cả các freelancer

    # Sắp xếp lại các cột theo thứ tự kỹ năng ID
    pivot_table = pivot_table.reindex(sorted(pivot_table.columns), axis=1)

    # Đổi tên các cột từ ID Kỹ năng sang Tên kỹ năng
    pivot_table.columns = [ky_nang.loc[ky_nang['ID'] == col, 'Tên kỹ năng'].values[0]
                           for col in pivot_table.columns]

    # Kiểm tra và tạo thư mục 'ProcessData' nếu chưa tồn tại
    output_dir = 'ProcessData'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Đường dẫn lưu tệp CSV
    output_path = os.path.join(output_dir, 'freelancer_skill_matrix.csv')

    # Xuất bảng pivot ra tệp CSV mới
    pivot_table.to_csv(output_path)

    print("Bảng kỹ năng của freelancer đã được tạo và lưu vào freelancer_skill_matrix.csv trong thư mục 'ProcessData'.")

# Gọi hàm để thực hiện quá trình xử lý
processRawData()
