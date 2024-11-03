
'''
import pandas as pd
from pyvi import ViTokenizer
import string
import numpy as np

from  sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Danh sách stop words tiếng Việt
stop_words = set([
    "bị", "bởi", "cả", "các", "cái", "cần", "càng", "chỉ", "chiếc", "cho", "chứ",
    "chưa", "chuyện", "có", "có_thể", "cứ", "của", "cùng", "cũng", "đã", "đang",
    "đây", "để", "đến_nỗi", "đều", "điều", "do", "đó", "được", "dưới", "gì",
    "khi", "không", "là", "lại", "lên", "lúc", "mà", "mỗi", "một_cách", "này",
    "nên", "nếu", "ngay", "nhiều", "như", "nhưng", "những", "nơi", "nữa", "phải",
    "qua", "ra", "rằng", "rất", "rồi", "sau", "sẽ", "so", "sự", "tại", "theo",
    "thì", "trên", "trước", "từ", "từng", "và", "vẫn", "vào", "vậy", "vì", "việc",
    "với", "vừa"
])


# Hàm để loại bỏ dấu câu, ký hiệu xuống dòng và chuyển thành chữ thường
def clean_text(text):
    if isinstance(text, str):
        # Loại bỏ ký hiệu xuống dòng
        text = text.replace("\n", " ")
        text = text.replace("•", "")
        # Loại bỏ dấu câu và chuyển thành chữ thường
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator).lower()
    return text


# Hàm để loại bỏ số, từ chứa số và các cụm từ có ký tự đặc biệt
def remove_numbers_and_special_chars(text):
    if isinstance(text, str):
        words = text.split()
        cleaned_words = []

        for word in words:
            # Kiểm tra nếu từ không chứa số
            if not any(char.isdigit() for char in word):
                # Kiểm tra nếu từ không chứa ký tự đặc biệt
                if all(char.isalnum() or char.isspace() for char in word):
                    cleaned_words.append(word)

        return ' '.join(cleaned_words)
    return text


# Hàm để loại bỏ stop words
def remove_stop_words(text):
    if isinstance(text, str):
        # Tách từ và loại bỏ stop words
        words = text.split()
        return ' '.join([word for word in words if word not in stop_words])
    return text

def processData():
    # Đọc dữ liệu từ tệp CSV
    sampleData = pd.read_csv('ProcessData/SampleData.csv')

    # Chuẩn hóa dữ liệu
    columns_to_clean = ["Tên công việc", "Mô tả", "Yêu cầu", "Danh sách kỹ năng", "Lĩnh vực"]
    for column in columns_to_clean:
        sampleData[column] = sampleData[column].apply(clean_text)  # Chuẩn hóa dữ liệu
        sampleData[column] = sampleData[column].apply(remove_numbers_and_special_chars)  # Loại bỏ số và ký tự đặc biệt
        sampleData[column] = sampleData[column].apply(remove_stop_words)  # Loại bỏ stop words

    # Hàm để tách từ tiếng Việt
    def tokenize_text(text):
        if isinstance(text, str):
            return ViTokenizer.tokenize(text)
        return text

    # Áp dụng hàm tách từ cho từng cột đã chuẩn hóa
    for column in columns_to_clean:
        sampleData[column] = sampleData[column].apply(tokenize_text)

    # Kiểm tra kết quả
    # print(sampleData["Yêu cầu"])
    # Tạo cột TAG bằng cách nối dữ liệu từ các cột đã chuẩn hóa
    # Đảm bảo tất cả các giá trị đều là chuỗi
    sampleData['TAG'] = sampleData[columns_to_clean].fillna('').astype(str).agg(' '.join, axis=1)
   # print( sampleData['TAG'])

    # Tạo bảng dữ liệu mới chỉ với các cột ID và TAG
    new_data = sampleData[['ID', 'TAG']].copy()

    # Kiểm tra kết quả
    # print(new_data.iloc[10]['TAG'])
    tf = TfidfVectorizer(min_df=0.4, max_df=0.7 ) # min_df=0.2, max_df=0.8 50 max_features=len(sampleData) min_df=0.1, max_df=0.8, max_features=len(sampleData)
    vector = tf.fit_transform(new_data['TAG'])
    similary = cosine_similarity(vector)

    np.save('ProcessData/similary.npy', similary)
    print(similary)

processData()

'''
'''
import pandas as pd
from pyvi import ViTokenizer
import string
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Danh sách stop words tiếng Việt
stop_words = set([
    "bị", "bởi", "cả", "các", "cái", "cần", "càng", "chỉ", "chiếc", "cho", "chứ",
    "chưa", "chuyện", "có", "có_thể", "cứ", "của", "cùng", "cũng", "đã", "đang",
    "đây", "để", "đến_nỗi", "đều", "điều", "do", "đó", "được", "dưới", "gì",
    "khi", "không", "là", "lại", "lên", "lúc", "mà", "mỗi", "một_cách", "này",
    "nên", "nếu", "ngay", "nhiều", "như", "nhưng", "những", "nơi", "nữa", "phải",
    "qua", "ra", "rằng", "rất", "rồi", "sau", "sẽ", "so", "sự", "tại", "theo",
    "thì", "trên", "trước", "từ", "từng", "và", "vẫn", "vào", "vậy", "vì", "việc",
    "với", "vừa"
])

# Hàm để loại bỏ dấu câu, ký hiệu xuống dòng và chuyển thành chữ thường
def clean_text(text):
    if isinstance(text, str):
        text = text.replace("\n", " ")
        text = text.replace("•", "")
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator).lower()
    return text

# Hàm để loại bỏ số, từ chứa số và các cụm từ có ký tự đặc biệt
def remove_numbers_and_special_chars(text):
    if isinstance(text, str):
        words = text.split()
        cleaned_words = []

        for word in words:
            if not any(char.isdigit() for char in word):
                if all(char.isalnum() or char.isspace() for char in word):
                    cleaned_words.append(word)

        return ' '.join(cleaned_words)
    return text

# Hàm để loại bỏ stop words
def remove_stop_words(text):
    if isinstance(text, str):
        words = text.split()
        return ' '.join([word for word in words if word not in stop_words])
    return text

def processData():
    # Đọc dữ liệu từ tệp CSV
    sampleData = pd.read_csv('ProcessData/SampleData.csv')

    # Chuẩn hóa dữ liệu
    columns_to_clean = ["Tên công việc", "Mô tả", "Lĩnh vực"]  # Bỏ "Yêu cầu" và "Danh sách kỹ năng"
    for column in columns_to_clean:
        sampleData[column] = sampleData[column].apply(clean_text)
        sampleData[column] = sampleData[column].apply(remove_numbers_and_special_chars)
        sampleData[column] = sampleData[column].apply(remove_stop_words)

    # Hàm để tách từ tiếng Việt
    def tokenize_text(text):
        if isinstance(text, str):
            return ViTokenizer.tokenize(text)
        return text

    # Áp dụng hàm tách từ cho từng cột đã chuẩn hóa
    for column in columns_to_clean:
        sampleData[column] = sampleData[column].apply(tokenize_text)

    # Tạo cột TAG bằng cách nối dữ liệu từ các cột đã chuẩn hóa
    sampleData['TAG'] = sampleData[columns_to_clean].fillna('').astype(str).agg(' '.join, axis=1)

    # Tạo bảng dữ liệu mới chỉ với các cột ID và TAG
    new_data = sampleData[['ID', 'TAG']].copy()

    tf = TfidfVectorizer(min_df=0.2, max_df=0.8)
    vector = tf.fit_transform(new_data['TAG'])
    similary = cosine_similarity(vector)

    np.save('ProcessData/similary.npy', similary)
    print(similary)

processData()
'''


