#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import random
from tkinter import *
from tkinter import messagebox
p=[]
for x in range(4):
    r=random.randint(0,9)
    p.append(str(r))
db={'2094639698':"OBINNA EZEOBI MARTINS", '1234567890':'CHIMEREMEZE','2024327982':'Hamber Thomas'} 
pin=p[0]+p[1]+p[2]+p[3]               
print("This is a new account, make deposit of NGN500 or more before you can withdraw")
print("your pin is ",pin)
chance=3
bal=0

pin = pin
enterpin=input('enter your pin: ')
login=True
while login is True:
    if enterpin==pin:
        print('Choose what you want to do: ')
        print('enter 1 to check balance')
        print('enter 2 to make withrawal')
        print('enter 3 to make deposit')
        print("enter 4 to make transfer")
        reply=int(input())
        if reply==1:
            print(f"your balance is {bal}")
            print('do you want to perform another transaction?')
            response=input("Enter yes or no: ")
            if response.lower()=='yes':
                enterpin=input('enter your pin: ')
                login = True
            elif response.lower()=='no': 
                print("Thank you for banking with us")
                break
            else:
                print("Invali Entry. Please enter yes or no")
                response=input()
                
                if response.lower()=='yes':
                    enterpin=input('enter your pin: ')
                    login = True
                elif response.lower()=='no': 
                    print("Thank you for banking with us")
                    break
        elif reply==2:
            amount=int(input("Enter amount to withdraw: "))
            if amount<500 and bal>amount :
                print("amount too low")
                print('do you want to perform another transaction?')
                response=input("Enter yes or no: ")
                if response.lower()=='yes':
                    enterpin=input('enter your pin: ')
                    login = True
                elif response.lower()=='no': 
                    print("Thank you for banking with us")
                    break
                else:
                    print("Invali Entry. Please enter yes or no")
                    response=input()
                
                    if response.lower()=='yes':
                        enterpin=input('enter your pin: ')
                        login = True
                    elif response.lower()=='no': 
                        print("Thank you for banking with us")
                        break
            elif amount>bal:
                
                print("amount higher than account balance")
                print('do you want to perform another transaction?')
                response=input("Enter yes or no: ")
                if response.lower()=='yes':
                    enterpin=input('enter your pin: ')
                    login = True
                elif response.lower()=='no': 
                    print("Thank you for banking with us")
                    break
                else:
                    print("Invali Entry. Please enter yes or no")
                    response=input()

                    if response.lower()=='yes':
                        enterpin=input('enter your pin: ')
                        login = True
                    elif response.lower()=='no': 
                        print("Thank you for banking with us")
                        break  
            elif amount>=500 and bal>=amount and amount%500!=0 :
                print("you can only withdraw in multiples of 500")
                print('do you want to perform another transaction?')
                response=input("Enter yes or no: ")
                if response.lower()=='yes':
                    enterpin=input('enter your pin: ')
                    login = True
                elif response.lower()=='no': 
                    print("Thank you for banking with us")
                    break 
                else:
                    print("Invali Entry. Please enter yes or no")
                    response=input()

                    if response.lower()=='yes':
                        enterpin=input('enter your pin: ')
                        login = True
                    elif response.lower()=='no': 
                        print("Thank you for banking with us")
                        break    
            elif bal<500:
                print("Insufficient fund")
                print('do you want to perform another transaction?')
                response=input("Enter yes or no: ")
                if response.lower()=='yes':
                    enterpin=input('enter your pin: ')
                    login = True
                elif response.lower()=='no': 
                    print("Thank you for banking with us")
                    break
                else:
                    print("Invali Entry. Please enter yes or no")
                    response=input()

                    if response.lower()=='yes':
                        enterpin=input('enter your pin: ')
                        login = True
                    elif response.lower()=='no': 
                        print("Thank you for banking with us")
                        break    
            elif bal>amount and amount%500==0:    
                bal=bal-amount
                print("Take your cash")
                time.sleep(3)
                print('do you want to perform another transaction?')
                response=input("Enter yes or no: ")
                if response.lower()=='yes':
                    enterpin=input('enter your pin: ')
                    login = True
                elif response.lower()=='no': 
                    print("Thank you for banking with us")
                    break
                else:
                    print("Invali Entry. Please enter yes or no")
                    response=input()

                    if response.lower()=='yes':
                        enterpin=input('enter your pin: ')
                        login = True
                    elif response.lower()=='no': 
                        print("Thank you for banking with us")
                        break
            else:
                print("Insufficient Fund")
                print('do you want to perform another transaction?')
                response=input("Enter yes or no: ")
                if response.lower()=='yes':
                    enterpin=input('enter your pin: ')
                    login = True
                elif response.lower()=='no': 
                    print("Thank you for banking with us")
                    break
                else:
                    print("Invali Entry. Please enter yes or no")
                    response=input("Enter yes or no:" )                
                    if response.lower()=='yes':
                        enterpin=input('enter your pin: ')
                        login = True
                    elif response.lower()=='no': 
                        print("Thank you for banking with us")
                        break
        elif reply==3:
            amount=int(input("Enter amount to deposit: "))
            bal=bal+amount    
            print('do you want to perform another transaction?')
            response=input("Enter yes or no: ")
            if response.lower()=='yes':
                enterpin=input('enter your pin: ')
                login = True
            elif response.lower()=='no': 
                print("Thank you for banking with us")
                break
            else:
                print("Invali Entry. Please enter yes or no")
                response=input()                
                if response.lower()=='yes':
                    enterpin=input('enter your pin: ')
                    login = True
                elif response.lower()=='no': 
                    print("Thank you for banking with us")
                    break
        elif reply==4:            
            number=input("Enter Destination Account Number: ")
            #for num in db:
            if number in db:
                print(f"You are about to make transfer to {db[number]}")
                amount=int(input("Enter amount to transfer: "))
            else:
                print("Invalid Account Number. Try again later, Thank you.")
                break
                    
            if amount>bal:
                print("Insufficient Fund")
            else:    
                bal=bal-amount
                print("Wait while your transaction is processing...")
                time.sleep(3)
                #root=Tk()
                messagebox.showinfo("Status","Transaction Completed")
                #root.mainloop()
            print('do you want to perform another transaction?')
            response=input("Enter yes or no: ")
            if response.lower()=='yes':
                enterpin=input('enter your pin: ')
                login = True
            elif response.lower()=='no': 
                print("Thank you for banking with us")
                break
            else:
                print("Invali Entry. Please enter yes or no")
                response=input()
                
                if response.lower()=='yes':
                    enterpin=input('enter your pin: ')
                    login = True
                elif response.lower()=='no': 
                    print("Thank you for banking with us")
                    break
    else:
        chance=chance-1
        if chance>0:
            print(f"Invalid pin. You have {chance} more tries")
            enterpin=input('enter your pin: ')
        else: 
            print("No more tries. Thank you")
            break

                
            
            
        
    
        
            
            
        


