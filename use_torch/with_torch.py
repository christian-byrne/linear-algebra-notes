#!/usr/bin/env python3

import torch
import numpy as np

vector_u = torch.tensor([1, 2, 3])
vector_v = torch.tensor([4, 5, 6])
vector_w = torch.tensor([7, 8, 9])

print(vector_u.dot(vector_v))
