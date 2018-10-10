import requests
url = input("Which url do you want to check? ").strip()
#get information from the url
req = requests.get(url)
#check if the status is ok, 200.
code = req.status_code

#if it's not 200, you quit the program
if code != 200:
    print("Error")
    exit()
else:
    print("You got it girl" + "\n")

#the first ten lines. But only the code
everything = req.text
index = 0
while index < 10:
	line = everything.splitlines()[index]
	print(line)
	index = index + 1
