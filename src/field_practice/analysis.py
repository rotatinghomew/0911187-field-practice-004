"""检查现场问题到验证证据之间的项目链路。"""

from collections import defaultdict
from .field_conditions import usable_trials as select_usable_trials


def summarize(records):
    projects = defaultdict(list)
    for record in records:
        projects[str(record["project_id"])].append(record)
    result = {}
    for project, entries in sorted(projects.items()):
        entries.sort(key=lambda item: (item.get("date", ""), item["id"]))
        versions = {entry["version"] for entry in entries if entry.get("kind") in {"model", "trial"}}
        field_conditions = {entry.get("condition") for entry in entries if entry.get("kind") == "feedback"}
        usable_trials = select_usable_trials(entries)
        result[project] = {
            "problem_ids": [entry["id"] for entry in entries if entry.get("kind") == "field_problem"],
            "assumption_ids": [entry["id"] for entry in entries if entry.get("kind") == "assumption"],
            "model_versions": sorted(versions),
            "trial_versions": sorted({entry["version"] for entry in usable_trials}),
            "trial_count": sum(1 for entry in entries if entry.get("kind") == "trial"),
            "usable_trial_count": len(usable_trials),
            "feedback_conditions": sorted(str(value) for value in field_conditions if value is not None),
            "unverified": not usable_trials,
        }
    return result
