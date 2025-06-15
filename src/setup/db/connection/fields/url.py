from typing import TypedDict
from logging import getLogger

from sqlalchemy.engine import make_url, URL


DATABASE_DRIVERNAME_MAP = {
    # PostgreSQL with asyncpg (high performance)
    "postgresql": "postgresql+asyncpg",

    # MySQL with aiomysql (most stable async support)
    "mysql": "mysql+aiomysql",

    # SQLite with aiosqlite (good for local/dev use)
    "sqlite": "sqlite+aiosqlite",

    # Oracle - no mature async driver; fallback to sync
    "oracle": "oracle+cx_oracle",

    # MSSQL with pyodbc (no solid async support yet)
    "mssql": "mssql+pyodbc",

    # MariaDB with asyncmy (specific to MariaDB, faster than aiomysql for some workloads)
    "mariadb": "mariadb+asyncmy"
}


logger = getLogger(__name__)


class UrlConfig(TypedDict):
    """
    Configuration model for database URL management.

    Attributes:
        initial_url (Optional[str]): Direct database URL string (overrides env).
        url_env (Optional[str]): Environment variable name to fetch the URL from.
        database_drivername_map (Dict[str, str]): Mapping of base database names
            (e.g., 'postgresql') to full SQLAlchemy driver names
            (e.g., 'postgresql+asyncpg').
    
    Validation:
        Exactly one of `initial_url` or `url_env` must be provided.
    """

    url: str


class ConnectionUrl:

    def __init__(self, **config: UrlConfig) -> None:
        self.__url = None
        self.set_url(config["url"])

    @property
    def database_drivername_map(self) -> dict[str, str]:
        return DATABASE_DRIVERNAME_MAP
    
    def set_url(self, url: str) -> None:
        """
        Set and normalize the internal database URL.

        Args:
            url (str): Raw database URL string.

        Side Effects:
            Updates the internal URL string to a normalized form with a mapped driver.
        """
        self.__url = url
        self._normalize_url()

    def _normalize_url(self) -> None:
        """
        Normalize the database URL's driver name according to the configured mapping.

        Parses the current URL, extracts the base database type, checks if it is supported,
        substitutes the driver name accordingly, and updates the internal URL string.

        Raises:
            ValueError: If the base database type is not supported by the mapping.
        """
        parsed_url = self.make_url
        original_driver = parsed_url.drivername
        base_database = original_driver.split("+")[0]

        if base_database not in self.database_drivername_map:
            raise ValueError(f"Unsupported database type: '{base_database}'")

        mapped_driver = self.database_drivername_map[base_database]
        normalized_url = parsed_url.set(drivername=mapped_driver)

        # Render URL as string, including password (do not hide)
        self.__url = normalized_url.render_as_string(hide_password=False)

    @property
    def url(self) -> str:
        """
        Get the normalized database URL string.

        Returns:
            str: Fully normalized SQLAlchemy database URL.
        """
        return self.__url

    @property
    def make_url(self) -> URL:
        """
        Parse the internal URL string into a SQLAlchemy URL object.

        Returns:
            sqlalchemy.engine.url.URL: Parsed URL instance for detailed inspection or modification.
        """
        return make_url(self.url)
