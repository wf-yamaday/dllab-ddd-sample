from abc import ABC, abstractmethod

from fa_analysis.domains import Analysis as DomainAnalysis


class AbstractAnalysisRepository(ABC):
    @abstractmethod
    def save(self, analysis: DomainAnalysis) -> DomainAnalysis:
        """Domain層のAnalysisを永続化するメソッド

        Args:
            analysis (Analysis): Domain層のAnalysisオブジェクト

        Returns:
            Analysis: 保存済みのAnalysisオブジェクト。別のインスタンスとして返す
        """
        ...
