
import json
from time import sleep
import platform
import mouse
import os
import pyautogui
import keyboard
login = [] # dados




def safeClick(coordinates, pos_delay: int = 2):
        pyautogui.moveTo(coordinates)
        sleep(0.75)
        pyautogui.click()
        sleep(pos_delay)

def prepareTabs(tabs_to_open):
    if platform.system() == 'Windows':
        for acc in range(tabs_to_open):
            os.system('start "" "https://app.bombcrypto.io/"')
            sleep(5)
            # os.system('start chrome --start-fullscreen')

def doLogin(connect_button, login_input, pass_input, login_button):
    for acc in login:
        safeClick(connect_button, 2)
        safeClick(login_input, 2)
        keyboard.write(acc['user'])
        safeClick(pass_input, 2)
        keyboard.write(acc['pass'])
        safeClick(login_button, 2)
        if len(login) > 1: keyboard.press_and_release(['ctrl', 'tab'])
        sleep(2)


def reconnect(account, connect_button, login_input, pass_input, login_button):
    print(f"A conta desconectada foi: {account['user']}? ")
    sleep(11)
    safeClick(connect_button)
    safeClick(login_input)
    keyboard.write(account['user']); sleep(2)
    safeClick(pass_input)
    keyboard.write(account['pass']); sleep(2)
    safeClick(login_button)
    sleep(15)


def startTasks(mapping: dict, accounts: list):
    print("[!] Preparando as abas...")
    prepareTabs(len(accounts))
    print("[OK] Abas preparadas!")
    sleep(10)
    login_requirements = mapping['connect_wallet'], mapping['username_input'], mapping['password_input'], mapping['login_button']
    print("[!] Efetuando Login")
    doLogin(*login_requirements)
    print("[OK] Login efetuado")
    sleep(4)
    first_time = True
    round_time = 60 * 100 # 1h40
    fake_round_time = 60 * 3 # Rodizio de 3 minutos
    round_timecount = 0
    next_round = False
    print("[i] Iniciando o rodízio geral...")
    while True:
        for index, acc in enumerate(accounts):
            print("[!] Procurando botão de desconexão")
            error = pyautogui.locateOnScreen('./images/ConnLostOk.png', confidence=.75)
            if error:
                safeClick(error, 2)
                reconnect(acc, *login_requirements)
            else:
                print("[OK] Tudo certo! Não foi desconectado")
            if not first_time: 
                print("[i] Voltando ao menu principal")
                safeClick(mapping['back_button'], 2)
                
            print("[i] Abrindo menu de Heróis")
            safeClick(mapping['heroes'], 2)
            if next_round or first_time:
                print("[i] Colocando todos para trabalhar")
                safeClick(mapping['work_all'], 2)
                if not first_time and index == len(accounts) - 1:
                    next_round = not next_round # False

            print("[i] Fechando menu de Heróis")
            safeClick(mapping['close_heroes'], 2)
            print("[i] Abrindo modo Treasure Hunt")
            safeClick(mapping['treasure_hunt'], 2)
            print("[i] Indo para próxima conta")

            if len(login) > 1: keyboard.press_and_release(['ctrl', str(index + 1)])

        first_time = False
        round_timecount += fake_round_time
        if round_timecount >= round_time:
            round_timecount = 0
            next_round = True
        if len(login) > 1:
            for _ in range(int(fake_round_time/3)):
                keyboard.press_and_release(['ctrl', 'tab'])
                sleep(3)
        else: sleep(fake_round_time)


def loadMapping():
    try:
        with open("mapping.json", "r") as f:
            data = json.load(f)
            f.close()
            return data or None
    except:
        print("Ocorreu um erro ao consultar as configurações de mapeamento")
        return False  

def saveMapping(mapping_item: dict):
    try:
        f = open("mapping.json", "w")
        json.dump(mapping_item, f, indent=4)
        return True
    except:
        print("Ocorreu um erro ao salvar mapeamento.")
        return False  


def getUserCoord(phrase: str):
    print(phrase)
    while not mouse.is_pressed(button='left'): pass
    pos = pyautogui.position()
    print("Coordenadas capturadas!")
    sleep(2)
    return pos

