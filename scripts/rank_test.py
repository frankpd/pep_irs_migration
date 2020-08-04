#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPERIMENTAL
Create array that indicates whether places have changed positions in rank over time
"""

import numpy as np

#ranks=[['NYC','NYC','LA'],
#        ['LA','LA','PHL'],
#        ['PHL','CHI','NYC'],
#        ['CHI','PHL','CHI']]
#
#for r, vlist in enumerate(ranks): # r is row number
#    for c, v in enumerate(vlist): # c is column position
#        print(r,v)
        
places=np.array([['NYC','NYC','LA'],
        ['LA','LA','PHL'],
        ['PHL','CHI','NYC'],
        ['CHI','PHL','HOU']])

rowcount=places.shape[0]
colcount=places.shape[1]

# Create a number of blank lists
changelist = [[] for _ in range(rowcount)]
    
for i in range(colcount):
    if i==0:
        # Rank change for 1st year is 0, as there is no previous year
        for j in range(rowcount):
            changelist[j].append(0)
    else:
        col=places[:,i] #Get all values in this col
        prevcol=places[:,i-1] #Get all values in previous col
        for v in col:
            array_pos=np.where(col == v) #returns array
            current_pos=int(array_pos[0]) #get first array value
            array_pos2=np.where(prevcol == v) #returns array
            if len(array_pos2[0])==0: #if array is empty, because place was not in previous year
                previous_pos=current_pos+1
            else:
                previous_pos=int(array_pos2[0]) #get first array value
            if current_pos==previous_pos:
                changelist[current_pos].append(0)
                print('Processed',v, current_pos)
                print('No change in rank for',v)
            elif current_pos<previous_pos: #Smaller value = higher rank
                changelist[current_pos].append(1)
                print('Processed',v, current_pos)
                print('Rank has increased for',v)
            elif current_pos>previous_pos: #Larger value = smaller rank
                changelist[current_pos].append(-1)
                print('Processed',v, current_pos)
                print('Rank has decreased for',v)
            else:
                pass
  
rankchange=np.array(changelist)            
              
print(places)
print(rankchange)
            
            
