import unittest
import time
from question_c import Cache


class TestVersionCompare(unittest.TestCase):
    def test_cache(self):
        cache = Cache(3, 999)
        cache.add(2)
        cache.add(4)
        cache.add(7)
        self.assertEqual(cache.get(2), 2)
        cache.add(123)
        self.assertIsNone(cache.get(4))
        self.assertEqual(cache.get(7), 7)

        self.assertIsNone(cache.get(13))

    def test_expired(self):
        cache=Cache(3,0)
        cache.add(33)

        #sleeps for 3 seconds to make sure the cache has expired
        time.sleep(3)
        self.assertIsNone(cache.get(33))

    def test_to_json(self):
        cache1 = Cache(3,1)
        cache2 = Cache(3,1)

        cache1.add(1)
        cache1.add(2)
        cache1.add(3)

        json = cache1.to_json()
        cache2.resync(json)

        self.assertEqual(cache2.get(2),2)

    def test_expired_resync(self):
        cache1 = Cache(3, 0)
        cache2 = Cache(3, 1)

        cache1.add(1)
        cache1.add(2)
        cache1.add(3)

        json = cache1.to_json()
        cache2.resync(json)

        self.assertIsNone(cache2.get(2))