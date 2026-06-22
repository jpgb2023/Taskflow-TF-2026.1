import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


class Conexao:
    def __init__(
        self,
        host=None,
        user=None,
        password=None,
        database=None
    ):
        self.host = host or os.getenv("DB_HOST", "localhost")
        self.user = user or os.getenv("DB_USER", "root")
        self.password = password or os.getenv("DB_PASSWORD", "")
        self.database = database or os.getenv("DB_NAME", "taskflow")
        self.conexao = None

    def conectar(self):
        if self.conexao and self.conexao.is_connected():
            return self.conexao

        try:
            temp_conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = temp_conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            cursor.close()
            temp_conn.close()

            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if self.conexao.is_connected():
                self._criar_tabela_se_nao_existe()
                print("Conexão ao banco de dados estabelecida com sucesso!")

            return self.conexao

        except Exception as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            return None

    def _criar_tabela_se_nao_existe(self):
        if self.conexao and self.conexao.is_connected():
            cursor = self.conexao.cursor()
            try:
                cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    prioridade VARCHAR(50),
    data_tarefa DATE,
    concluida BOOLEAN DEFAULT FALSE
)
""")
                self.conexao.commit()
            except Exception as e:
                print(f"Erro ao criar tabela: {e}")
            finally:
                cursor.close()

    def desconectar(self):
        if self.conexao and self.conexao.is_connected():
            self.conexao.close()
            self.conexao = None
            print("Conexão ao banco de dados encerrada.")

    def get_cursor(self):
        if self.conexao and self.conexao.is_connected():
            return self.conexao.cursor()
        print("Conexão não estabelecida. Chame conectar() primeiro.")
        return None
