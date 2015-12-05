# CBGA
##Organization’s Mission
Center for Budget and Governance Accountability (CBGA) is a policy research and advocacy organisation based in New Delhi. 
It analyses public policies and government finances in India, and advocates for greater transparency, accountability and public participation in budget processes.

##Project - Open Budget Portal
The organisation is aimed to develop a Comprehensive and User-Friendly Data Portal on Budgets in India, 
which could provide the citizens free, easy and timely access to relevant data on budgets at various levels of governance in the country. 
Such a Portal can augment considerably the use of appropriate budget data by researchers, policy analysts and journalists, which in turn could 
generate a lot more useful inputs for policy and budget formulation in the country at different levels. 
Moreover, such a Portal, over time, can also boost significantly the engagement of common citizens in budget processes, which in turn could
strengthen public monitoring and social accountability in the process of implementation of the budgetary policies in the country.

##Data Viz for the Budget Portal
The proposed Budget portal is intended to consist some insightful Visualizations along with other useful features.
VISUALIZATIONS – Visualizations created by us using relevant budget data for various levels of governance (addressing questions like, 
“Where is the Money Coming From?”, “Where is the Money Going?”, and so on)

###DataKind scope in Data Viz development
Few of the visualization exercise which CBGA expects DataKind to help with which can be later integrated with the budget portal:
1) BE, RE and Actuals for all Departments as given under Part A of 'Expenditure Budget', 'Volume II' of the Union Budget.  Actual figures are available from 2009-10 to 2013-14. BE and RE for 2014-15 and BE for 2015-16. Please note that Part B and C have figures for Public Sector Units and SHOULD NOT be included. There will be some chopping and changing between Departments as well. Some Ministries will only have a single Department.
2) Difference between BE & Actuals, RE & Actuals and BE & RE for all Departments during the same time period.
3) Keep focus on Agricultural department

###Technical approach
<b> Tasks break-up </b>
####1. Data Conversion
       Algorithm has been developed which would convert all the budget documents in PDF format to CSV format
       <Gaurav to add more technical details here>
####2. Data Extraction
       The data required for to build the insightful visualization has been extracted from the initially provided expenditure budget         documents in excel format.
       <Deepthi to add more technical details here>
       
####3. Data Visualization
       Designs to visualize the budget data provided at different levels are proposed. Implementation to be done during the Data Dive.
       D3.js is one of the options to build visualization
       
       D3.js is very comprehensive and difficult to master.
       D3.js Possible visualizations available at
              http://christopheviau.com/d3list/gallery.html
              https://github.com/mbostock/d3/wiki/Gallery
       
       NVD3 is a chart specific js library built on top of d3 (which will be most relevant for this project)
              http://nvd3.org/
              http://nvd3.org/examples/index.html  (This link has examples. Much easier to implement than what to be done in d3)
              
       Other charting js libraries which can be explored are HighCharts, PolyCharts
       
       Options in R
              1. ggplot library 
                     https://plot.ly/ggplot2/           (Examples)
                     http://ggplot2.org/
                     https://cran.r-project.org/web/packages/ggplot2/index.html
                     
              2. rCharts library
                     http://rcharts.io/
                     http://rcharts.io/gallery/
                     
              3. googleVis library
                     https://cran.r-project.org/web/packages/googleVis/vignettes/googleVis.pdf
                     http://rpubs.com/gallery/googleVis


