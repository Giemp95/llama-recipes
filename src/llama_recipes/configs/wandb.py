# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class wandb_config:
    project: str = 'Federated_Llama' # wandb project name
    entity: Optional[str] = 'gmittone' # wandb entity name
    job_type: Optional[str] = None
    tags: Optional[List[str]] = None
    group: Optional[str] = 'leonardo'
    notes: Optional[str] = None
    mode: Optional[str] = None