import pandas as pd
from pyvi import ViTokenizer
import string
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Danh sách stop words tiếng Việt
stop_words = set([
    "bị", "bởi", "cả", "các", "cái", "cần", "càng", "chỉ", "chiếc", "cho", "chứ",
    "chưa", "chuyện", "có", "có_thể", "cứ", "của", "cùng", "cũng", "đã", "đang",
    "đây", "để", "đến_nỗi", "đều", "điều", "do", "đó", "được", "dưới", "gì",
    "khi", "không", "là", "lại", "lên", "lúc", "mà", "mỗi", "một_cách", "này",
    "nên", "nếu", "ngay", "nhiều", "như", "nhưng", "những", "nơi", "nữa", "phải",
    "qua", "ra", "rằng", "rất", "rồi", "sau", "sẽ", "so", "sự", "tại", "theo",
    "thì", "trên", "trước", "từ", "từng", "và", "vẫn", "vào", "vậy", "vì", "việc",
    "với", "vừa"
])

# Hàm để loại bỏ dấu câu, ký hiệu xuống dòng và chuyển thành chữ thường
def clean_text(text):
    if isinstance(text, str):
        text = text.replace("\n", " ")
        text = text.replace("•", "")
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator).lower()
    return text

# Hàm để loại bỏ số, từ chứa số và các cụm từ có ký tự đặc biệt
def remove_numbers_and_special_chars(text):
    if isinstance(text, str):
        words = text.split()
        cleaned_words = []

        for word in words:
            if not any(char.isdigit() for char in word):
                if all(char.isalnum() or char.isspace() for char in word):
                    cleaned_words.append(word)

        return ' '.join(cleaned_words)
    return text

# Hàm để loại bỏ stop words
def remove_stop_words(text):
    if isinstance(text, str):
        words = text.split()
        return ' '.join([word for word in words if word not in stop_words])
    return text

def processData():
    # Đọc dữ liệu từ tệp CSV
    sampleData = pd.read_csv('ProcessData/SampleData.csv')

    # Chuẩn hóa dữ liệu
    columns_to_clean = ["Tên công việc", "Mô tả"]  # Bỏ "Lĩnh vực"
    for column in columns_to_clean:
        sampleData[column] = sampleData[column].apply(clean_text)
        sampleData[column] = sampleData[column].apply(remove_numbers_and_special_chars)
        sampleData[column] = sampleData[column].apply(remove_stop_words)

    # Hàm để tách từ tiếng Việt
    def tokenize_text(text):
        if isinstance(text, str):
            return ViTokenizer.tokenize(text)
        return text

    # Áp dụng hàm tách từ cho từng cột đã chuẩn hóa
    for column in columns_to_clean:
        sampleData[column] = sampleData[column].apply(tokenize_text)

    # Tạo cột TAG bằng cách nối dữ liệu từ các cột đã chuẩn hóa
    sampleData['TAG'] = sampleData[columns_to_clean].fillna('').astype(str).agg(' '.join, axis=1)

    # Tạo bảng dữ liệu mới chỉ với các cột ID và TAG
    new_data = sampleData[['ID', 'TAG']].copy()

    tf = TfidfVectorizer()
    vector = tf.fit_transform(new_data['TAG'])
    similary = cosine_similarity(vector)

    np.save('ProcessData/similary.npy', similary)
    print(similary)

processData()
