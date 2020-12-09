import tkinter as tk
from tkinter import ttk

from aes import start_encrypt_file
from database import *
from passwordGenerator import *

# Основное окно
auth_window = tk.Tk()
auth_window.configure(bg='#36393f')

# Стили программы
style = ttk.Style()
style.theme_use('clam')

style.configure('common.TFrame',
                background='#36393f')

style.configure('common.TButton',
                background='#7289da',
                foreground='#ffffff',
                borderwidth=0,
                focuscolor='none',
                font='bahnschrift 12')
style.map('common.TButton',
          background=[('active', '#677bc4')])

style.configure('TCheckbutton',
                background='#36393f',
                focuscolor='none')
style.map('TCheckbutton',
          background=[('active', '#36393f')])

style.configure('toolbar.TFrame',
                background='#2f3136')

style.configure('toolbar.TButton',
                background='#2f3136',
                foreground='#888a91',
                width=12,
                borderwidth=0,
                focuscolor='none',
                font='bahnschrift 12',
                anchor='w')
style.map('toolbar.TButton',
          background=[('active', '#34373c'), ('disabled', '#27292d')],
          foreground=[('active', '#bcddde')])

style.configure('search.TButton',
                background='#36393f',
                foreground='#888a91',
                borderwidth=0,
                focuscolor='none',
                font='bahnschrift 10')
style.map('search.TButton',
          background=[('active', '#36393f')],
          foreground=[('active', '#bcddde')])

style.configure('name.TLabel',
                background='#36393f',
                foreground='#888a91',
                font='bahnschrift 16')
style.configure('TLabel',
                background='#36393f',
                foreground='#888a91',
                font='bahnschrift 10')

style.configure('TEntry',
                background='#36393f',
                foreground='#ffffff',
                fieldbackground='#313339',
                bordercolor='#222428',
                lightcolor='#222428',
                insertcolor='#ffffff',
                font='bahnschrift 10')
style.map('TEntry',
          lightcolor=[('focus', '#7289da')])

style.configure('my.Treeview',
                background='#36393f',
                foreground='#888a91',
                fieldbackground='#36393f',
                font='bahnschrift 11')
style.configure('my.Treeview.Heading',
                background='#36393f',
                foreground='#bcddde',
                fieldbackground='#36393f',
                bordercolor='#36393f',
                lightcolor='#36393f',
                darkcolor='#36393f',
                font='bahnschrift 12')
style.map('my.Treeview',
          background=[('selected', '#2f3136')],
          foreground=[('selected', '#bcddde')])
style.map('my.Treeview.Heading',
          background=[('active', '#36393f')])
style.layout('my.Treeview', [('my.Treeview.treearea', {'sticky': 'nswe'})])

global profile_login_verify
global profile_password_verify
global label_auth


def start_auth_window():
    auth_window.geometry('480x250+500+200')
    auth_window.title('Password manager')
    auth_window.resizable(False, False)

    global profile_login_verify
    global profile_password_verify
    profile_login_verify = tk.StringVar()
    profile_password_verify = tk.StringVar()

    void_label = ttk.Label()
    void_label.pack()

    name_frame = ttk.Frame(style='common.TFrame')
    name_frame.pack(fill='x')

    name_label = ttk.Label(name_frame,
                           text='Password Manager',
                           style='name.TLabel')
    name_label.pack(ipadx=100)

    login_label = ttk.Label(text='Login')
    login_label.place(x=10, y=70)
    login_enter = ttk.Entry(textvariable=profile_login_verify,
                            width=60)
    login_enter.place(x=85, y=70)

    pass_label = ttk.Label(text='Password')
    pass_label.place(x=10, y=100)
    pass_enter = ttk.Entry(textvariable=profile_password_verify,
                           width=60,
                           show='*')
    pass_enter.place(x=85, y=100)

    global label_auth
    label_auth = ttk.Label(text='')
    label_auth.place(x=85, y=121)

    login_btn = ttk.Button(text='Login',
                           command=authorization,
                           style='common.TButton')
    login_btn.place(x=85, y=140)

    register_btn = ttk.Button(text='Create profile',
                              command=start_register_w,
                              style='common.TButton', width=14)
    register_btn.place(x=199, y=140)

    close_btn = ttk.Button(text='Exit',
                           command=auth_window.destroy,
                           style='common.TButton')
    close_btn.place(x=340, y=140)

    auth_window.mainloop()


