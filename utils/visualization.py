# utils/visualization.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_grid_field(X, t=0, ax=None, title=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(5,4))
    im = ax.imshow(X[t], origin='lower', aspect='auto')
    ax.set_title(title or f'Time {t}')
    plt.colorbar(im, ax=ax)
    return ax

def plot_forecast_vs_true(times, true, pred, ax=None, title=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(times, true, label='true')
    ax.plot(times, pred, label='pred')
    ax.legend()
    ax.set_title(title or 'Forecast vs True')
    return ax
