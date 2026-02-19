# %% [markdown]
# # Anscombe's Quartet — Analysis and Visualization
#
# The Anscombe Quartet is a set of four datasets that have nearly identical
# descriptive statistics (mean, variance, correlation, linear regression)
# but look completely different when plotted. This notebook demonstrates
# why visualization is essential in data analysis.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("anscombe_quartet.tsv", sep="\t")
df.head()

# %% [markdown]
# ## Descriptive Statistics
#
# All four datasets share the same summary statistics — the classic Anscombe result.

# %%
stats = []
for ds in ["I", "II", "III", "IV"]:
    sub = df[df["dataset"] == ds]
    m, b = np.polyfit(sub.x, sub.y, 1)
    stats.append({
        "Dataset": ds,
        "n": len(sub),
        "x mean": round(sub.x.mean(), 4),
        "x var": round(sub.x.var(), 4),
        "y mean": round(sub.y.mean(), 4),
        "y var": round(sub.y.var(), 4),
        "Pearson r": round(sub[["x", "y"]].corr().iloc[0, 1], 4),
        "slope": round(m, 4),
        "intercept": round(b, 4),
    })

pd.DataFrame(stats).set_index("Dataset")

# %% [markdown]
# ## Plot 1: 2×2 Scatter Plots with Regression Lines
#
# The canonical Anscombe visualization. Each panel shows the raw data with
# the fitted regression line (y ≈ 3 + 0.5x) overlaid.

# %%
fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=False, sharey=False)
axes = axes.flatten()
palette = sns.color_palette("tab10", 4)

for i, ds in enumerate(["I", "II", "III", "IV"]):
    sub = df[df["dataset"] == ds]
    ax = axes[i]
    ax.scatter(sub.x, sub.y, color=palette[i], s=60, zorder=3, label="data")
    x_line = np.linspace(sub.x.min() - 0.5, sub.x.max() + 0.5, 100)
    m, b = np.polyfit(sub.x, sub.y, 1)
    ax.plot(x_line, m * x_line + b, color="steelblue", linewidth=1.8,
            linestyle="--", label=f"y = {b:.2f} + {m:.2f}x")
    ax.set_title(f"Dataset {ds}", fontsize=13, fontweight="bold")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(fontsize=8)
    ax.grid(True, linestyle=":", alpha=0.5)

fig.suptitle("Anscombe's Quartet — Scatter Plots with Regression Lines",
             fontsize=14, fontweight="bold", y=1.01)
plt.tight_layout()
plt.savefig("plot1_scatter_regression.png", dpi=150, bbox_inches="tight")
plt.show()

# %% [markdown]
# ## Plot 2: Residual Plots
#
# Residuals (y − ŷ) vs. fitted values. A standard regression diagnostic.
# - Dataset I: random scatter → assumptions met
# - Dataset II: curved pattern → nonlinearity
# - Dataset III: one extreme residual → outlier
# - Dataset IV: near-zero residuals except for one leverage point

# %%
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

for i, ds in enumerate(["I", "II", "III", "IV"]):
    sub = df[df["dataset"] == ds].copy()
    m, b = np.polyfit(sub.x, sub.y, 1)
    sub["fitted"] = m * sub.x + b
    sub["residual"] = sub.y - sub["fitted"]
    ax = axes[i]
    ax.scatter(sub["fitted"], sub["residual"], color=palette[i], s=60, zorder=3)
    ax.axhline(0, color="steelblue", linewidth=1.5, linestyle="--")
    ax.set_title(f"Dataset {ds} — Residuals", fontsize=13, fontweight="bold")
    ax.set_xlabel("Fitted values (ŷ)")
    ax.set_ylabel("Residual (y − ŷ)")
    ax.grid(True, linestyle=":", alpha=0.5)

fig.suptitle("Anscombe's Quartet — Residual Plots",
             fontsize=14, fontweight="bold", y=1.01)
plt.tight_layout()
plt.savefig("plot2_residuals.png", dpi=150, bbox_inches="tight")
plt.show()

# %% [markdown]
# ## Plot 3: Box Plots of x and y by Dataset
#
# Shows how similar the spread looks in summary form across all four datasets.

# %%
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(data=df, x="dataset", y="x", hue="dataset", palette="tab10",
            legend=False, ax=axes[0])
axes[0].set_title("Distribution of x by Dataset", fontsize=13, fontweight="bold")
axes[0].set_xlabel("Dataset")
axes[0].set_ylabel("x")
axes[0].grid(True, linestyle=":", alpha=0.5)

sns.boxplot(data=df, x="dataset", y="y", hue="dataset", palette="tab10",
            legend=False, ax=axes[1])
axes[1].set_title("Distribution of y by Dataset", fontsize=13, fontweight="bold")
axes[1].set_xlabel("Dataset")
axes[1].set_ylabel("y")
axes[1].grid(True, linestyle=":", alpha=0.5)

fig.suptitle("Anscombe's Quartet — Box Plots", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("plot3_boxplots.png", dpi=150, bbox_inches="tight")
plt.show()

# %% [markdown]
# ## Plot 4: Violin Plots of y by Dataset
#
# A richer view than box plots — the kernel density estimate reveals shape
# differences that summary statistics and box plots obscure.

# %%
fig, ax = plt.subplots(figsize=(10, 6))

sns.violinplot(data=df, x="dataset", y="y", hue="dataset", palette="tab10",
               inner="box", cut=0, legend=False, ax=ax)
ax.set_title("Anscombe's Quartet — Violin Plots of y",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Dataset", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.grid(True, linestyle=":", alpha=0.5)

plt.tight_layout()
plt.savefig("plot4_violins.png", dpi=150, bbox_inches="tight")
plt.show()

# %% [markdown]
# ## Key Takeaway
#
# All four datasets share nearly identical summary statistics:
# - x̄ = 9.0, var(x) = 11.0
# - ȳ ≈ 7.5, var(y) ≈ 4.12
# - Pearson r ≈ 0.816
# - Linear fit: y ≈ 3.00 + 0.50x
#
# Yet they represent fundamentally different relationships:
# - **I**: Well-behaved linear relationship
# - **II**: Nonlinear (quadratic) curve — a linear model is wrong
# - **III**: Linear with one high-influence outlier distorting the fit
# - **IV**: Vertical cluster (x=8) with a single high-leverage point driving the regression
#
# **Always plot your data.**
