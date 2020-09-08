# scripts

The Ipython aka Jupyter Notebook and python 3.x files in this folder were used to summarize, analyze, and create output for all the data in this project.

- coverage_estimates: calculates how many filers are included in the migration db out of total filers for each year
- create_total_filers: was run before coverage_estimates to aggregate the source data
- foreign_pop: short script that fetched ACS table from the census API to study the origin of recent foreign-born migrants
- irs_migration: studies inflows, outflows, and net flows of migrants from the IRS migration database
- metro_county_list: was run before irs_migration to create a county to metro area relational file
- pop_estimates: studies data from the census population estimates program, loaded from csv files downloaded from their website
- rank_test: experimental script used for creating the annual rank change grids for migration (was refined and incorporated in irs_migration)