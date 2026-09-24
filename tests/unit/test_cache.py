from aiutils.cache import MemoryCache


def test_cache() -> None:
    cache = MemoryCache()

    cache.set("name", "Taruneshwar")

    assert cache.get("name") == "Taruneshwar"

    cache.delete("name")

    assert cache.get("name") is None

def test_cache_delete() -> None:
    cache = MemoryCache()

    cache.set("name", "Tarun")
    cache.delete("name")

    assert cache.get("name") is None


def test_cache_clear() -> None:
    cache = MemoryCache()

    cache.set("a", "1")
    cache.set("b", "2")

    cache.clear()

    assert cache.get("a") is None
    assert cache.get("b") is None