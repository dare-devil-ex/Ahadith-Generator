try:
    from tkinter import *
    from os import system as s
    import requests as r
except:
    s("pip install requests")
    
    
root = Tk()
root.title("Ahadith Generator")
root.geometry("1080x1090")

class Wkaie:
    def __init__(self):
        self.url = "https://random-hadith-generator.vercel.app/bukhari/"
        self.load = r.get(self.url).json()
        self.book = str(self.load['data']["book"])
        self.bookName = str(self.load['data']["bookName"]).replace("\t", "").replace("\n", "")
        self.chapter = str(self.load['data']["chapterName"]).replace("Chapter:", "").replace("\n", "")
        self.ref = str(self.load['data']["refno"])
        self.hadith = str(self.load['data']["hadith_english"])
        
        Lbook = Label(root, text=f"Book: {self.book}", font=("Helvetica", 14))
        LbookName = Label(root, text=f"Book name: {self.bookName}", font=("Helvetica", 14))
        LchapterName = Label(root, text=f"Chapter name: {self.chapter}", font=("Helvetica", 14))
        LrefNo = Label(root, text=f"Reference no: {self.ref}", font=("Helvetica", 14))
        Lhadith = Label(root, text=f"Hadith: {self.hadith}", wraplength=1050, font=("Helvetica", 14))
        
        Lbook.pack(pady=5)
        LbookName.pack(pady=6)
        LchapterName.pack(pady=7)
        LrefNo.pack(pady=8)
        Lhadith.pack(pady=9)
        
    def wkaie():
        Wkaie.generator()
        Lb
        
        
button = Button(root, text="GENERATE", command=Wkaie.wkaie)
button.pack(pady=1)
        
if __name__ == "__main__":
    root.mainloop()