# In[4]:





# In[3]:



from tkinter import *
from tkinter import messagebox
import random
import time
name=input("Please Enter Your Full Name: ")
root=Tk()
root.geometry("1400x1000+200+0")
root.configure(background="gainsboro")
frame=Frame(root,width=20,height=25,bd=20,relief=RIDGE,bg="yellow")
frame2=Frame(root,width=1200,height=1050,bd=20,relief=RIDGE,bg="blue")
frame2.grid(row=1,column=0)
frame.grid(row=0,column=0)
ent=Text(frame,height=12,width=60,bd=12,font=('arial',18,'bold'))
ent.tag_config('warning',background='brown')
ent.insert(END,"\t\t Enter Your PIN",'warning')
ent.pack()


p=[]
for x in range(4):
    r=random.randint(0,9)
    p.append(str(r))        
pin=p[0]+p[1]+p[2]+p[3] 

messagebox.showinfo("PIN",f"Welcome {name},\n\n Enter this pin {str(pin)}")
depos=[0]
wid_bal=[0]
amount_wid=[]
def enter_pin(): 
    global pin1
    pin1=ent.get("1.0","end-1c")
    #Check if pin1 you entered is equal to random pin generated
    if pin==pin1:
        ent.delete('1.0',END)
        ent.insert(END,f"{name}\n\n Welcome to Zenith Bank \n\n Click any of the following buttons to perform operation:\n\n 1. WITHDRAW \n\n 2. BALANCE \n\n 3. DEPOSIT")
        global d
        d=ent.get("1.0","end-1c")
    else:
        ent.delete('1.0',END)
        ent.insert(END,"\t\t Invalid Pin. Enter Correct Pin")        
