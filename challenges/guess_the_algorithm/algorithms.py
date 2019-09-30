"""
	@file		main
	@description
	@author	  Res260
	@created_at  20180808
	@updated_at  20190903
"""
from typing import List
from math import sqrt


# 1: moyenne
def a(b: List[float]) -> float:
	c = 0
	for d in b:
		c += d
	return c/len(b)


# 2: mediane
def b(c: List[float]) -> float:
	d = sorted(c)
	e = (len(d) // 2) - 1
	if len(d) % 2 == 1:
		f = d[e + 1]
	else:
		f = (d[e] + d[e + 1]) / 2
	return f


# 3: fibonnacci
def c(d: int) -> int:
	if d == 1:
		return 0
	if d == 2:
		return 1

	return c(d - 1) + c(d - 2)


# 4: selection sort
def e(f: List[float]):
	for g in range(len(f)):
		h = g
		for i in range(g + 1, len(f)):
			if f[i] < f[h]:
				h = i
		if h != g:
			j = f[g]
			f[g] = f[h]
			f[h] = j


# 5: rc4
def h(i: bytes, j: bytes) -> bytes:
	k = list(range(256))
	l = 0
	m = []

	for n in range(256):
		l = (l + k[n] + j[n % len(j)]) % 256
		k[n], k[l] = k[l], k[n]

	n = l = 0
	for o in i:
		n = (n + 1) % 256
		l = (l + k[n]) % 256
		k[n], k[l] = k[l], k[n]
		m.append(o ^ k[(k[n] + k[l]) % 256])

	return m
