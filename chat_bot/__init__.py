from dotenv import load_dotenv

from chat_bot.logger import setup_logger

setup_logger()
load_dotenv(dotenv_path=".env")
