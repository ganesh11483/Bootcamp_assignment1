
# coding: utf-8

# In[13]:


a=[]
i=2000
n=3200
while(i<=n):
    i=i+1
    if i%7 == 0:
        if i%5 != 0:
            new_element = int(i)
            a.append(new_element)
print(a)


# In[16]:


pi = 3.142
r=int(input("enter the diameter : "))
V= 4.0/3.0*pi* r**3
print(V)

