import requests
import json

url = input("Please, put your wikipedia article here. ").strip()
url = url.replace(" ", "_")
newurl = "https://en.wikipedia.org/api/rest_v1/page/summary/" + url

req = requests.get(newurl)
#data is a dictionary now
data = json.loads(req.text)

code = req.status_code

if code != 200:
    print("please try again")
    exit()
else:
    print("You got it girl" + "\n")

title = data["title"]
print(f"The title is: \n{title}\n")

if "description" in data:
    description = data["description"]
    print(f"The description is: \n{description}\n")
if "extract" in data:
    extract = data["extract"]
    print(f"The extract is: \n{extract}\n")
