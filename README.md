# pep_irs_migration

These are the project files used for analyzing census population estimates and IRS migration data for New York City and the New York Metro Area for the paper "[New York's Population and Migration Trends for the 2010s](https://zicklin.baruch.cuny.edu/wp-content/uploads/sites/10/2020/09/Paper-Series-Fall-2020-9-8-20.pdf)" published in the [*Weissman Center for International Business Occasional Paper Series*](https://zicklin.baruch.cuny.edu/faculty-research/centers-institutes/weissman-center-international-business/occasional-paper-series/) in Fall 2020.

Scripts for data processing and analysis are Python Jupyter Notebooks  with Pandas stored in the scripts folder. Source and output data is saved in subfolders under this folder. Go to [scripts/output/data](https://github.com/frankpd/pep_irs_migration/tree/master/scripts/output/data) to access summary migration and estimates data for NYC and the NYMA.

The data for this project comes from: Vintage 2019 census population estimates, IRS county to county migration data from 2011-12 to 2017-18, and the 2014-18 American Community Survey.

All Python and Ipython files in this repository are released <a href="https://github.com/anastasiaclark/irs_nyc_migration/blob/master/LICENSE">under an MIT license</a>. All other files in this repository (input and output files, documentation, etc) are released under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a> <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a>.

The following are not included in this repo:

- The IRS county migration sqlite database. [Download it from the Baruch Geoportal](https://www.baruch.cuny.edu/confluence/display/geoportal/IRS+Migration+Database) and store it under scripts/source_data. Note that the database  is licensed under Creative Commons Attribution-NonCommercial-ShareAlike.
- Articles and notes for the literature review. See citations in the paper for sources.
- The paper itself, which is freely available but copyrighted.