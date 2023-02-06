
# %%
import numpy as np 

# %%
M=np.array([[1,2,3],[-1,0,np.nan],[0,0,1]])
# %%
np.isnan(M)
# %%
M[~np.isnan(M).any(axis=1),:]
# %%
print(np.isnan(M).any(axis=1))
# %%
M
# %%
print(M)
# %%
