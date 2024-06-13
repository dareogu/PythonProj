import csv

#with open("test.csv","w") as csvfile:
   # writer =csv.writer(csvfile)

   # writer.writerow(["index","name","grade"])
   # writer.writerows([[0,5,6],[1,9,2],[2,5,6]])


stu1 = ['marry', 26]
stu2 = ['bob', 23]

out = open('CSVOperateTest.csv', 'a', newline='')

csv_write = csv.writer(out, dialect='excel')

csv_write.writerow(stu1)
csv_write.writerow(stu2)
print("write over")
