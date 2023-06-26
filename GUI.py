# importing all lib
import tensorflow as tf
from tensorflow import keras
from keras.models import Model
import tkinter as tk
from tkinter import ttk
import PIL
from tkinter import filedialog
from tkinter import *
from PIL import Image
import numpy as np

# Loading the model
from keras.models import load_model
model=load_model('Age_sex_Detection.h5')

# initializing the GUI
top=tk.Tk()
top.geometry("800x600")
top.title('Age & Gender Detector')
top.configure(background='#CDCDCD')

# initializing the labels (1 for age and 1 for sex)//
label1=Label(top,background="#CDCDCD",font=('arial',15,"bold"))
label2=Label(top,background="#CDCDCD",font=('arial',15,"bold"))
sign_image=Label(top)

# Defining Detect fuction which detects the age and gender of the person in image using the model
def Detect(file_path):
    global Label_packed
    image=Image.open(file_path)
    image=Image.resize(48,48,3)
    image=np.expand_dims(image,axis=0)
    image=np.array(image)
    image=np.delete(image,0.1)
    image=np.resize(image,(48,48,3))
    print(image.shape)
    sex_f=["Male","Female"]
    image=np.array([image])/255
    pred=model.predict(image)
    age=int(np.round(pred[1][0]))
    sex=int(np.round(pred[0][0]))
    print("Predicted Age is "+ str(age))
    print("Predicted Gender is "+ sex_f[sex])
    label1.configure(foreground="#011638",text=age)
    label1.configure(foreground="#011638",text=sex_f[sex])

#Defining show_detect button function
def show_Detect_button(file_path):
    Detect_b=Button(top,text="Detect Image",command=lambda:Detect(file_path),padx=10,paddy=50)
    Detect_b.configure(background="#364156",foreground='white',font=('arial',10,"bold"))
    Detect_b.place(relx=0.79,rely=0.46)

#Defining Upload Image Function
def upload_image():
    try:
        file_path=filedialog.askopenfile
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        show_Detect_button(file_path)
    except:
        pass
upload=Button(top,text="Upload an Image",command=upload_image,padx=10,pady=50)
upload.configure(background="#364156",foreground='white',font=('arial',10,"bold")) 
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand=True)
label1.pack(side="bottom",pady=50)
label2.pack(side="bottom",pady=50)
heading=Label(top,text='Age and Gender Detector',pady=20,font=('arial',20,'bold'))
heading.configure(background="#CDCDCD",foreground="#364156")
heading.pack()
top.mainloop()
                                                               

