# GoCueCellAnalysis
Analysis of cells with distinct go-cue related responses

## Usage

```python
import GoCueCell.analysis
import matplotlib.pylab as plt

ppsth, trialidx, target_labels, rtime = GoCueCellAnalysis.analysis.get_data("data/ppsth_fef_mov_raw.jld2")
GoCueCellAnalysis.analysis.plot_data(ppsth,trialidx)

plt.ion()
plt.show()
```
