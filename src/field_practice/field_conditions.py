"""判定试用记录是否处于已登记的限制工况。"""


def usable_trials(records):
    restricted = {
        (str(row["project_id"]), str(row.get("condition")))
        for row in records
        if row.get("kind") == "feedback" and row.get("condition")
    }
    return [
        row for row in records
        if row.get("kind") == "trial"
        and row.get("result") is not None
        and (str(row["project_id"]), str(row.get("condition"))) not in restricted
    ]
