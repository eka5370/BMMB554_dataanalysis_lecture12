# BMMB554_dataanalysis_lecture12

## Overview

Analysis of Anscombe's Quartet — a classic dataset demonstrating why visualization is essential in data analysis. All four datasets share nearly identical summary statistics yet reveal fundamentally different structures when plotted.

## Dataset

**`anscombe_quartet.tsv`** — tab-separated file containing four datasets (I, II, III, IV), each with 11 (x, y) pairs.

## Steps of Work

### 1. Data Exploration & Descriptive Statistics
Computed summary statistics for each of the four datasets:

| Statistic   | Dataset I | Dataset II | Dataset III | Dataset IV |
|------------|-----------|------------|-------------|------------|
| x mean     | 9.0000    | 9.0000     | 9.0000      | 9.0000     |
| x variance | 11.0000   | 11.0000    | 11.0000     | 11.0000    |
| y mean     | 7.5009    | 7.5009     | 7.5000      | 7.5009     |
| y variance | 4.1273    | 4.1276     | 4.1226      | 4.1232     |
| Pearson r  | 0.8164    | 0.8162     | 0.8163      | 0.8165     |
| Linear fit | y=3.00+0.50x | y=3.00+0.50x | y=3.00+0.50x | y=3.00+0.50x |

Despite identical statistics, the four datasets represent very different underlying relationships.

### 2. Visualization
Four plots were generated (saved as PNG files and embedded in the notebook):

- **Plot 1 — Scatter plots with regression lines** (`plot1_scatter_regression.png`): The canonical Anscombe visualization. Each panel shows raw (x, y) data with the fitted linear regression line overlaid, making the structural differences immediately visible.

- **Plot 2 — Residual plots** (`plot2_residuals.png`): Residuals (y − ŷ) vs. fitted values for each dataset. A standard diagnostic for linear regression assumptions — reveals nonlinearity (II), an outlier (III), and a leverage point (IV).

- **Plot 3 — Box plots** (`plot3_boxplots.png`): Side-by-side box plots of x and y for all four datasets. Illustrates how similar the distributions appear in summary form.

- **Plot 4 — Violin plots** (`plot4_violins.png`): Kernel density estimates of y by dataset. Reveals shape differences that box plots and summary statistics obscure.

### 3. Notebook
**`anscombe_analysis.py`** — a Jupytext Light format notebook containing all analysis code, plots, and commentary. Can be opened interactively in JupyterLab or VS Code (see below).

## Key Finding

All four datasets have virtually identical means, variances, correlations, and linear regression coefficients, yet represent:
- **I**: A well-behaved linear relationship
- **II**: A nonlinear (quadratic) curve — a linear model is inappropriate
- **III**: A linear relationship with one high-influence outlier distorting the fit
- **IV**: A vertical cluster (all x=8) with a single high-leverage point driving the regression

**Conclusion: Always plot your data.**

## Running the Notebook

**VS Code** — Open `anscombe_analysis.py`; the Jupyter extension auto-detects `# %%` cell markers.

**JupyterLab:**
```bash
pip install jupyterlab jupytext
jupyter lab
```
Right-click `anscombe_analysis.py` → *Open With* → *Notebook*.

**Convert to `.ipynb`:**
```bash
pip install jupytext
jupytext --to notebook anscombe_analysis.py
jupyter notebook anscombe_analysis.ipynb
```