from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import (
    criar_tabela,
    inserir_aluno,
    buscar_alunos,
    buscar_aluno,
    atualizar_aluno,
    excluir_aluno
)


app = FastAPI(
    title="API de Alunos",
    description="API didática utilizando FastAPI e SQLite",
    version="1.0.0"
)


criar_tabela()


class Aluno(BaseModel):

    nome: str
    email: str
    idade: int


@app.get("/")
def inicio():

    return {
        "mensagem": "API de Alunos funcionando"
    }


@app.get("/alunos")
def listar_alunos():

    return buscar_alunos()


@app.get("/alunos/{id}")
def consultar_aluno(id: int):

    aluno = buscar_aluno(id)

    if aluno is None:

        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return aluno


@app.post("/alunos")
def criar_aluno(aluno: Aluno):

    id_aluno = inserir_aluno(
        aluno.nome,
        aluno.email,
        aluno.idade
    )

    return {
        "id": id_aluno,
        "mensagem": "Aluno criado com sucesso"
    }


@app.put("/alunos/{id}")
def atualizar(id: int, aluno: Aluno):

    alterados = atualizar_aluno(
        id,
        aluno.nome,
        aluno.email,
        aluno.idade
    )

    if alterados == 0:

        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return {
        "mensagem": "Aluno atualizado com sucesso"
    }


@app.delete("/alunos/{id}")
def excluir(id: int):

    excluidos = excluir_aluno(id)

    if excluidos == 0:

        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return {
        "mensagem": "Aluno excluído com sucesso"
    }