#!/usr/bin/python
# -*- coding: utf-8 -*-


def id_from_list_dict(list_dict, key_name):
    for d in list_dict:
        if d['name'] == key_name:
            return d['id']
