# Automatización de Reportes Semanales por Correo

Script en Python que automatiza el envío semanal de un reporte Excel
por correo electrónico, usando programación de tareas (schedule) y
envío seguro vía SMTP.

## Problema que resuelve
Elimina el envío manual y recurrente de reportes, ejecutándose de
forma programada sin intervención humana.

## Tecnologías
Python · smtplib · schedule · email.message

## Configuración
1. `pip install schedule`
2. Definir variables de entorno EMAIL_ADDRESS y EMAIL_PASSWORD
   (usar una contraseña de aplicación de Gmail, nunca la real)
3. Ajustar REPORTE_PATH a la ubicación del archivo a enviar

## Ejecución
python reporte_semanal_smtp.py
