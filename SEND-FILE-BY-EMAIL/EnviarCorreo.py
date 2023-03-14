# Esto es un script que se hizo para mandar un Excel, se puede mandar cualquier otro archivo, cambiando la informacion en cuerpo.txt

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os

# aqui va el asunto del correo.
with open("cuerpo.txt") as f:
    data = f.readlines()[0]

email_subject = data
#--------------------------------------------------------#
sender_email_address = "email@correp.com" 
# Array que contendra la lista de correos
emailList = []
send_confirmed = []
email_smtp = "smtp.gmail.com" # El smtp de gmail como ejemplo.

#Contraseña del email, en algunos casos como google, tienen una sesion apps passwords key.
email_password = "..."

#documento. nombre sacado del archivo ('information.txt')
with open("cuerpo.txt") as f:
    dataDoc = f.readlines()[1]
    characters = "\n"
    for x in range(len(characters)):
        dataDoc = dataDoc.replace(characters[x], "")

# Recorrido de la lista de correos en el txt, separados por una coma, y anadirlos al array.
with open('Correos.txt') as f:
    for line in f:
        emailList = [elt.strip() for elt in line.split('|')]

# Recorrido del array con la lista de emails 
for i in emailList:
    mensaje = MIMEMultipart('plain')
    mensaje['from'] = sender_email_address
    mensaje['to'] = i
    mensaje['subject'] = email_subject
    adjunto = MIMEBase('application', 'octect-stream')
    adjunto.set_payload(open(dataDoc, 'rb').read())
    encode_base64(adjunto)
    adjunto.add_header('content-Disposition', 'attachment; filename="%s"'% os.path.basename(dataDoc))
    mensaje.attach(adjunto)
    smtp = SMTP(host='smtp.gmail.com', port=587)
    smtp.starttls()
    # loguearse 
    smtp.login(sender_email_address, email_password)
    smtp.sendmail(sender_email_address,i,mensaje.as_string())
    send_confirmed.append("Enviado")
    smtp.quit()

for i in send_confirmed:
    if(i == 'Enviado'):
        with open('informacion.txt', 'w') as f:
            f.write("Enviado")
            f.close()