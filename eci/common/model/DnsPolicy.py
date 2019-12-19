#!/usr/bin/python

from enum import Enum


class DnsPolicy(Enum):
    """
    It allows a Pod to ignore DNS settings from the Kubernetes environment.
    All DNS settings are supposed to be provided using the dnsConfig field in the Pod(ECI) Spec
    """
    Policy_None = 'None'

    """
    Any DNS query that does not match the configured cluster domain suffix 
    is forwarded to the upstream name server inherited from the node.
    """
    Policy_ClusterFirst = 'ClusterFirst'
