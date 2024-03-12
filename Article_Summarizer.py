import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article 

def Del():
    title.config(state='normal')
    author.config(state='normal')
    publishing_date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    author.delete('1.0','end')
    publishing_date.delete('1.0','end')
    summary.delete('1.0','end')
    sentiment.delete('1.0','end')
    utext.delete('1.0','end')

    title.config(state='disabled')
    author.config(state='disabled')
    publishing_date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')
    

def summarize():
    nltk.download('punkt')

    #Backend Code 
    #takes the url and parse it into an article
    url = utext.get('1.0',"end").strip()
    #creating an article object of the newspaper lib 
    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publishing_date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0', article.title)

    author.delete('1.0','end')
    author.insert('1.0', article.authors)

    publishing_date.delete('1.0','end')
    publishing_date.insert('1.0', article.publish_date)

    summary.delete('1.0','end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0','end')
    sentiment.insert('1.0',f'Polarity{analysis.polarity}, 'f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    
    title.config(state='disabled')
    author.config(state='disabled')
    publishing_date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

    # print(f'Title : {article.title}')
    # print(f'Authors : {article.authors}')
    # print(f'Publication Date : {article.publish_date}')
    # print(f'Summary : {article.summary}')

    # analysis = TextBlob(article.text)
    # print(analysis.polarity)
    # print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')


#the graphical user interface(GUI)
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x610')

tlabel = tk.Label(root, text='Title')
tlabel.pack()
title = tk.Text(root,height=1 ,width=140)
title.config(state='disabled',bg='#dddddd')
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()
author = tk.Text(root,height=1 ,width=140)
author.config(state='disabled',bg='#dddddd')
author.pack()

plabel = tk.Label(root, text='Publication Date')
plabel.pack()
publishing_date = tk.Text(root,height=1 ,width=140)
publishing_date.config(state='disabled',bg='#dddddd')
publishing_date.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()
summary = tk.Text(root,height=20 ,width=140)
summary.config(state='disabled',bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text='Sentiment Analysis')
selabel.pack()
sentiment= tk.Text(root,height=1 ,width=140)
sentiment.config(state='disabled',bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text='Url')
ulabel.pack()
utext = tk.Text(root,height=1 ,width=140) 
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

dbtn = tk.Button(root ,text="Clear",command= Del)
dbtn.pack()

root.mainloop()
