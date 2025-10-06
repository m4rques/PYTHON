import win32com.client as win32
from pathlib import Path

destino = Path.cwd() / "Emails"
destino.mkdir(parents=True, exist_ok=True)

outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")

root_folders = outlook.Folders.Item(1)


for folder in root_folders.Folders: 
    print(folder.Name)

caixa_entrada = outlook.GetDefaultFolder(3)


mensagens  = caixa_entrada.Items

for m in mensagens:
    
    assunto = m.Subject 
    corpo = m.Body 
    anexos = m.Attachments

    pasta_destino = destino / str(assunto).replace(':',"").replace('/', "")
    pasta_destino.mkdir(parents=True, exist_ok=True)

    Path(pasta_destino / 'Corpo_email.txt').write_text(str(corpo))

    for a in anexos:
        a.SaveAsFile(pasta_destino / str(a))
    
    

