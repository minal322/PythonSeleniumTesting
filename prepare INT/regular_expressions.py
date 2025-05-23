import re

# #check file name starts with a letter
# filename = "report.txt"
# patterns = r"[a-zA-Z]"
# match_found = re.match(patterns,filename)
# print(match_found.group())
#
#
# #check username starts with a character
# username = "Minal"
# patterns = r"[a-zA-z]\w+"
# match_found = re.match(patterns,username)
# print(match_found.group())
#
#
# #check number is 10 digits number or not
# number = "9075025012"
# pattern = r"\d{10}"
# match = re.fullmatch(pattern,number)
# print(match.group())
#
#
# #validate Vehicle registration number
# vehicle_number = "TX02FG8566"
# vpattern = "[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}"
# match = re.fullmatch(vpattern,vehicle_number)
# print(match.group())
#
# #check if email contains @gmail.com
# email = "patilminal322@gmail.com"
# pattern = "@gmail.com"
# match = re.search(pattern,email)
# print(match.group())
# print(match.start())

# # check https or not
# url = "https://www.google.com"
# pattern = "https"
# match = re.search(pattern,url)
# print(match.start())

# text = "My name is ghhj my gmail address aare kmr_123@gmail.com and abc5678@gmail.com"
# patten = "[a-z0-9_.%-+]+@[a-z]{5}.[a-z]{3}"
# match = re.findall(patten,text)
# print(match)
#
# text = "My project completed on 25/03/2025 and started on 01/01/2024"
# pattern = r"\d{2}/\d{2}/\d{4}"
# listt = re.findall(pattern,text)
# print(listt)

#
text =  "9078526356 and 37899965412"
pattern = r"\d{10}"
matches = re.finditer(pattern,text)
for match in matches:
    print(match.group(),match.start(), match.end())

# #find all hashtag positions in instagram
# text = "loving the sunset #vibes #travel and #nature"
# pattern= r"#\w+"
# matches = re.finditer(pattern,text)
# for match in matches:
#     print(match.group(),match.start(), match.end())
#
# # repalce python with PYTHON
# text = "python python"
# text.lower()
# print(text)
# pattern = r"python"
# output = re.sub(pattern,"PYTHON", text)
# print(output)
#
# #cenbsor bad word
# text = "you are a badword"
# output = re.sub(r"badword","****" ,text)
# print(output)
#
#
# #formatting phone numbers to standard format  (xxx) xxx-xxxx
# text = "call me at 563-455-8950 and 869-458-752 "
# pattern = r"(\d{3})-(\d{3})-(\d{3,4})"
# replace = r"(\1) \2-\3"
# matches = re.sub(pattern,replace,text)
# print(matches)
#
# #formatting phone numbers to standard format  (xxx) xxx-xxxx
# text = "call me at 563-455-8950 and 869-458-752 "
# pattern = r"(\d{3})-(\d{3})-(\d{3,4})"
# replace = r"(\1) \2-\3"
# matches = re.subn(pattern,replace,text)
# print(matches)

#mask original data
text = "My credit card is 5638-4586-1234-7894 and 7894-5668-2688-4865"
pattern = r"(\d{4})-(\d{4})-(\d{4})-(\d{4})"
replace = r"****-****-****-\4"
masked_data = re.sub(pattern,replace,text)
print(masked_data)


#split a sentance into words
t = "python is fun"
p = r"\s"
print(re.split(p,t))

text = "apple,banana,  cvggerg apple,banana,  cvggerg"
patten = r",\s*"
print(re.split(patten,text))


text = "My name is ghhj my gmail address aare kmr_123@gmail.com and abc5678@gmail.com and abc5678@perforce.in"
patten = "([a-z0-9_.%-+]+)@([a-z]{3,}).([a-z]{2,3})"
replace = r"*****@\2.\3"
match = re.sub(patten,replace,text)
print(match)

#check string starts with specific word or not
text1 = "Hello , welcome to python!"
text2 = "Welcome, to pune"
pattern1 = "^Hello"
p2 = "python!$"
print(bool(re.match(pattern1,text1)))
print(bool(re.match(p2,text1)))

print(bool(re.match(pattern1,text2)))
print(bool(re.match(p2,text2)))


test = "this contains ip address 192.46.10.2 and 10.237.25.78, 10.237.25.78685 and 10.237.25.7"
pattern = r"\d{2,3}.\d{1,3}.\d{1,3}.\d{1,3}"
match = re.findall(pattern, test)
print(match)