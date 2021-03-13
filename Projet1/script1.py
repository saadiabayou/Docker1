#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 07:43:11 2021

@author: Saadia Bayou
"""
from flask import Flask

app=Flask (__name__)

@app.route("/")
def demo():
    return " ***      Demonstration n° 1  Docker  -  Saadia Bayou ***  "

if __name__=="__main__":
    app.run(host='0.0.0.0', port=9090)



