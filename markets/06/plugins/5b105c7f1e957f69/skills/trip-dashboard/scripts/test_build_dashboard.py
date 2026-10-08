import importlib.util
import json
import pathlib
import tempfile
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("build_dashboard.py")
SPEC = importlib.util.spec_from_file_location("build_dashboard", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def sample_data():
    image = [{"url": "https://example.com/image.jpg", "alt": "Example travel image", "credit": "Example", "source_url": "https://example.com"}]
    return {
        "meta": {"title": "Test Trip", "currency": "USD", "travelers": 2, "trip_days": 2, "route": "A -> B", "researched_at": "2026-09-19", "target": 2000, "canonical_total": 1500, "contingency_rate": 0},
        "assumptions": [{"id": "air", "label": "Airfare", "category": "Flights", "value": 800, "min": 0, "max": 2000, "step": 10, "status": "estimated"}],
        "fixed_costs": [{"label": "Rail", "category": "Transport", "amount": 100, "status": "included"}],
        "hotels": [{"base": "A", "options": [{"id": "hotel-a", "name": "Hotel A", "amount": 500, "nights": 1, "location": "Center", "selected": True, "description": "A central hotel.", "why_fit": "Easy access.", "images": image}]}],
        "activities": [{"id": "tour", "name": "Tour", "amount": 100, "selected": True, "day": "Day 1", "source_type": "operator", "url": "https://example.com/tour", "description": "A guided visit.", "why_fit": "Fits the route.", "images": image}],
        "restaurants": [],
        "transport": [],
        "days": [{"label": "Day 1", "date": "2026-10-01", "base": "A", "morning": "Arrive", "afternoon": "Walk", "evening": "Dinner", "transit": "Train", "notes": "Easy day", "commitments": 1}],
        "sources": [{"label": "Operator", "url": "https://example.com", "type": "official", "checked_at": "2026-09-19"}],
    }


class DashboardBuilderTests(unittest.TestCase):
    def test_build_replaces_marker(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            source = root / "trip.json"
            output = root / "dashboard.html"
            source.write_text(json.dumps(sample_data()), encoding="utf-8")
            MODULE.build(source, output)
            rendered = output.read_text(encoding="utf-8")
            self.assertNotIn(MODULE.MARKER, rendered)
            self.assertIn("Test Trip", rendered)
            self.assertIn("https://ko-fi.com/quietengine", rendered)
            self.assertIn("Decision workspace", rendered)
            self.assertIn("Dining", rendered)
            self.assertIn("Compare", rendered)

    def test_duplicate_ids_fail(self):
        data = sample_data()
        data["activities"][0]["id"] = "air"
        with self.assertRaises(ValueError):
            MODULE.validate(data)

    def test_invalid_url_fails(self):
        data = sample_data()
        data["sources"][0]["url"] = "javascript:alert(1)"
        with self.assertRaises(ValueError):
            MODULE.validate(data)

    def test_hotel_requires_one_selection(self):
        data = sample_data()
        data["hotels"][0]["options"][0]["selected"] = False
        with self.assertRaises(ValueError):
            MODULE.validate(data)

    def test_canonical_total_mismatch_fails(self):
        data = sample_data()
        data["meta"]["canonical_total"] = 1499
        with self.assertRaises(ValueError):
            MODULE.validate(data)

    def test_decision_item_requires_image_provenance(self):
        data = sample_data()
        data["activities"][0]["images"] = []
        with self.assertRaises(ValueError):
            MODULE.validate(data)

    def test_transport_requires_one_selection(self):
        data = sample_data()
        data["transport"] = [{"leg": "A to B", "options": [{"id": "train", "name": "Train", "mode": "Rail", "amount": 0, "selected": False, "description": "Fast rail.", "why_fit": "Direct.", "images": data["activities"][0]["images"]}]}]
        with self.assertRaises(ValueError):
            MODULE.validate(data)


if __name__ == "__main__":
    unittest.main()
