import json
import keyboard
import mouse
from numpy import True_
import pyautogui
import time

login = []
connect_wallet = [] # Botões de conexão da carteira
username_input = [] # Campos de usuário
password_input = [] # Campos de senha
login_button = [] # Botão de Login
heroes = [] # Botão de Herois
_all = [] # Botão de colocar Todos para trabalhar
back = [] # Botão de fechar Menu de Herois
treasure_hunt = [] # Botão de Treasure Hunt
main_menu = [] # Botão de sair do jogo para voltar ao Menu Principal

def getUsers():
    with open("users.json", "r") as f:
        data = json.load(f)
        f.close()
        return (data if len(data) > 0 else None)

def addUser(login: dict):
    try:
        f = open("users.json", "r")
        old_data = json.loads(f.read())
        old_data.append(login)
        f.close()
        f = open("users.json", "w")
        json.dump(old_data, f, indent=4)
        return True
    except:
        print("Ocorreu um erro ao salvar usuário")
        return False    

users_from_file = getUsers()
if users_from_file:

    action = input("Identificamos usuários salvos no arquivo de dados de Login. Deseja carregar os dados a partir deste arquivo [S/n]? ")
    if action.lower() in ["s", '']:
        for index, single_data in enumerate(users_from_file):
            print(f"{index + 1} - Usuário: {single_data['user']} | Senha: {single_data['pass']}")
        selected_users = input("Qual dessas contas você deseja carregar? Ex.: 1,2,3,4... ou all para selecionar todas: ").lower()
        selected_users = selected_users.split(',')
        selected_users = list(map(int , selected_users)) if selected_users[0] != "all" else range(len(users_from_file))
        print(f"=== Contas Selecionadas ({len(selected_users)}) ===")
        for selected_user in selected_users:
            login.append(selected_user)
            print(users_from_file[selected_user - 1])
        def addMore():
            if input("Deseja adicionar mais alguma conta à essa lista [S/n]? ").lower() in ['s', '']:
                addUser({"user": input("Usuário: "), "pass": input("Senha: ")})
                return addMore()
        addMore()
accounts = int(input("Quantidade de contas: ")) if len(login) == 0 else None
from_file = False if len(login) == 0 else True
print(
"\nAtenção! Você terá que clicar nos respectivos botões de cada janela para cada conta.\n"
"Toda vez após clicar, haverá um delay de 2s para executar o próximo click.\n"
"Inicialmente, vamos precisar do login de cada conta para efetuar o login automaticamente "
"em casos de perda de conexão.\n"
)

for x in range(accounts or len(login)):
    print(("=" * 10) + f" Conta {x+1} " + ("=" * 10) )
    def loginData():
        username = input(f"Digite o usuário da conta {x+1}: ")
        password = input(f"Digite a senha da conta {x+1}: ")
        action = input("Os dados coincidem? [S/n]").lower()
        if action == "s":
            user_data = {"user": username, "pass": password}
            login.append(user_data)
            addUser(user_data)
            print("Usário adicionado ao arquivo users.json")

        elif action == "n":
            loginData()
        else:
            pass
    if not from_file:
        loginData()

    print("Clique no botão de conectar a carteira")
    while not mouse.is_pressed(button='left'): pass
    connect_wallet.append(pyautogui.position())
    print("Wallet - OK")
    time.sleep(2)

    print("Clique no campo de usuário")
    while not mouse.is_pressed(button='left'): pass
    username_input.append(pyautogui.position())
    time.sleep(0.5)
    keyboard.write(login[x]['user'])
    print("Username - OK")
    time.sleep(2)

    print("Clique no campo de senha")
    while not mouse.is_pressed(button='left'): pass
    password_input.append(pyautogui.position())
    time.sleep(0.5)
    keyboard.write(login[x]['pass'])
    print("Password - OK")
    time.sleep(2)

    print("Clique no botão de efetuar login")
    while not mouse.is_pressed(button='left'): pass
    login_button.append(pyautogui.position())
    print("Login Button - OK")
    time.sleep(2)



    print("Clique no botão de Herois")
    while not mouse.is_pressed(button='left'): pass
    heroes.append(pyautogui.position())
    print("Heroes - OK")
    time.sleep(2)

    print("Clique no botão para todos trabalharem")
    while not mouse.is_pressed(button='left'): pass
    _all.append(pyautogui.position())
    print("Work All - OK")
    time.sleep(2)

    print("Clique no botão para fechar os o menu de heróis")
    while not mouse.is_pressed(button='left'): pass
    back.append(pyautogui.position())
    print("Close Heroes Menu - OK")
    time.sleep(2)


    print("Clique no botão de treasure hunt")
    while not mouse.is_pressed(button='left'): pass
    treasure_hunt.append(pyautogui.position())
    print("Treasure Hunt - OK")
    time.sleep(2)

    print("Clique no botão de voltar")
    while not mouse.is_pressed(button='left'): pass
    main_menu.append(pyautogui.position())
    print("Menu - OK")
    print(f"Finalizado mapeamento de botões para conta {x+1}.")
    time.sleep(2)
    
    
menu_loop_time = 60 * 180 # Loop para colocar todos para trabalhar (Padrão: 1h40m)
sleep_loop = 180 # Loop para evitar desconexão
time_count = 0




def safeClick(coordinates):
    pyautogui.moveTo(coordinates)
    pyautogui.click()
    time.sleep(0.75)
while True:
    for x in range(accounts):
        time.sleep(4)
        error = pyautogui.locateOnScreen('./images/ConnLostOk.png', confidence=.8)
        if error:
            safeClick(error)
            time.sleep(11)
            safeClick(connect_wallet[x])
            time.sleep(2)
            safeClick(username_input[x]); time.sleep(1); keyboard.write(login[x]['user'])
            time.sleep(2)
            safeClick(password_input[x]); time.sleep(1); keyboard.write(login[x]['pass'])
            time.sleep(2)
            safeClick(login_button[x]); time.sleep(1)
            time.sleep(2)

        time.sleep(4)
        safeClick(main_menu[x])
        time.sleep(2)
        safeClick(heroes[x])
        time.sleep(2)
        if time_count >= menu_loop_time:
            time_count = 0
            safeClick(_all[x])
            time.sleep(2)
        safeClick(back[x])
        time.sleep(2)
        safeClick(treasure_hunt[x])
    time_count += sleep_loop
    time.sleep(sleep_loop)