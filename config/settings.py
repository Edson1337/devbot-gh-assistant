from decouple import config

class Settings:
    """Application settings"""
    
    def __init__(self):
        self.azure_openai_api_key = config('AZURE_OPENAI_API_KEY', default=None)
        self.azure_openai_endpoint = config('AZURE_OPENAI_ENDPOINT', default=None)
        self.azure_openai_deployment_name = config('AZURE_OPENAI_DEPLOYMENT_NAME', default=None)
    
    def validate(self):
        """Validates that all required settings are present"""
        if not all([self.azure_openai_api_key, self.azure_openai_endpoint, self.azure_openai_deployment_name]):
            raise ValueError("Missing required Azure OpenAI configuration")

settings = Settings()