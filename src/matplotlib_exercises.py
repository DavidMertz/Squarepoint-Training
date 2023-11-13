import numpy as np
import pandas as pd
import gzip
from datetime import datetime

def brad_house():
    df = pd.DataFrame()
    for location in ['basement', 'lab', 'livingroom', 'outside']:
        with gzip.open('data/%s.gz' % location) as f:
            readings = dict()
            for line in f:
                Y, m, d, H, M, temp = line.split()
                readings[datetime(*map(int, (Y, m, d, H, M)))] = float(temp)
        df[location] = pd.Series(readings)

    return df.sort_index()

alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * np.cos(phi_p)*np.cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p)

X_q, Y_q = np.meshgrid(np.linspace(0, 2*np.pi, 200), 
                   np.linspace(0, 2*np.pi, 200))
Z_q = flux_qubit_potential(X_q, Y_q).T