"""
import os

HOST: str = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", "2001"))
DEBUG: bool = os.getenv("DEBUG", "False") == "True"

VERSION: str = os.getenv("VERSION", "1.0.0")
TITLE: str = os.getenv("TITLE", "MICROSERVICE-MOVIE")

DATABASE_URL: str = os.getenv("DATABASE_URL", "")
DATABASE_URL_DEV: str = os.getenv("DATABASE_URL_DEV", "")

ALLOW_ORIGINS: list[str] = os.getenv("ALLOW_ORIGINS", "*").split(",")
ALLOW_CREDENTIALS: bool = os.getenv("ALLOW_CREDENTIALS", "False") == "True"
ALLOW_METHODS: list[str] = os.getenv("ALLOW_METHODS", "*").split(",")
ALLOW_HEADERS: list[str] = os.getenv("ALLOW_HEADERS", "*").split(",")

ALLOW_EXTENSIONS_FILE_IMG: list[str] = os.getenv("ALLOW_EXTENSIONS_FILE_IMG").split(",")
ALLOW_EXTENSIONS_FILE_VIDEO: list[str] = os.getenv("ALLOW_EXTENSIONS_FILE_VIDEO").split(",")

MAX_SIZE_VIDEO_FILE_MB: int = int(os.getenv("MAX_SIZE_VIDEO_FILE_MB", "100"))
MAX_SIZE_IMG_FILE_MB: int = int(os.getenv("MAX_SIZE_IMG_FILE_MB", "7"))
"""
from dotenv import dotenv_values

config: dict = dotenv_values(".env")

HOST: str = config.get("HOST", "0.0.0.0")
PORT: int = int(config.get("PORT", "2001"))
DEBUG: bool = config.get("DEBUG", "False") == "True"

VERSION: str = config.get("VERSION", "1.0.0")
TITLE: str = config.get("TITLE", "MICROSERVICE-MOVIE")

DATABASE_URL: str = config.get("DATABASE_URL", "")
DATABASE_URL_DEV: str = config.get("DATABASE_URL_DEV", "")

ALLOW_ORIGINS: list[str] = config.get("ALLOW_ORIGINS", "*").split(",")
ALLOW_CREDENTIALS: bool = config.get("ALLOW_CREDENTIALS", "False") == "True"
ALLOW_METHODS: list[str] = config.get("ALLOW_METHODS", "*").split(",")
ALLOW_HEADERS: list[str] = config.get("ALLOW_HEADERS", "*").split(",")

ALLOW_EXTENSIONS_FILE_IMG: list[str] = config.get("ALLOW_EXTENSIONS_FILE_IMG").split(",")
ALLOW_EXTENSIONS_FILE_VIDEO: list[str] = config.get("ALLOW_EXTENSIONS_FILE_VIDEO").split(",")

MAX_SIZE_VIDEO_FILE_MB: int = int(config.get("MAX_SIZE_VIDEO_FILE_MB", "100"))
MAX_SIZE_IMG_FILE_MB: int = int(config.get("MAX_SIZE_IMG_FILE_MB", "7"))