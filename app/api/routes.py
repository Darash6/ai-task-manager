from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse
from app.services.ollama_service import gerar_tarefa

router = APIRouter()


@router.get("/tasks", response_model=list[TaskResponse])
def listar_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


@router.post("/tasks", response_model=TaskResponse)
def criar_task(task: TaskCreate, db: Session = Depends(get_db)):
    nova = Task(
        title=task.title,
        description=task.description
    )
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


@router.post("/tasks/ai", response_model=TaskResponse)
def criar_task_ai(texto: str, db: Session = Depends(get_db)):
    titulo, descricao = gerar_tarefa(texto)

    nova = Task(
        title=titulo,
        description=descricao
    )

    db.add(nova)
    db.commit()
    db.refresh(nova)

    return nova