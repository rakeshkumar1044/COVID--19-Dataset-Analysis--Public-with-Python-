#!/usr/bin/env python
# coding: utf-8

# # Rakesh Kumar

# # Working on Real Project with python on COVID -19 Dataset
# 
# (A part of big data Analysis)
# covid -19 SMALL DATASET
# 

# In[22]:


import pandas as pd
co=pd.read_csv(r"C:\Users\Dell\Desktop\Covid 19 Data Files\Covid 19.csv")


# In[2]:


co


# In[3]:


co.head(5)


# In[5]:


co.tail(5)


# In[6]:


co.shape


# In[7]:


co.index


# In[8]:


co.columns


# In[10]:


co.count()


# In[12]:


co.isnull().sum()


# In[13]:


co.notnull().sum()


# In[15]:


co.notna().sum()


# In[16]:


co.nunique()


# In[17]:


co.value_counts()


# In[19]:


co.dtypes


# In[20]:


co


# In[21]:


co


# In[23]:


#  2.  
#  import seaborn as sns
#  import matplotlib.pyplot as plt
#  sns.heatmap (df.null())
#  plt.show()


# In[25]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(co.isnull())


# In[26]:


sns.heatmap(co.notnull())


# #  Q. 1 ) Show the number of Confirmed , Deaths and Recoverd cases in eah Region.
#     

# In[59]:


co.groupby("Region").sum()


# In[60]:


co.groupby("Region").Confirmed.sum().sort_values(ascending=False)


# In[61]:


co.groupby("Region").Deaths.sum().sort_values(ascending=False)


# In[62]:


co.groupby("Region").Recovered.sum().sort_values(ascending=False)


# # Q. 2)  Remove all the records where confirmed cases is less than 10. 

# In[80]:


co=co[~(co.Confirmed <10)]   #Answer   To Remove the records Satisfying a particular condition.


# In[79]:


co


# # Q. 3)   In which Region, Maximum number of Confirmed cases were recorded ?
# 

# In[103]:


import pandas as pd
aa=pd.read_csv(r"C:\Users\Dell\Desktop\Covid 19 Data Files\Covid 19.csv")


# In[104]:


aa.groupby("Region").Confirmed.sum().sort_values(ascending=False).head(1)   # Answer  US  1039909


# In[105]:


aa.groupby("Region").Confirmed.sum().sort_values(ascending=False).head(20)   # Answer  US  1039909


# # Q. 4)  In Which Region ,Minimum number of Deaths cases were recorded ?
#     
# 

# In[93]:


co


# In[94]:


import pandas as pd
cd=pd.read_csv(r"C:\Users\Dell\Desktop\Covid 19 Data Files\Covid 19.csv")


# In[101]:


cd.groupby("Region").Deaths.sum().sort_values().head(20)         # Answer


# In[ ]:





# # Q. 5)  How Many Confirmed ,Deaths & Recovered Cases were reported from india till 29 th april 2020?
# 
# 

# In[119]:


cd[cd.Region=="India"]   #Answer


# In[120]:


cd[cd.Region=="India"].sum()   #Answer


# In[ ]:





# In[122]:


cd.groupby("Region").get_group("India").sum()   #Answer


# In[123]:


cd.groupby("Region").get_group("India")    #Answer


# In[124]:


cd


# # Q. 6-A)  Sort the entire data write No. of Confirmed Cases in Ascending Order.
# 
# 

# In[127]:


cd.sort_values(by="Confirmed",ascending=True)    # answer


# In[132]:


cd.sort_values(by="Confirmed",ascending=True).head(50)    # answer


# # Q. 6-B)  Sort the entire data write no. of recovered cases in descending order.
# 

# In[129]:


cd.sort_values(by="Recovered",ascending=False)    #answer 


# In[133]:


cd.sort_values(by="Recovered",ascending=False).head(50)    #answer 


# # Rakesh Kumar

# In[ ]:




