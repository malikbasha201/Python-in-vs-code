import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("choose",key='files')

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2  = sg.FolderBrowse("choose",key='folder')

compress_button = sg.Button("Compress")

window = sg.Window("File compression",layout=[[label1 ,input1 ,choose_button1 ],
                                              [label2 ,input2 ,choose_button2],
                                              [compress_button]])

while True:
    event,values = window.read()
    print(event,values)
    filepath = values['files'].split(";")
    folder = values['folder']
    make_archive(filepath,folder)
    
window.close() 