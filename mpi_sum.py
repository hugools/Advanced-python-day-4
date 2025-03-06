#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 14:01:27 2025

@author: hugoo
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
rn = np.zeros(12)
y = np.random.random(1)

if rank > 0:
    comm.Send(y, dest=0)

if rank == 0:
    rn[0] = y
    for x in range(1,12,1):
        comm.Recv(y, source = x)
        rn[x] = y
    print(np.sum(rn))




