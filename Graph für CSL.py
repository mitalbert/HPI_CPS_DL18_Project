
# coding: utf-8

# In[1]:


import numpy,utils
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf','png')
plt.rcParams['savefig.dpi'] = 90


# In[48]:


# Plot the results in a graph
graph = plt.figure(figsize=(6, 6))
dlist= numpy.arange(8,30)
dlist2= numpy.arange(17,32)
pylist= numpy.array([0.751, 0.774, 0.788, 0.812, 0.832, 0.840, 0.837, 0.850, 0.849, 0.855, 0.856, 0.851, 0.855, 0.858, 0.846, 0.852, 0.853, 0.855, 0.856, 0.851, 0.852, 0.856])
nplist= numpy.array([0.792,0.821,0.818,0.816,0.805,0.811,0.827,0.823,0.811,0.806,0.801,0.808,0.808,0.811,0.797])
plt.plot(dlist, pylist,'-o', label='COCO + RMSprop')
plt.plot(dlist2, nplist, '-o', label='COCO + Flickr30k + Adam')
plt.legend(loc='lower right')
#plt.xscale('log'); plt.yscale('log'); 
plt.xlabel('Epochs'); plt.ylabel('CIDEr Score'); plt.grid(True)
plt.title('Evaluation')
graph.savefig("Evaluation.jpg", bbox_inches='tight')
# <<<<< END YOUR CODE


# In[49]:


# Plot the results in a graph
graph = plt.figure(figsize=(6, 6))
dlist= numpy.arange(8,30)
dlist2= numpy.arange(17,32)
pylist= numpy.array([3.272195,3.179642,3.109171,3.050278,2.999105,2.952385,2.899782,2.846114,2.827768,2.811885,2.796882,2.782877,2.768873,2.755560,2.742388,2.721907,2.715255,2.710304,2.705526,2.701080,2.696402,2.692314])
nplist= numpy.array([3.017715,2.945729,2.890914,2.842160,2.798363,2.758815,2.722164,2.687995,2.655973,2.626023,2.597423,2.570187,2.544071,2.519419,2.495884])
plt.plot(dlist, pylist,'-o', label='COCO + RMSprop')
plt.plot(dlist2, nplist, '-o', label='COCO + Flickr30k + Adam')
plt.legend(loc='lower left')
#plt.xscale('log'); plt.yscale('log');  
plt.xlabel('Epochs'); plt.ylabel('Loss'); plt.grid(True) 
plt.title('Training Loss')
graph.savefig("Loss.jpg", bbox_inches='tight')
# <<<<< END YOUR CODE


# In[25]:


dlist= np.arange(8,29)
print (dlist)