def deposit():
    if pin==pin1:
        num=ent.get("1.0","end-1c")
        if num.isdigit():
            depos.append(int(num))
            messagebox.showinfo("Status",f"Deposit Successful")
            ent.delete("1.0",END)
        else:        
            ent.delete("1.0",END)
            ent.insert(END,"Enter Amount You Want to Deposit and Click on DEPOSIT")                    
    else:
        ent.delete("1.0",END)
        ent.insert(END,"Please Enter PIN") 

def clear():
    screen=ent.get("1.0","end-1c")
    ent.delete("1.0",END)
from PIL import ImageTk, Image
click_wid=[]
def withraw(): 
    num=ent.get("1.0","end-1c")
    if pin==pin1:
        click_widr=0
        click_wid.append(click_widr)
        if num.isdigit():
            amount_wid.append(int(num))
            #from PIL import Image
            img=Image.open(r"C:\files\images.jpg")
            balanc1=sum(depos)-sum(amount_wid)
            if int(num)<=sum(depos) and int(num)>0:
                if sum(depos)>=sum(amount_wid):
                    if int(num)%500==0:
                        ent.delete('1.0',END)
                        messagebox.showinfo("Status",f"Wait Your Transaction is Processing")
                        time.sleep(2)
                        #ent.insert(END,f"\t\t You withdrew {num} succesfully")
                        #time.sleep(2)
                        ent.delete('1.0',END)
                        ent.insert(END,f"\n \t\t Take Your Cash")
                        ent.image_create(END, image=img)
                    else:
                        ent.delete('1.0',END)
                        ent.insert(END,f"\n\n\n\n \t Enter Amount in multiples of 500")
                        amount_wid.pop()        
                else:
                    ent.delete('1.0',END)
                    ent.tag_config('warning',foreground='red')
                    ent.insert(END,'\n\n\n\n \t\t Insufficient Balance','warning')
                    amount_wid.pop()
            elif int(num)==0:
                ent.insert(END,"\n\n\n\n \t\t  You Cannot Withdraw 0")
            else:
                ent.delete('1.0',END)
                ent.tag_config('warning',foreground='red')
                ent.insert(END,'\n\n\n\n \t\t Amount Higher Than Balance','warning')
                amount_wid.pop()
        else:
            ent.delete('1.0',END)
            ent.insert(END,"Enter Amount You Want To Withdraw")
    else:
        ent.delete('1.0',END)
        ent.insert(END,"Please Enter PIN")
def balance():
    if pin==pin1:
        if len(click_wid)>0:
            ent.delete('1.0',END)
            bal=sum(depos)-sum(amount_wid)
            if bal >=0:
                ent.insert(END,f"\n\n\n\n \t\t  Your Balance is {bal}")
            else:
                bal=sum(depos)-sum(amount_wid)+sum(amount_wid)
                ent.insert(END,f"\n\n\n\n \t\t Your Balance is {bal}")
        else:
            ent.delete('1.0',END)
            ent.insert(END,f"\n\n\n\n \t\t Your BAlance is {sum(depos)}")
    else:
        ent.delete("1.0",END)
        ent.insert(END,"Please Enetr PIN")
def dis(n):
    num=ent.get("1.0","end-1c")
    if ent.get("1.0","end-1c").isdigit() or num=="":
        num=ent.get("1.0","end-1c")
        ent.delete("1.0",END)
        ent.insert(END,str(num)+str(n))
    else:
        if num!="":
            ent.delete("1.0",END)
            ent.insert(END,str(n))   
