import urllib.parse
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    mongo_user: str
    mongo_password: str
    mongo_base_connection_string: str
    mongo_cluster: str
    mongo_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: str
    postgres_db: str
    postgres_base_connection_string: str
    app_name: str
    debug: bool
    access_token_expire_minutes: int
    access_token_expire_hours: int
    access_token_expire_days: int
    jwt_algorithm: str
    secret_key: str


    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def jwt_secret(self)->int:
        hours:int = self.access_token_expire_hours
        days:int = self.access_token_expire_days
        minutes:int = self.access_token_expire_minutes

        total_in_minutes: int = minutes * hours * days

        return total_in_minutes

    @property
    def mongo_connection(self)->str:
        user = urllib.parse.quote_plus(self.mongo_user)
        password = urllib.parse.quote_plus(self.mongo_password)
        cluster = urllib.parse.quote_plus(self.mongo_cluster)
        return self.mongo_base_connection_string.format(
            USER=user,
            PASSWORD=password,
            CLUSTER=cluster
        )


    @property
    def postgres_connection(self)->str:
        user = urllib.parse.quote_plus(self.postgres_user)
        password = urllib.parse.quote_plus(self.postgres_password)
        host = self.postgres_host
        port = self.postgres_port
        db = self.postgres_db
        return self.postgres_base_connection_string.format(
            USER=user,
            PASSWORD=password,
            HOST=host,
            PORT=port,
            NAME=db
        )

settings = Settings()
