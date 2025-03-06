# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#hello.py
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("The rank of this process is  ", rank)
