#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pathlib import Path
import sys
from sys import argv

K8_SYSTEM_CONFIG_PATH = "~/.kube"
# VALID_K8S_ENVS = [f"k8s-{env}" for env in ["dev", "pro", "local"]]


def get_cluster_argument():
    """Retrieve command line argument and returns it"""
    if len(argv) != 2:
        print("You should pass k8s environment. Ex: k8s-pro")
        sys.exit(1)
    return argv[1]


def get_k8s_enviroments():
    """Returns kubeconfig file cluster."""
    k8s_search_path = os.path.expanduser(K8_SYSTEM_CONFIG_PATH)
    return [r for r in os.listdir(k8s_search_path) if r.startswith("k8s-")]


def create_symlink(cluster_argument):
    symlink_source = os.path.join(
        os.path.expanduser(K8_SYSTEM_CONFIG_PATH),
        "config"
    )

    if os.path.islink(symlink_source):
        Path(symlink_source).unlink()

    symlink_dest = os.path.join(
        os.path.expanduser(K8_SYSTEM_CONFIG_PATH),
        cluster_argument
    )

    os.symlink(dst=symlink_source, src=symlink_dest)


def show_error(cluster_argument):
    print(f"The cluster argument '{cluster_argument}' is not a valid config on {K8_SYSTEM_CONFIG_PATH}")


def change_paths():
    cluster_argument = get_cluster_argument()

    environments = get_k8s_enviroments()

    if cluster_argument in environments:
         create_symlink(cluster_argument)
    else:
         show_error(cluster_argument)
