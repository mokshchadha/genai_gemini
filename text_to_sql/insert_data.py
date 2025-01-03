import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor
cursor = connection.cursor()

# Creating table
table_info = """
CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT, LOCATION VARCHAR(50), NOTICE_PERIOD INT);
"""
cursor.execute(table_info)

# Insert 50 records into the STUDENT table
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Olivia Martinez', '10', 'A', 80, 'New York', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Liam Robinson', '11', 'B', 75, 'Los Angeles', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Noah Clark', '12', 'A', 94, 'Chicago', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Emma Lewis', '11', 'A', 90, 'Houston', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Ava Walker', '10', 'B', 86, 'Phoenix', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Sophia Hall', '12', 'A', 95, 'Philadelphia', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Isabella Allen', '11', 'B', 82, 'San Antonio', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Mason Young', '10', 'A', 77, 'San Diego', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Ethan King', '11', 'A', 79, 'Dallas', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Logan Wright', '12', 'B', 88, 'San Jose', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Charlotte Scott', '10', 'B', 93, 'Austin', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Amelia Turner', '11', 'A', 89, 'Jacksonville', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Harper Adams', '12', 'B', 96, 'Fort Worth', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Evelyn Baker', '10', 'A', 81, 'Columbus', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Jack Carter', '11', 'B', 76, 'San Francisco', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Henry Foster', '12', 'A', 92, 'Charlotte', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Alexander Russell', '10', 'A', 84, 'Indianapolis', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Sebastian Gray', '11', 'B', 85, 'Seattle', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Daniel Price', '12', 'B', 87, 'Denver', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Lucas Bennett', '10', 'A', 78, 'Washington', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Mila Powell', '11', 'A', 91, 'Boston', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Scarlett Howard', '12', 'B', 90, 'El Paso', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Grace Myers', '10', 'A', 79, 'Detroit', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Zoe Bell', '11', 'B', 83, 'Nashville', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Chloe Ward', '12', 'A', 94, 'Portland', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Ella Hughes', '10', 'B', 85, 'Memphis', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Riley Rogers', '11', 'A', 82, 'Oklahoma City', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Victoria Reed', '12', 'B', 88, 'Las Vegas', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Lily Cook', '10', 'A', 86, 'Louisville', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Hannah Morgan', '11', 'B', 77, 'Baltimore', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Aria Cooper', '12', 'A', 92, 'Milwaukee', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Elijah Richardson', '10', 'B', 81, 'Albuquerque', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Layla Wood', '11', 'A', 89, 'Tucson', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('William Nelson', '12', 'B', 93, 'Fresno', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Zoe Mitchell', '10', 'A', 80, 'Sacramento', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('James Anderson', '11', 'B', 78, 'Long Beach', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Penelope Taylor', '12', 'A', 95, 'Kansas City', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Benjamin Thomas', '10', 'B', 84, 'Mesa', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Nora Jackson', '11', 'A', 87, 'Atlanta', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Christopher White', '12', 'B', 91, 'Colorado Springs', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Luna Harris', '10', 'A', 83, 'Raleigh', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Mateo Martin', '11', 'B', 76, 'Omaha', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Stella Thompson', '12', 'A', 94, 'Miami', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Jack Lee', '10', 'B', 82, 'Oakland', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Hazel Garcia', '11', 'A', 88, 'Minneapolis', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Leo Rodriguez', '12', 'B', 90, 'Tulsa', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Aurora Wilson', '10', 'A', 79, 'Cleveland', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Ellie Moore', '11', 'B', 85, 'Wichita', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Ezra Davis', '12', 'A', 96, 'Arlington', 30)")

cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Avery Johnson', '10', 'B', 88, 'New York', 15)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Scarlett Brown', '11', 'A', 92, 'Los Angeles', 20)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Wyatt Miller', '12', 'B', 79, 'Chicago', 25)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Sofia Davis', '10', 'A', 85, 'Houston', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Levi Wilson', '11', 'B', 91, 'Phoenix', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Mia Taylor', '12', 'A', 87, 'Philadelphia', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Asher Anderson', '10', 'B', 83, 'San Antonio', 15)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Evelyn Thomas', '11', 'A', 95, 'San Diego', 20)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Jackson Moore', '12', 'B', 80, 'Dallas', 25)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Aria Jackson', '10', 'A', 89, 'San Jose', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Carter White', '11', 'B', 93, 'Austin', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Aubrey Harris', '12', 'A', 86, 'Jacksonville', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Leo Martin', '10', 'B', 81, 'Fort Worth', 15)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Bella Thompson', '11', 'A', 94, 'Columbus', 20)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Grayson Lee', '12', 'B', 78, 'San Francisco', 25)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Nora Clark', '10', 'A', 90, 'Charlotte', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Ezra Rodriguez', '11', 'B', 84, 'Indianapolis', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Paisley Lewis', '12', 'A', 97, 'Seattle', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Maverick Hall', '10', 'B', 82, 'Denver', 15)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Elena Young', '11', 'A', 88, 'Washington', 20)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Miles King', '12', 'B', 91, 'Boston', 25)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Eliana Wright', '10', 'A', 85, 'El Paso', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Kai Scott', '11', 'B', 79, 'Detroit', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Nova Green', '12', 'A', 93, 'Nashville', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Zion Baker', '10', 'B', 87, 'Portland', 15)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Emery Foster', '11', 'A', 96, 'Oklahoma City', 20)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Lydia Cooper', '12', 'B', 81, 'Las Vegas', 25)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Declan Reed', '10', 'A', 89, 'Louisville', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Aaliyah Morgan', '11', 'B', 92, 'Milwaukee', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Bryson Powell', '12', 'A', 84, 'Albuquerque', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Athena Wood', '10', 'B', 78, 'Tucson', 15)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Axel Nelson', '11', 'A', 95, 'Fresno', 20)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Ivy Mitchell', '12', 'B', 86, 'Sacramento', 25)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Ryder Anderson', '10', 'A', 90, 'Long Beach', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Jade Taylor', '11', 'B', 83, 'Kansas City', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Rowan Thomas', '12', 'A', 97, 'Mesa', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Willow Jackson', '10', 'B', 80, 'Atlanta', 15)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Emmett White', '11', 'A', 94, 'Colorado Springs', 20)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Nova Harris', '12', 'B', 88, 'Raleigh', 25)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Silas Martin', '10', 'A', 82, 'Omaha', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Autumn Thompson', '11', 'B', 91, 'Miami', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Weston Lee', '12', 'A', 85, 'Oakland', 60)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Isla Garcia', '10', 'B', 79, 'Minneapolis', 15)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Everett Rodriguez', '11', 'A', 93, 'Tulsa', 20)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Emilia Wilson', '12', 'B', 87, 'Cleveland', 25)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Sawyer Moore', '10', 'A', 96, 'Wichita', 30)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Lila Davis', '11', 'B', 81, 'Arlington', 45)")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, LOCATION, NOTICE_PERIOD) VALUES ('Felix Johnson', '12', 'A', 89, 'New York', 60)")

# Display the records
print("The inserted records are:")
data = cursor.execute("SELECT * from STUDENT")

for row in data:
    print(row)

connection.commit()
connection.close()