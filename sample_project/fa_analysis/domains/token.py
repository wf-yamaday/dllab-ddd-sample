from pydantic import BaseModel


class Token(BaseModel):
    """単語クラス"""

    value: str

    class Config:
        frozen = True
