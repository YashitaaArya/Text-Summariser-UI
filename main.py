import customtkinter 
import tkinter
from tkinter import ttk, END
from tkinter.scrolledtext import *
import tkinter.filedialog
from spacy_summarization import text_summarizer
from nltk_summarization import nltk_summarizer
from bs4 import BeautifulSoup
from urllib.request import urlopen

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("700x400") 
root.title("Summarizer GUI")

style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn',)

tab_control = ttk.Notebook(root,style='lefttab.TNotebook')
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Summarize":^20s}')
tab_control.add(tab2, text=f'{"URL":^20s}')
label1 = customtkinter.CTkLabel(tab1, text= 'Summaryzer',padx=5, pady=5)
label1.grid(column=0, row=0)
label2 = customtkinter.CTkLabel(tab2, text= 'URL',padx=5, pady=5)
label2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

# Functions 
def get_summary():
    raw_text = str(entry.get('1.0',END))
    final_text = text_summarizer(raw_text)
    print(final_text)
    result = '\nSummary:{}'.format(final_text)
    tab1_display.insert(END,result)

# Clear entry widget
def clear_text():
    entry.delete('1.0',END)

def clear_display_result():
    tab1_display.delete('1.0',END)

# Clear For URL
def clear_url_entry():
    url_entry.delete(0,END)

def clear_url_display():
    tab3_display_text.delete('1.0',END)


# Fetch Text From Url
def get_text():
    raw_text = str(url_entry.get())
    page = urlopen(raw_text)
    soup = BeautifulSoup(page)
    fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
    url_display.insert(END,fetched_text)

def get_url_summary():
    raw_text = url_display.get('1.0',END)
    final_text = text_summarizer(raw_text)
    result = '\nSummary:{}'.format(final_text)
    tab2_display_text.insert(END,result)    

l1=customtkinter.CTkLabel(tab1,text="Enter Text To Summarize")
l1.grid(row=1,column=0)

entry=ScrolledText(tab1,height=10)
entry.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

# BUTTONS
button1=customtkinter.CTkButton(tab1,text="Reset",command=clear_text)#, width=12,bg='blue',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=customtkinter.CTkButton(tab1,text="Summarize",command=get_summary)#, width=12,bg='red',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=customtkinter.CTkButton(tab1,text="Clear Result", command=clear_display_result)#,width=12,bg='green',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

# Display Screen For Result
tab1_display = ScrolledText(tab1)
tab1_display.grid(row=7,column=0, columnspan=3)

#URL TAB
l1=customtkinter.CTkLabel(tab2,text="Enter URL To Summarize")
l1.grid(row=1,column=0)

url_entry=customtkinter.CTkEntry(tab2)
url_entry.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

#BUTTONS FOR URL TAB
button1=customtkinter.CTkButton(tab2,text="Reset",command=clear_url_entry)#,width=12,command=clear_url_entry,bg='blue',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=customtkinter.CTkButton(tab2,text="Get Text",command=get_text)#,width=12,command=get_text,bg='orange',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=customtkinter.CTkButton(tab2,text="Summarize",command=get_url_summary)#,width=12,command=get_url_summary,bg='red',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=customtkinter.CTkButton(tab2,text="Clear Result",command=clear_url_display)#,width=12,command=clear_url_display,bg='green',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)

#Display Screen For URL Tab
url_display = ScrolledText(tab2)
url_display.grid(row=7,column=0, columnspan=3)

tab2_display_text = ScrolledText(tab2,height=10)
tab2_display_text.grid(row=10,column=0, columnspan=3,padx=5,pady=5)

root.mainloop()