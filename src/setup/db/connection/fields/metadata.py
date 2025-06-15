from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import MetaData


class ConnectionMetaData:
    def __init__(self):
        self.__metadata: MetaData = MetaData()

    async def sync(self, engine: AsyncEngine) -> None:
        async with engine.begin() as conn:
            await conn.run_sync(self.metadata.reflect)    

    @property
    def metadata(self):
        return self.__metadata
    