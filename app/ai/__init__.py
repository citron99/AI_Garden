from app.ai.base import AIGateway, AIProviderError
from app.config import settings


def create_ai_gateway(provider: str) -> AIGateway:
    normalized = provider.strip().lower()
    if normalized == "mock":
        from app.ai.providers.mock import MockAIGateway

        return MockAIGateway()
    if normalized == "openai":
        from app.ai.providers.openai_multimodal import OpenAIMultimodalGateway

        if not settings.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY обязателен для AI_PROVIDER=openai")
        return OpenAIMultimodalGateway(
            api_key=settings.openai_api_key,
            model=settings.openai_model,
            timeout_seconds=settings.openai_timeout_seconds,
        )
    raise RuntimeError(f"AI_PROVIDER={provider!r} не поддерживается")


__all__ = ["AIGateway", "AIProviderError", "create_ai_gateway"]
