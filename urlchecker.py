import requests
url = input("Which url do you want to check? ").strip()

req = requests.get(url)

code = req.status_code

if code != 200:
    print("Error")
    exit()
else:
    print("You got it girl" + "\n")


everything = req.text
index = 0
while index < 10:
	line = everything.splitlines()[index]
	print(line)
	index = index + 1