def authorization():
    if profile_login_verify.get() and profile_password_verify.get() != '':
        login_info = profile_login_verify.get()
        password_info = profile_password_verify.get()
        user_info = (login_info, password_info)
        if login_user(user_info) == 0:
            start_main_w(login_info)
        else:
            label_auth.configure(text='Login or password is incorrect')
    else:
        label_auth.configure(text='Input fields are empty!')


global register_window
global profile_login_for_register
global profile_password_for_register
global label_reg


def start_register_w():
    global register_window
    register_window = tk.Toplevel(auth_window)
    register_window.configure(bg='#36393f')
    register_window.geometry('480x250+500+200')
    register_window.title('Register')
    register_window.resizable(False, False)

    global profile_login_for_register
    global profile_password_for_register
    profile_login_for_register = tk.StringVar()
    profile_password_for_register = tk.StringVar()

    void_label = ttk.Label(register_window)
    void_label.pack()

    name_frame = ttk.Frame(register_window, style='common.TFrame')
    name_frame.pack(fill='x')

    name_label = ttk.Label(name_frame,
                           text='Profile creation',
                           style='name.TLabel')
    name_label.pack(ipadx=100)

    login_label = ttk.Label(register_window,
                            text='Login*')
    login_label.place(x=10, y=70)
    login_enter = ttk.Entry(register_window,
                            textvariable=profile_login_for_register,
                            width=60)
    login_enter.place(x=85, y=70)

    pass_label = ttk.Label(register_window,
                           text='Password*')
    pass_label.place(x=10, y=100)
    pass_enter = ttk.Entry(register_window,
                           textvariable=profile_password_for_register,
                           show='*',
                           width=60)
    pass_enter.place(x=85, y=100)

    global label_reg
    label_reg = ttk.Label(register_window,
                          text='')
    label_reg.place(x=85, y=121)

    register_btn = ttk.Button(register_window,
                              text='Register',
                              command=register_user,
                              style='common.TButton')
    register_btn.place(x=85, y=140)

    close_btn = ttk.Button(register_window,
                           text='Close',
                           command=register_window.destroy,
                           style='common.TButton')
    close_btn.place(x=199, y=140)

    register_window.grab_set()
    register_window.focus_set()


def register_user():
    if profile_login_for_register.get() and profile_password_for_register.get() != '':
        login_info = profile_login_for_register.get()
        password_info = profile_password_for_register.get()
        user_info = (login_info, password_info)
        if insert_user_to_users_table(user_info) is None:
            label_reg.configure(text='Registration failed. User exists')
        else:
            create_login_table(login_info)
            label_reg.configure(text='Registration completed')
    else:
        label_reg.configure(text='Input fields are empty!')


global main_window
global btn_edit
global btn_change_passwords
global entry_search_by_service
global tree
global inf_label


