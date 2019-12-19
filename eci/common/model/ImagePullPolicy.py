#!/usr/bin/python

from enum import Enum


class ImagePullPolicy(Enum):
    """
    PullAlways means that kubelet always attempts to pull the latest image. Container will fail If the pull fails.
    """
    Always = 'Always'

    """
    PullNever means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn't present
    """
    Never = 'Never'

    """
    PullNever means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn't present
    """
    IfNotPresent = 'IfNotPresent'
