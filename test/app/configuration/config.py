from dotenv import load_dotenv
from os import path, environ

load_dotenv()


class Settings:

    BASE_DIR: str = path.dirname(path.abspath(path.join(__file__, "../..")))


settings = Settings()
