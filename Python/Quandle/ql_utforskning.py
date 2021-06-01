#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 07:50:11 2020

@author: bwarland
"""

# import numpy as np
import quandl as ql
# import eikon as ek

ql.ApiConfig.api_key="aRr-8SCxC3K-BQz89yar"
# WTI=ql.get("EIA/PET_RWTC_D", 
#            returns="pandas",
#            transformation="rdiff")

mYE=ql.get("UNAE/GVAKD_YEM", returns="pandas")
mNO=ql.get("UNAE/GVAKD_NOR", returns="pandas")
mSE=ql.get("UNAE/GVAKD_SWE", returns="pandas")
# https://www.iban.com/country-codes

