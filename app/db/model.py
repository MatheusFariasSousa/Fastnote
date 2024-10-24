from sqlalchemy.orm import registry,mapped_column,Mapped
from app.db.connection import engine
from datetime import datetime
from sqlalchemy import func,ForeignKey



table_registry = registry()



@table_registry.mapped_as_dataclass
class User():
    __tablename__="User_db"
    id:Mapped[int] = mapped_column("id",primary_key=True,autoincrement=True,init=False)
    name:Mapped[str] = mapped_column("name",nullable=False)
    cpf:Mapped[str] = mapped_column("cpf",nullable=False,unique=True)
    password:Mapped[str] = mapped_column("password",nullable=False)
    
    


@table_registry.mapped_as_dataclass
class Notes():
    __tablename__="Note_db"
    id:Mapped[int] = mapped_column("id",primary_key=True,autoincrement=True,init=False)
    title:Mapped[str] = mapped_column("title",nullable=False)
    text:Mapped[str] = mapped_column("text",nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    user_id:Mapped[int] = mapped_column(ForeignKey("User_db.id"))
    





table_registry.metadata.create_all(engine)