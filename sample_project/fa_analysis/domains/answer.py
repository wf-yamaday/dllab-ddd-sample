from typing import List

from fa_analysis.domains.token import Token
from pydantic import BaseModel


class FreeAnswer(BaseModel):
    """自由回答クラス"""

    id: int
    value: str
    tokens: List[Token]
