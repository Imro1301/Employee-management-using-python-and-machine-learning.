from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from tkinter import ttk
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Employee Turnover Prediction")
    root.configure(background="LightSkyBlue")
    
    satisfaction_level= tk.IntVar()
    last_evaluation= tk.IntVar()
    number_project = tk.IntVar()
    average_montly_hours = tk.IntVar()
    time_spend_company= tk.IntVar()
    Work_accident = tk.IntVar()
    salary =  tk.StringVar()
    promotion_last_5years = tk.IntVar()
    Department = tk.StringVar()
    
    
    #===================================================================================================================

    
    def Reset():
        satisfaction_level.delete(0, 'end')
        last_evaluation.delete(0, 'end')
        number_project.delete(0, 'end')
        average_montly_hours.delete(0, 'end')
        time_spend_company.delete(0, 'end')
        Work_accident.delete(0, 'end')
        salary.set('')
        promotion_last_5years.delete(0, 'end')
        Department.set('')
        yes.config(text='')

    
    def home():
        from subprocess import call
        call(["python","emp GUI_Master.py"])

    def Detect():
        e1=satisfaction_level.get()
        print(e1)
        e2=last_evaluation.get()
        print(e2)
        e3=number_project.get()
        print(e3)
        e4=average_montly_hours.get()
        print(e4)
        e5=time_spend_company.get()
        print(e5)
        e6=Work_accident.get()
        print(e6)
        e7=salary.get()
        if e7=="low":
            e7=0
        elif e7=="medium":
            e7=1
        elif e7=="high":
            e7=2
        else:    
             e7=3
        print(e7)
        
        e8=promotion_last_5years .get()
        print(e8)
        e9=  Department.get()
        if e9=="sales":
            e9=0
        elif e9=="accounting":
            e9=1
        elif e9=="hr":
            e9=2
        elif e9=="technical":
            e9=3
        elif e9=="marketing":
            e9=4
        elif e9=="IT":
             e9=5
        else:    
             e9=6
        print(e9)
        
    
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('model.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9]])
        print(v)
    
        if v[0]==0:
           print("Employee Leave ")
           yes = tk.Label(root,text="As per employee performance. \n employee can not be promoted ",background="red",foreground="white",font=('times', 20, ' bold '),width=30,height=2)
           yes.place(x=500,y=600)
           
           
        if v[0]==1:
           print("Employee  not Leave")
           yes = tk.Label(root,text="Employee  promoted",background="green",foreground="white",font=('times', 20, ' bold '),width=30,height=2)
           yes.place(x=500,y=600)

           
      

    l1=tk.Label(root,text="satisfaction_level",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l1.place(x=5,y=1)
    satisfaction_level=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=satisfaction_level)
    satisfaction_level.place(x=500,y=1)

    l2=tk.Label(root,text="last_evaluation",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l2.place(x=5,y=50)
    last_evaluation=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=last_evaluation)
    last_evaluation.place(x=500,y=50)

    l3=tk.Label(root,text="number_project",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l3.place(x=5,y=100)
    number_project=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=number_project)
    number_project.place(x=500,y=100)
    
    
    l4=tk.Label(root,text="average_montly_hours",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l4.place(x=5,y=150)
    average_montly_hours=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=average_montly_hours)
    average_montly_hours.place(x=500,y=150)

    l5=tk.Label(root,text="time_spend_company",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l5.place(x=5,y=200)
    time_spend_company=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=time_spend_company)
    time_spend_company.place(x=500,y=200)

    l6=tk.Label(root,text="Work_accident",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l6.place(x=5,y=250)
    Work_accident=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Work_accident)
    Work_accident.place(x=500,y=250)
    
    
    l7=tk.Label(root,text="salary",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l7.place(x=5,y=300)
    
    l7=tk.Label(root,text="salary",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l7.place(x=5,y=300)
    monthchoosen = ttk.Combobox(root, width = 27, textvariable = salary)
    # Adding combobox drop down list
    monthchoosen['values'] = (' low',
    						' medium',
    						' high')
    monthchoosen.place(x=500,y=300)
    #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()
   

    l8=tk.Label(root,text="promotion_last_5years",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l8.place(x=5,y=350)
    promotion_last_5years=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=promotion_last_5years)
    promotion_last_5years.place(x=500,y=350)

    l9=tk.Label(root,text="Department",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l9.place(x=5,y=400)
    monthchoosen = ttk.Combobox(root, width = 27, textvariable = Department)

   # Adding combobox drop down list
    monthchoosen['values'] = (' sales',
   						' accounting',
   						' hr',
   						' technical',
   						' marketing',
   						' IT')
    monthchoosen.place(x=500,y=400)
   #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()
   

    button1 = tk.Button(root,text="Predict",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=500,y=600)

    button2 = tk.Button(root, text="Check For Another Employee", command=Reset, font=('times', 20, 'bold'), width=30)
    button2.place(x=300, y=700)

    button5 = tk.Button(root, font=("times", 20, "bold"),
                        text="Go To Home", command=home, width=10)
    button5.place(x=300, y=600)
    
    root.mainloop()

Train()