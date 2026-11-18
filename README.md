# 工程实践证据分析

整理能源工程实践中的现场问题、建模假设、方案版本、工程师反馈与试用结果，帮助区分仿真产出和适用于现场工况的证据。

输入是本地合成 UTF-8 JSON 数组，记录以 `id` 和 `project_id` 关联。`kind` 支持 `field_problem`、`assumption`、`model`、`feedback`、`trial`；模型和试用记录须包含版本。反馈中的 `condition` 用于标出会限制试用解释的现场条件。报告能识别当前可用试用证据，但尚未保存评审提交时的方案及证据快照。

需要 Python 3.11 或更新版本，不依赖外部服务。运行 `PYTHONPATH=src python -m unittest discover -s tests -v` 执行测试。`field_practice.facts` 负责事件校验，`field_practice.field_conditions.usable_trials` 判断工况适用性，`field_practice.analysis` 追踪问题到试用的项目链路，`field_practice.reports` 生成带来源修订号的汇总。示例见 `examples/sample.json`。
