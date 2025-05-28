import requests
import urllib.request
from bs4 import BeautifulSoup
from tkinter import *

url = ""

def retrieve_input():
    global url
    url = textBox.get("1.0","end-1c")
    print(url)


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

def save():
    global url
    page  = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    file = open( "article.txt", "w", encoding="utf-8")# Name the file as per the dpcument/ as per your want
    soup_title = soup.title.string+"\n"
    file.write(soup_title)
    for para in soup.find_all("p"):
        soup_para=(str(para.text))
        file.write(soup_para+ "\n")
    file.close()
    lb.config(text = "Saved "+ url +" Sucessfully")

if __name__ == "__main__":
	root = Tk()
	root.configure(background="White")
	root.title("Sample of Web Scrapping")
	root.geometry("900x400")
	root.resizable(False,False)
	textBox = Text(root, height=2, width = 150)
	textBox.pack()
	buttonCommit = Button(root, height=1, width=10, text="Target URL",command=lambda: retrieve_input())
	buttonCommit.pack()
	save = Button(root, height=1, width =10, text="Save", command = save)
	save.pack()
	lb = Label(root, text = " ")
	lb.pack()
	root.mainloop()
