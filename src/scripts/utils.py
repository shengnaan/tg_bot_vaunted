import random

from core.config import Settings


def get_url_with_random_tag() -> str:
    return f"https://cataas.com/cat?tag={random.choice(Settings.CAT_TAGS)}"

