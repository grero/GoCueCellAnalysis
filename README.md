# GoCueCellAnalysis
Analysis of cells with distinct go-cue related responses

## Installation
1) Clone this repository
2) Optionally, create a conda environment
```bash
conda create -n gocuecells
conda activate gocuecells
conda install pip
```
3) Navigate to the repository and install using `pip`
```bash
pip install .
```

## Usage
Download data from Zenodo: [https://zenodo.org/records/10499868](https://zenodo.org/records/10499868)

Load the data and plot the raster for a single, showing responses aligned to the response saccade onset.

```python
from GoCueCellAnalysis import analysis
import matplotlib.pylab as plt

ppsth, trialidx, target_labels, rtime = analysis.get_data("data/ppsth_fef_mov_raw.jld2")

analysis.plot_data(ppsth,trialidx)

plt.ion()
plt.show()
```
