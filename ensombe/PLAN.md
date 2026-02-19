# An analysis of Anscombe data

## Goal

Analyze data set and visualize it, and what we want to do next with it.

## Implementation

- Need to analyze data in Anscombe_Quartet.tsc.
- First look at data and generate descriptive statistics
- Second, create a Jupyter Light notebook in which you'll generate plots.
- Propose types of plots that you would like to generate
- Save this proposal to the end of this file and let me look at it.
- Append plan to the end of this file, I need to confirm before moving forward.

---

## Descriptive Statistics Summary

All four datasets (n=11 each) have nearly identical statistics — the hallmark of the Anscombe Quartet:

| Statistic        | Dataset I | Dataset II | Dataset III | Dataset IV |
|-----------------|-----------|------------|-------------|------------|
| x mean          | 9.0000    | 9.0000     | 9.0000      | 9.0000     |
| x variance      | 11.0000   | 11.0000    | 11.0000     | 11.0000    |
| y mean          | 7.5009    | 7.5009     | 7.5000      | 7.5009     |
| y variance      | 4.1273    | 4.1276     | 4.1226      | 4.1232     |
| Pearson r       | 0.8164    | 0.8162     | 0.8163      | 0.8165     |
| Linear fit      | y=3.00+0.50x | y=3.00+0.50x | y=3.00+0.50x | y=3.00+0.50x |

Despite these identical statistics, the datasets have very different underlying distributions.

---

## Proposed Plots (awaiting confirmation)

### 1. 2×2 Scatter Plot Grid with Regression Lines
The canonical Anscombe visualization. One panel per dataset showing the raw (x, y) points with the fitted regression line (y = 3 + 0.5x) overlaid. This is the most important plot — it makes immediately visible why summary statistics alone are insufficient:
- Dataset I: linear relationship with moderate scatter
- Dataset II: clear nonlinear (quadratic) curve
- Dataset III: linear with a single high-leverage outlier
- Dataset IV: vertical cluster at x=8 with one outlier at x=19

### 2. Residual Plots (2×2 grid)
Residuals (y − ŷ) vs. fitted values for each dataset. This is the standard diagnostic for linear regression assumptions. Expected patterns:
- I: random scatter (assumptions met)
- II: curved pattern (nonlinearity)
- III: one extreme residual (outlier)
- IV: all residuals identical except one point

### 3. Box Plots of x and y by Dataset
Side-by-side box plots comparing the distribution of x values and y values across all four datasets. Reinforces how similar the spread looks in summary form.

### 4. Violin Plots of y by Dataset
A richer version of the box plot showing the full kernel density estimate of y for each dataset. Reveals the true shape differences that box plots and summary stats obscure.

**Please confirm this plot proposal before I create the Jupyter Light notebook.**

## Iteration 1
- Execute plan
- Save in Jupyter notebook
- Explain how to start Jupyter Notebooks to validate these results

## Iteration 2 
- Make it colorful so the four panels have different colors