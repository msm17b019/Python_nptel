import string

a=input()
a=a.replace('.','')
a=a.replace(',','')
a=a.replace(':','')
a=a.replace(';','')
a=a.replace('?','')
a=a.replace('"','')
a=a.replace('\'','')
a=a.replace('!','')
a=a.replace('-','')

print(a)