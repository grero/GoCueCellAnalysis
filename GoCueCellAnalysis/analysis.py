import matplotlib.pylab as plt
import numpy as np
from juliacall import Main as jl
jl.seval("using JLD2")

def get_data(fname):
    qdata = jl.JLD2.load(fname)
    ppsth = qdata["ppsth"]
    trialidx = qdata["trialidx"]
    target_labels = qdata["labels"]
    rtimes = qdata["rtimes"]
    
    return ppsth, trialidx, target_labels, rtimes


def plot_data(ppsth, trialidx):
    spike_counts = ppsth.counts
    bins = ppsth.bins
    # plot spike counts for the first cell
    ax = plt.subplot(111)
    ax.imshow(np.transpose(spike_counts[:,:len(trialidx[1]),1]), origin='lower', extent=(bins[0], bins[-1], 0, spike_counts.shape[1]))
    ax.set_xlabel("Time from saccade [ms]")
    ax.set_ylabel("Trial number")
    ax


