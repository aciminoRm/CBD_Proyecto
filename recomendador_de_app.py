import os
import time
import inquirer
from pyfiglet import Figlet

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    custom_fig = Figlet(font='pagga')
    print(custom_fig.renderText("Recomendador de app"))
    time.sleep(1)

def print_menu(menu_options):
    print("Menu:")
    for key, value in menu_options.items():
        print(f"[{key}] {value}")

def print_submenu(submenu_options):
    print("Sotto-menu:")
    for key, value in submenu_options.items():
        print(f"[{key}] {value}")

def perform_operation(option):
    print(f"Eseguito: {option}")

def choice_category(listaGeneros):
    categories_choices = ['SelectAll','Action', 'Adventure', 'Arcade', 'Art', 'Audio', 'Auto', 'Beauty', 'Board', 'Books', 'Business', 'Card', 'Casino', 'Casual', 'Comics', 'Communication', 'Dating', 'Demo', 'Design', 'Drink', 'Editors', 'Education', 'Educational', 'Entertainment', 'Events', 'Finance', 'Fitness', 'Food', 'Health', 'Home', 'House', 'Libraries', 'Lifestyle', 'Local', 'Magazines', 'Maps', 'Medical', 'Music', 'Navigation', 'News', 'Parenting', 'Personalization', 'Photography', 'Productivity', 'Puzzle', 'Racing', 'Reference', 'Role_Playing', 'Shopping', 'Simulation', 'Social', 'Sports', 'Strategy', 'Tools', 'Travel', 'Trivia', 'Vehicles', 'Video_Players', 'Weather', 'Word']
    questions = [
        inquirer.Checkbox(name='Categories',
                          message="Choose the Categories",
                          choices=categories_choices,
                          ),
    ]
    answers = inquirer.prompt(questions)
    
    if 'SelectAll' in answers['Categories']:
        return categories_choices[1:]  
    else:
        return answers["Categories"]

menu = {
    '1': 'Info App',
    '2': 'Lista Top App',
    '0': 'Quit'
}

submenu_top = {
    '1': 'Top Download',
    '2': 'Top Rating',
    '3': 'Top Paid x Download',
    '4': 'Top Paid x Price',
    '5': 'Top Release Update',
    '6': 'Top Pegi 18',
    '7': 'Top best developers',
    '0': 'Torna al Menu Principale'
}

submenu_info = {
    '1': 'Info App',
    '2': 'ContentRating and Price',
    '3': 'Info Developer x App',
    '4': 'Info App x Developer',
    '0': 'Torna al Menu Principale'
}

exit_program = False

while not exit_program:
    print_title()
    print_menu(menu)

    choice = input("Inserisci la tua scelta (0-2): ")

    if choice == '1':
        while True:
            print_submenu(submenu_info)

            submenu_choice = input("Inserisci la tua scelta (0-4): ")

            if submenu_choice == '0':
                clear_terminal()
                break 
            elif submenu_choice.isdigit() and 0 <= int(submenu_choice) <= 4:
                switch_dict = {
                    '1': 1,
                    '2': 2,
                    '3': 3,
                    '4': 4,
                }
                script_number = switch_dict.get(submenu_choice)
                if script_number == 4:
                    app_name_input = input("Inserisci il nome dello sviluppatore: ")
                else:
                    app_name_input = input("Inserisci il nome dell'app: ")
                
                start_time = time.time()
                
                if script_number is not None:
                    script_path = f"script_app/app_{str(script_number)}.py"
                    if os.path.exists(script_path):
                        command = f"python {script_path} '{app_name_input}'"
                        os.system(command)
                    else:
                        print(f"Lo script {script_path} non esiste.")
                else:
                    print(f"Numero di script non valido: {script_number}")
                    
                
                end_time = time.time()
                total_time = end_time - start_time
                print(f"Tempo di esecuzione totale: {total_time} secondi")
                
                print_title()
                perform_operation(submenu_info[submenu_choice])
            else:
                print("Scelta non valida. Inserisci un numero compreso tra 0 e 3.")
    elif choice == '2':
        clear_terminal()
        print_title()
        while True:
            print_submenu(submenu_top)
            submenu_choice = input("Inserisci la tua scelta (0-7): ")

            if submenu_choice == '0':
                clear_terminal()
                break
            elif submenu_choice.isdigit() and 0 <= int(submenu_choice) <= 7:
                listaGeneros = []
                listaGeneros = choice_category(listaGeneros)

                switch_dict = {
                    '1': 1,
                    '2': 2,
                    '3': 3,
                    '4': 4,
                    '5': 5,
                    '6': 6,
                    '7': 7,
                }

                script_number = switch_dict.get(submenu_choice)
                while True:
                    number_choice = input("How many occurrences do you want printed? (max 1000)\n-->")
                    try:
                        number_choice = int(number_choice)
                        if 1 <= number_choice <= 1000:
                            break
                        else:
                            print("Inserisci un numero compreso tra 1 e 1000.")
                    except ValueError:
                        print("Inserisci un numero valido.")
                        
                start_time = time.time()
                
                if script_number is not None:
                    script_path = f"script_top/top_{str(script_number)}.py"
                    if os.path.exists(script_path):
                        print(listaGeneros)
                        print(number_choice)
                        command = f"python {script_path} {','.join(listaGeneros)} {number_choice}"
                        os.system(command)
                    else:
                    	print(f"Lo script {script_path} non esiste.")
                else:
                    print(f"Numero di script non valido: {script_number}")	
                    
                end_time = time.time()
                total_time = end_time - start_time
                print(f"Tempo di esecuzione totale: {total_time} secondi")

                print_title()
                perform_operation(submenu_top[submenu_choice])
            else:
                print("Scelta non valida. Inserisci un numero compreso tra 0 e 3.")
    elif choice == '0':
        clear_terminal()
        print_title()
        print("Arrivederci!")
        exit_program = True
    else:
        print("Scelta non valida. Inserisci un numero tra 0 e 2.")













