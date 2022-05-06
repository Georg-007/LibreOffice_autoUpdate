#from glob import glob
import requests
import tempfile
import os
from time import sleep
import PySimpleGUI as sg
from threading import Thread

archs = ["x64", "x86"]
arch = archs[0]
fullArch = "x86_64" if arch == "x64" else "x86"

#? currently installed version
#? Win11 x64
#? registry
#? Computer\HKEY_CLASSES_ROOT\Installer\Products\5966D1008B9FDBC4AA29EFA885360806\ProductName
#? 7.3.2.2 --> not matching website (7.3.3)

sg.theme("Dark")
layout = [  [sg.Text("LibreOffice autoUpdate", key = "-I-")],
            [sg.Text("latest version:"), sg.Text("loading...", key = "-V-")],
            [sg.Button("Install", bind_return_key=True), sg.Button("Reload")] ]
window = sg.Window("LibreOffice autoUpdate", layout)

temp = tempfile.gettempdir()
latestversion = "loading..."
install_finished = True
guictrl_ready = False
reload_finished = True
run = True

def get_versions():
    urldownloads = 'https://www.libreoffice.org/download/download/index.html'
    r = requests.get(urldownloads)
    versions = []
    for i, v in enumerate(str(r.content).split('class="dl_version_number">')[1:]):
        versions.append(v.split("</span>")[0])
    return versions

def get_msi(version):
    urlmsi = f"https://download.documentfoundation.org/libreoffice/stable/{version}/win/{fullArch}/LibreOffice_{version}_Win_{arch}.msi"
    #urlmsi = f"https://download.documentfoundation.org/libreoffice/stable/{version}/win/x86_64/LibreOffice_{version}_Win_x64.msi"
    r = requests.get(urlmsi)
    filename = temp + "/" + urlmsi.split('/')[-1]
    with open(filename,'wb') as output_file:
        output_file.write(r.content)
    return filename

def run_msi(filename):
    os.system('"' + filename.replace("/", "\\") + '"')

def install():
    global install_finished
    install_finished = False
    filename = get_msi(latestversion)
    run_msi(filename)
    sleep(3)
    os.remove(filename)
    install_finished = True

def reload():
    global reload_finished
    global latestversion
    reload_finished = False
    versions = get_versions()
    latestversion = max(versions)
    reload_finished = True

def guictrl():
    global run
    global latestversion
    global install_finished
    global guictrl_ready
    global reload_finished
    while not guictrl_ready:
        pass
    versions = get_versions()
    latestversion = max(versions)
    window["-V-"].update(latestversion)
    while run:
        if install_finished:
            window["-I-"].update("LibreOffice autoUpdate")
        if reload_finished:
            window["-V-"].update(latestversion)
        sleep(1)

def main():
    global run
    global latestversion
    global install_finished
    global guictrl_ready
    global reload_finished
    versions = get_versions()
    latestversion = max(versions)
    guictrl_ready = False
    Thread(target = guictrl).start()
    while True:
        guictrl_ready = True
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            run = False
            return
        if event == "Reload" and reload_finished:
            window["-V-"].update("loading...")
            reload_finished = False
            Thread(target = reload).start()
        if event == "Install" and install_finished and reload_finished:
            window["-I-"].update("processing...")
            install_finished = False
            Thread(target = install).start()

if __name__ =="__main__":
    main()
