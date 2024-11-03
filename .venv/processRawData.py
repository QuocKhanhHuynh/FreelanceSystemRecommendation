
'''
import pandas as pd
import os
from bs4 import BeautifulSoup

def processRawData():
    # Đọc các file CSV
    categories = pd.read_csv("Data/linh_vuc_hoat_dong.csv")
    skills = pd.read_csv("Data/ky_nang.csv")
    jobs = pd.read_csv("Data/cong_viec.csv")
    jobSkill = pd.read_csv("Data/ky_nang_cong_viec.csv")

    # Bước 1: Kết hợp bảng jobSkill với bảng skills để lấy tên kỹ năng cho mỗi công việc
    jobSkill_with_skill_name = jobSkill.merge(skills, left_on="ID Kỹ năng", right_on="ID",
                                              suffixes=('_jobSkill', '_skill'))

    # Bước 2: Nhóm kỹ năng theo ID công việc và giữ lại dưới dạng danh sách
    job_skills = jobSkill_with_skill_name.groupby("ID Công việc")["Tên kỹ năng"].apply(list).reset_index()

    # Bước 3: Đổi tên cột để dễ gộp với bảng jobs
    job_skills.columns = ["ID", "Danh sách kỹ năng"]

    # Bước 4: Gộp danh sách kỹ năng vào bảng jobs
    jobs_with_skills = jobs.merge(job_skills, left_on="ID", right_on="ID", how="left")

    # Bước 5: Gộp với bảng categories để thay thế ID lĩnh vực bằng tên lĩnh vực
    jobs_with_categories = jobs_with_skills.merge(categories, left_on="ID lĩnh vực", right_on="ID",
                                                  suffixes=('', '_category'))

    # Bước 6: Loại bỏ thẻ HTML trong các trường "Mô tả" và "Yêu cầu"
    def remove_html_tags(text):
        if isinstance(text, str):  # Kiểm tra xem text có phải là chuỗi không
            return BeautifulSoup(text, "html.parser").get_text().strip()
        return text  # Trả về giá trị không thay đổi nếu không phải chuỗi

    jobs_with_categories['Mô tả'] = jobs_with_categories['Mô tả'].apply(remove_html_tags)
    jobs_with_categories['Yêu cầu'] = jobs_with_categories['Yêu cầu'].apply(remove_html_tags)

    # Bước 7: Chọn các cột cần thiết cho bảng mới
    new_jobs_table = jobs_with_categories[
        ["ID", "Tên công việc", "Mô tả", "Loại công việc", "Loại lương", "Yêu cầu", "Danh sách kỹ năng",
         "Tên lĩnh vực"]]

    # Đổi tên cột cho dễ hiểu
    new_jobs_table.columns = ["ID", "Tên công việc", "Mô tả", "Loại công việc", "Loại lương", "Yêu cầu",
                              "Danh sách kỹ năng", "Lĩnh vực"]
    print(new_jobs_table["Danh sách kỹ năng"])
    # Đảm bảo thư mục ProcessData tồn tại
    output_dir = "ProcessData"
    os.makedirs(output_dir, exist_ok=True)

    # Ghi tệp CSV, để lưu danh sách kỹ năng trong một cột dưới dạng danh sách
    new_jobs_table.to_csv(os.path.join(output_dir, "SampleData.csv"), index=False, encoding='utf-8')

    # Kết quả
    print("Bảng đã được ghi vào tệp SampleData.csv")
processRawData()
'''
'''
import pandas as pd
import os
from bs4 import BeautifulSoup

def processRawData():
    # Đọc các file CSV
    categories = pd.read_csv("Data/linh_vuc_hoat_dong.csv")
    skills = pd.read_csv("Data/ky_nang.csv")
    jobs = pd.read_csv("Data/cong_viec.csv")
    jobSkill = pd.read_csv("Data/ky_nang_cong_viec.csv")

    # Bước 1: Kết hợp bảng jobSkill với bảng skills để lấy tên kỹ năng cho mỗi công việc
    jobSkill_with_skill_name = jobSkill.merge(skills, left_on="ID Kỹ năng", right_on="ID",
                                              suffixes=('_jobSkill', '_skill'))

    # Bước 2: Nhóm kỹ năng theo ID công việc và giữ lại dưới dạng danh sách
    job_skills = jobSkill_with_skill_name.groupby("ID Công việc")["Tên kỹ năng"].apply(list).reset_index()

    # Bước 3: Đổi tên cột để dễ gộp với bảng jobs
    job_skills.columns = ["ID", "Danh sách kỹ năng"]

    # Bước 4: Gộp danh sách kỹ năng vào bảng jobs
    jobs_with_skills = jobs.merge(job_skills, left_on="ID", right_on="ID", how="left")

    # Bước 5: Gộp với bảng categories để thay thế ID lĩnh vực bằng tên lĩnh vực
    jobs_with_categories = jobs_with_skills.merge(categories, left_on="ID lĩnh vực", right_on="ID",
                                                  suffixes=('', '_category'))

    # Bước 6: Loại bỏ thẻ HTML trong các trường "Mô tả"
    def remove_html_tags(text):
        if isinstance(text, str):  # Kiểm tra xem text có phải là chuỗi không
            return BeautifulSoup(text, "html.parser").get_text().strip()
        return text  # Trả về giá trị không thay đổi nếu không phải chuỗi

    jobs_with_categories['Mô tả'] = jobs_with_categories['Mô tả'].apply(remove_html_tags)

    # Bước 7: Chọn các cột cần thiết cho bảng mới, bỏ "Yêu cầu" và "Danh sách kỹ năng"
    new_jobs_table = jobs_with_categories[["ID", "Tên công việc", "Mô tả", "Loại công việc", "Loại lương", "Tên lĩnh vực"]]

    # Đổi tên cột cho dễ hiểu
    new_jobs_table.columns = ["ID", "Tên công việc", "Mô tả", "Loại công việc", "Loại lương", "Lĩnh vực"]

    # Đảm bảo thư mục ProcessData tồn tại
    output_dir = "ProcessData"
    os.makedirs(output_dir, exist_ok=True)

    # Ghi tệp CSV
    new_jobs_table.to_csv(os.path.join(output_dir, "SampleData.csv"), index=False, encoding='utf-8')

    # Kết quả
    print("Bảng đã được ghi vào tệp SampleData.csv")

processRawData()
'''

