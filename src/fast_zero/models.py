from sqlalchemy.orm import registry, Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime

table_registry = registry()

@table_registry.mapped_as_dataclass()
class User:
    """
    User model for the database.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
