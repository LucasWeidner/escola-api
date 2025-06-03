from pydantic import BaseModel, Field
from typing_extensions import Optional


# class CursoTradicional:
#     def __init__(self, id: int, nome: str, sigla: str):
#         self.id = id
#         self.nome = nome
#         self.sigla = sigla
# from dataclasses import dataclass, field


class Curso(BaseModel):
    id: int = Field()
    nome: str = Field()
    sigla: Optional[str] = Field(default=None)


class CursoCadastro(BaseModel):
    nome: str = Field()
    sigla: Optional[str] = Field(default=None)


class CursoEditar(BaseModel):
    nome: str = Field()
    sigla: Optional[str] = Field(default=None)
