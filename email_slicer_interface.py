import email
from tkinter import *
root = Tk()
root.title('Mortgage Calculator')

def button_slice():
    email = email_box.get()

    if '@' in email:
        username = email[:email.index('@')]
        domain = email[email.index('@') + 1:]
        username_box.insert(0, username)
        domain_box.insert(0, domain)
    else:
        email_box.delete(0, END)
        email_box.insert(0, str('Not a valid email!'))

def button_reset():
    email_box.delete(0, END)
    username_box.delete(0, END)
    domain_box.delete(0, END)

# Define entry boxes
email_box = Entry(root, width=35, borderwidth=5)
username_box = Entry(root, width=35, borderwidth=5)
domain_box = Entry(root, width=35, borderwidth=5)


# Define labels
email_label = Label(root, text='Email address')
username_label = Label(root, text='Username')
domain_label = Label(root, text='Domain')


# Define buttons
but_slice = Button(root, text='Slice Email!', padx=91, pady=20, command=button_slice)
but_reset = Button(root, text='Reset', padx=91, pady=20, command=button_reset)

# Layout of entry boxes
email_box.grid(row=0, column=1)
username_box.grid(row=2, column=1)
domain_box.grid(row=3, column=1)


# Layout of labels
email_label.grid(row=0, column=0)
username_label.grid(row=2, column=0)
domain_label.grid(row=3, column=0)

# Layout of buttons
but_slice.grid(row=1, column=1)
but_reset.grid(row=1, column=0)

root.mainloop()