#Frank June 5, 2020
#Create formatted text tables and csvs from irs migration database for NYC
#Used to verify metro results from Jupyter Notebook
#Set first time: path to database
#Change each time: outfolder, target, series labels

from prettytable import PrettyTable
import sqlite3, csv, os

def dosql(series,sql,label):
    curs.execute(sql)
    colnames=[cn[0] for cn in curs.description]
    rows = curs.fetchall()
    x = PrettyTable(colnames)
    x.padding_width = 1
    for row in rows:
        x.add_row(row)
    print (series,":",tab)
    print (x)
    print('\n')
    tabstring = x.get_string()

    txtfile=os.path.join(outfolder,'tables',label+'.txt')

    txtoutput=open(txtfile,'w')
    txtoutput.write(series+'\n')
    txtoutput.write(label+'\n')
    txtoutput.write(tabstring)
    txtoutput.close()

    csvfile=os.path.join(outfolder,'csv',label+'.csv')
    with open(csvfile,'w', newline='') as csvoutput:
        writer=csv.writer(csvoutput, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(colnames)
        writer.writerows(rows)
    print('* Created tables for ',series, label,'\n')

#Change outfolder to a title that reflects what the data is
outfolder='nymetro'
if not os.path.exists(outfolder):
    os.makedirs(os.path.join(outfolder,'tables'))
    os.makedirs(os.path.join(outfolder,'csv'))
    
#Set first time - path to database
data_path = os.path.join('..','scripts','source_data')
sqldb = os.path.join(data_path,'irs_migration_county.sqlite')

#Change targets to FIPS code geographies to process
target_met='35620'#nymetro area
target="('34003','34013','34017','34019','34023','34025','34027','34029','34031', \
      '34035','34037','34039','36005','36047','36059','36061',\
      '36079','36081','36085','36087','36103','36119','42103')" #nymetro counties

#target_met='31080' #la metro area
#target="('06037','06059')" #la metro counties

tabs_inflow=['inflow_2017_18','inflow_2016_17','inflow_2015_16',
             'inflow_2014_15','inflow_2013_14','inflow_2012_13','inflow_2011_12']
tabs_outflow=['outflow_2017_18','outflow_2016_17','outflow_2015_16',
        'outflow_2014_15','outflow_2013_14','outflow_2012_13','outflow_2011_12']
tabs_inout=list(zip(tabs_inflow,tabs_outflow))

tabs_intotal=list((item+'_totals' for item in tabs_inflow))
tabs_outtotal=list((item+'_totals' for item in tabs_outflow))
tabs_net=list(zip(tabs_intotal,tabs_outtotal))

#Inflows
sql1='SELECT coalesce(mo.mcode, "0") AS mcode, coalesce (mo.mname, "All Other Flows") AS mname, \
sum(returns) AS returns, sum(exemptions) AS exempts \
FROM %s i \
LEFT JOIN metros md ON i.destination = md.ccode \
LEFT JOIN metros mo ON i.origin = mo.ccode \
WHERE md.mcode =  %s AND (mo.mcode != %s OR mo.mcode IS NULL) AND st_orig_abbrv != "FR" \
GROUP BY mo.mcode, mo.mname \
ORDER BY sum(exemptions) DESC' 

#Outflows
sql2='SELECT coalesce(md.mcode, "0") AS mcode, coalesce (md.mname, "All Other Flows") AS mname, \
sum(returns) AS returns, sum(exemptions) AS exempts \
FROM %s o \
LEFT JOIN metros md ON o.destination = md.ccode \
LEFT JOIN metros mo ON o.origin = mo.ccode \
WHERE mo.mcode =  %s AND (md.mcode != %s OR md.mcode IS NULL) AND st_dest_abbrv != "FR" \
GROUP BY md.mcode, md.mname \
ORDER BY sum(exemptions) DESC'

#Net change
sql3='SELECT mcode, mname, sum(returns) AS returns, sum(exemptions) AS exempts \
FROM ( \
SELECT coalesce(mo.mcode, "0") AS mcode, coalesce (mo.mname, "All Other Flows") AS mname, \
sum(returns) AS returns, sum(exemptions) AS exemptions \
FROM %s i \
LEFT JOIN metros md ON i.destination = md.ccode \
LEFT JOIN metros mo ON i.origin = mo.ccode \
WHERE md.mcode =  %s AND (mo.mcode != %s OR mo.mcode IS NULL) AND st_orig_abbrv != "FR" \
GROUP BY mo.mcode \
UNION \
SELECT coalesce(md.mcode, "0") AS mcode, coalesce (md.mname, "All Other Flows") AS mname, \
sum(returns)*-1 AS returns, sum(exemptions)*-1 AS exemptions \
FROM %s o \
LEFT JOIN metros md ON o.destination = md.ccode \
LEFT JOIN metros mo ON o.origin = mo.ccode \
WHERE mo.mcode =  %s AND (md.mcode != %s OR md.mcode IS NULL) AND st_dest_abbrv != "FR" \
GROUP BY md.mcode) \
GROUP BY mcode, mname \
ORDER BY exempts DESC'

#Summary net change
sql4='SELECT i.origin AS Summary_Level, sum(i.returns - o.returns) AS Net_Change_Returns, \
sum(i.exemptions - o.exemptions) AS Net_Change_Exempts \
FROM %s AS i JOIN %s AS o \
WHERE i.uid = o.uid \
AND i.origin LIKE "9%%" AND i.destination IN %s \
AND o.destination LIKE "9%%" AND o.origin IN %s \
GROUP BY i.origin'

con=sqlite3.connect(sqldb)
curs=con.cursor()

#Change the series labels to reflect the geography for the table

for tab in tabs_inflow:
    statement=sql1 %(tab,target_met,target_met)
    dosql('NY Metro In Migration',statement,tab)

for tab in tabs_outflow:
    statement=sql2 %(tab,target_met,target_met)
    dosql('NY Metro Out Migration',statement,tab)

for tab in tabs_inout:
    statement=sql3 %(tab[0], target_met, target_met, tab[1], target_met, target_met)
    dosql('NY Metro Net Migration',statement,str(tab[0])+'_'+str(tab[1]))

for tab in tabs_net:
    statement=sql4 %(tab[0], tab[1], target, target)
    dosql('NY Metro Total Net Migration',statement,str(tab[0])+'_'+str(tab[1]))

   
con.close()
