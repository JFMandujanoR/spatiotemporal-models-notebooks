# utils/data_generation.py
import numpy as np
import pandas as pd

def simulate_spatiotemporal_grid(nx=16, ny=16, T=200, seed=0):
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 1, nx)
    y = np.linspace(0, 1, ny)
    X = np.zeros((T, nx, ny), dtype=float)
    xv, yv = np.meshgrid(x, y, indexing='xy')
    base = np.sin(2 * np.pi * xv) * np.cos(2 * np.pi * yv)
    phi = 0.8
    noise_scale = 0.2
    state = rng.normal(scale=noise_scale, size=(nx, ny))
    for t in range(T):
        seasonal = 0.3 * np.sin(2 * np.pi * t / 24)
        forcing = 0.1 * np.cos(2 * np.pi * t / 48)
        state = phi * state + rng.normal(scale=noise_scale, size=(nx, ny))
        X[t] = base + seasonal + forcing + state
    return X, {'x': x, 'y': y}

def aggregate_to_locations(X, coords, n_locations=20, seed=1):
    rng = np.random.default_rng(seed)
    T, nx, ny = X.shape
    x = coords['x']
    y = coords['y']
    xv, yv = np.meshgrid(x, y, indexing='xy')
    xv = xv.ravel(); yv = yv.ravel()
    grid_points = np.vstack([xv, yv]).T
    loc_idx = rng.choice(len(grid_points), size=n_locations, replace=False)
    loc_coords = grid_points[loc_idx]
    values = np.zeros((T, n_locations))
    for i, (lx, ly) in enumerate(loc_coords):
        ix = np.abs(x - lx).argmin()
        iy = np.abs(y - ly).argmin()
        values[:, i] = X[:, ix, iy]
    times = np.arange(T)
    rows = []
    for t in times:
        for i in range(n_locations):
            rows.append({'time': t, 'loc': f'L{i}', 'x': loc_coords[i,0], 'y': loc_coords[i,1], 'value': float(values[t,i])})
    import pandas as pd
    df = pd.DataFrame(rows)
    locs = pd.DataFrame({'loc': [f'L{i}' for i in range(n_locations)], 'x': loc_coords[:,0], 'y': loc_coords[:,1]})
    return df, locs
