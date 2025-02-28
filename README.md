<table style='border:0;'>
  <tr>
    <td  valign="top">
      <pre><code>
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er


Base = declarative_base()


class Studente(Base):
    __tablename__ = "studenti"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    corsi = relationship("Iscrizione")

class Corso(Base):
    __tablename__ = "corsi"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    studenti = relationship("Iscrizione")



class Iscrizione(Base):
    __tablename__ = "iscrizioni"
    id = Column(Integer, primary_key=True)
    studente_id = Column(Integer, ForeignKey("studenti.id"))
    corso_id = Column(Integer, ForeignKey("corsi.id"))
    studente = relationship("Studente")
    corso = relationship("Corso")



database = create_engine("sqlite:///universita.db")
Base.metadata.create_all(database)
render_er("sqlite:///universita.db", "schema.png")
      </code></pre>
    </td>
    <td valign="top">
      <img src="ER ALCHEMY2/schema.png" alt="Schema ER" width="300">
    </td>
  </tr>
</table>
