import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import calculate

def row(o, start, end):
    return {"outage_id": o, "start": start, "end": end}

class TestOutageDuration(unittest.TestCase):
    def test_duration(self):
        result, _ = calculate([row("O1", "2026-11-03T10:00", "2026-11-03T10:30")])
        self.assertEqual(result[0][1], 30)
    def test_ongoing_excluded(self):
        result, ongoing = calculate([row("O1", "2026-11-03T10:00", "")])
        self.assertEqual(result, [])
        self.assertEqual(ongoing, ["O1"])
    def test_longest_first(self):
        result, _ = calculate([row("A", "2026-11-03T10:00", "2026-11-03T10:10"), row("B", "2026-11-03T10:00", "2026-11-03T11:00")])
        self.assertEqual(result[0][0], "B")
    def test_total_is_sum(self):
        result, _ = calculate([row("A", "2026-11-03T10:00", "2026-11-03T10:10"), row("B", "2026-11-03T10:00", "2026-11-03T10:20")])
        self.assertEqual(sum(m for _, m in result), 30)
