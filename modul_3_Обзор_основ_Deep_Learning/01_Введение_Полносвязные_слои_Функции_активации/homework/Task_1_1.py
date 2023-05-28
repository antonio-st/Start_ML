import torch
import numpy as np


def function01(tensor: torch.Tensor, count_over: str) -> torch.Tensor:
    if count_over == 'columns':
        return tensor.mean(dim=0)
    elif count_over == 'rows':
        return tensor.mean(dim=1)