def start_main_w(login_info):
    global main_window
    main_window = tk.Toplevel(auth_window)
    main_window.configure(bg='#36393f')
    main_window.geometry('861x380')
    main_window.title('Password manager: ' + login_info)
    main_window.resizable(False, False)

    global tree
    tree = ttk.Treeview(main_window,
                        columns=('ID', 'Service', 'Login', 'E-mail', 'Password'),
                        height=15,
                        show='headings',
                        style='my.Treeview')
    tree.column('ID',
                minwidt=0, width=0,
                anchor=tk.CENTER)
    tree.column('Service',
                width=200,
                anchor=tk.CENTER)
    tree.column('Login',
                width=150,
                anchor=tk.CENTER)
    tree.column('E-mail',
                width=200,
                anchor=tk.CENTER)
    tree.column('Password',
                width=200,
                anchor=tk.CENTER)
    tree.heading('ID',
                 text='')
    tree.heading('Service',
                 text='Service')
    tree.heading('Login',
                 text='Login')
    tree.heading('E-mail',
                 text='E-mail')
    tree.heading('Password',
                 text='Password')
    tree.place(x=110, y=25)
    tree.bind('<Button-3>', click_to_clipboard)
    tree.bind('<Button-1>', on_edit)

    toolbar = ttk.Frame(main_window,
                        style='toolbar.TFrame')
    toolbar.pack(side=tk.LEFT, fill='y')

    btn_add = ttk.Button(toolbar,
                         text='Add',
                         command=start_add_w,
                         style='toolbar.TButton')
    btn_add.pack()

    global btn_edit
    btn_edit = ttk.Button(toolbar,
                          text='Edit',
                          command=start_edit_w,
                          state=tk.DISABLED,
                          style='toolbar.TButton')
    btn_edit.pack()

    tree.bind('<Double-1>', double_click_edit)

    btn_del = ttk.Button(toolbar,
                         text='Delete',
                         command=delete_one_data,
                         style='toolbar.TButton')
    btn_del.bind('<Button-1>', lambda event: disable_edit(), add='+')
    btn_del.pack()

    btn_duplicate_passwords = ttk.Button(toolbar,
                                         text='Find duplicate \npasswords',
                                         command=search_duplicate_passwords,
                                         style='toolbar.TButton')
    btn_duplicate_passwords.bind('<Button-1>', lambda event: disable_edit())
    btn_duplicate_passwords.pack()

    btn_weak_passwords = ttk.Button(toolbar,
                                    text='Find weak \npasswords',
                                    command=search_weak_password,
                                    style='toolbar.TButton')
    btn_weak_passwords.bind('<Button-1>', lambda event: disable_edit())
    btn_weak_passwords.pack()

    global btn_change_passwords
    btn_change_passwords = ttk.Button(toolbar,
                                      text='Change found \npasswords',
                                      command=change_find_passwords,
                                      state=tk.DISABLED,
                                      style='toolbar.TButton')
    btn_change_passwords.bind('<Button-1>', lambda event: disable_edit())
    btn_change_passwords.pack()

    btn_reset = ttk.Button(toolbar,
                           text='Reset filters',
                           command=reset_filters,
                           style='toolbar.TButton')
    btn_reset.bind('<Button-1>', lambda event: disable_edit())
    btn_reset.pack()

    btn_change_user = ttk.Button(toolbar,
                                 text='Change profile',
                                 style='toolbar.TButton')
    btn_change_user.pack()
    btn_change_user.bind('<Button-1>', exit_profile)

    btn_exit = ttk.Button(toolbar,
                          text='Exit',
                          command=auth_window.destroy,
                          style='toolbar.TButton')
    btn_exit.pack()

    global entry_search_by_service
    entry_search_by_service = ttk.Entry(main_window)
    entry_search_by_service.insert(0, 'Search by service...')
    entry_search_by_service.place(x=120, y=3)

    btn_search = ttk.Button(main_window,
                            text='Search',
                            style='search.TButton')
    btn_search.bind('<Button-1>', lambda event: search_by_service())
    btn_search.bind('<Button-1>', lambda event: disable_edit(), add='+')
    btn_search.place(x=250, y=2)

    btn_clear = ttk.Button(main_window,
                           text='Clear',
                           style='search.TButton')
    btn_clear.bind('<Button-1>', lambda event: entry_search_by_service.delete(0, tk.END))
    btn_clear.bind('<Button-1>', lambda event: search_by_service(), add='+')
    btn_clear.bind('<Button-1>', lambda event: disable_edit(), add='+')
    btn_clear.bind('<Button-1>', lambda event: disable_change(), add='+')
    btn_clear.place(x=315, y=2)

    view_data()

    global inf_label
    inf_label = ttk.Label(main_window, text='')
    inf_label.place(x=123, y=355)

    main_window.focus_set()
    main_window.grab_set()
    # screen.withdraw()


global entry_service
global entry_login
global entry_email
global entry_pass


def start_add_w():
    add_window = tk.Toplevel(main_window)
    add_window.configure(bg='#36393f')
    add_window.geometry('390x300')
    add_window.title('Add')
    add_window.resizable(False, False)

    global entry_service
    global entry_login
    global entry_email
    global entry_pass

    label_service = ttk.Label(add_window,
                              text='Service')
    label_service.place(x=10, y=10)
    entry_service = ttk.Entry(add_window)
    entry_service.place(x=13, y=32, width=365)

    label_login = ttk.Label(add_window,
                            text='Login')
    label_login.place(x=10, y=60)
    entry_login = ttk.Entry(add_window)
    entry_login.place(x=13, y=82, width=365)

    label_email = ttk.Label(add_window,
                            text='E-mail')
    label_email.place(x=10, y=110)
    entry_email = ttk.Entry(add_window)
    entry_email.place(x=13, y=132, width=365)

    label_pass = ttk.Label(add_window,
                           text='Password')
    label_pass.place(x=10, y=160)
    entry_pass = ttk.Entry(add_window)
    entry_pass.place(x=13, y=182, width=365)

    btn_add = ttk.Button(add_window,
                         text='Add',
                         width=10,
                         command=add_data,
                         style='common.TButton')
    btn_add.bind('<Button-1>', lambda event: disable_edit())
    btn_add.place(x=13, y=220)

    btn_generator = ttk.Button(add_window,
                               text='Generate password',
                               width=16,
                               style='common.TButton')
    btn_generator.bind('<Button-1>', lambda event: start_generator_w(add_window))
    btn_generator.place(x=118, y=220)

    btn_cancel = ttk.Button(add_window,
                            text='Close',
                            width=10,
                            command=add_window.destroy,
                            style='common.TButton')
    btn_cancel.place(x=277, y=220)

    add_window.focus_set()
    add_window.grab_set()


