import pyautogui
import time
import pyperclip
from credenciais import segredos #do arquivo credencias, import pra mim o object segredos

pyautogui.alert("O codigo vai começar, não utilize nada do computador até o codigo finalizar!")
pyautogui.PAUSE = 1  # deixando claro pro autogui que a cada vez que ele executar um comando, esperar determinado tempo
pyautogui.hotkey('alt', 'tab')

pyautogui.hotkey('ctrl', 'shift', 'n')
time.sleep(3)
linkado = segredos.get('link')
pyperclip.copy(linkado)

pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.press('enter')

screenWidth, screenHeighy = pyautogui.size() # pega o tamanho do monitor

currentMouseX, currentMouseY = pyautogui.position() #pegando x e y

time.sleep(7)
pyautogui.doubleClick(614, 435)

name = segredos.get('name')
pyperclip.copy(name)
pyautogui.hotkey('ctrl', 'v')

time.sleep(5)
pyautogui.doubleClick(614, 535)
security = segredos.get('API_KEY')
pyperclip.copy(security)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(614,600)

time.sleep(5)
pyautogui.scroll(20)