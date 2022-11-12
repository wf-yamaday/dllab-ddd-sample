from typing import List

from fa_analysis.domains.answer import FreeAnswer
from pydantic import BaseModel


class Analysis(BaseModel):
    """分析クラス"""

    id: int
    name: str
    answers: List[FreeAnswer]
