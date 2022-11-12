from django.db import models
from fa_analysis.domains.analysis import Analysis as DomainAnalysis
from fa_analysis.domains.answer import FreeAnswer as DomainFreeAnswer
from fa_analysis.domains.token import Token as DomainToken


class Analysis(models.Model):
    """Domain層のAnalysisとマッピングされるDjangoモデル"""

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    @classmethod
    def from_domain(cls, obj: DomainAnalysis) -> "Analysis":
        """ドメインモデルからのファクトリメソッド"""
        return cls(id=obj.id, name=obj.name)

    def to_domain(self) -> DomainAnalysis:
        """Djangoモデルからドメインモデルに変換するメソッド"""
        return DomainAnalysis(
            id=self.id,
            name=self.name,
            answers=[a.to_domain() for a in FreeAnswer.objects.filter(analysis=self)],
        )


class FreeAnswer(models.Model):
    """Domain層のFreeAnswerとマッピングされるDjangoモデル"""

    id = models.IntegerField(primary_key=True)
    value = models.TextField()
    analysis = models.ForeignKey(to=Analysis, on_delete=models.CASCADE)

    @classmethod
    def from_domain(cls, obj: DomainFreeAnswer, analysis_id: int) -> "FreeAnswer":

        """ドメインモデルからのファクトリメソッド"""

        return cls(
            id=obj.id,
            value=obj.value,
            analysis=Analysis(id=analysis_id),
        )

    def to_domain(self) -> DomainFreeAnswer:
        return DomainFreeAnswer(
            id=self.id,
            value=self.value,
            tokens=[t.to_domain() for t in Token.objects.filter(free_answer=self)],
        )


class Token(models.Model):
    """Domain層のTokenとマッピングされるDjangoモデル"""

    value = models.CharField(max_length=256)
    free_answer = models.ForeignKey(to=FreeAnswer, on_delete=models.CASCADE)

    @classmethod
    def from_domain(cls, obj: DomainToken, answer_id: int) -> "Token":
        """ドメインモデルからのファクトリメソッド"""
        return cls(value=obj.value, free_answer=FreeAnswer(id=answer_id))

    def to_domain(self) -> DomainToken:
        return DomainToken(value=self.value)
