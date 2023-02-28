from multiprocessing.sharedctypes import Value
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk 
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital: 
      def __init__(self,root):
       self.root=root
       self.root.geometry("1540x800+0+0")
       self.root.title("Hospital Management System")



       self.Nameoftablets=StringVar()
       self.ref=StringVar()
       self.Dose=StringVar()
       self.NumberofTablets=StringVar()
       self.Lot=StringVar()
       self.Issuedate=StringVar()
       self.ExpDate=StringVar()
       self.DailyDose=StringVar()
       self.SideEffect=StringVar()
       self.FurtherInformation=StringVar()
       self.BloodPressure=StringVar()
       self.Storage=StringVar()
       self.DrivingMachine=StringVar()
       self.Medication=StringVar()
       self.PatientId=StringVar()
       self.NhsNumber=StringVar()
       self.PatientName=StringVar()
       self.DateOfBirth=StringVar()
       self.PatientAddress=StringVar()


       lbltitle=Label(self.root,bd=20,relief=RIDGE,text=" +HOSPITAL MANAGEMENT SYSTEM",fg="blue",bg="white",font=("times new roman",50,"bold"))
       lbltitle.pack(side=TOP,fill=X)

      #  ************************************Dataframe******************************

       Dataframe=Frame(self.root,bd=20,relief=RIDGE)
       Dataframe.place(x=0,y=130,width=1530,height=400)

       #  **********************************Leftframe**********************************

       Dataframeleft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE, font=("arial",12,"bold"),text="patient Information",fg="red")

       Dataframeleft.place(x=0,y=0,width=980,height=350)

       #   **********************************Rightframe********************************

       Dataframeright=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE, font=("arial",12,"bold"),text="Prescription")

       Dataframeright.place(x=990,y=5,width=460,height=350)

       #   **********************************Button frame********************************

       Buttonframe=Frame(self.root,bd=20,relief=RIDGE)

       Buttonframe.place(x=0,y=530,width=1530,height=70)

       #   ********************************** Details frame********************************

       Detailsframe=Frame(self.root,bd=20,relief=RIDGE)

       Detailsframe.place(x=0,y=600,width=1530,height=190)

       #   *********************************DataframeLeft***********************************

       lblNameOfTablet=Label(Dataframeleft,text="Name of Tablet",font=("time new roman",12,"bold"),padx=2,pady=6)
       lblNameOfTablet.grid(row=0,column=0)

       comNameOfTablet=ttk.Combobox(Dataframeleft,textvariable=self.Nameoftablets,state="readonly",
                                                       font=("arial",12,"bold"),width=33)

       comNameOfTablet['values']=(" ","Nice","Corona Vacacine","Acetaminophen","adderall","Anmlodipine","Ativan")
       comNameOfTablet.current(0)
       comNameOfTablet.grid(row=0,column=1)

       lblref=Label(Dataframeleft,font=("arial",12,"bold"),text="Reference No",padx=2,pady=2)
       lblref.grid(row=1,column=0,sticky=W)
       txtref=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
       txtref.grid(row=1,column=1)

       lblDose=Label(Dataframeleft,font=("arial",12,"bold"),text="Dose",padx=2,pady=4)
       lblDose.grid(row=2,column=0,sticky=W)
       txtDose=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
       txtDose.grid(row=2,column=1)

       lblNoOfTablets=Label(Dataframeleft,font=("arial",12,"bold"),text="No of Tablets::",padx=2,pady=6)
       lblNoOfTablets.grid(row=3,column=0,sticky=W)
       txtNoOfTablets=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
       txtNoOfTablets.grid(row=3,column=1)

       lblLot=Label(Dataframeleft,font=("arial",12,"bold"),text="Lot",padx=2,pady=6)
       lblLot.grid(row=4,column=0,sticky=W)
       txtLot=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
       txtLot.grid(row=4,column=1)

       lblissueDate=Label(Dataframeleft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
       lblissueDate.grid(row=5,column=0,sticky=W)
       txtissueDate=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
       txtissueDate.grid(row=5,column=1)

       lblExpDate=Label(Dataframeleft,font=("arial",12,"bold"),text="Exp Date",padx=2,pady=6)
       lblExpDate.grid(row=6,column=0,sticky=W)
       txtExpDate=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
       txtExpDate.grid(row=6,column=1)
       
       lblDrivingMachine=Label(Dataframeleft,font=("arial",12,"bold"),text="Lot",padx=2,pady=6)
       lblDrivingMachine.grid(row=4,column=0,sticky=W)
       txtDrivingMachine=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.DrivingMachine,width=35)
       txtDrivingMachine.grid(row=4,column=1)

       lblDailyDose=Label(Dataframeleft,font=("arial",12,"bold"),text="Daily Dose",padx=2,pady=4)
       lblDailyDose.grid(row=7,column=0,sticky=W)
       txtDailyDose=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
       txtDailyDose.grid(row=7,column=1)

       lblSideEffect=Label(Dataframeleft,font=("arial",12,"bold"),text="Side Effect",padx=2,pady=6)
       lblSideEffect.grid(row=8,column=0,sticky=W)
       txtSideEffect=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.SideEffect,width=35)
       txtSideEffect.grid(row=8,column=1)

       lblFurtherinfo=Label(Dataframeleft,font=("arial",12,"bold"),text="Further Information",padx=2,)
       lblFurtherinfo.grid(row=0,column=2,sticky=W)
       txtFurtherinfo=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
       txtFurtherinfo.grid(row=0,column=3)

       lblBloodPressure=Label(Dataframeleft,font=("arial",12,"bold"),text="Blood Pressure",padx=2,pady=6)
       lblBloodPressure.grid(row=1,column=2,sticky=W)
       txtBloodPressure=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.BloodPressure,width=35)
       txtBloodPressure.grid(row=1,column=3)

       lblStorage=Label(Dataframeleft,font=("arial",12,"bold"),text="Storage",padx=2,pady=6)
       lblStorage.grid(row=2,column=2,sticky=W)
       txtStorage=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.Storage,width=35)
       txtStorage.grid(row=2,column=3)

       lblNhsNumber=Label(Dataframeleft,font=("arial",12,"bold"),text="Nhs Number",padx=2,pady=6)
       lblNhsNumber.grid(row=3,column=2,sticky=W)
       txtNhsNumber=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.NhsNumber,width=35)
       txtNhsNumber.grid(row=3,column=3)

       lblPatientId=Label(Dataframeleft,font=("arial",12,"bold"),text="Patient Id",padx=2,pady=6)
       lblPatientId.grid(row=4,column=2,sticky=W)
       txtPatientId=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.PatientId,width=35)
       txtPatientId.grid(row=4,column=3)

       lblMedication=Label(Dataframeleft,font=("arial",12,"bold"),text="Medication",padx=2,pady=6)
       lblMedication.grid(row=5,column=2,sticky=W)
       txtMedication=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.Medication,width=35)
       txtMedication.grid(row=5,column=3)

       lblPatientName=Label(Dataframeleft,font=("arial",12,"bold"),text="Patient Name",padx=2,pady=6)
       lblPatientName.grid(row=6,column=2,sticky=W)
       txtPatientName=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.PatientName,width=35)
       txtPatientName.grid(row=6,column=3)

       lblDateOfBirth=Label(Dataframeleft,font=("arial",12,"bold"),text="Date Of Birth",padx=2,pady=6)
       lblDateOfBirth.grid(row=7,column=2,sticky=W)
       txtDateOfBirth=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=35)
       txtDateOfBirth.grid(row=7,column=3)

       lblPatientAddress=Label(Dataframeleft,font=("arial",12,"bold"),text="Patient Address",padx=2,pady=6)
       lblPatientAddress.grid(row=8,column=2,sticky=W)
       txtPatientAddress=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=35)
       txtPatientAddress.grid(row=8,column=3)


      #  *************************************Dataframeright************************************************

       self.txtPrescription=Text(Dataframeright,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
       self.txtPrescription.grid(row=0,column=0)

      #  ***************************************BUTTON******************************************************

       btnPrescription=Button(Buttonframe,command=self.iPrescription,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=24,padx=2,pady=6)
       btnPrescription.grid(row=0,column=0)

       btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=24,padx=2,pady=6)
       btnPrescriptionData.grid(row=0,column=1)


       btnUpdate=Button(Buttonframe,command=self.Update_data,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=24,padx=2,pady=6)
       btnUpdate.grid(row=0,column=2)

       btnDelete=Button(Buttonframe,command=self.delete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=24,padx=2,pady=6)
       btnDelete.grid(row=0,column=3)

       btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=24,padx=2,pady=6)
       btnClear.grid(row=0,column=4)

       btnExit=Button(Buttonframe,command=self.Exit,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
       btnExit.grid(row=0,column=5)

       #  ***************************************Table**********************************************
       #  ***********************************Scrollbar***********************************************

       scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
       self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablets","ref","dose","nooftablets","lot","issuedate",
                                          "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)

       scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
       scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)


       self.hospital_table.heading("nameoftablets",text="Name Of Tablets")
       self.hospital_table.heading("ref",text="Reference No.")
       self.hospital_table.heading("dose",text="Dose")
       self.hospital_table.heading("nooftablets",text="No Of Tablets")
       self.hospital_table.heading("lot",text="Lot")
       self.hospital_table.heading("issuedate",text="Issue Date")
       self.hospital_table.heading("expdate",text="Exp Date")
       self.hospital_table.heading("dailydose",text="Daily Dose")
       self.hospital_table.heading("storage",text="Storage")
       self.hospital_table.heading("nhsnumber",text="NHS Number")
       self.hospital_table.heading("pname",text="Patient Name")
       self.hospital_table.heading("dob",text="DOB")
       self.hospital_table.heading("address",text="Address") 

       self.hospital_table["show"]="headings"


       self.hospital_table.column("nameoftablets",width=110)
       self.hospital_table.column("ref",width=100)
       self.hospital_table.column("dose",width=100)
       self.hospital_table.column("nooftablets",width=100)
       self.hospital_table.column("lot",width=100)
       self.hospital_table.column("issuedate",width=100)
       self.hospital_table.column("expdate",width=100)
       self.hospital_table.column("dailydose",width=100)
       self.hospital_table.column("storage",width=100)
       self.hospital_table.column("pname",width=100)
       self.hospital_table.column("dob",width=100)
       self.hospital_table.column("address",width=100) 



       self.hospital_table.pack(fill=BOTH,expand=1)
       self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

       self.fatch_data()

      #  ******************************************************functionlity Declration****************************************************
      def iPrescriptionData(self):
         if self.Nameoftablets.get()=="" or self.ref.get()=="":
             messagebox.showerror("Error","All fields are required")
         else:
             conn=mysql.connector.connect(host="localhost",user="root",password="Sachin@123#123",database="Mydata")
             my_cursor=conn.cursor()
             qu = "insert into hospital(Nameoftablets,ref,Dose,NumberofTablets,Lot,Issuedate,ExpDate,DailyDose,Storage,NhsNumber,PatientName,DateofBirth,PatientAddress) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
             data= (
                    self.Nameoftablets.get(), self.ref.get(), self.Dose.get(),
                    self.NumberofTablets.get(),self.Lot.get(), self.Issuedate.get(),
                    self.ExpDate.get(), self.DailyDose.get(), self.Storage.get(),
                    self.NhsNumber.get(), self.PatientName.get(),
                    self.DateOfBirth.get(), self.PatientAddress.get()
            )
             my_cursor.execute(qu,data)
             conn.commit()
             self.fatch_data()    
             conn.close()
             messagebox.showinfo("success","Record has been inserted") 


      def Update_data(self):
          conn=mysql.connector.connect(host="localhost",user="root",password="Sachin@123#123",database="Mydata")
          my_cursor=conn.cursor()
          qu="update hospital set Nameoftablets=%s,Dose=%s,NumberOfTablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,DailyDose=%s,Storage=%s,NhsNumber=%s,PatientName=%s,DateOfBirth=%s,PatientAddress=%s where ref=%s"
          data=(         self.Nameoftablets.get(),self.Dose.get(),
                    self.NumberofTablets.get(), self.Lot.get(), self.Issuedate.get(),
                    self.ExpDate.get(), self.DailyDose.get(), self.Storage.get(),
                    self.NhsNumber.get(), self.PatientName.get(),
                    self.DateOfBirth.get(), self.PatientAddress.get(),self.ref.get(),
              
                    )
          my_cursor.execute(qu,data)
          conn.commit()
          self.fatch_data()
          conn.close()
          messagebox.showerror("success","record has been inserted")


      def fatch_data(self):
         conn=mysql.connector.connect(host="localhost",user="root",password="Sachin@123#123",database="mydata")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from hospital")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.hospital_table.delete(*self.hospital_table.get_children())
             for i in rows:
                 self.hospital_table.insert("",END,values=i)
         conn.commit()
         conn.close()             
      def get_cursor(self,event=""):
          cursor_row=self.hospital_table.focus()
          content=self.hospital_table.item(cursor_row)
          row=content["values"]
          self.Nameoftablets.set(row[0])
          self.ref.set(row[1])
          self.Dose.set(row[2])
          self.NumberofTablets.set(row[3])
          self.Lot.set(row[4])
          self.Issuedate.set(row[5])
          self.ExpDate.set(row[6])
          self.DailyDose.set(row[7])
          self.Storage.set(row[8])
          self.NhsNumber.set(row[9])
          self.PatientName.set(row[10])
          self.DateOfBirth.set(row[11])
          self.PatientAddress.set(row[12])
      def iPrescription(self):
          self.txtPrescription.insert(END,"name of Tablet:\t\t\t"+ self.Nameoftablets.get()+ "\n")
          self.txtPrescription.insert(END,"Refrence NO:\t\t\t"+ self.ref.get()+"\n")
          self.txtPrescription.insert(END,"Dose:\t\t\t"+ self.Dose.get()+"\n")
          self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+ self.NumberofTablets.get()+"\n")
          self.txtPrescription.insert(END,"Lot:\t\t\t"+ self.Lot.get()+"\n")
          self.txtPrescription.insert(END,"Issue date:\t\t\t"+ self.Issuedate.get()+"\n")
          self.txtPrescription.insert(END,"Exp date:\t\t\t"+ self.ExpDate.get()+"\n")
          self.txtPrescription.insert(END,"daily Dose:\t\t\t"+ self.DailyDose.get()+"\n")
          self.txtPrescription.insert(END,"side effect:\t\t\t"+ self.SideEffect.get()+"\n")
          self.txtPrescription.insert(END,"further information :\t\t\t"+ self.FurtherInformation.get()+"\n")
          self.txtPrescription.insert(END,"Blood Pressure:\t\t\t"+ self.BloodPressure.get()+"\n")
          self.txtPrescription.insert(END,"Storage:\t\t\t"+ self.Storage.get()+"\n")
          self.txtPrescription.insert(END,"Patient Id:\t\t\t"+ self.PatientId.get()+"\n")
          self.txtPrescription.insert(END,"Medicatio:\t\t\t"+ self.Medication.get()+"\n")
          self.txtPrescription.insert(END,"NHS Number:\t\t\t"+ self.NhsNumber.get()+"\n")
          self.txtPrescription.insert(END,"Patient Name:\t\t\t"+ self.PatientName.get()+"\n")
          self.txtPrescription.insert(END,"Date of Birth:\t\t\t"+ self.DateOfBirth.get()+"\n")
          self.txtPrescription.insert(END,"Patient Address:\t\t\t"+ self.PatientAddress.get()+"\n")
      
      def delete(self):
         if self.Nameoftablets.get()=="" or self.ref.get()=="":
             messagebox.showerror("Error","All fields are required")
         else:
             conn=mysql.connector.connect(host="localhost",user="root",password="Sachin@123#123",database="Mydata")
             my_cursor=conn.cursor()
             qu = "delete from hospital where ref=%s"
             Value=(self.ref.get(),)

             my_cursor.execute(qu,Value)
             conn.commit()
             self.fatch_data()
             conn.close()
             messagebox.showinfo("success","record has been delete")


      def clear(self):
          self.Nameoftablets.set("")
          self.ref.set("")
          self.Dose.set("")
          self.NumberofTablets.set("")
          self.Lot.set("")
          self.Issuedate.set("")
          self.ExpDate.set("")
          self.DailyDose.set("")
          self.SideEffect.set("")
          self.FurtherInformation.set("")
          self.Storage.set("")
          self.Medication.set("")
          self.PatientId.set("")
          self.NhsNumber.set("")
          self.PatientName.set("")
          self.DateOfBirth.set("")
          self.PatientAddress.set("")
          self.txtPrescription.delete.set("1.0",END)

      def Exit(self):
          Exit=messagebox.askyesno("Hospital management system","confirm you want to exit")
          if Exit>0:
              root.destroy()
              return

       
         
if __name__=="__main__":
    root=Tk()
    ob=Hospital(root)
    root.mainloop()