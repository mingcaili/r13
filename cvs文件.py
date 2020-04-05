import csv
#1创建csv数据
'''
outputFile=open('output.csv','w',newline='')#当前目录下创建一个csv文件
outputWriter=csv.writer(outputFile)
outputWriter.writerow([i for i in range(0,5)])
outputWriter.writerow([i for i in range(6,11)])
outputWriter.writerow([i for i in range(12,17)])
outputFile.close()

'''

#2读取CSV文件
f=open('output.csv','r')
fr=csv.reader(f)
fdata=list(fr)
print(fdata.row)
