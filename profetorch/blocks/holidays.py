# AUTOGENERATED! DO NOT EDIT! File to edit: Holidays.ipynb (unless otherwise specified).

__all__ = ['Holiday', 'HolidayRange']

# Cell
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F

torch.Tensor.ndim = property(lambda x: x.dim())

# Cell
class Holiday(nn.Module):
    def __init__(self, holiday, repeat_every=365, mean=0, scale=1):
        super().__init__()
        self.holiday = (holiday - mean) / scale
        self.repeat_every = repeat_every / scale
        self.w = nn.Parameter(torch.zeros(1)+0.05)

    def forward(self, t):
        rem = torch.remainder(t - self.holiday, self.repeat_every)
        return (rem == 0).float() * self.w


class HolidayRange(nn.Module):
    def __init__(self, holidays):
        """
        holidays: list of lists containing lower and upper bound of hols
        """
        super().__init__()
        self.holidays = holidays
        self.w = nn.Parameter(torch.zeros(1)+0.05)

    def forward(self, t):
        bounded = [(l<=t) & (t<=u) for l,u in self.holidays]
        return sum(bounded).float()*self.w