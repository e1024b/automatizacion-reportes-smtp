import smtplib                                                                     #librería para enviar correos por SMTP.
import schedule                                                                    #librería para programar tareas.
import time                                                                        #herramientas relacionadas con el tiempo.
from email.message import EmailMessage                                             #permite construir un correo estructurado con asunto, destinatarios, cuerpo y archivos adjuntos.
from datetime import datetime                                                      #sirve para obtener la fecha y hora actual y usarla en el asunto y en los registros.

#DATOS DE CONFIGURACION (Aquí se guardan las credenciales del correo desde el cual se enviará el mensaje.)
EMAIL_ADDRESS = 'EMAIL_ADDRESS' 
EMAIL_PASSWORD = 'EMAIL_PASSWORD''
DESTINATARIOS = ['destinatario1@example.com', 'destinatario2@example.com']


REPORTE_PATH = 'ruta/del/reporte_semanal.xlsx'                                       #Ruta del archivo Excel que se va a adjuntar al correo.

#FUNCION PRINCIPAL
def enviar_reporte():
    msg = EmailMessage()                                                              #Crea un objeto de correo vacío.
    msg['Subject'] = f'Reporte Semanal - {datetime.now().strftime("%d/%m/%Y")}'       #Asigna el asunto del correo. Incluye la fecha actual en formato día/mes/año.
    msg['From'] = EMAIL_ADDRESS                                                       #Indica quién envía el correo.
    msg['To'] = ', '.join(DESTINATARIOS)                                              #Define los destinatarios separados por comas en una sola cadena
    msg.set_content('Hola,\n\nAdjunto encontrarás el reporte semanal.\n\nSaludos.')   #Escribe el cuerpo del correo.

#LECTURA DEL ARCHIVO ADJUNTO    
    with open(REPORTE_PATH, 'rb') as f:                                               #Abre el archivo Excel en modo binario (rb), que es necesario para adjuntarlo al correo.
        file_data = f.read()                                                          #Lee todo el contenido del archivo y lo guarda en memoria.
        file_name = f.name.split('/')[-1]                                             #Extrae solo el nombre del archivo, por ejemplo reporte_semanal.xlsx, sin la ruta completa.

#Adjuntar el archivo al mensaje
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)  #Agrega el archivo al correo como adjunto.(application/octet-stream se usa como tipo genérico para archivos binarios.)
   
#ENVIO DEL CORREO
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:                             #Se conecta al servidor SMTP seguro de Gmail usando el puerto 465.
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)                                     #Inicia sesión con las credenciales del remitente.
        smtp.send_message(msg)                                                        #Envía el correo construido con el asunto, cuerpo y adjunto.

#CONFIRMACION EN CONSOLA
    print(f"Reporte enviado el {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")       #Muestra en pantalla la fecha y hora exacta en que se envió el reporte.

#Programación del envío
schedule.every().monday.at("09:00").do(enviar_reporte)                                #Le dice al programa que ejecute la función enviar_reporte todos los lunes a las 09:00.

#MENSAJE INICIAL
print("Esperando al próximo envío del reporte semanal...")                            #Muestra un mensaje indicando que el programa quedó esperando la hora programada.

#Bucle infinito
while True:                                                                           #Crea un ciclo que nunca termina.(Esto mantiene el programa corriendo todo el tiempo para poder revisar cuándo llega la hora de envío.)
    schedule.run_pending()                                                            #Revisa si hay tareas programadas que deban ejecutarse en ese momento.
    time.sleep(60)                                                                    #Hace una pausa de 60 segundos antes de volver a revisar.(Esto evita que el programa consuma demasiados recursos.)
