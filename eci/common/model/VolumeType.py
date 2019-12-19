#!/usr/bin/python

from enum import Enum


class VolumeType(Enum):
    EmptyDirVolume = 'EmptyDirVolume'

    NFSVolume = 'NFSVolume'

    ConfigFileVolume = 'ConfigFileVolume'

    DiskVolume = 'DiskVolume'

    FlexVolume = 'FlexVolume'
