import numpy as np
import pandas as pd


def getRecommend(inputTitle):
    similary = np.load('Processdata/similary.npy')
    sampleData = pd.read_csv('ProcessData/SampleData.csv')

    # Tìm chỉ số của hàng dựa trên ID công việc
    row_index = sampleData.index[sampleData['ID'] == int(inputTitle)]

    # Kiểm tra xem có tìm thấy hàng không
    if not row_index.empty:
        # Lấy hàng tương ứng từ ma trận similarity
        row_similarities = similary[row_index[0]]

        # Đặt giá trị tại row_index thành -inf để bỏ qua công việc hiện tại
        row_similarities[row_index[0]] = -np.inf

        # Lấy chỉ số của các giá trị có độ tương đồng từ 0.7 trở lên
        top_indices = np.where(row_similarities >= 0.1)[0]

        # Sắp xếp các chỉ số này theo giá trị từ cao đến thấp
        top_indices = top_indices[np.argsort(row_similarities[top_indices])[::-1]]

        # Giới hạn chỉ lấy 10 phần tử nếu có nhiều hơn 10 phần tử
        top_indices = top_indices[:10]

        # In kết quả
        recommendations = []
        for idx in top_indices:
            job_name = sampleData.iloc[idx]['Tên công việc']
            job_id = sampleData.iloc[idx]['ID']
            print(job_name)
            recommendations.append(job_id)

        return recommendations
    else:
        print(f"Không tìm thấy công việc với ID {inputTitle}.")
        return []


def getRecommend2(inputTitle):
    similary = np.load('Processdata/similary.npy')
    sampleData = pd.read_csv('ProcessData/SampleData.csv')
    # Nhập tên công việc để tìm
    #inputTitle = input("Nhập ID công việc tìm: ")
    row_index = sampleData.index[sampleData['ID'] == int(inputTitle)]

    # Kiểm tra xem có tìm thấy hàng không
    if not row_index.empty:
        # Lấy hàng tương ứng từ ma trận similarity
        row_similarities = similary[row_index[0]]
        # Đặt giá trị tại row_index thành giá trị rất nhỏ để bỏ qua
        row_similarities[row_index[0]] = -np.inf

        # Lấy chỉ số của hai phần tử có giá trị cao nhất

        top_indices = np.argsort(row_similarities)[-2:][
                      ::-1]  # Lấy hai chỉ số lớn nhất, đảo ngược để có giá trị cao nhất đầu tiên

        # In kết quả
        recommend1 = sampleData.iloc[top_indices[0]]['Tên công việc']
        recommend2 = sampleData.iloc[top_indices[1]]['Tên công việc']
        print(recommend1)
        print(recommend2)

        return [sampleData.iloc[top_indices[0]]['ID'], sampleData.iloc[top_indices[1]]['ID']]
    else:
        print(f"Không tìm thấy công việc với ID {inputTitle}.")
        return []