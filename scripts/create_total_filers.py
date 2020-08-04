#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reads in several years of data on total filers published by the IRS to create 
one file for specific counties. This script generates output that;s required by
the coverage estimates notebook.
"""

import os,csv

data_path = os.path.join('source_data','total_filers')
metro_counties=('34003','34013','34017','34019','34023','34025','34027','34029','34031', \
      '34035','34037','34039','36005','36047','36059','36061',\
      '36079','36081','36085','36087','36103','36119','42103') #nymetro counties
cols2keep={'STATEFIPS':None,'STATE':None,'COUNTYFIPS':None,'COUNTYNAME':None,'N1':None,'N2':None}

data=[]

for f in os.listdir(data_path):
    if f[-7:]=='agi.csv':
        fpath=os.path.join(data_path,f)
        fyear=int(f[0:2]) #This and next 2 lines create year format to match migration data
        nyear=fyear+1
        year='20'+str(fyear)+'_'+str(nyear)
        count=0
        with open (fpath,'r',encoding='latin1') as readfile:
            reader=csv.reader(readfile, delimiter=',',quotechar='"')
            row1=next(reader)
            for i,v in enumerate(row1): #Column positions shift each year; find the columns and capture their positions
                if v in cols2keep:
                    cols2keep[v]=i
            for row in reader:
                fips=row[cols2keep['STATEFIPS']]+row[cols2keep['COUNTYFIPS']] #create state-county fips
                if fips in metro_counties:
                    line=[]
                    line.extend([fips,row[cols2keep['COUNTYNAME']],row[cols2keep['STATE']],
                                 year,row[cols2keep['N1']],row[cols2keep['N2']]])
                    data.append(line)
                    count=count+1
            print('Read in ',count,'records for',f)
            
data.sort()
data.insert(0,['fips','cname','state','year','returns','exempts'])

newfile=os.path.join(data_path,'total_filers_nycmetro.csv')
with open(newfile,'w', newline='', encoding='latin1') as csvoutput:
    writer=csv.writer(csvoutput, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(data)
print('Created', newfile)
        
                    
                    
                
                

    
