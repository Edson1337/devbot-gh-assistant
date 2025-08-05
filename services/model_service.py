from langchain_openai import ChatOpenAI
from config.settings import settings

class ModelService:
    """Service responsible for initializing and configuring the model"""
    
    def __init__(self):
        self._model = None
    
    def get_model(self) -> ChatOpenAI:
        """Returns a configured instance of the model"""
        if self._model is None:
            self._model = ChatOpenAI(
                model=settings.azure_openai_deployment_name,
                api_key=settings.azure_openai_api_key,
                base_url=settings.azure_openai_endpoint,
            )
        return self._model