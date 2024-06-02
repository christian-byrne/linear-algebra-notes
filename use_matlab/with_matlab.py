#!/usr/bin/env python3

from matlab import engine
import numpy as np

matlab_engine = engine.start_matlab()
result = matlab_engine.sqrt(4.0)
print(result)
matlab_engine.eval('disp("Hello, World!")')