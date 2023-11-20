import os

from pathlib import Path

from enum import Enum


class AssetType(Enum):
    """
    Asset type correspondent to the folder '''asset'''
    """
    IMAGE = "images"
    OBJECT = "objects"


def get_asset(file_name: str, asset_type: AssetType) -> str:
    """
    Get a file from `assets` folder.

    Parameters
    ----------
    file_name : str
        File name with it's format.
    asset_type : `AssetType`
        The type of the file, to determine the asset location

    Returns
    -------
    str
    """
    path = Path(f"./fmcw/asset/{asset_type.value}/{file_name}")

    try:
        os.makedirs(f"./fmcw/asset/{asset_type.value}")
    except FileExistsError:
        pass

    return str(path.expanduser())
