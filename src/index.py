import keyboard
import mouse
import pyautogui
import time

accounts = int(input("Quantidade de contas: "))
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

print(
"Atenção! Você terá que clicar nos respectivos botões de cada janela para cada conta.\n"
"Toda vez após clicar, haverá um delay de 2s para executar o próximo click.\n"
"Inicialmente, vamos precisar do login de cada conta para efetuar o login automaticamente "
"em casos de perda de conexão."
)

for x in range(accounts):
    print(("=" * 10) + f" Conta {x+1} " + ("=" * 10) )
    def loginData():
        username = input(f"Digite o usuário da conta {x+1}: ")
        password = input(f"Digite a senha da conta {x+1}: ")
        action = input("Os dados coincidem? [S/n]").lower()
        if action == "s":
            login.append({"user": username, "pass": password})
        elif action == "n":
            return loginData()
        else:
            pass

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
    
    
    
while True:
    for x in range(accounts):
        error = pyautogui.locateOnScreen('./images/ConnLostOk.png', confidence=.8)
        if error:
            pyautogui.click(error)
            time.sleep(2)
            pyautogui.click(connect_wallet[x])
            time.sleep(2)
            pyautogui.click(username_input[x]); time.sleep(1); keyboard.write(login[x]['user'])
            time.sleep(2)
            pyautogui.click(password_input[x]); time.sleep(1); keyboard.write(login[x]['pass'])
            time.sleep(2)
            pyautogui.click(login_button[x]); time.sleep(1)
            time.sleep(2)

        time.sleep(2)
        pyautogui.click(main_menu[x])
        time.sleep(2)
        pyautogui.click(heroes[x])
        time.sleep(2)
        pyautogui.click(_all[x])
        time.sleep(2)
        pyautogui.click(back[x])
        time.sleep(2)
        pyautogui.click(treasure_hunt[x])
    time.sleep(180)