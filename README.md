# Spatiotemporal Models in Python

This repository contains examples of core spatiotemporal modeling approaches implemented in Python using popular libraries. It is intended for educational and research purposes, providing ready-to-run Jupyter notebooks for time series, spatial, and graph-based data.

## Project Overview
Spatiotemporal modeling is essential for analyzing data that varies across both space and time, such as climate records, sensor networks, and traffic flows. This repository demonstrates several approaches:
- Classical time series models (ARIMA)
- Probabilistic models (Gaussian Processes, Bayesian AR)
- Deep learning models (Graph Neural Networks)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/JFMandujanoR/spatiotemporal-models-notebooks.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Additional packages may be required for some notebooks (e.g., `pymc`, `torch`, `torch-geometric`).
3. Launch JupyterLab or Jupyter Notebook:
   ```bash
   jupyter lab
   ```
4. Open the notebooks in the `notebooks/` folder and run the cells.

## Notebooks
- `spatiotemporal_arima.ipynb`: ARIMA modeling and forecasting for simulated spatiotemporal time series across multiple locations.
- `st_gp.ipynb`: Gaussian Process regression for spatially and temporally correlated data, including uncertainty visualization.
- `st_gnn.ipynb`: Graph Neural Network for dynamic graphs, showing node-level predictions and training diagnostics.
- `bayesian_spatiotemporal.ipynb`: Bayesian AR(1) modeling for spatiotemporal data using PyMC, with posterior inference and probabilistic forecasting.

## Utilities
- `utils/data_generation.py`: Functions for simulating spatiotemporal grids and aggregating to locations.
- `utils/visualization.py`: Helper functions for plotting fields and forecasts.

## References
- [Statsmodels](https://www.statsmodels.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [PyMC](https://www.pymc.io/)
- [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/)

## Attribution
These files were created with the help of ChatGPT and Copilot.
