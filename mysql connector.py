import mysql.connector


conn = mysql.connector.connect(
    user="root",
    password="22011975",
    host="localhost",
    port=3306
)

print("connected")
cursor = conn.cursor()
cursor.execute("USE gietu")
cursor.execute("SELECT * FROM student ORDER BY salary DESC LIMIT 3")
#1
for row in cursor.fetchall():
    print(row)
#2
print("\n2. Not from CSE")
cursor.execute("SELECT * FROM student WHERE dept != 'CSE'")
for row in cursor.fetchall():
    print(row)
#3
print("\n3. Dept not CSE")
cursor.execute("SELECT * FROM student WHERE dept != 'CSE'")
for row in cursor.fetchall():
    print(row)
#4
print("\n4. Name aman or naman")
cursor.execute("SELECT * FROM student WHERE name IN ('aman','naman')")
for row in cursor.fetchall():
    print(row)
#5
print("\n5. Name contains two 'a'")
cursor.execute("SELECT * FROM student WHERE name LIKE '%a%a%'")
for row in cursor.fetchall():
    print(row)
#6
print("\n6. Name with 5 characters")
cursor.execute("SELECT * FROM student WHERE name LIKE '_____'")
for row in cursor.fetchall():
    print(row)
#7
print("\n7. Name starts with r")
cursor.execute("SELECT * FROM student WHERE name LIKE 'r%'")
for row in cursor.fetchall():
    print(row)
#8
print("\n8. Top 3 highest salary")
cursor.execute("SELECT * FROM student ORDER BY salary DESC LIMIT 3")
for row in cursor.fetchall():
    print(row)
#9
print("\n9. Lowest salary")
cursor.execute("SELECT * FROM student ORDER BY salary ASC LIMIT 1")
for row in cursor.fetchall():
    print(row)
#10
print("\n10. Total salary")
cursor.execute("SELECT SUM(salary) FROM student")
print(cursor.fetchone())
#11
print("\n11. Average salary")
cursor.execute("SELECT AVG(salary) FROM student")
print(cursor.fetchone())
#12
print("\n12. Count salary > 20000")
cursor.execute("SELECT COUNT(*) FROM student WHERE salary > 20000")
print(cursor.fetchone())
#13
print("\n13. Count per dept")
cursor.execute("SELECT dept, COUNT(*) FROM student GROUP BY dept")
for row in cursor.fetchall():
    print(row)
#14
print("\n14. Avg salary per dept")
cursor.execute("SELECT dept, AVG(salary) FROM student GROUP BY dept")
for row in cursor.fetchall():
    print(row)
#15
print("\n15. Total salary per dept")
cursor.execute("SELECT dept, SUM(salary) FROM student GROUP BY dept")
for row in cursor.fetchall():
    print(row)
#16
print("\n16. Dept avg salary > 20000")
cursor.execute("SELECT dept, AVG(salary) FROM student GROUP BY dept HAVING AVG(salary) > 20000")
for row in cursor.fetchall():
    print(row)
#17
print("\n17. Dept with more than 1 student")
cursor.execute("SELECT dept, COUNT(*) FROM student GROUP BY dept HAVING COUNT(*) > 1")
for row in cursor.fetchall():
    print(row)
#18
print("\n18. Salary > average salary")
cursor.execute("SELECT * FROM student WHERE salary > (SELECT AVG(salary) FROM student)")
for row in cursor.fetchall():
    print(row)
#19
print("\n19. Max salary")
cursor.execute("SELECT * FROM student WHERE salary=(SELECT MAX(salary) FROM student)")
for row in cursor.fetchall():
    print(row)
#20
print("\n20. Min salary")
cursor.execute("SELECT * FROM student WHERE salary=(SELECT MIN(salary) FROM student)")
for row in cursor.fetchall():
    print(row)

conn.close()    