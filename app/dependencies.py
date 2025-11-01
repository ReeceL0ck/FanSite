from typing import Annotated
from dotenv import load_dotenv

from fastapi import Header, HTTPException
import os
load_dotenv()

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != os.getenv("X_TOKEN"):
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