def loadFromFile(): # Função para carregar as contas ao programa. Não retorna valor algum, apenas adiciona os dados na lista login.   
    users_from_file = getUsers() # Pega os usuários do users.json
    if users_from_file: # Se tiver usuário no arquivo: 
        action = input("Identificamos usuários salvos no arquivo de dados de Login. Deseja carregar os dados a partir deste arquivo [S/n]? ")
        if action.lower() in ["s", '']:
            for index, single_data in enumerate(users_from_file):
                print(f"{index + 1} - Usuário: {single_data['user']} | Senha: {single_data['pass']}")
            selected_users = input("Qual dessas contas você deseja carregar? Ex.: 1,2,3,4... ou all para selecionar todas: ").lower()
            selected_users = selected_users.split(',')
            selected_users = list(map(int , selected_users)) if selected_users[0] != "all" else range(len(users_from_file))
            print(f"=== Contas Selecionadas ({len(selected_users)}) ===")
            for selected_user in selected_users:
                login.append(users_from_file[selected_user - 1])
                print(users_from_file[selected_user - 1])
            def addMore():
                if input("Deseja adicionar mais alguma conta à essa lista [S/n]? ").lower() in ['s', '']:
                    addUser({"user": input("Usuário: "), "pass": input("Senha: ")})
                    addMore()
            addMore()

def loginData(): # Da o input para o usuário digitar os dados da conta e pergunta se os dados coincidem
    username = input(f"Digite o usuário da conta: ")
    password = input(f"Digite a senha da conta: ")
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

def getUsers(): # Retorna a lista de usuários do arquivo users.json
    with open("users.json", "r") as f:
        data = json.load(f)
        f.close()
        return (data if len(data) > 0 else None)




def addUser(login_dict: dict): # Adiciona um dict ao arquivo de users.json
    try:
        f = open("users.json", "r")
        old_data = json.loads(f.read())
        old_data.append(login_dict)
        f.close()
        f = open("users.json", "w")
        json.dump(old_data, f, indent=4)
        login.append(login_dict)
        return True
    except:
        print("Ocorreu um erro ao salvar usuário")
        return False  

def main():
    users_from_file = getUsers()
    if users_from_file:
        loadFromFile()
    
    accounts = int(input("Quantidade de contas: ")) if len(login) == 0 else None
    from_file = False if len(login) == 0 else True
    if not from_file:
        for _ in range(accounts):
            loginData()

    sleep(.75)
    print("Agora vamos mapear os botões! Recomendamos deixar a tela do navegador cheia.")
    print("A cada 2 segundos será solicitado um clique em um objeto.")

    mapping_saved_data = loadMapping()
    if not mapping_saved_data:
        connect_wallet = getUserCoord('Clique no botão de conectar a carteira')
        username_input = getUserCoord('Clique no campo de Username')
        password_input = getUserCoord('Clique no campo de Senha')
        login_button = getUserCoord('Clique no botão de Login')
        heroes = getUserCoord('Clique no botão de Herois')
        work_all = getUserCoord('Clique no botão para todos Trabalharem')
        close_heroes = getUserCoord('Clique no botão de fechar menu de Heróis')
        treasure_hunt = getUserCoord('Clique no Treasure Hunt')
        back_button = getUserCoord('Clique no botão de Voltar para o menu')
        mapping_dict = {
            "connect_wallet": connect_wallet,
            "username_input": username_input,
            "password_input": password_input,
            "login_button": login_button,
            "heroes": heroes,
            "work_all": work_all,
            "close_heroes": close_heroes,
            "treasure_hunt": treasure_hunt,
            "back_button": back_button
        }
        saveMapping(mapping_dict)
    print("Mapeamento Salvo com sucesso!")
    input("Quando estiver tudo pronto, pressione enter e minimize este programa. Você terá 5 segundos.\n"
    "Não esqueça de fechar o navegador onde mapeou os botões.")
    startTasks(mapping_dict if not mapping_saved_data else mapping_saved_data, login)





if __name__ == '__main__':
    main()