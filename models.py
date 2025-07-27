from sqlalchemy import Column, String, Enum, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum

Base = declarative_base()

class JobStatus(str, enum.Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True)
    job_type = Column(String)
    status = Column(Enum(JobStatus))
    result_path = Column(Text, nullable=True)

engine = create_engine("sqlite:///./jobs.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
