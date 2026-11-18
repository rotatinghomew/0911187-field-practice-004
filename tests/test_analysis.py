import unittest

from field_practice.analysis import summarize
from field_practice.reports import build_report


class FieldPracticeTests(unittest.TestCase):
    def setUp(self):
        self.records = [
            {"id": "p1", "project_id": "grid", "kind": "field_problem", "date": "2026-01-01", "text": "负荷波动"},
            {"id": "a1", "project_id": "grid", "kind": "assumption", "date": "2026-01-05", "text": "窗口内负荷稳定"},
            {"id": "m1", "project_id": "grid", "kind": "model", "date": "2026-02-01", "version": "v1"},
            {"id": "f1", "project_id": "grid", "kind": "feedback", "date": "2026-02-10", "condition": "检修期"},
            {"id": "t1", "project_id": "grid", "kind": "trial", "date": "2026-02-11", "version": "v1", "condition": "检修期", "result": 1.2},
            {"id": "t2", "project_id": "grid", "kind": "trial", "date": "2026-03-11", "version": "v1", "condition": "常态", "result": 1.4},
        ]

    def test_field_condition_excludes_inapplicable_trial_from_usable_evidence(self):
        project = summarize(self.records)["grid"]
        self.assertEqual(project["trial_count"], 2)
        self.assertEqual(project["usable_trial_count"], 1)
        self.assertEqual(project["trial_versions"], ["v1"])

    def test_report_preserves_chain_ids_and_revision(self):
        report = build_report(self.records, "data-r8")
        self.assertEqual(report["source_revision"], "data-r8")
        self.assertEqual(report["projects"]["grid"]["problem_ids"], ["p1"])
        self.assertEqual(report["projects"]["grid"]["assumption_ids"], ["a1"])


if __name__ == "__main__":
    unittest.main()