but1=Button(frame2, text='1',padx=87,pady=15,bd=7, font=12,command= lambda:dis(1))
but1.grid(row=1,column=0)
but2=Button(frame2, text='2',padx=87,pady=15,bd=7,font=12,  command= lambda: dis(2))
but2.grid(row=1,column=1)
but3=Button(frame2, text='3',padx=87,pady=15,bd=7, font=12, command=lambda : dis(3))
but3.grid(row=1,column=2)
but4=Button(frame2, text='4',padx=87,pady=15,bd=7, font=12, command=lambda : dis(4))
but4.grid(row=2,column=0)
but5=Button(frame2, text='5',padx=87,pady=15, bd=7,font=12, command=lambda : dis(5))
but5.grid(row=2,column=1)
but6=Button(frame2, text='6',padx=87,pady=15, bd=7,font=12,command=lambda : dis(6))
but6.grid(row=2,column=2)
but7=Button(frame2, text='7',padx=87,pady=15,bd=7, font=12, command=lambda : dis(7))
but7.grid(row=3,column=0)
but8=Button(frame2, text='8',padx=87,pady=15,bd=7, font=12, command=lambda : dis(8))
but8.grid(row=3,column=1)
but9=Button(frame2, text='9',padx=87,pady=15, bd=7,font=12, command=lambda : dis(9))
but9.grid(row=3,column=2)
butclear=Button(frame2, text='DEPOSIT',padx=55,pady=16,bd=10,font=10,fg='brown',  command=deposit)
butclear.grid(row=4,column=0)
butenter=Button(frame2, text='ENTER PIN',fg='blue',padx=50,pady=20,bd=7,font=10, command=enter_pin)
butenter.grid(row=4,column=1)
but0=Button(frame2, text='0',padx=87,pady=15, bd=10,font=12 ,command=lambda : dis(0))
but0.grid(row=4,column=2)
butstart=Button(frame2,text="WITHDRAW \n ",padx=55,pady=13,bd=7,fg='green',font=10, command=withraw)
butstart.grid(row=5,column=0)
butstart=Button(frame2,text="CHECK \n BALANCE",padx=55,pady=13,bd=7, fg='cyan',font=10, command=balance)
butstart.grid(row=5,column=1)
butstart=Button(frame2,text="CLEAR \n ",padx=62,pady=13,bd=7,fg='red',font=10, command=clear)
butstart.grid(row=5,column=2)
root.mainloop() 


# In[ ]:



from tkinter import *
from tkinter import messagebox
import random
import time
name=input("Please Enter Your Full Name: ")
root=Tk()
root.geometry("1400x1000+200+0")
root.configure(background="gainsboro")
frame=Frame(root,width=20,height=25,bd=20,relief=RIDGE,bg="yellow")
frame.grid(row=0,column=0)
frame2=Frame(root,width=1200,height=1050,bd=20,relief=RIDGE,bg="blue")
frame2.grid(row=1,column=0)
frame3=Frame(root,width=90,height=500,bd=20,relief=RIDGE,bg="blue")
frame3.grid(row=0,column=1)
ent=Text(frame,height=12,bg='red',width=60,bd=12,font=('arial',18,'bold'))
ent.insert(END,"\t\t Enter Your PIN")
ent.pack() 

p=[]
for x in range(4):
    r=random.randint(0,9)
    p.append(str(r))        
pin=p[0]+p[1]+p[2]+p[3] 
messagebox.showinfo("PIN",f"Welcome {name},\n\n Enter this pin {str(pin)}")

