"""Generate descriptive RQWB capability figures; this is not a performance benchmark."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


ROOT = Path(__file__).parent
DATA = json.loads((ROOT / "comparison_data.json").read_text(encoding="utf-8"))
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)

plt.rcParams.update(
    {
        "font.family": "Arial",
        "font.size": 10,
        "axes.titleweight": "bold",
        "axes.labelcolor": "#1F2933",
        "xtick.color": "#1F2933",
        "ytick.color": "#1F2933",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


def save(fig: plt.Figure, name: str) -> None:
    fig.savefig(FIGURES / name, dpi=220, bbox_inches="tight")
    plt.close(fig)


skills = DATA["skills"]
ids = [item["id"] for item in skills]
names = [item["name"] for item in skills]

# Figure 1: documented capability heatmap
capabilities = DATA["capabilities"]
coverage = np.array([DATA["coverage"][skill_id] for skill_id in ids]).T
fig, ax = plt.subplots(figsize=(10.8, 5.4))
cmap = ListedColormap(["#F3F4F6", "#B9D7EA", "#5EA8A7", "#0F766E"])
image = ax.imshow(coverage, cmap=cmap, vmin=0, vmax=3, aspect="auto")
ax.set_xticks(np.arange(len(names)), names, rotation=25, ha="right")
ax.set_yticks(np.arange(len(capabilities)), capabilities)
for row in range(coverage.shape[0]):
    for column in range(coverage.shape[1]):
        ax.text(column, row, str(coverage[row, column]), ha="center", va="center", color="#102A43")
ax.set_title("Documented capability coverage, not empirical performance")
colorbar = fig.colorbar(image, ax=ax, ticks=[0, 1, 2, 3], pad=0.02)
colorbar.ax.set_yticklabels(["Not intended", "Supporting", "Primary", "Explicit gate"])
save(fig, "01_documented_capability_heatmap.png")

# Figure 2: task-fit heatmap
tasks = DATA["task_types"]
task_fit = np.array([DATA["task_fit"][skill_id] for skill_id in ids]).T
fig, ax = plt.subplots(figsize=(10.8, 4.8))
task_cmap = ListedColormap(["#F3F4F6", "#F8C9A6", "#F29E4C", "#C7522A"])
image = ax.imshow(task_fit, cmap=task_cmap, vmin=0, vmax=3, aspect="auto")
ax.set_xticks(np.arange(len(names)), names, rotation=25, ha="right")
ax.set_yticks(np.arange(len(tasks)), tasks)
for row in range(task_fit.shape[0]):
    for column in range(task_fit.shape[1]):
        ax.text(column, row, str(task_fit[row, column]), ha="center", va="center", color="#4A1D0B")
ax.set_title("Intended task fit from documented skill scope")
colorbar = fig.colorbar(image, ax=ax, ticks=[0, 1, 2, 3], pad=0.02)
colorbar.ax.set_yticklabels(["Not intended", "Supporting", "Primary", "Explicit gate"])
save(fig, "02_intended_task_fit_heatmap.png")

# Figure 3: candidate-case composition
case_counts = DATA["case_counts"]
labels = list(case_counts)
values = list(case_counts.values())
fig, ax = plt.subplots(figsize=(9.6, 4.6))
bars = ax.bar(labels, values, color=["#0F766E", "#2F80ED", "#E07A5F", "#457B9D", "#6A994E", "#F2CC8F", "#9B5DE5"])
ax.set_ylim(0, 2.6)
ax.set_ylabel("Candidate cases")
ax.set_title("RQWB-v1 case design: 12 source-grounded tasks")
ax.tick_params(axis="x", rotation=25)
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 0.06, str(value), ha="center", va="bottom", color="#1F2933")
ax.spines[["top", "right"]].set_visible(False)
save(fig, "03_case_design.png")

# Figure 4: evidence-status counts
tier_counts = DATA["source_tiers"]
labels = list(tier_counts)
values = list(tier_counts.values())
colors = ["#2F80ED", "#5B6C8F", "#BDBDBD", "#BDBDBD"]
fig, ax = plt.subplots(figsize=(9.6, 4.6))
bars = ax.barh(labels, values, color=colors)
ax.set_xlabel("Count")
ax.set_title("Benchmark readiness and evidence status")
ax.spines[["top", "right"]].set_visible(False)
for bar, value in zip(bars, values):
    ax.text(value + 0.08, bar.get_y() + bar.get_height() / 2, str(value), va="center", color="#1F2933")
ax.text(0.02, -0.25, "Zero approved public cases and zero blinded scores mean no performance claim is warranted yet.", transform=ax.transAxes, color="#7A271A")
save(fig, "04_benchmark_readiness.png")

# Figure 5: workflow role map
fig, ax = plt.subplots(figsize=(12.8, 3.8))
ax.axis("off")
positions = np.linspace(0.07, 0.93, len(skills))
colors = ["#3B82F6", "#0F766E", "#6A994E", "#9B5DE5", "#E07A5F", "#F2CC8F"]
role_labels = [
    "Research-to-publication\nworkflow",
    "Thermal-fluid\njudgment",
    "Technical argument\nand literature",
    "Review-revise-\nverify loop",
    "Pattern-aware\nrevision",
    "Reader-centered\nclarity",
]
for index, (skill, x, color) in enumerate(zip(skills, positions, colors)):
    if index:
        ax.annotate("", xy=(x - 0.075, 0.54), xytext=(positions[index - 1] + 0.075, 0.54), arrowprops={"arrowstyle": "->", "color": "#6B7280", "lw": 1.5})
    ax.text(x, 0.6, skill["id"], ha="center", va="center", fontsize=11, weight="bold", color="white", bbox={"boxstyle": "round,pad=0.65", "facecolor": color, "edgecolor": "none"})
    ax.text(x, 0.27, role_labels[index], ha="center", va="center", fontsize=9, linespacing=1.3)
ax.set_title("Six complementary layers in the research-writing workflow", pad=12)
ax.text(0.5, 0.02, "The arrows describe a possible workflow, not a mandatory sequence or a performance ranking.", ha="center", transform=ax.transAxes, color="#4B5563")
save(fig, "05_complementary_workflow_map.png")
