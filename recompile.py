import re
string = 'dkajdkflks.zip'
obj = re.compile(r'\.[a-z]{3,5}$')
print(obj.search(string))
match=obj.search(string)
print(match.group())
text=match.group()
print(type(text))
print(type(string))
text.replace('.','')
print(text.lstrip('.'))
