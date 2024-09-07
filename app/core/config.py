from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://root:root@localhost:5432/url_shortener"

    class Config:
        env_file = ".env"

settings = Settings()

