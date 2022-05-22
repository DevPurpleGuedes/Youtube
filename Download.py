import PySimpleGUI as sg
from pytube import YouTube

def executar_download(link, path):
        video = YouTube(link)
        video.streams.get_highest_resolution().download(output_path=path)
    
janela = sg.Window('Download de Videos', layout = [
    [sg.Text('Informe o link do vídeo: ', s=20), sg.InputText()],
    [sg.Text('Local aonde o video ficará: ', s=20), sg.InputText(), sg.FolderBrowse()],
    [sg.Button('Baixar'), sg.Button('Cancelar')]
])

while True:
    event, values = janela.read()   
    if event == 'Cancelar' or event == sg.WIN_CLOSED:
        break
    elif event == 'Baixar':
        executar_download(values[0], values [1])
        sg.popup_ok('Download Concluído com sucesso!')
        
janela.close()

