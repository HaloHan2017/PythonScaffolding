"""Application configuration management"""

import os
from functools import lru_cache
from pathlib import Path
from typing import Optional

# Load .env file
try:
    from dotenv import load_dotenv

    # Load .env from project root
    env_path = Path(__file__).parent.parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
except ImportError:
    # python-dotenv not installed, skip
    pass


class Config:
    """Base configuration"""

    # Application
    APP_NAME: str = "Flask API Scaffold"
    DEBUG: bool = False

    # Database
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


class LocalConfig(Config):
    """local configuration"""

    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"


class CloudConfig(Config):
    """cloud configuration"""

    DEBUG: bool = False
    LOG_LEVEL: str = "WARNING"


@lru_cache()
def get_config() -> Config:
    """Get configuration based on environment"""
    env = os.getenv("FLASK_ENV", "local").lower()

    config_map = {
        "local": LocalConfig,
        "cloud": CloudConfig,
    }

    config_class = config_map.get(env, LocalConfig)
    return config_class()


# Convenience instance
settings = get_config()
