import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import app


def record(report_id, report, item, colour=None, brand=None, place=None, day=date(2026, 10, 5)):
    return {
        "id": report_id, "date": day.isoformat(), "report": report,
        "date_value": day,
        "details": {"item": item, "colour": colour, "brand": brand, "place": place, "summary": report}
    }


class MatcherTests(unittest.TestCase):
    def test_likely_match(self):
        lost = record("L1", "Black Samsung phone library", "phone", "black", "Samsung", "library")
        found = record("F1", "Black Samsung phone library", "phone", "black", "Samsung", "library")
        result = app.score_pair(lost, found)
        self.assertEqual(result["level"], "likely")
        self.assertEqual(result["score"], 5)

    def test_possible_match(self):
        lost = record("L1", "Blue bottle", "bottle", "blue")
        found = record("F1", "Blue bottle", "bottle", "blue")
        result = app.score_pair(lost, found)
        self.assertEqual(result["level"], "possible")
        self.assertEqual(result["score"], 2)

    def test_colour_mismatch_rejected(self):
        lost = record("L1", "Red bottle", "bottle", "red")
        found = record("F1", "Blue bottle", "bottle", "blue")
        self.assertIsNone(app.score_pair(lost, found))

    def test_different_items_rejected(self):
        lost = record("L1", "Black phone", "phone", "black")
        found = record("F1", "Black wallet", "wallet", "black")
        self.assertIsNone(app.score_pair(lost, found))

    def test_old_reports_rejected(self):
        lost = record("L1", "Black phone", "phone", "black", day=date(2026, 12, 10))
        found = record("F1", "Black phone", "phone", "black", day=date(2026, 10, 5))
        self.assertIsNone(app.score_pair(lost, found))

    def test_fact_check_removes_guessed_brand(self):
        details = {"item": "phone", "colour": "black", "brand": "Samsung",
                   "place": "library", "summary": "Black phone"}
        checked = app.check_facts(details, "Black phone near library")
        self.assertIsNone(checked["brand"])
        self.assertEqual(checked["colour"], "black")
        self.assertEqual(checked["place"], "library")


if __name__ == "__main__":
    unittest.main()
