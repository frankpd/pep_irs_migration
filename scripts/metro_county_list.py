#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creates a one-to-one list of counties and the metro areas they belong to. 
The source data mixes metro-level, division-level, and county-level data in the 
same file. This script generates output that's used by the IRS migration
flows notebook.
"""
import os,csv

metro_file=os.path.join('source_data','cbsa-est2019-alldata.csv')

metros={}
counties={}

with open (metro_file,'r',encoding='latin1') as readfile:
    reader=csv.reader(readfile, delimiter=',',quotechar='"')
    next(reader, None)
    for line in reader:
        cbsa=line[0]
        metdiv=line[1]
        county=line[2]
        name=line[3]
        cbsa_type=line[4]
        if metdiv =='' and county =='':
            if cbsa in metros: #Creates unique listing of metro areas
                pass
            else:
                metros[cbsa]={'name':name,'cbsa_type':cbsa_type}
        elif county != '': #Creates unique listing of counties
            counties[county]={'name':name, 'cbsa':cbsa}
        else:
            pass
        
counties_mets=[]
        
for k in counties.keys(): #Associates each county with their metro area
    countymet=counties[k]['cbsa']
    counties_mets.append([k,counties[k]['name'],countymet,
                          metros[countymet]['name'],metros[countymet]['cbsa_type']])

counties_mets.sort()
counties_mets.insert(0,['ccode','cname','mcode','mname','mtype'])
    
newfile=os.path.join('source_data','counties_metros_2019.csv')
with open(newfile,'w', newline='', encoding='latin1') as csvoutput:
    writer=csv.writer(csvoutput, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(counties_mets)
print('Created', newfile)
