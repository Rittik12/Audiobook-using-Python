#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3
import PyPDF2


# In[ ]:


mybook=open('C:/Users/user/Desktop/PythonNotes.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(mybook)
pages=pdfreader.numPages
print('number of pages:',pages )
speaker= pyttsx3.init()
for num in range(6,pages):
    page= pdfreader.getPage(6)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()


# In[ ]:




