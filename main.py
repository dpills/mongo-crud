from typing import Any

import anyio
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    mongo_uri: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Config()

db: AsyncIOMotorDatabase[Any] = AsyncIOMotorClient(
    settings.mongo_uri, tlsAllowInvalidCertificates=True
)["CHANGE_ME"]


async def create() -> None:
    """
    Insert data into Mongo collection
    """
    print("Creating a document")


async def read() -> None:
    """
    Get documents from Mongo collection
    """
    print("Reading documents")


async def update() -> None:
    """
    Update a document in a Mongo collection
    """
    print("Updating a document")


async def delete() -> None:
    """
    Delete a document in a Mongo collection
    """
    print("Deleting a document")


async def main() -> None:
    """
    Mongo CRUD Practice
    """
    operation = "READ"

    if operation == "CREATE":
        await create()
    elif operation == "READ":
        await read()
    elif operation == "UPDATE":
        await update()
    elif operation == "DELETE":
        await delete()


if __name__ == "__main__":
    anyio.run(main)
