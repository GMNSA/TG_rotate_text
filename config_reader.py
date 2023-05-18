from pydantic import BaseSettings, SecretStr


class HostConfig():
    host = "127.0.0.1"
    user = "postgres"
    password = ""
    db_name = "TEST_DB"


class Settings(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        allow_mutation = False


config = Settings()
host_config = HostConfig()
