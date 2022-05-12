# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# can be used to install requirements from within Jupyter
# !wget -nc https://raw.githubusercontent.com/dhh22/convoy-analysis/main/requirements.txt
# !pip install -r requirements.txt

# %%
import os
import sys
if "__file__" in globals():
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.getcwd()+"/code")
sys.path.append("./code")
sys.path.append(".")
sys.path.append("..")
import common_basis

con = common_basis.con

import pandas as pd
import seaborn as sns
# %%

d = pd.read_sql_query("""
  SELECT COUNT(*) as tweets 
  FROM tweets_c 
  GROUP BY conversation_id""", con)

# %%

sns.histplot(d, x="tweets", bins=100, log_scale=(True, True))

# %%