chances=[]
no_of_trials=[]
def enter_pin(): 
    global pin1
    chance=0
    chances.append(chance)
    a=3-len(chances)
    no_of_trials.append(a)
    pin1=ent.get("1.0","end-1c")
    if pin==pin1:
        ent.delete('1.0',END)
        #ent.tag_config('warning',background='')
        ent.insert(END,f"{name}\n\n Welcome to Zenith Bank  \t\t\t\t\t\t  Withdrawal \n\n\n\n \t\t\t\t\t\t  Deposit \n\n\n \t\t\t\t\t\t  Balance ")
        ent.insert(END,"\n\n\n","warning")
    elif len(chances)>0 and len(chances)<3: 
        ent.delete('1.0',END)
        if a==2:
            ent.insert(END," Invalid Pin. Enter Correct Pin \n\n")
            ent.insert(END,f"You have {a} more chances") 
        else:
            ent.insert(END," Invalid Pin. Enter Correct Pin \n\n")
            ent.insert(END,f"You have {a} more chance") 
    elif len(chances)==3:
        ent.delete('1.0',END)
        ent.insert(END,f"You have 0 chance \n\n")        
        ent.insert(END,f" No more tries. goodbye")
        but1=Button(frame2, text='1',padx=87,pady=15,bd=7, font=12,state=DISABLED,command= lambda:dis(1))
        but1.grid(row=1,column=0)
        but2=Button(frame2, text='2',padx=87,pady=15,bd=7,font=12, state=DISABLED, command= lambda: dis(2))
        but2.grid(row=1,column=1)
        but3=Button(frame2, text='3',padx=87,pady=15,bd=7, font=12,state=DISABLED, command=lambda : dis(3))
        but3.grid(row=1,column=2)
        but4=Button(frame2, text='4',padx=87,pady=15,bd=7, font=12,state=DISABLED, command=lambda : dis(4))
        but4.grid(row=2,column=0)
        but5=Button(frame2, text='5',padx=87,pady=15, bd=7,font=12, state=DISABLED,command=lambda : dis(5))
        but5.grid(row=2,column=1)
        but6=Button(frame2, text='6',padx=87,pady=15, bd=7,font=12,state=DISABLED,command=lambda : dis(6))
        but6.grid(row=2,column=2)
        but7=Button(frame2, text='7',padx=87,pady=15,bd=7, font=12,state=DISABLED, command=lambda : dis(7))
        but7.grid(row=3,column=0)
        but8=Button(frame2, text='8',padx=87,pady=15,bd=7, font=12,state=DISABLED, command=lambda : dis(8))
        but8.grid(row=3,column=1)
        but9=Button(frame2, text='9',padx=87,pady=15, bd=7,font=12, state=DISABLED,command=lambda : dis(9))
        but9.grid(row=3,column=2)
        but0=Button(frame2, text='0',padx=87,pady=15, bd=10,font=12 ,state=DISABLED,command=lambda : dis(0))
        but0.grid(row=4,column=2)   
        butclear=Button(frame2, text='DEPOSIT',padx=55,pady=16,bd=10,font=10,fg='brown', state=DISABLED, command=deposit)
        butclear.grid(row=4,column=0)
        butstart=Button(frame2,text="WITHDRAW \n ",padx=55,pady=13,bd=7,fg='green',font=10,state=DISABLED, command=withraw)
        butstart.grid(row=5,column=0)
        butstart=Button(frame2,text="CHECK \n BALANCE",padx=55,pady=13,bd=7, fg='cyan',font=10, state=DISABLED,command=balance)
        butstart.grid(row=5,column=1)
        butwid=Button(frame3, text='<<< Withdraw',padx=87,pady=15,bd=7,bg='green', font=12,state=DISABLED,command= withraw)
        butwid.grid(row=0,column=0)
        butwid=Button(frame3, text='------------',padx=0,pady=0,bg='yellow',fg='red',bd=1,state=DISABLED, font=12)
        butwid.grid(row=1,column=0)
        buttran=Button(frame3, text='<<< Deposit',padx=87,pady=13,bd=7,font=12, bg='magenta',state=DISABLED, command= deposit)
        buttran.grid(row=2,column=0)
        butwid=Button(frame3, text='------------',padx=0,pady=0,bg='yellow',fg='red',bd=1,state=DISABLED, font=12)
        butwid.grid(row=3,column=0)
        butdepos=Button(frame3, text='<<< Balance',padx=87,pady=11,bd=7, font=12,bg='orange', state=DISABLED,command=balance)
        butdepos.grid(row=4,column=0)

depos=[0]        
def deposit():
    if pin==pin1:
        num=ent.get("1.0","end-1c")
        if num.isdigit():
            depos.append(int(num))
            messagebox.showinfo("Status",f"Deposit Successful")
            ent.delete("1.0",END)
        else:        
            ent.delete("1.0",END)
            ent.tag_config('warning',foreground='white')
            ent.insert(END,"Enter Amount You Want to Deposit and Click on DEPOSIT",'warning')                    
    else:
        ent.delete("1.0",END)
        ent.insert(END,"Please Enter PIN") 

def clear():
    screen=ent.get("1.0","end-1c")
    ent.delete("1.0",END)

