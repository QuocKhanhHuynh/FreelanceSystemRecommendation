import pypyodbc as odbc
import csv

def getDatabase():
    connection_string1 = 'Server=.;Database=freelancer_platform_v2;Trusted_Connection=True;Encrypt=False;MultipleActiveResultSets=true;'
    '''
    DRIVER_NAME = 'SQl SERVER'
    SERVER_NAME = '.'
    DATABASE_NAME = 'freelancer_platform_v2'

    connection_string = f"""
        DRIVER={DRIVER_NAME};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    """
    '''
    DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
    SERVER_NAME = 'localhost'
    DATABASE_NAME = 'freelancer_platform_v2'

    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trusted_Connection=yes;
    """
    try:
        conn = odbc.connect(connection_string)
        print("Kết nối thành công:", conn)

        queryJobs(conn)
        querySkills(conn)
        queryCategories(conn)
        querySkillJobs(conn)

        conn.close()
    except Exception as e:
        print("Lỗi khi kết nối:", e)

def querySkillJobs(conn):
    cursor = conn.cursor()
    query = """
            SELECT TOP (1000) [JobId]
              ,[SkillId]
          FROM [freelancer_platform_v2].[dbo].[JobSkill]
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    with open("Data/ky_nang_cong_viec.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Ghi tiêu đề cột
        writer.writerow(["ID Công việc", "ID Kỹ năng"])

        # Ghi từng dòng dữ liệu vào file CSV
        for row in rows:
            writer.writerow(row)

    cursor.close()

def queryJobs(conn):
    cursor = conn.cursor()
    query = """
            SELECT TOP (1000) [ma_cong_viec]
      ,[ten_viec]
      ,[mo_ta]
      ,[CategoryId]
      ,[loai_cong_viec]
      ,[loai_luong]
      ,[yeu_cau]
  FROM [freelancer_platform_v2].[dbo].[cong_viec]
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    with open("Data/cong_viec.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Ghi tiêu đề cột
        writer.writerow(["ID","Tên công việc", "Mô tả", "ID lĩnh vực", "Loại công việc", "Loại lương", "Yêu cầu"])

        # Ghi từng dòng dữ liệu vào file CSV
        for row in rows:
            writer.writerow(row)

    cursor.close()

def queryCategories(conn):
    cursor = conn.cursor()
    query = """
            SELECT TOP (1000) [linh_vuc_hoat_dong]
      ,[ten_linh_vuc]
  FROM [freelancer_platform_v2].[dbo].[linh_vuc_hoat_dong]
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    with open("Data/linh_vuc_hoat_dong.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Ghi tiêu đề cột
        writer.writerow(["ID","Tên lĩnh vực"])

        # Ghi từng dòng dữ liệu vào file CSV
        for row in rows:
            writer.writerow(row)

    cursor.close()

def querySkills(conn):
    cursor = conn.cursor()
    query = """
            SELECT TOP (1000) [ma_ky_nang]
      ,[ten_ky_nang]
  FROM [freelancer_platform_v2].[dbo].[ky_nang]
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    with open("Data/ky_nang.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Ghi tiêu đề cột
        writer.writerow(["ID","Tên kỹ năng"])

        # Ghi từng dòng dữ liệu vào file CSV
        for row in rows:
            writer.writerow(row)
    cursor.close()
getDatabase()