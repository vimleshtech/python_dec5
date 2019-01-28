import pandas as pd
import statistics as s

eid = [11,22,33,44,55]
name = ['jatin','monika','ayush','ridhi','nitisha']
gender = ['male','female','male','female','female']
sal = [23000,24000,30000,35000,50000]


df = pd.DataFrame(data={'eid':eid,'name':name,'gender':gender,'sal':sal})
print(df)

##
print(df.index)
print(df.columns)
print(df.shape)
print(df.head(2)) #from top 
print(df.tail(3)) #from buttom
 

##print paticular columns
print(df['name'])

##convert dataframe to list
#read by given index
data = df.values 
print(data[:,1]) #all rows, and 2 col
print(data[:,1:3]) 

print(data[2,:]) #3rd row and all columns
print(data[2:5,:])  #from 2 to 4 rows and all columns
print(data[2:5,1:3])

###
print(df.info())

###group by
print(df.groupby('gender').size())
a = df.groupby('gender').size()

print(df.groupby('gender').sum())
print(df.groupby('gender').max())
print(df.groupby('gender').min())

print(df.groupby('gender').sum()['sal'])


##sorting
out = df.sort_values('sal',ascending=False)
#out.to_csv(r'C:\Users\vkumar15\Desktop\out_emp_sorted.csv')

#filter : search
out  = df.loc[df['sal']>40000]
print(out)


out  = df.loc[df['gender']=='female']
print(out)


##describe : show basic stats
'''
count
mean
std
min
25%
50%
75%
max
'''
print(df.describe())

######
######


print(data[:,0])
xid = data[:,0]

#statistics
print('max = ',max(xid))
print('min = ',min(xid))
print('total  = ',sum(xid))
print('mean/avg = ',sum(xid)/len(xid))

print(s.mean(xid ))
print(s.mean(xid ))

#out
out = [1,2,1,1,2,3,3,1,3,4,3,3,3,5]
print(s.mode(out))
print(s.median(out))

print('range  : ',(max(out) - min(out)) )

print('range  : ',min(out) , ' to ', max(out) )


print(s.variance(xid ) )
print(s.pvariance(xid ) )

print(s.stdev(xid) )



import numpy as np
print (np.percentile([1,3,4,463,2,3,6,8,9,4,254,6,72], [0, 100]))
print (np.percentile([1,3,4,463,2,3,6,8,9,4,254,6,72], [10,20,78,90, 100]))
























           


























