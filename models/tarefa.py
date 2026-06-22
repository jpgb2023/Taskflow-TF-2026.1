class Tarefa:
    def __init__(
        self,
        titulo,
        descricao,
        prioridade,
        data_tarefa,
        id=None,
        concluida=False
    ):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.data_tarefa = data_tarefa
        self.concluida = concluida

    def __repr__(self):
        return f"Tarefa(ID: {self.id}, Título: {self.titulo}, Concluída: {self.concluida})"