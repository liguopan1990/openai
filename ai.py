import openai
from tkinter import *
from tkinter import scrolledtext
import tkinter.filedialog
import tkinter as tk
global question

top = tkinter.Tk()
top.geometry("800x600")
msg = tkinter.StringVar()
sucmsg = tkinter.StringVar()


def upData():
    global stop_count
    if not stop_count:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=50
        )
        # print(response)
        content = response.choices[0].text
        if 'length' not in response.choices[0].finish_reason:
            question.insert(tk.END, content)
        else:
            question.insert(tk.END, content)
            question.update()
            top.after(2000, upData)


def cancel():
    global stop_count
    stop_count = True


def choose():
    global stop_count
    global model
    global prompt
    global content
    openai.organization = "xxxxxxxxx"
    openai.api_key = 'xxxxxxxxxxxxx'
    prompt = msg.get()
    model = "text-davinci-003"
    content = ""
    stop_count = False
    upData()


Label(top, text='有本事你随便问').grid(row=0, column=0, padx=5, pady=5)
lb1 = Label(top, text='请输入问题：').grid(row=1, column=0, sticky=E)
Entry(top, bd='5', textvariable=msg, width="60").grid(
    row=1, column=1, sticky=E)
btn = Button(top, width=10, text="确定", command=choose)
btn.grid(row=1, column=2)
btn = Button(top, width=10, text="取消", command=cancel)
btn.grid(row=1, column=3)
question = scrolledtext.ScrolledText(top,  width="80", height="36")
question.grid(
    row=3, column=0, padx=30, pady=5, columnspan=3)
top.mainloop()
