import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # keep it if you use database
    database_host: str = os.getenv("MYSQL_HOST")
    database_name: str = os.getenv("MYSQL_DATABASE")
    database_user: str = os.getenv("MYSQL_USER")
    database_password: str = os.getenv("MYSQL_PASSWORD")

    # uncomment if you use aws bucket
    # aws_region_name = os.getenv("AWS_REGION_NAME")
    # aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    # aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    # aws_bucket = os.getenv("AWS_BUCKET")

    # keep it if you use message queue
    broker_url: str = os.environ.get("BROKER_URL", "redis://127.0.0.1:6379/0")
    task_default_queue: str = "default"

    # resources base settings
    resources_folder: str = "project/app/resources"


@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    return settings
