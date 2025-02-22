from reportlab.pdfgen import canvas
from textwrap import wrap
from sqlalchemy.orm import Session
from app.db.model import Notes

from io import BytesIO

class Pdf_Use_Case:
    def __init__(self,db_session:Session,id:int):
        self.db_session=db_session
        self.id=id
        note = db_session.query(Notes).where(Notes.id==self.id).first()
        self.title = note.title
        self.text = note.text
        self.date  = str(note.created_at.strftime("%d-%m-%Y"))
        
    
    def creat_pdf(self):
        buffer = BytesIO()

        
        c = canvas.Canvas(buffer)
        
        
        
       
        c.drawString(250, 800, self.title)
        c.drawString(50, 600, self.text)
        c.drawString(400, 400, self.date)

        
        c.showPage()
        c.save()
    
    def create_pdf_in_memory(self):
        
        buffer = BytesIO()

        
        c = canvas.Canvas(buffer)

        
        c.setFont("Times-Roman",36)
        c.drawCentredString(300, 800, self.title)

        text_object = c.beginText(40, 680)  
        text_object.setFont("Courier", 18)
        max_width = 500  

        
        wrapped_text = wrap(self.text, width=int(max_width / 10))  

        
        for line in wrapped_text:
            text_object.textLine(line)

            
            if text_object.getY() < 50:  
                c.drawText(text_object)
                c.showPage()  # Nova página
                text_object = c.beginText(40, 680) 
                text_object.setFont("Courier", 18)

        
        c.drawText(text_object)

        
        c.setFont("Courier",20)
        c.drawString(400, 165, self.date)

        
        c.showPage()
        c.save()

        
        buffer.seek(0)

        return buffer
        
        
      
        
        


    
