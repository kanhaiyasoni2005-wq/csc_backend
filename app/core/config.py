from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra= "ignore")
    DB_CONNECTION:str
    SECRET_KEY:str
    ALGORITHM:str
    EXP_TIME:str
    CASHFREE_SECRET_KEY:str
    CASHFREE_APP_ID:str
    CASHFREE_BASE_URL:str


settings = Settings()