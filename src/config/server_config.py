from psutil import cpu_count

from .base_config import base_config
from .yml_schema.schema_fields.server import Server
from src.utils.misc import if_none


config = if_none(base_config.server, Server())

WORKERS_COUNT = if_none(config.workers, cpu_count() * 2 + 1)
THREADS_COUNT = if_none(config.threads, 1)
TIMEOUT = if_none(config.timeout, 30)
KEEP_ALIVE = if_none(config.keep_alive)
