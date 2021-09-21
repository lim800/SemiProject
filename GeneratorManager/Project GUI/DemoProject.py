import time
from tkcalendar import DateEntry
import sys
from tkinter import Tk, Label, Button, Canvas, ttk
from tkinter.ttk import Entry
import tkinter as tk
import tkinter
import tkinter.messagebox
import time
import threading
import csv
import GeneratorClass as GC
status = True
def getValue(value):
    print(value)

window=Tk()

window.title("Project Prototype")
canvas1 = Canvas(window, width=720, height=250, relief='raised')
canvas1.pack()

label1 = Label(window, text='Login to the System')
label1.config(font=('helvetica', 17))
canvas1.create_window(310, 40, window=label1)

label2 = Label(window, text='Enter the username:')
label2.config(font=('helvetica', 12))
canvas1.create_window(250, 90, window=label2)

usernameentry = Entry(window)
canvas1.create_window(470, 90, window=usernameentry)

label4 = Label(window, text='Enter password:')
label4.config(font=('helvetica', 12))
canvas1.create_window(250, 130, window=label4)

passwordentry = Entry(window, show="*")
canvas1.create_window(470, 130, window=passwordentry)

def start():
    global progressbar
    progressbar  = ttk.Progressbar(window, orient = 'horizontal', length = 300, mode = 'determinate')
    canvas1.create_window(400, 220, window=progressbar)
    progressbar.start()

def login():
    window.withdraw()
    username = str(usernameentry.get())
    password = str(passwordentry.get())
    if (len(username) == 0 or len(password) == 0):
        tkinter.messagebox.showinfo("Missing Fields", "Please Fill in the credentials")
    else:
        global newWindow
        newWindow = tk.Toplevel(window)
        newWindow.title("Project Proof of concept")
        canvas2 = Canvas(newWindow, width=720, height=250, relief='raised')
        canvas2.pack()
        enterdatabtn = Button(newWindow,text='Enter the Generator Data', bg='green', fg='white', command=enterdata,
                          font=('helvetica', 14))
        canvas2.create_window(340, 100, window=enterdatabtn)
        viewdatabtn = Button(newWindow,text='View the Data Report', bg='green', fg='white', command=showDataReport,
                              font=('helvetica', 14))
        canvas2.create_window(340, 150, window=viewdatabtn)


def enterdata():
    newWindow.withdraw()
    newWindow2 = tk.Toplevel(window)
    newWindow2.title("Enter Generator Data")
    canvas3 = Canvas(newWindow2, width=820, height=500, relief='raised')
    canvas3.pack()

    gennamelabel = Label(newWindow2, text='Please enter the generator name among the followings:\n1A, 2A, 3A, 4A, 1B, 2B, 3B, 4B')
    gennamelabel.config(font=('helvetica', 12))
    canvas3.create_window(250, 50, window=gennamelabel)

    global gennameentry
    gennameentry = Entry(newWindow2)
    canvas3.create_window(510, 50, window=gennameentry)

    startdatelabel = Label(newWindow2,
                         text='Enter the start date in format mm-dd-yy')
    startdatelabel.config(font=('helvetica', 12))
    canvas3.create_window(250, 90, window=startdatelabel)

    global startdateentry
    startdateentry = DateEntry(newWindow2)
    canvas3.create_window(510, 90, window=startdateentry)

    starttimelabel = Label(newWindow2,
                           text='Enter the start time in format hh:mm')
    starttimelabel.config(font=('helvetica', 12))
    canvas3.create_window(250, 130, window=starttimelabel)

    global starttimeentry
    starttimeentry = Entry(newWindow2)
    canvas3.create_window(510, 130, window=starttimeentry)
    # timeentry = time.strftime('%H:%M%p')
    #
    # starttimeentry = Entry(newWindow2, cursor='plus')
    # starttimeentry.place(x=0, y=0)
    # starttimeentry.insert(0, timeentry)
    # canvas3.create_window(510, 130, window=starttimeentry)

    stopdatelabel = Label(newWindow2,
                           text='Enter the stop date in format mm-dd-yy')
    stopdatelabel.config(font=('helvetica', 12))
    canvas3.create_window(250, 170, window=stopdatelabel)

    global stopdateentry

    stopdateentry = DateEntry(newWindow2)
    canvas3.create_window(510, 170, window=stopdateentry)

    stoptimelabel = Label(newWindow2,
                           text='Enter the stop time in format hh:mm')
    stoptimelabel.config(font=('helvetica', 12))
    canvas3.create_window(250, 210, window=stoptimelabel)

    global stoptimeentry

    stoptimeentry = Entry(newWindow2)
    canvas3.create_window(510, 210, window=stoptimeentry)

    loadvaluelabel = Label(newWindow2,
                          text='Enter the value of load')
    loadvaluelabel.config(font=('helvetica', 12))
    canvas3.create_window(250, 250, window=loadvaluelabel)

    global loadvalueentry
    loadvalueentry = Entry(newWindow2)
    canvas3.create_window(510, 250, window=loadvalueentry)

    runreasonlabel = Label(newWindow2,
                          text='Enter the reason for run')

    runreasonlabel.config(font=('helvetica', 12))
    canvas3.create_window(250, 290, window=runreasonlabel)

    global runreasonentry
    runreasonentry = Entry(newWindow2)
    canvas3.create_window(510, 290, window=runreasonentry)

    submitdatabtn = Button(newWindow2, text='Insert the Data', bg='green', fg='white', command=submitdata,
                          font=('helvetica', 14))
    canvas3.create_window(440, 350, window=submitdatabtn)

