from typing import TypeVar, Optional
import os
from logging import getLogger


logger = getLogger(__name__)


T = TypeVar("T")


def get_env(key: str) -> str | None:
    """
    A os.getenv wrapper which logs agressively the process on debug mode.
    """
    logger.debug(f"Extracting env: key=\"{key}\"")
    env_value = os.getenv(key)

    if env_value is None:
        logger.debug(f"Could not find env: key=\"{key}\"")
        return
    
    logger.debug(f"Env was successfully found: key=\"{key}\"")
    return env_value


def if_none(value: Optional[T], default: T) -> T:
    """
    Returns the given value if it is not None; otherwise returns the provided default.

    This utility is helpful for safely falling back to default values in a more expressive way,
    and ensures consistent handling of None values.

    Args:
        value (Optional[T]): The primary value to check.
        default (T): The fallback value to return if `value` is None.

    Returns:
        T: Either `value` if it is not None, or `default`.
    """
    if value is not None:
        logger.debug(f"[if_none] Returning provided value: {value}")
        return value

    logger.debug(f"[if_none] Value is None. Returning default: {default}")
    return default
