import mouse
import pyautogui
import time

accounts = int(input("Quantidade de contas: "))
heroes = []
_all = []
back = []
treasure_hunt = []
main_menu = []

print(
"Atenção! Você terá que clicar nos respectivos botões de cada janela para cada conta."\
"Toda vez após clicar, haverá um delay de 2s para executar o próximo click."\
)

for x in range(accounts):
    print(("=" * 10) + f" Conta {x+1} " + ("=" * 10) )
    print("Clique no botão de Herois para conta 1")
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