import sqlite3


DATABASE = "alunos.db"


def conectar():

    return sqlite3.connect(DATABASE)


def criar_tabela():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def inserir_aluno(nome, email, idade):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO alunos (nome, email, idade)
        VALUES (?, ?, ?)
    """, (nome, email, idade))

    conexao.commit()

    id_aluno = cursor.lastrowid

    conexao.close()

    return id_aluno


def buscar_alunos():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email, idade
        FROM alunos
        ORDER BY id
    """)

    registros = cursor.fetchall()

    conexao.close()

    alunos = []

    for registro in registros:

        alunos.append({
            "id": registro[0],
            "nome": registro[1],
            "email": registro[2],
            "idade": registro[3]
        })

    return alunos


def buscar_aluno(id):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email, idade
        FROM alunos
        WHERE id = ?
    """, (id,))

    registro = cursor.fetchone()

    conexao.close()

    if registro is None:
        return None

    return {
        "id": registro[0],
        "nome": registro[1],
        "email": registro[2],
        "idade": registro[3]
    }


def atualizar_aluno(id, nome, email, idade):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE alunos
        SET nome = ?, email = ?, idade = ?
        WHERE id = ?
    """, (nome, email, idade, id))

    conexao.commit()

    alterados = cursor.rowcount

    conexao.close()

    return alterados


def excluir_aluno(id):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM alunos
        WHERE id = ?
    """, (id,))

    conexao.commit()

    excluidos = cursor.rowcount

    conexao.close()

    return excluidos