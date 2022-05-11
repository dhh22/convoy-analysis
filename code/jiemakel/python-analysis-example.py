import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import common_basis

con = common_basis.con

import pandas as pd
import seaborn as sns
#%%

d = pd.read_sql_query("""
  SELECT COUNT(*) as tweets 
  FROM tweets_c 
  GROUP BY conversation_id""", con)

#%%

sns.histplot(d, x="tweets", bins=100, log_scale=(True, True))

#%%

