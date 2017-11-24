#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: wufeng

import docker

c = docker.Client(base_url='unix://var/run/docker.sock',version='1.13',timeout=10)

c.images()  