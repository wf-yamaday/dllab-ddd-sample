from fa_analysis.domains import Analysis as DomainAnalysis
from fa_analysis.models.analysis import Analysis, FreeAnswer, Token
from fa_analysis.repositories.abstract import AbstractAnalysisRepository


class AnalysisRepository(AbstractAnalysisRepository):
    """AnalysisRepositoryの実装"""

    def save(self, analysis: DomainAnalysis) -> DomainAnalysis:
        db_analysis = Analysis.from_domain(obj=analysis)
        db_answers = []
        db_tokens = []
        for answer in analysis.answers:
            db_answers.append(
                FreeAnswer.from_domain(obj=answer, analysis_id=analysis.id)
            )
            for token in answer.tokens:
                db_tokens.append(Token.from_domain(obj=token, answer_id=answer.id))

        db_analysis.save()
        FreeAnswer.objects.bulk_create(db_answers)
        Token.objects.bulk_create(db_tokens)
        return db_analysis.to_domain()
