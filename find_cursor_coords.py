import pyautogui as gui


try:
    while True:
        x, y = gui.position()
        print(x, y)
except KeyboardInterrupt:
    print("\n")

