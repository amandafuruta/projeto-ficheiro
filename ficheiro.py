import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import shutil

def select_folder():
    # Open the folder selection dialog
    folder_selected = filedialog.askdirectory(title="Selecione uma pasta")

    # Return the path of the selected folder
    return folder_selected

def list_files_in_folder(folder_path):
    # Create a Path object for the folder
    folder = Path(folder_path)

    # Filter only .txt files
    txt_files = [file.name for file in folder.iterdir() if file.is_file() and file.suffix == '.txt']
    
    # List all txt files and directories in the folder
    print()
    print('###########')
    print()
    print(f"Ficheiros .txt dentro da pasta '{folder_path}':")
    print()
    for txt_file in txt_files:
        print(txt_file)  # Display the name of the item
    print()
    print('###########')

def list_folders_in_folder():
    folder = Path(folder_path)        
    # List only directories inside the folder
    subdirectories = [item.name for item in folder.iterdir() if item.is_dir()]
    
    print()
    print('***********')
    print(f"Pastas dentro de '{folder_path}':")
    for subfolder in subdirectories:
        print(subfolder)
    print('************')
    choice = input('Qual pasta deseja excluir ?')
    return choice

def create_folder(folder_name):
    folder = Path(folder_path + '/' + folder_name)
    try:
        folder.mkdir()
        print(f"Pasta '{folder_name}' foi criada com sucesso.")
    except FileExistsError:
        print(f"Erro: A pasta '{folder_name}' já existe.")
    except Exception as e:
        print(f"Error: {e}")

def create_txt_file(file_name, file_content):
    try:
        file_path = folder_path + '/' + file_name
        # Open the file in write mode ('w')
        with open(file_path, 'w') as file:
            # Write content to the file
            file.write(file_content)
        print(f"File '{file_name}' created and content written successfully.")
    except Exception as e:
        print(f"Error: {e}")

def read_file(file_name):
    try:
        file_path = folder_path + '/' + file_name
        with open(file_path, 'r') as file:  # Open file in read mode
            content = file.read()  # Read the entire file content
            print()
            print('Conteúdo do arquivo:')
            print(content)  # Print the content
    except Exception as e:
        print(f"Error: {e}")

def delete_file(file_name):
    try:
        file_path = folder_path + '/' + file_name
        file = Path(file_path)
        if file.exists():  # Check if the file exists
            file.unlink()  # Delete the file
            print(f"Ficheiro '{file_name}' deletado com sucesso.")
        else:
            print(f"Erro: Ficheiro '{file_name}' não existe.")
    except Exception as e:
        print(f"Error: {e}")

def search_in_file(file_name, search_data):    

    file_path = folder_path + '/' + file_name
    file = Path(file_path)

    # Check if the file exists
    if not file.exists():
        print(f"Erro: O ficheiro '{file_name}' não existe.")
        return
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read all lines from the file
            
            matching_lines = []  # List to store lines containing the search data
            for line in lines:
                if search_data.lower() in line.lower():  # Case insensitive search
                    matching_lines.append(line.strip())  # Add the line to the list

            # Display the results
            if matching_lines:
                print(f"\nLinhas contendo '{search_data}':")
                for line in matching_lines:
                    print(line)
                print(f"\nTotal de {len(matching_lines)} linha(s) encontrada(s).")
            else:
                print(f"\nNenhuma linha encontrada com o dado '{search_data}'.")
    except Exception as e:
        print(f"Erro ao ler o ficheiro: {e}")

# Seleciona a pasta
folder_path = select_folder()

def menu():
    print()
    print()
    print('### MENU ### ')
    print('1. Ficheiros')
    print('2. Eliminar Pasta')
    print('3. Criar Pasta')
    print('0. Sair')

    option = input("Escolha uma opção: ")
    return option

def menu1():
    print()
    print()
    print('Manipulação de ficheiros:')
    print('1 Abrir ficheiro')
    print('2 Criar ficheiro')
    print('3 Eliminar ficheiro')
    print('4 Procurar dados')
    print('0 Menu anterior')
    option = input("Escolha uma opção: ")
    return option

def main():
    while True:
        # 1) Step 01
        first_choice = menu()

        if first_choice == '0': # Sair
            break

        if first_choice == '2': # Eliminar Pasta
            try:   
                #Listar as pastas  
                folder_name = list_folders_in_folder()
                folder_to_delete = Path(folder_path) / folder_name
                if folder_to_delete.exists() and folder_to_delete.is_dir() and folder_name != '':
                    shutil.rmtree(folder_to_delete)
                    print(f"A pasta '{folder_name}' foi excluída com sucesso.")
                else:
                    print(f"A pasta '{folder_name}' não foi encontrada.")
            except:
                print('Erro para deletar a pasta')

        if first_choice == '3': # Criar Pasta
            folder_name = input('Qual nome da pasta?')
            create_folder(folder_name)

        if first_choice == '1':
            list_files_in_folder(folder_path)
            second_choice = menu1()

            if second_choice == '0': # Volta ao menu anterior
                continue

            if second_choice == '1': # Abrir ficheiro
                print()
                file_name= input('Qual o nome do ficheiro deseja abrir? ')
                file_name += '.txt'
                read_file(file_name)

            if second_choice == '2': # Criar ficheiro
                print()
                print()
                file_name= input('Nome do ficheiro: ')
                file_name += '.txt'
                file_content= input('Conteúdo do ficheiro: ')
                create_txt_file(file_name, file_content)

            if second_choice == '3': # Eliminar ficheiro
                print()
                file_name = input('Qual o nome do ficheiro deseja apagar? ')
                file_name += '.txt'
                delete_file(file_name)

            if second_choice == '4': # Procurar dados
                file_name = input('Em qual ficheiro deseja procurar? ')
                file_name += '.txt'
                search_data = input('O que deseja procurar? ')

                search_in_file(file_name, search_data)

main()