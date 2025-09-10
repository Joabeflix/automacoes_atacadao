import imaplib

EMAIL = "joabe@samarc.com.br"
SENHA = "bmcq yvjy xdqa uwll"  # senha de app, não a senha normal!

try:
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, SENHA)
    print("✅ IMAP está ativado e conexão bem-sucedida!")
    mail.logout()
except Exception as e:
    print("❌ Erro na conexão:", e)

