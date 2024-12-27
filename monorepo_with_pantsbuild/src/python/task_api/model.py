from sqlalchemy import Column, Integer, String
from task_api.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description}