amount_wid=[0]
click_wid=[]
def withraw(): 
    num=ent.get("1.0","end-1c")
    if pin==pin1:
        click_widr=0
        click_wid.append(click_widr)
        if num.isdigit():
            amount_wid.append(int(num))

            balanc1=sum(depos)-sum(amount_wid)
            
            
            if int(num)<=sum(depos) and int(num)>0:
                if sum(depos)>=sum(amount_wid):
                    if int(num)%500==0:
                        ent.delete('1.0',END)
                        messagebox.showinfo("Status",f"Wait Your Transaction is Processing")
                        time.sleep(2)
                        ent.tag_config('warning',foreground='green',background='white')
                        ent.insert(END,f"\n\n \t\t")
                        ent.insert(END,f"You withdrew {num} succesfully",'warning')
                        #ent.tag_config('warning',foreground='white')
                        ent.insert(END,f"\n\n\n\n \t\t")
                        ent.insert(END,"Take Your Cash")
                        
                    else:
                        ent.delete('1.0',END)
                        ent.insert(END,f"\n\n\n\n \t Enter Amount in multiples of 500")
                        amount_wid.pop() 
                else:
                    ent.delete('1.0',END)
                    ent.tag_config('warning',foreground='red')
                    ent.insert(END,'\n\n\n\n \t\t Insufficient Balance','warning')
                    amount_wid.pop()
            elif sum(depos)==0 and int(num)>0:
                ent.delete('1.0',END)
                ent.insert(END,f"\n\n\n\n \t Your Account Is Empty. Please Deposit Some Money")
                amount_wid.pop()         
            elif int(num)==0:
                ent.delete('1.0',END)
                ent.insert(END,"\n\n\n\n \t\t  You cannot Withdraw 0")
            else:
                ent.delete('1.0',END)
                ent.tag_config('warning',foreground='red')
                ent.insert(END,'\n\n\n\n \t\t Amount Higher Than Balance','warning')
                amount_wid.pop()
            
                
        else:
            ent.delete('1.0',END)
            ent.tag_config('warning',foreground='white')
            ent.insert(END,"Enter Amount You Want To Withdraw and Click On Withdraw",'warning')
    else:
        ent.delete('1.0',END)
        ent.insert(END,"Please Enter PIN")
def balance():
    if pin==pin1:
        if len(click_wid)>0:
            ent.delete('1.0',END)
            bal=sum(depos)-sum(amount_wid)
            if bal >=0:
                ent.insert(END,f"\n\n\n\n \t\t  Your Balance is {bal}")
            else:
                bal=sum(depos)-sum(amount_wid)+sum(amount_wid)
                ent.insert(END,f"\n\n\n\n \t\t Your Balance is {bal}")
        else:
            ent.delete('1.0',END)
            ent.insert(END,f"\n\n\n\n \t\t Your Balance is {sum(depos)}")
    else:
        ent.delete("1.0",END)
        ent.insert(END,"Please Enter PIN")
def dis(n):
    num=ent.get("1.0","end-1c")
    if ent.get("1.0","end-1c").isdigit() or num=="":
        num=ent.get("1.0","end-1c")
        ent.delete("1.0",END)
        ent.insert(END,str(num)+str(n))
    else:
        if num!="":
            ent.delete("1.0",END)
            ent.insert(END,str(n)) 
butwid=Button(frame3, text='<<< Withdraw',padx=87,pady=15,bd=7,bg='green', font=12,command= withraw)
butwid.grid(row=0,column=0)
butwid=Button(frame3, text='------------',padx=0,pady=0,bg='yellow',fg='red',bd=1,state=DISABLED, font=12)
butwid.grid(row=1,column=0)
buttran=Button(frame3, text='<<< Deposit',padx=87,pady=13,bd=7,font=12, bg='magenta', command= deposit)
buttran.grid(row=2,column=0)
butwid=Button(frame3, text='------------',padx=0,pady=0,bg='yellow',fg='red',bd=1,state=DISABLED, font=12)
butwid.grid(row=3,column=0)
butdepos=Button(frame3, text='<<< Balance',padx=87,pady=11,bd=7, font=12,bg='orange', command=balance)
butdepos.grid(row=4,column=0) 
but1=Button(frame2, text='1',padx=87,pady=15,bd=7, font=12,command= lambda:dis(1))
but1.grid(row=1,column=0)
but2=Button(frame2, text='2',padx=87,pady=15,bd=7,font=12,  command= lambda: dis(2))
but2.grid(row=1,column=1)
but3=Button(frame2, text='3',padx=87,pady=15,bd=7, font=12, command=lambda : dis(3))
but3.grid(row=1,column=2)
but4=Button(frame2, text='4',padx=87,pady=15,bd=7, font=12, command=lambda : dis(4))
but4.grid(row=2,column=0)
but5=Button(frame2, text='5',padx=87,pady=15, bd=7,font=12, command=lambda : dis(5))
but5.grid(row=2,column=1)
but6=Button(frame2, text='6',padx=87,pady=15, bd=7,font=12,command=lambda : dis(6))
but6.grid(row=2,column=2)
but7=Button(frame2, text='7',padx=87,pady=15,bd=7, font=12, command=lambda : dis(7))
but7.grid(row=3,column=0)
but8=Button(frame2, text='8',padx=87,pady=15,bd=7, font=12, command=lambda : dis(8))
but8.grid(row=3,column=1)
but9=Button(frame2, text='9',padx=87,pady=15, bd=7,font=12, command=lambda : dis(9))
but9.grid(row=3,column=2)
butclear=Button(frame2, text='DEPOSIT',padx=55,pady=16,bd=10,font=10,fg='brown',  command=deposit)
butclear.grid(row=4,column=0)
butenter=Button(frame2, text='ENTER PIN',fg='blue',padx=50,pady=20,bd=7,font=10, command=enter_pin)
butenter.grid(row=4,column=1)
but0=Button(frame2, text='0',padx=87,pady=15, bd=10,font=12 ,command=lambda : dis(0))
but0.grid(row=4,column=2)
butstart=Button(frame2,text="WITHDRAW \n ",padx=55,pady=13,bd=7,fg='green',font=10, command=withraw)
butstart.grid(row=5,column=0)
butstart=Button(frame2,text="CHECK \n BALANCE",padx=55,pady=13,bd=7, fg='cyan',font=10, command=balance)
butstart.grid(row=5,column=1)
butstart=Button(frame2,text="CLEAR \n ",padx=62,pady=13,bd=7,fg='red',font=10, command=clear)
butstart.grid(row=5,column=2)
root.mainloop() 


