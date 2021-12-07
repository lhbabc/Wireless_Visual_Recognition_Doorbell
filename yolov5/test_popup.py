import ctypes, threading

for i in range(11):
    if i%5 == 0:  # Any condition
        popup = ctypes.windll.user32.MessageBoxW
        threading.Thread(target = lambda :popup(None, 'Parth is here!', 'Ting Bell', 0)).start()
