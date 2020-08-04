Files in this folder represent data on total number of tax filers for IRS tax years 2011 to 2017, which translates to calendar years 2012 to 2018 (i.e. taxes for the year 2011 were filed during calendar year 2012). 

The data was taken from here: https://www.irs.gov/statistics/soi-tax-stats-county-data

This data is useful in comparing the total filers in the IRS migration database, as an indicator of the percentage of all filers who were not matched between calendar years. For example, if you sum the total migrants in the inflow table, which includes all new in-migrants and total county non-migrants, you'll get the total number of filers who were matched in the migration database. Divide this by the total number of filers from this source to get the percentage of all filers who are included in the migration database.

The data for all the counties in the NY Metro area were selected and stored in the file total_filers_nycmetro.csv. The years in the column headers, which includes filers and exemptions, represents calendar years. So returns2012 and exempt2012 can be compared to migration data for 2011-2012. 

Note that the we modified the original file for 2016 in a spreadsheet, because the fips codes for counties and states had been stored incorrectly (they were saved as integers and the codes we truncated, with leading zeros dropped).
