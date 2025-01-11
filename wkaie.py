import requests as r

url = "https://random-hadith-generator.vercel.app/bukhari/"
load = r.get(url).json()

book = str(load['data']["book"])
bookName = str(load['data']["bookName"]).replace("\t", "").replace("\n", "")
chapter = str(load['data']["chapterName"]).replace("Chapter:", "").replace("\n", "")
ref = str(load['data']["refno"])
hadith = str(load['data']["hadith_english"])

print("Book:", book)
print("Book name:", bookName)
print("Chapter name:", chapter)
print("Reference no:", ref)
print("Hadith:", hadith)