def start_edit_w():
    edit_window = tk.Toplevel(main_window)
    edit_window.configure(bg='#36393f')
    edit_window.geometry('390x300')
    edit_window.title('Edit')
    edit_window.resizable(False, False)

    global entry_service
    global entry_login
    global entry_email
    global entry_pass

    data = get_one_data()

    label_service = ttk.Label(edit_window,
                              text='Service')
    label_service.place(x=10, y=10)
    entry_service = ttk.Entry(edit_window)
    entry_service.insert(0, (data[0][1]))
    entry_service.place(x=13, y=32, width=365)

    label_login = ttk.Label(edit_window,
                            text='Login')
    label_login.place(x=10, y=60)
    entry_login = ttk.Entry(edit_window)
    entry_login.insert(0, (data[0][2]))
    entry_login.place(x=13, y=82, width=365)

    label_email = ttk.Label(edit_window,
                            text='E-mail')
    label_email.place(x=10, y=110)
    entry_email = ttk.Entry(edit_window)
    entry_email.insert(0, (data[0][3]))
    entry_email.place(x=13, y=132, width=365)

    label_pass = ttk.Label(edit_window,
                           text='Password')
    label_pass.place(x=10, y=160)
    entry_pass = ttk.Entry(edit_window)
    entry_pass.insert(0, (data[0][4]))
    entry_pass.place(x=13, y=182, width=365)

    btn_add = ttk.Button(edit_window,
                         text='Confirm',
                         width=10,
                         style='common.TButton')
    btn_add.bind('<Button-1>', lambda event: update_data())
    btn_add.bind('<Button-1>', lambda event: disable_edit(), add='+')
    btn_add.bind('<Button-1>', lambda event: edit_window.destroy(), add='+')
    btn_add.place(x=13, y=220)

    btn_generator = ttk.Button(edit_window,
                               text='Generate password',
                               width=16,
                               style='common.TButton')
    btn_generator.bind('<Button-1>', lambda event: start_generator_w(edit_window))
    btn_generator.place(x=118, y=220)

    btn_cancel = ttk.Button(edit_window,
                            text='Close',
                            width=10,
                            command=edit_window.destroy,
                            style='common.TButton')
    btn_cancel.place(x=277, y=220)

    edit_window.focus_set()
    edit_window.grab_set()


def on_edit(event):
    global btn_edit
    row = (tree.identify_row(event.y))
    if row != "":
        btn_edit['state'] = 'normal'


def disable_edit():
    btn_edit['state'] = 'disabled'


def double_click_edit(event):
    row = (tree.identify_row(event.y))
    if row != "":
        start_edit_w()


global label_error


def start_generator_w(window):
    generator_window = tk.Toplevel(window)
    generator_window.configure(bg='#36393f')
    generator_window.geometry('390x200')
    generator_window.title('Generator')
    generator_window.resizable(False, False)

    label_length = ttk.Label(generator_window,
                             text='Password length (minimum is 8)')
    label_length.place(x=10, y=10)
    entry_length = ttk.Entry(generator_window)
    entry_length.place(x=13, y=32, width=365)

    label_spec = ttk.Label(generator_window,
                           text='Use special characters')
    label_spec.place(x=10, y=60)
    checkbutton_var = tk.IntVar()
    checkbutton_spec = ttk.Checkbutton(generator_window,
                                       variable=checkbutton_var,
                                       onvalue=1,
                                       offvalue=0)
    checkbutton_spec.place(x=13, y=82)

    global label_error
    label_error = ttk.Label(generator_window,
                            text='')
    label_error.place(x=10, y=99)

    btn_generate = ttk.Button(generator_window,
                              text='Generate',
                              width=10,
                              style='common.TButton')
    btn_generate.bind('<Button-1>', lambda event: generate_password(entry_length.get(), checkbutton_var.get()))
    btn_generate.place(x=13, y=120)

    btn_close = ttk.Button(generator_window,
                           text='Close',
                           width=10,
                           command=generator_window.destroy,
                           style='common.TButton')
    btn_close.place(x=118, y=120)

    generator_window.focus_set()
    generator_window.grab_set()


