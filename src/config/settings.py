"""

Production configuration management.

Loads environment variables using Pydantic Settings.

"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    """Application settings loaded from environment variables."""

    # Application

    APP_NAME: str = "AI Research Assistant"

    APP_ENV: str = "development"

    DEBUG: bool = True

    # API

    API_V1_PREFIX: str = "/api/v1"

    REQUEST_TIMEOUT: int = 30

    # Streamlit

    STREAMLIT_SERVER_PORT: int = 8501

    # AI Providers

    OPENAI_API_KEY: str | None = None

    ANTHROPIC_API_KEY: str | None = None

    model_config = SettingsConfigDict(

        env_file=".env",

        env_file_encoding="utf-8",

        case_sensitive=True,

    )

@lru_cache()

def get_settings() -> Settings:

    """Returns a cached Settings instance."""

    return Settings()