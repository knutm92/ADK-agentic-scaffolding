from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    """
    App settings fetched from env variables
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    # Google API
    google_api_key: str | None = None