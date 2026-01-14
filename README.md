# GoCueCellAnalysis
Analysis of cells with distinct go-cue related responses

## Usage
Download data from Zenodo: [https://zenodo.org/records/10499868](https://zenodo.org/records/10499868)

```python
import GoCueCell.analysis
import matplotlib.pylab as plt

ppsth, trialidx, target_labels, rtime = GoCueCellAnalysis.analysis.get_data("data/ppsth_fef_mov_raw.jld2")

GoCueCellAnalysis.analysis.plot_data(ppsth,trialidx)

plt.ion()
plt.show()
```
