from sqlalchemy.orm import Session
from src.fast_zero.models import User
from sqlalchemy import select

def test_create_user(fix_session: Session):
    user = User(
        username="Ludovico",
        password="123",
        email="ludo@vico.com"
    )
    fix_session.add(user)
    fix_session.commit()
    result = fix_session.scalar(
        select(User).where(User.username == "Ludovico")
    )
    assert result.username == "Ludovico"

