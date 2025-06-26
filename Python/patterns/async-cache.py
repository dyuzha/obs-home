import asyncio
import time
from abc import ABC, abstractmethod

class AsyncBaseCache(ABC):
    def __init__(self, ttl_seconds=300):
        self._data = None
        self._timestamp = 0
        self.ttl = ttl_seconds
        self._lock = asyncio.Lock()

    async def get(self):
        async with self._lock:
            if self._data is None or (time.time() - self._timestamp) > self.ttl:
                self._data = await self.load()
                self._timestamp = time.time()
            return self._data

    async def refresh(self):
        async with self._lock:
            self._data = await self.load()
            self._timestamp = time.time()

    def invalidate(self):
        self._data = None
        self._timestamp = 0

    @abstractmethod
    async def load(self):
        pass
