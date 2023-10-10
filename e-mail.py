import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Configurações de e-mail
remetente_email = 'seu_email@gmail.com'
senha = 'sua_senha'  # Insira sua senha aqui
destinatario_email = 'destinatario@example.com'
assunto = 'Assunto do E-mail'
mensagem = 'Corpo do e-mail.'

# Configuração do servidor SMTP (exemplo para o Gmail)
smtp_servidor = 'smtp.gmail.com'
smtp_porta = 587

# Crie o objeto SMTP
server = smtplib.SMTP(smtp_servidor, smtp_porta)
server.starttls()
server.login(remetente_email, senha)

# Crie a mensagem
msg = MIMEMultipart()
msg['From'] = remetente_email
msg['To'] = destinatario_email
msg['Subject'] = assunto

# Adicione o corpo do e-mail
msg.attach(MIMEText(mensagem, 'plain'))

# Anexe um arquivo (opcional)
arquivo_anexo = 'anexo.txt'
with open(arquivo_anexo, 'rb') as anexo:
    part = MIMEApplication(anexo.read(), Name='anexo.txt')
    part['Content-Disposition'] = f'attachment; filename="{arquivo_anexo}"'
    msg.attach(part)

# Envie o e-mail
server.sendmail(remetente_email, destinatario_email, msg.as_string())

# Encerre a conexão SMTP
server.quit()

print('E-mail enviado com sucesso!')