def generate_password(length, spec):
    if length == '':
        length = 0
    if int(length) < 8:
        label_error.configure(text='The minimum password length is 8!')
    else:
        label_error.configure(text='')
        entry_pass.delete(0, tk.END)
        entry_pass.insert(0, start_password_generator(int(length), int(spec)))


def view_data():
    data = selection_all_data_from_login_table(profile_login_verify.get())
    [tree.delete(i) for i in tree.get_children()]
    [tree.insert('', 'end', values=row) for row in data]


search = 0  # 0 - показывает все, 1 - показывает поиск по сервису, 2 - показывает поиск одинаковых паролей,


# 3 - показывает поиск слабых паролей


def search_by_service():
    global search
    service = entry_search_by_service.get()
    if service == "":
        reset_filters()
    else:
        data = search_service_in_login_table(profile_login_verify.get(), service)
        [tree.delete(i) for i in tree.get_children()]
        [tree.insert('', 'end', values=row) for row in data]
        search = 1


def search_duplicate_passwords():
    global search
    enable_change()
    data = selection_password_in_login_table(profile_login_verify.get())
    data.sort(key=lambda x: x[4])
    [tree.delete(i) for i in tree.get_children()]
    [tree.insert('', 'end', values=row) for row in data]
    search = 2


def search_weak_password():
    global search
    enable_change()
    data = selection_all_data_from_login_table(profile_login_verify.get())
    i = 0
    while i < len(data):
        if check_password(data[i][4]) >= 3:
            del data[i]
        else:
            i += 1
    [tree.delete(i) for i in tree.get_children()]
    [tree.insert('', 'end', values=row) for row in data]
    search = 3


def change_find_passwords():
    children = tree.get_children()
    for i in range(len(children)):
        item = children[i]
        update_passwords_in_login_table(profile_login_verify.get(), start_password_generator(16, 0),
                                        tree.set(item, '#1'))
    view_data()
    disable_change()


def disable_change():
    btn_change_passwords['state'] = 'disabled'


def enable_change():
    btn_change_passwords['state'] = 'normal'


def reset_filters():
    global search
    search = 0
    view_data()
    disable_change()


def add_data():
    data = (entry_service.get(), entry_login.get(), entry_email.get(), entry_pass.get())
    insert_data_to_login_table(profile_login_verify.get(), data)
    if search == 1:
        search_by_service()
    elif search == 2:
        search_duplicate_passwords()
    elif search == 3:
        search_weak_password()
    else:
        view_data()


def update_data():
    data = (entry_service.get(), entry_login.get(), entry_email.get(), entry_pass.get())
    key = tree.set(tree.selection()[0], '#1')
    # key = tree.index(tree.selection()[0]) + 1
    update_data_in_login_table(profile_login_verify.get(), data, key)
    if search == 1:
        search_by_service()
    elif search == 2:
        search_duplicate_passwords()
    elif search == 3:
        search_weak_password()
    else:
        view_data()


def get_one_data():
    key = tree.set(tree.selection()[0], '#1')
    # key = tree.index(tree.selection()[0]) + 1
    data = selection_one_data_from_login_table(profile_login_verify.get(), key)
    return data


def delete_one_data():
    for i in reversed(tree.selection()):
        # key = tree.index(i) + 1
        key = tree.set(i, '#1')
        delete_one_data_from_login_table(profile_login_verify.get(), key)
    if search == 1:
        search_by_service()
    elif search == 2:
        search_duplicate_passwords()
    elif search == 3:
        search_weak_password()
    else:
        view_data()


def click_to_clipboard(click):
    # key = tree.index(tree.selection()[0]) + 1
    # print(key)
    row = (tree.identify_row(click.y))
    column = tree.identify_column(click.x)
    to_clipboard = tree.set(row, column)
    main_window.clipboard_clear()
    main_window.clipboard_append(to_clipboard)
    if to_clipboard != '':
        inf_label.configure(text=to_clipboard + ' copy to clipboard')
    else:
        inf_label.configure(text='')


def exit_profile(_):
    main_window.destroy()


if __name__ == '__main__':
    start_auth_window()
    cursor.close()
    db.close()
    start_encrypt_file('etc.db', main_key)
