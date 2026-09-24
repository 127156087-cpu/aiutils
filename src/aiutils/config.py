from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str="aiutils"
    version:str="0.1.0"
    debug: bool=False