import pandas as pd
import os
from bs4 import BeautifulSoup

def processRawData():
    # Đọc các file CSV
    categories = pd.read_csv("Data/linh_vuc_hoat_dong.csv")
    skills = pd.read_csv("Data/ky_nang.csv")
    jobs = pd.read_csv("Data/cong_viec.csv")
    jobSkill = pd.read_csv("Data/ky_nang_cong_viec.csv")

    # Bước 1: Kết hợp bảng jobSkill với bảng skills để lấy tên kỹ năng cho mỗi công việc
    jobSkill_with_skill_name = jobSkill.merge(skills, left_on="ID Kỹ năng", right_on="ID",
                                              suffixes=('_jobSkill', '_skill'))

    # Bước 2: Nhóm kỹ năng theo ID công việc và giữ lại dưới dạng danh sách
    job_skills = jobSkill_with_skill_name.groupby("ID Công việc")["Tên kỹ năng"].apply(list).reset_index()

    # Bước 3: Đổi tên cột để dễ gộp với bảng jobs
    job_skills.columns = ["ID", "Danh sách kỹ năng"]

    # Bước 4: Gộp danh sách kỹ năng vào bảng jobs
    jobs_with_skills = jobs.merge(job_skills, left_on="ID", right_on="ID", how="left")

    # Bước 5: Loại bỏ thẻ HTML trong các trường "Mô tả"
    def remove_html_tags(text):
        if isinstance(text, str):  # Kiểm tra xem text có phải là chuỗi không
            return BeautifulSoup(text, "html.parser").get_text().strip()
        return text  # Trả về giá trị không thay đổi nếu không phải chuỗi

    jobs_with_skills['Mô tả'] = jobs_with_skills['Mô tả'].apply(remove_html_tags)

    # Bước 6: Chọn các cột cần thiết cho bảng mới, bỏ "Yêu cầu", "Danh sách kỹ năng" và "Lĩnh vực"
    new_jobs_table = jobs_with_skills[["ID", "Tên công việc", "Mô tả", "Loại công việc", "Loại lương"]]

    # Đổi tên cột cho dễ hiểu
    new_jobs_table.columns = ["ID", "Tên công việc", "Mô tả", "Loại công việc", "Loại lương"]

    # Đảm bảo thư mục ProcessData tồn tại
    output_dir = "ProcessData"
    os.makedirs(output_dir, exist_ok=True)

    # Ghi tệp CSV
    new_jobs_table.to_csv(os.path.join(output_dir, "SampleData.csv"), index=False, encoding='utf-8')

    # Kết quả
    print("Bảng đã được ghi vào tệp SampleData.csv")

processRawData()
