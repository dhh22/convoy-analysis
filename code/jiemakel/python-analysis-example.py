import sys
sys.path.append('code')
sys.path.append('..')
from common_basis import con

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

