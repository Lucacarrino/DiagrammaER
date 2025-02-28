import graphviz


grafico = graphviz.Graph(comment="Schema ER")

grafico.node("S", "Studente | {<id> ID(pk) | nome}", shape="record", fontcolor="black")
grafico.node("C", "Corso | {<id> ID(pk) | nome}", shape="record", fontcolor="black")
grafico.node("R", "Iscrizione", shape="diamond")


grafico.edge("S", "R")
grafico.edge("C", "R")


grafico.render("schema", format="png", view=True)
