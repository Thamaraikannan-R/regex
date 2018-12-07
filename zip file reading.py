import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os.path, time
import re
import os
file_incoming_path="C:\\Users\\lotus\\Desktop\\new"
ls=list(os.listdir(file_incoming_path))
file_name=[]
source={'1','2','3','4','5','6'}
for i in ls:
    if re.search("[\w,\W].rar",i) or re.search("[\w,\W].zip",i):
        file_name.append(i)
li=[]
li1=['.zip','.rar']
not_present=[]
temp2=''
for i in file_name:
    for j in li1:
        temp=re.compile(j)
        li.append(temp.sub('',i))
for i in li:
    for j in source:
        if re.search(j,i):
            not_present.append(i)
not_present=set(not_present)
not_present=list(source.difference(not_present))
not_present.sort()
#print(not_present)
#print(file_name)
TimeArrived = list()
file_size_found = list()
File_type=list()
for i in file_name:
    s = ''
    s = file_incoming_path
    s = s.__add__('\\')
    s = s.__add__(i)  # i is file name to read size and time of creation
    TimeArrived.append(time.ctime(os.path.getmtime(s)))
    file_size_found.append(str(os.path.getsize(s)))
html = """\
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 10px;
    text-align: centre;
}
</style>
</head>
<body>
<center>
<h2><center>File Access Using List</center></h2>
<p>This program having:\n1. Read all files from Dir.\n2. Check wether recommended Files and\n3. Get File name, File size, File created time and Received or not.4. Show Green If received else show Red</p>
<table style="width:65%">
  <caption> File Date and Time </caption>
  <tr>
    <th>File Name</th>
    <th>File Type</th>
    <th>Date and Time</th>
    <th>Present or Not</th>
  </tr>

 """
source=list(source)
source.sort()
print(source)
#print(file_size_found)
#print(TimeArrived)
for (j, k, l) in zip(file_name, file_size_found, TimeArrived):
    html = html + "<tr><td>" + j + "</td><td>" + str(
        int(int(k) / 1024)) + "Kb</td><td>" + l + "</td><td td style=""background-color:Green;""></td></tr>"
for i in not_present:
    html = html + "<tr><td>" + i + "</td><td>" + "null" + "</td><td>" + "null" + "</td><td td style=""background-color:Red;""></td></tr>"
html = html + """
</table>
</center>
</body>
</html>
"""
print(html)
me = "rtkcse2@gmail.com"
you = "rtkcse@gmail.com"
msg = MIMEMultipart('alternative')
msg['Subject'] = "Subject"
msg['From'] = me
msg['To'] = you
part1 = MIMEText(html, 'html')
msg.attach(part1)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('rtkcse2@gmail.com', 'kannankannan')
mail.sendmail(me, you, msg.as_string())
print("Sucessfully email Sent")