# In[14]:


from tkinter import *
from tkinter import messagebox
root=Tk()
ent=Entry(root, width=80,justify=LEFT,bd=5)
ent.grid(row=0,column=0)


chance=3
bal=0
def start():
    ent.delete(0,END)
    import time
    import random
    
    p=[]
    for x in range(4):
        r=random.randint(0,9)
        p.append(str(r)) 
        
    pin=p[0]+p[1]+p[2]+p[3]
    ent.insert(0,str(pin))
    pintext=StringVar()
    label=Label(root,textvariable=pintext,font=13)
    label.grid(row=6,column=0)
    pintext.set(f"your pin {pin} is")       
def enter():  
    pin=ent.get() 
    ent.delete(0,END)
    ent.insert(0,"enter pin")
def withd():
    pin2=ent.get()
    if pin==pin2:
        ent.insert(0,"Enter Amount to withdraw")
        amount=ent.get()
        messagebox.showinfo('Showinfo',f'you have withdrawn str{amount}')        
def dis(n):
    g=ent.get()
    ent.delete(0,END)
    ent.insert(0,str(g)+str(n))
def clear():
    ent.delete(0,END)
but1=Button(root, text='1',padx=40,pady=2, command=lambda : dis(1))
but1.grid(row=1,column=0)
but2=Button(root, text='2',padx=40,pady=2, command=lambda : dis(2))
but2.grid(row=1,column=1)
but3=Button(root, text='3',padx=40,pady=2, command=lambda : dis(3))
but3.grid(row=1,column=2)
but4=Button(root, text='4',padx=40,pady=2, command=lambda : dis(4))
but4.grid(row=2,column=0)
but5=Button(root, text='5',padx=40,pady=2, command=lambda : dis(5))
but5.grid(row=2,column=1)
but6=Button(root, text='6',padx=40,pady=2, command=lambda : dis(6))
but6.grid(row=2,column=2)
but7=Button(root, text='7',padx=40,pady=2, command=lambda : dis(7))
but7.grid(row=3,column=0)
but8=Button(root, text='8',padx=40,pady=2, command=lambda : dis(8))
but8.grid(row=3,column=1)
but9=Button(root, text='9',padx=40,pady=2, command=lambda : dis(9))
but9.grid(row=3,column=2)
butclear=Button(root, text='Clear',padx=40,pady=2, command=clear)
butclear.grid(row=4,column=0)
butenter=Button(root, text='Enter',fg='green',padx=40,pady=2,command=enter)
butenter.grid(row=4,column=1)
but0=Button(root, text='0',padx=40,pady=2, command=lambda : dis(0))
but0.grid(row=4,column=2)
butstart=Button(root,text="Start ATM",padx=40,pady=2,command=start)
butstart.grid(row=5,column=0)
butstar=Button(root,text="withdraw",padx=40,pady=2,command=withd)
butstar.grid(row=5,column=1)

root.mainloop()


# In[ ]:





# In[ ]:




