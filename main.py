import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED, Window
sg.theme('Reddit')

def main_window():    # function to create the initial registration screen
    signup_layout= [
    [sg.Text('Name'), sg.Input(key='name', size= (20,1))],
    [sg.Text('User'), sg.Input(key='user', size= (20,1))],
    [sg.Text('Email'), sg.Input(key='email', size= (20,1))],
    [sg.Text('Password'), sg.Input(key='password', size= (20,1))],
    [sg.Button('Submit')]
]

    signup_screen = sg.Window('Sign Up Screen', signup_layout)
    
    while True:
        event, values = signup_screen.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Submit':
            signup_screen.close()

            check_window(values['name'], values['user'], values['email'], values['password'])  # calls the check screen with the parameteres inputed



def check_window(name, user, email, password):   # window responsible of ask to the user if the everithyng is ok 
    check_layout = [
        [sg.Text('YOUR NAME: '), sg.Text(name)],
        [sg.Text('YOUR USER: '), sg.Text(user)],
        [sg.Text('YOUR EMAIL:'), sg.Text(email)],
        [sg.Text('YOUR PASSWORD'), sg.Text(password)],
        [sg.Text('Is everything OK?'), sg.Button('YES'), sg.Button('NO')]
    ]    
    check_screen = sg.Window('Check screen', check_layout)
    while True:
        event, values = check_screen.read()
        if event == 'YES' or event == sg.WIN_CLOSED:
            break
        if event == 'NO':
            check_screen.close()
            main_window()
main_window()