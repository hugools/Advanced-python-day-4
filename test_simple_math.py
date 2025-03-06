#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 15:19:47 2025

@author: hugoo
"""
import simple_math

def test_simple_add():
    assert simple_math.simple_add(1,2) == 3

def test_simple_sub():
    assert simple_math.simple_sub(2,1) == 1

def test_simple_mult():
    assert simple_math.simple_mult(2,3) == 6

def test_simple_div():
    assert simple_math.simple_div(4, 2) == 2

def test_poly_first():
    assert simple_math.poly_first(2, 1, 2) == 5

def test_poly_second():
    assert simple_math.poly_second(1, 2, 2, 2) == 6