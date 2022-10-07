
# Hong Kong October Housing Dynamic Dashboard

To view the Tableau dashboard, please follow this [link] (https://public.tableau.com/app/profile/jacky1833/viz/HongKongHousingV5/Dashboard1).
The information below will detail the project's goal, creation of dataset,
tool used, and a comprehensive user guide for the dashboard.


## Project Motivation and Goals
Hong Kong housing prices are among the highest in the world. Having lived in Hong Kong
and my parent's desire to become a homeowner in the city, the goal of this project is to create
a user-friendly and interactive dashboard that can quickly display relevant housing information.

## Dataset Creation
There are three parts in creating the housing dataset.

1. Web Scraping 

* The data is created by web scraping the three major realtor companies (Midland,squarefoot,Hkp) in Hong Kong by using the webcrawler Scrapy and Selenium. For each realtor website, we gather the key housing information such as location, address, price, and various housing features (floor level, balcony,etc). The information is then exported as csv to be cleaned.
2. Data Cleanup
* Since each of the websites has different formatting and housing features, we used Pandas to clean up the data and ensure proper merging of three datasets. Since each website has their own set of housing features(i.e. HKP was the only realtor that has rooftop as a housing feature), we only kept features that are available across the three websites. This resulted in 50+ unique housing features. To narrow down the features for cleaner data visualization, we performed exploratory analysis, correlation analysis, and mutual information to see which features have the highest impact on price.
3. Data Enhancement

* Not all key informations were available from the respective websites such longitude/latitude and respective subdistrict of each house listings. To get the longitude and latitude, we used GeoPy with the address we scrapped. This allows us to plot individual housing lists onto an interactive map on Tableau. Once we got the longitude and latitude, we were able to find the sub-district by using Hong Kong Public GeoData.

## Tools
| Tools                   | Purpose                  | Link                                                                       |
|-------------------------|--------------------------|----------------------------------------------------------------------------|
| Tableau Public          | Data Visualization       | http://public.tableau.com/profile/api/publish/HongKongHousingV4/Dashboard1 |
| Jyputer Notebook        | Python IDE               | https://jupyter.org/                                                       |
| Pandas                  | Data Management/Clean Up | https://pandas.pydata.org/                                                 |
| Scrapy                  | Web Crawler framework    | https://scrapy.org/                                                        |
| Selenium                | Automated Browser        | https://www.selenium.dev/                                                  |
| GeoPy                   | Spatial Data             | https://geopy.readthedocs.io/en/stable/                                    |
| Hong Kong GeoData Store | Spatial Data             | https://geodata.gov.hk/                                                    |
| Scikit-learn            | Feature Selections       | https://scikit-learn.org/stable/                                           |

## User Guide
The dashboard is divided into 6 different sections.

1. Map
 
 * The street view map serves two functions: the dynamic filtering for the other graphs and the relative price per square foot for each house listing. Clicking into the map will filter the district you want, and various other charts will be automatically filtered as well. To return back to whole of Hong Kong view, reselect the country that was fitlered. Housing with darker blue means a higher price per square foot. 
2. Bar graph
 
 * The bar graph shows the average price per square foot per area in a district. The darker the blue, the higher the average price per square foot.

3. Table

*  This table shows the housing information for each listing. Each house listing has a hyperlink attached. By clicking it, it will bring you to the webpage of the listings.

4. Price filter
 
 * There are two filters. The first filter allows you to filter the price range. The second filter allows you to filter the range of prices per square foot. You can either move the slider or type in the maximum or minimum values. 
5. Housing Attribute Filter
 
 * You can filter on the specific housing features you want by clicking into the circle next to the fitlers. To unselect, please click on the filter feature again. 
6. Region Filter
 
 * Instead of clicking into the map, you can also filter on region/district you want to see by clicking into the respective boxes.
 
