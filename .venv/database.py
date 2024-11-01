import pypyodbc as odbc
import csv

def getDatabase():
    connection_string1 = 'Server=.;Database=freelancer_platform_v2;Trusted_Connection=True;Encrypt=False;MultipleActiveResultSets=true;'

    DRIVER_NAME = 'SQl SERVER'
    SERVER_NAME = '.'
    DATABASE_NAME = 'freelancer_platform_v2'

    connection_string = f"""
        DRIVER={DRIVER_NAME};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    """

    try:
        conn = odbc.connect(connection_string)
        print("Kết nối thành công:", conn)
        cursor = conn.cursor()

        query = """
        SELECT TOP (1000) [JobId]
          ,[SkillId]
      FROM [freelancer_platform_v2].[dbo].[JobSkill]
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        with open("ky_nang_cong_viec.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Ghi tiêu đề cột
            writer.writerow(["ID Công việc", "ID Kỹ năng"])

            # Ghi từng dòng dữ liệu vào file CSV
            for row in rows:
                writer.writerow(row)

        cursor.close()
        conn.close()
    except Exception as e:
        print("Lỗi khi kết nối:", e)

getDatabase()