import pytest
from fa_analysis.domains import Analysis, FreeAnswer, Token
from fa_analysis.repositories.analysis import AnalysisRepository


class TestAnalysisRepository:
    @pytest.fixture
    def init_test(self) -> None:
        self.repository = AnalysisRepository()

    @pytest.mark.django_db
    def test_save(self, init_test: str) -> None:
        tokens = [
            Token(value="すもも"),
            Token(value="も"),
            Token(value="もも"),
            Token(value="も"),
            Token(value="もも"),
            Token(value="の"),
            Token(value="うち"),
        ]
        answers = [FreeAnswer(id=1, value="すもももももももものうち", tokens=tokens)]
        analysis = Analysis(id=1, name="分析サンプル", answers=answers)
        result = self.repository.save(analysis=analysis)

        assert result.id == analysis.id
        assert result.answers == analysis.answers
