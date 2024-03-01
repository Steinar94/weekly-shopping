# config.py
import tomli
from pathlib import Path
from pydantic_settings import BaseSettings

ROOT_PATH = Path(__file__).parent.absolute()


class Settings(BaseSettings):
    # Mail Settings
    email_server: str
    email_port: int
    email_username: str
    email_password: str
    email_sender: str
    email_to: str
    email_from: str
    email_recipients: list

    # App settings
    template_path: Path = ROOT_PATH.parent / "templates"
    debug: bool


with open(ROOT_PATH / "config.toml", "rb") as f:
    config = tomli.load(f)

settings = Settings(
    email_server=config["email_settings"]["server"],
    email_port=config["email_settings"]["port"],
    email_username=config["email_settings"]["username"],
    email_password=config["email_settings"]["password"],
    email_sender=config["email_settings"]["sender"],
    email_to=config["email_settings"]["to"],
    email_from=config["email_settings"]["from"],
    email_recipients=config["email_settings"]["recipients"],
    debug=config["app_settings"]["debug"],
)
