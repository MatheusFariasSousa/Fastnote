from sqlalchemy.orm import Session
from app.db.model import Notes
import smtplib
import email.message

class Emai_Use_Case:
    def __init__(self,db_session:Session):
        self.db_session = db_session
        


    def enviar_email(self,id:int,email_user:str):
        note = self.db_session.query(Notes).where(Notes.id == id).first()
        corpo_email=f""""
            <h1>{note.title}</h1>
            <p>{note.text}</p>
            """

        msg = email.message.Message()
        msg['Subject'] = "Assunto"
        msg["From"]="fast.note1000@gmail.com"
        msg["To"]=email_user
        password="amvtckwyphswedau"
        msg.add_header('Content-Type','text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()

        s.login(msg["From"],password=password)
        s.sendmail(msg["From"],[msg["To"]],msg.as_string().encode("utf-8"))
        print("Email enviado")

    def generate_code():
        return f"{random.randint(100000, 999999)}"

    def send_email(receiver_email: str, code: str):
        sender_email = "seu_email@example.com"
        sender_password = "sua_senha"

        msg = EmailMessage()
        msg['Subject'] = "Seu código de verificação"
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(f"Olá! Seu código de verificação é: {code}")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)









        