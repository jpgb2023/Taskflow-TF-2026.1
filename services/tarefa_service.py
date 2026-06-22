from database.conexao import Conexao
from models.tarefa import Tarefa


class TarefaService:
    def __init__(self):
        self.conexao = Conexao()
        self.conn = self.conexao.conectar()

    def _reconectar_se_necessario(self):
        if not self.conn or not self.conn.is_connected():
            self.conn = self.conexao.conectar()
        return self.conn

    def criar_tarefa(self, tarefa):
        conn = self._reconectar_se_necessario()
        if not conn:
            return False, "Não foi possível conectar ao banco de dados."

        cursor = conn.cursor()
        try:
            query = """
                INSERT INTO tarefas (titulo, descricao, prioridade, data_tarefa, concluida)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                tarefa.titulo,
                tarefa.descricao,
                tarefa.prioridade,
                tarefa.data_tarefa,
                tarefa.concluida
            ))
            conn.commit()
            print("Tarefa criada com sucesso!")
            return True, "Sucesso"
        except Exception as e:
            conn.rollback()
            error_msg = f"Erro ao inserir no banco: {e}"
            print(error_msg)
            return False, error_msg
        finally:
            cursor.close()

    def editar_tarefa(self, tarefa):
        conn = self._reconectar_se_necessario()
        if not conn:
            return False, "Não foi possível conectar ao banco de dados."

        cursor = conn.cursor()
        try:
            query = """
                UPDATE tarefas
                SET titulo = %s, descricao = %s, prioridade = %s, data_tarefa = %s
                WHERE id = %s
            """
            cursor.execute(query, (
                tarefa.titulo,
                tarefa.descricao,
                tarefa.prioridade,
                tarefa.data_tarefa,
                tarefa.id
            ))
            conn.commit()
            print(f"Tarefa {tarefa.id} editada com sucesso!")
            return True, "Sucesso"
        except Exception as e:
            conn.rollback()
            error_msg = f"Erro ao editar tarefa: {e}"
            print(error_msg)
            return False, error_msg
        finally:
            cursor.close()

    def inserir_tarefas_exemplo(self):
        conn = self._reconectar_se_necessario()
        if not conn:
            return False

        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM tarefas")
            count = cursor.fetchone()[0]

            if count == 0:
                print("Inserindo tarefas de exemplo...")
                tarefas_exemplo = [
                    ("Estudar Python", "Praticar conceitos básicos e avançados", "Alta", "2026-06-18"),
                    ("Fazer exercícios físicos", "Ir à academia ou caminhar no parque", "Média", "2026-06-18"),
                    ("Revisar projeto TaskFlow", "Verificar bugs e melhorias pendentes", "Alta", "2026-06-19"),
                    ("Comprar mantimentos", "Ir ao supermercado comprar itens básicos", "Baixa", "2026-06-20")
                ]

                query = """
                    INSERT INTO tarefas (titulo, descricao, prioridade, data_tarefa, concluida)
                    VALUES (%s, %s, %s, %s, %s)
                """
                for t in tarefas_exemplo:
                    cursor.execute(query, (t[0], t[1], t[2], t[3], False))

                conn.commit()
                print("Tarefas de exemplo inseridas com sucesso!")
                return True
        except Exception as e:
            conn.rollback()
            print(f"Erro ao inserir tarefas de exemplo: {e}")
        finally:
            cursor.close()
        return False

    def listar_tarefas(self, filtro=None):
        conn = self._reconectar_se_necessario()
        tarefas = []
        if not conn:
            return tarefas

        cursor = conn.cursor(dictionary=True)
        try:
            query = "SELECT * FROM tarefas"
            if filtro == "pendentes":
                query += " WHERE concluida = FALSE"
            elif filtro == "concluidas":
                query += " WHERE concluida = TRUE"

            cursor.execute(query)
            for row in cursor.fetchall():
                tarefas.append(Tarefa(
                    id=row['id'],
                    titulo=row['titulo'],
                    descricao=row['descricao'],
                    prioridade=row['prioridade'],
                    data_tarefa=row['data_tarefa'],
                    concluida=row['concluida']
                ))
        except Exception as e:
            print(f"Erro ao listar tarefas: {e}")
        finally:
            cursor.close()
        return tarefas

    def marcar_como_concluida(self, tarefa_id):
        conn = self._reconectar_se_necessario()
        if not conn:
            return False

        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE tarefas SET concluida = TRUE WHERE id = %s", (tarefa_id,))
            conn.commit()
            print(f"Tarefa {tarefa_id} marcada como concluída!")
            return True
        except Exception as e:
            conn.rollback()
            print(f"Erro ao marcar tarefa como concluída: {e}")
            return False
        finally:
            cursor.close()

    def excluir_tarefa(self, tarefa_id):
        conn = self._reconectar_se_necessario()
        if not conn:
            return False

        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM tarefas WHERE id = %s", (tarefa_id,))
            conn.commit()
            print(f"Tarefa {tarefa_id} excluída com sucesso!")
            return True
        except Exception as e:
            conn.rollback()
            print(f"Erro ao excluir tarefa: {e}")
            return False
        finally:
            cursor.close()