if(status):
    with open('SampleData.csv', mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Day', 'Pump', 'Pressure'])
        employee_file.close()
    status = False

def checktime(starttime,starttimeentry):
    status = False
    if (len(starttime) >0):
        if(starttime.__contains__(':') and len(starttime)==5):
            first,second = starttime.split(':')
            first = int(first)
            second = int(second)
            if(first>=0 and first<=23):
                if (second >= 0 and second <= 59):
                    status = True
                else:
                    tkinter.messagebox.showinfo("Error","Enter the time in the correct format")
                    starttimeentry.delete(0, 'end')
            else:
                tkinter.messagebox.showinfo("Error","Enter the time in the correct format")
                starttimeentry.delete(0, 'end')
        else:
            tkinter.messagebox.showinfo("Error","Enter the time in the correct format")
            starttimeentry.delete(0, 'end')
    return status

def submitdata():
    window.withdraw()
    genname = str(gennameentry.get())
    startdate = str(startdateentry.get())
    starttime = str(starttimeentry.get())
    stopdate = str(stopdateentry.get())
    stoptime = str(stoptimeentry.get())
    loadvalue = str(loadvalueentry.get())
    runreason = str(runreasonentry.get())

    generatornames = ['1A', '2A', '3A', '4A', '1B', '2B', '3B', '4B']
    print('Genname:',genname)

    if(genname not in generatornames):
        tkinter.messagebox.showinfo("Generator name must be from the following fields","'1A', '2A', '3A', '4A', '1B', '2B', '3B', '4B'")
        gennameentry.delete(0, 'end')
        startdateentry.delete(0, 'end')
        starttimeentry.delete(0, 'end')
        stopdateentry.delete(0, 'end')
        stoptimeentry.delete(0, 'end')
        loadvalueentry.delete(0, 'end')
        runreasonentry.delete(0, 'end')
    else:
        statstarttime = checktime(starttime,starttimeentry)
        statstoptime = checktime(stoptime,stoptimeentry)

        print('Stat Starttime',statstarttime)

        if(statstarttime and statstoptime):
            if (len(genname) == 0 or len(startdate) == 0 or len(starttime) == 0 or len(stopdate) == 0 or len(stoptime) == 0 or len(loadvalue) == 0 or len(runreason) == 0):
                tkinter.messagebox.showinfo("Missing Fields", "Some fields empty")
            else:
                firstresult = GC.checkCapacity(genname)
                tkinter.messagebox.showinfo("Generator Capacity", firstresult)
                secondresult = GC.dumpData(genname,startdate,starttime,stopdate,stoptime,loadvalue,runreason)
                tkinter.messagebox.showinfo("Generator Result", secondresult)
        else:
            tkinter.messagebox.showinfo("Data Error", "Error while filling the fields")

def showDataReport():
    newWindow.withdraw()
    newWindow2 = tk.Toplevel(window)
    newWindow2.title("Generator Data Calculation Year")
    canvas3 = Canvas(newWindow2, width=600, height=200, relief='raised')
    canvas3.pack()

    gennamelabel = Label(newWindow2,
                         text='Enter the year')
    gennamelabel.config(font=('helvetica', 12))
    canvas3.create_window(250, 50, window=gennamelabel)

    global yearentry
    yearentry = Entry(newWindow2)
    canvas3.create_window(390, 50, window=yearentry)

    submitdatabtn = Button(newWindow2, text='Show the Data', bg='green', fg='white', command=showdatayear,
                           font=('helvetica', 14))
    canvas3.create_window(300, 100, window=submitdatabtn)

def showdatayear():
    window.withdraw()
    datayear = str(yearentry.get())
    if (len(datayear) == 0):
        tkinter.messagebox.showinfo("Missing Fields", "Please Fill in the credentials")
    elif (len(datayear) != 4):
        tkinter.messagebox.showinfo("Invalid format", "Please Enter a valid year i.e. 2020")
    else:
        try:
            strr = GC.showData(datayear)
            tkinter.messagebox.showinfo("Data Report", strr)
        except:
            tkinter.messagebox.showerror("Data Report", 'Data does not exist')

def login2():
    window.withdraw()
    username = str(usernameentry.get())
    password = str(passwordentry.get())
    if(len(username)==0 or len(password)==0):
        tkinter.messagebox.showinfo("Missing Fields", "Please Fill in the credentials")
    else:
        # print('Message:',message)
        # t1 = threading.Thread(target=startSending,args=(message,ipaddress,datafile,ts))
        t3 = threading.Thread(target=start)
        # t1.start()
        t3.start()

loginbtn = Button(text='Sign in', bg='green', fg='white', command = login,
                    font=('helvetica', 14))
stat = True
if(stat):
    loginbtn.state=tk.DISABLED

def closedriver():
    progressbar.stop()
    sys.exit("The player doesn't want to play again")

canvas1.create_window(340, 180, window=loginbtn)
window.mainloop()