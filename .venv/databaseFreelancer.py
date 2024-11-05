import pypyodbc as odbc
import csv

def getDatabaseFreelancer():
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

        querySkills(conn)
        queryFreelancerSkills(conn)

        conn.close()
    except Exception as e:
        print("Lỗi khi kết nối:", e)

def queryFreelancerSkills(conn):
    cursor = conn.cursor()
    query = """
            SELECT TOP (1000) [FreelancerId]
      ,[SkillId]
  FROM [freelancer_platform_v2].[dbo].[FreelancerSkill]
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)

    with open("Data/freelancer_ky_nang.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Ghi tiêu đề cột
        writer.writerow(["ID Freelancer", "ID Kỹ năng"])

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
    with open("Data/ky_nang_freelancer.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Ghi tiêu đề cột
        writer.writerow(["ID","Tên kỹ năng"])

        # Ghi từng dòng dữ liệu vào file CSV
        for row in rows:
            writer.writerow(row)

    cursor.close()

getDatabaseFreelancer()