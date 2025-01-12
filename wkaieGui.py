try:
    from tkinter import *
    from os import system as s
    import requests as r
except:
    s("pip install requests")
    
class Wkaie:
    def __init__(self, root):
        self.root = root
        self.root.title("Ahadith Generator")
        self.root.geometry("1080x1090")
        self.generator()

    def generator(self):
        self.url = "https://random-hadith-generator.vercel.app/bukhari/"
        self.load = r.get(self.url).json()
        self.book = str(self.load['data']["book"])
        self.bookName = str(self.load['data']["bookName"]).replace("\t", "").replace("\n", "")
        self.chapter = str(self.load['data']["chapterName"]).replace("Chapter:", "").replace("\n", "")
        self.ref = str(self.load['data']["refno"])
        self.hadith = str(self.load['data']["hadith_english"])
        self.Lbook = Label(self.root, text="Book:", font=("Helvetica", 14))
        self.LbookName = Label(self.root, text="Book name:", font=("Helvetica", 14))
        self.LchapterName = Label(self.root, text="Chapter name:", font=("Helvetica", 14))
        self.LrefNo = Label(self.root, text="Reference no:", font=("Helvetica", 14))
        self.Lhadith = Label(self.root, text="Hadith:", wraplength=1050, font=("Helvetica", 14))
        
        self.LbookName.pack(pady=6)
        self.Lbook.pack(pady=5)
        self.LchapterName.pack(pady=7)
        self.LrefNo.pack(pady=8)
        self.Lhadith.pack(pady=9)
        
        button = Button(self.root, text="GENERATE", command=self.wkaie)
        button.pack(pady=1)
        
    def wkaie(self):
        self.LbookName.config(text=f"Book: {self.book}")
        self.Lbook.config(text=f"Book name: {self.bookName}")
        self.LchapterName.config(text=f"Chapter name: {self.chapter}")
        self.LrefNo.config(text=f"Reference no: {self.ref}")
        self.Lhadith.config(text=f"Hadith: {self.hadith}")

if __name__ == "__main__":
    wkaie = Tk()
    Wkaie(wkaie)
    wkaie.mainloop()