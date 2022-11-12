from fa_analysis.requests import CreateAnalysisRequest
from ninja import NinjaAPI

api = NinjaAPI(title="DLLAB Sample App", version="1.0.0")


@api.post("/analysis", summary="分析作成エンドポイント")
def create(request, data: CreateAnalysisRequest):
    return "Hello, World"
