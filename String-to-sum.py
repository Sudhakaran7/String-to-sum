import re

string = input()

pattern1= '\s+'
pattern2='\d+'

replace = ''
sums=0

result = re.findall(pattern2, string) 
for i in range(0,len(result)):
  sums+=int(result[i])
print(sums)
