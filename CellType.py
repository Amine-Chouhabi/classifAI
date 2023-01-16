# Enum for notebook cell types 
#

from enum import Enum

class CellType(Enum):
    """Enum for notebook cell types"""
    MARKDOWN = 1
    CODE = 2
    RAW = 3
    HEADING = 4