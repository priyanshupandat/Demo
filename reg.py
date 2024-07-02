import tkinter as tk
root = tk.Tk()
root.title("Registration Page")

label=tk.Label(root,text="Enter Name")
label.pack()
entry=tk.Entry(root)
entry.pack()

label1=tk.Label(root,text="Enter Phone number")
label1.pack()
entry1=tk.Entry(root)
entry1.pack()

label2=tk.Label(root,text="Enter e-mail")
label2.pack()
entry2=tk.Entry(root)
entry2.pack()

label3=tk.Label(root,text="Enter OTP")
label3.pack()
entry3=tk.Entry(root)
entry3.pack()

sub=tk.Button(root,text='submit',background='green',fg='white')
sub.pack(side=tk.RIGHT,pady=200,padx=200,ipady=10,ipadx=10)

b1=tk.Button(root,text='delet',background='red',fg='white')
b1.pack(side=tk.LEFT,pady=200,padx=200,ipady=10,ipadx=10)

root.mainloop
