# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from typing import Optional, Union

import torch


Device = Union[str, torch.device]


def make_device(device: Device) -> torch.device:
    """
    Makes an actual torch.device object from the device specified as
    either a string or torch.device object.

    Args:
        device: Device (as str or torch.device)

    Returns:
        A matching torch.device object
    """
    return torch.device(device) if isinstance(device, str) else device


def get_device(x, device: Optional[Device] = None) -> torch.device:
    """
    Gets the device of the specified variable x if it is a tensor, or
    falls back to a default CPU device otherwise. Allows overriding by
    providing an explicit device.

    Args:
        x: a torch.Tensor to get the device from or another type
        device: Device (as str or torch.device) to fall back to

    Returns:
        A matching torch.device object
    """

    # User overrides device
    if device is not None:
        return make_device(device)

    # Set device based on input tensor
    if torch.is_tensor(x):
        return x.device

    # Default device is cpu
    return torch.device("cpu")
