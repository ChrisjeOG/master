movie = {
    "title" : "Dead pool",
    "year" : 2016,
    "duration" : 108,
    "director" : "Tim Miller"
}

#basic
# for key, val in movie.items():
#     print(f"{key}: {val}")
#print(f"{val} is released in {val}, and the duration is {val} and directed by {val}")

movie["actors"] = ["Ryan Renolds" , "Morena Baccarin", "Brianna Hildebrand", "T.J. Miller"]


for key, val in movie.items():
    if key == "duration":
        print(f"{key} : {val} minutes")
    elif key == "actors":
        print(key + ": " + ",".join(val))
    else:
        print(f"{key} : {val}")
