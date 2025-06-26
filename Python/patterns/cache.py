import time
from abc import ABC, abstractmethod

class BaseCache(ABC):
    """
    Абстрактный базовый класс для реализации кеша с TTL (Time To Live).

    Логика:
    - Данные кешируются в памяти.
    - При запросе через метод get() проверяется, не устарели ли данные.
      Если устарели (или еще не загружены), происходит повторная загрузка данных
      через абстрактный метод load(), который должен быть реализован в подклассе.
    - Есть возможность явно обновить кеш вызовом refresh().
    - Можно сбросить кеш вызовом invalidate().
    """

    def __init__(self, ttl_seconds: int = 300):
        """
        :param ttl_seconds: Время жизни кеша в секундах (TTL).
                            По истечении этого времени данные будут обновлены
                            при следующем запросе.
        """
        self._data = None
        self._timestamp = 0
        self.ttl = ttl_seconds

    def get(self):
        """Возвращает кешированные данные"""
        if self._data is None or (time.time() - self._timestamp) > self.ttl:
            self._data = self.load()
            self._timestamp = time.time()
        return self._data

    def refresh(self):
        """Принудительно обновляет данные из источника."""
        self._data = self.load()
        self._timestamp = time.time()

    def invalidate(self):
        """Сбрасывает кеш, очищая данные."""
        self._data = None
        self._timestamp = 0

    @abstractmethod
    def load(self) -> dict:
        """Метод загрузки из источника"""
        ...
