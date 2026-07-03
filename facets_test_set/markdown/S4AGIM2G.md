## [Use of multi-temporal remotely sensed data for monitoring land reclamation in](https://www.researchgate.net/publication/4156755_Use_of_multi-temporal_remotely_sensed_data_for_monitoring_land_reclamation_in_Sudbury_Ontario_Canada?enrichId=rgreq-6b901852b86973e41d79c4755578c664-XXX&enrichSource=Y292ZXJQYWdlOzQxNTY3NTU7QVM6MjIyODI3MjY2NDgyMTc2QDE0MzAxMzc1Njg0OTg%3D&el=1_x_3&_esc=publicationCoverPdf) Sudbury, Ontario (Canada)

![](_page_0_Figure_3.jpeg)

# Use of Multi-temporal Remotely Sensed Data for Monitoring Land Reclamation in Sudbury, Ontario (Canada)

Abdelgadir Abuelgasim<sup>1</sup>, Chan-jo Chung<sup>1</sup>, Catherine Champagne<sup>2</sup>, Karl Staenz<sup>1</sup>, Steve Monet<sup>3</sup>, Ko Fung<sup>1</sup>

<sup>1</sup>Canada Centre for Remote Sensing, Earth Sciences Sector, Natural Resources Canada 588 Booth St., Ottawa, On, K1A 0Y7 <sup>2</sup>Agriculture and Agri-Food Canada 960 Carling Avenue Bldg. #57,Ottawa, On, K1A 0C6 <sup>3</sup>City of Greater Sudbury, Sudbury, On, Canada

#### Abstract

The industrial mining activities, conducted in the Sudbury area (Ontario, Canada) over the last 100 years, have had a significant environmental impact on the local ecosystems in the region. These impacts include habitat disturbance due to mine development, the impact of acid-generating tailings, and the effects of airborne pollution from smelting activities. The natural vegetation in the region was seriously affected, resulting in the loss of a significant portion of the vegetated cover and leading to soil erosion. As most mining regions, the city of greater Sudbury was faced with the challenges of restoration for the areas with significant ecological damage.

Towards the end of the seventies, an ambitious Regional Reclamation Program was initiated for re-vegetating affected regions. Areas with significant disturbance and barren regions were limed to reduce soil acidity and immobilize metal contaminants. The planting of mixed grasses, trees and shrubs followed this process. The major species of interest were pines (*Pinus resinosa*, *P. strobus*, *P. banksinana*), birch (*Betula papyrifera*) and trembling aspen (*Populus tremuloides*).

Planning ecological restoration activities and monitoring the results of these activities can be time consuming and expensive relying on field measurements alone. Multi-temporal remotely sensed imagery provides extensive repetitive coverage over large areas, with valuable geospatial and biological information. In this study, a multi-temporal data set of six Landsat TM images spanning a period of 20 years, was used to monitor the status of the vegetation cover, evaluate the success of the restoration program, and provide a base of information for the long-term monitoring of restored sites.

In this study, a set of environmental indicators was developed for characterizing the vegetation status at selected restoration sites. Indicators, such as the Normalized Difference Vegetation Index (NDVI), Leaf Area Index (LAI), canopy crown closure and land cover type, were used to identify the status of the vegetation over time. The changes of the environmental indicators were monitored during the 20-year period and the progress (or lack of) of the vegetation at each restoration site was assessed. The information, derived from the multi-temporal data set, was stored in a geographic information system (GIS) for evaluating the success of the re-vegetation efforts.

The results of the study indicate that as the soil and atmospheric conditions improved, the vegetation cover showed reasonable expansion in size for a larger number of restoration sites. Fewer restoration sites showed either no progress or rather a negative progress. The results, obtained from the analysis of the satellite data, showed reasonable agreement with the field measurements. Thus far, our preliminary results show that multi-temporal remote sensing data can produce useful information about the health of vegetation in the restored areas that are key in evaluating the success of the restoration program in Sudbury. The city of Sudbury will significantly benefit from the comprehensive study and make useful and informed decisions concerning the overall reclamation program.

### **Introduction and Objectives**

The intensive mining activities in the city of greater Sudbury, Ontario, Canada for the last 100 years have significantly affected the local ecosystems. The natural vegetation in the region was seriously affected, due to the habitat disturbance, acid-generating mine tailings, and the airborne pollution from the smelting activities. The combined result of these events is the damage of a significant portion of the vegetated cover and soil erosion (Winterhalder, 2002). An ambitious program of land cover restoration was initiated by the city of greater Sudbury. The program, the Sudbury Regional Land Reclamation Program, started more than three decades ago and is primarily concentrated in revegetating the seriously affected areas.

 Monitoring the success, or lack, of this re-vegetation program based on field surveys is time consuming and costly. The primary objectives of this study are to use multitemporal remotely sensed data to address key issues with respect to this program as raised by the city of greater Sudbury. The particular interests of the city of greater are summarized as:

- 1. Can relative health of trees and other vegetation be estimated from satellite imagery?
- 2. Identify indicators and measures to assess the relative health of the vegetated polygons.
- 3. Is there a relationship between lime-treated areas and the growth and relative health of trees?
- 4. Are there differences in vegetation patterns (e.g., tree cover, shrub cover, grass cover, vegetation density etc.) between lime-treated areas and untreated areas?

- 5. Is there a relationship between metal levels in soils and growth and relative health of the trees?
- 6. What is the relationship between vegetation change and wildlife habitat change in the Sudbury area?
- 7. What is the current area of barren or semi-barren land in the Sudbury area?
- 8. What vegetation cover classes currently exist within the area impacted by past mining activities?
- 9. What have been the changes to wetlands within the Sudbury area?
- 10. The development of a geographic information system (GIS) containing various layers of information to serve as the basis for future evaluation of the area and its sustainable development.

Multi-temporal remotely sensed data can certainly provide answers to some of the issues mentioned above. This study attempts to exploit the data for addressing these issues. However, the scope and results of this paper is limited to the first two.

### **Image Processing**

In this study, six Landsat TM 5 scenes have been acquired spanning the time period from 1984 to 2003. Table 1 shows the dates of acquisition for each scene. The choice was guided to a great extent by the availability of data and cloud coverage over the study area. Atmospheric correction was performed to these scenes using MODTRAN 4.2 to obtain surface reflectance (Staenz and Williams, 1997).

| Image | Acquisition Date |
|-------|------------------|
|       |                  |
| 1     | 4 June 1984      |
| 2     | 12 May 1987      |
| 3     | 5 June 1990      |
| 4     | 16 June 1994     |
| 5     | 13 July 1998     |
| 6     | 25 June 2003     |

Table 1. Landsat TM 5 Data Used

All scenes were geo-coded and geometrically corrected to a master geo-referenced scene The 2003 scene was selected as reference for the analysis. This scene was initially geocoded in accordance with the Canadian Centre for Topographic Information standards (Natural Resources Canada, 2004). Positional errors were limited to be less than 0.3 of a pixel in both the x and y direction. Radiometric calibration was performed using the bright and dark target method explained in Hall et. al., (1991). The Landsat TM 2003 scene was chosen to be the master scene for the process of radiometric calibration.

### **Methodology**

Of particular interests in this study are the assessment of the general vegetation status in the area, and the identification of the vegetation growth, or lack of, in the re-vegetated polygons. A sample of these polygons in red is overlaid on the Landsat TM 2003 image (Figure 1).

![](_page_4_Figure_2.jpeg)

Figure 1. Landsat TM scene of the study area with overlay of re-vegetated polygons

The NDVI was used as a performance measure in this study to assess the relative health of the vegetation over the time for the acquired scenes. NDVI images for each image acquisition were calculated from the reflectance data.

For assessing the general status of the vegetation between 1984 and 2003, a simple change percentile of the NDVI was developed according to:

$$NDVI_{Change} = 100*(NDVI_{2003} - NDVI_{1984})/NDVI_{1984} > 50\%$$

A 50% NDVIchange is considered the cutoff between changed and non-changed pixels.

### **Results and Discussion**

Figure 2 shows the changed pixels, in red, overlaid atop the 1984 image. Significant changes have occurred within the vicinity of the city of Sudbury in the 20 years period. Predominantly, the changes are occurring in the shrub and grasslands areas.

![](_page_5_Picture_2.jpeg)

Figure 2. Change pixels overlaid on Landsat TM image

The concentration of the vegetation growth in close proximity to the gas smelting locations (points 1,2 and 3) is an interesting finding. This suggests an overall improvement in the vegetation cover related to both the re-vegetated and natural growth in that area. These areas have been heavily damaged previously. This result is, also confirmed by field observations collected in the summer of 2004 for the area. Note that areas of natural forests, towards the lower right, are displaying less change in their NDVI values. These forests, which are further away from the smelting activities, have not been affected by the mining activities and, hence, portraying little to no-change in the forest health (Champagne, et. al., 2004).

Figures 3 (a-f) show the change of the mean NDVI value during the time period covered by the images (1984 – 2003) for selected re-vegetated polygons.

![](_page_6_Figure_1.jpeg)

Figure 3. Multi-temporal NDVI Change for selected re-vegetated polygons

The NDVI pattern shown describes the relative health and vegetation growth status within each polygon. In an ideal situation, with healthy tree growth, the NDVI line should show a continuous increasing trend in the NDVI value. Many re-vegetated polygons are displaying a pattern of tree growth while few ones are displaying negative/or lack of growth. Figures 3a, b and e, polygons planted in 1979, 1980 and 1987 are showing a positive tree growth, while those planted in 1981, 1982, and 1989 (Figures 3c, d, and f) are showing lack of healthy tree growth. This procedure was followed for all re-vegetated polygons to identify the polygons with lack of vegetation growth for field observations and further investigations.

### **Conclusions**

Uses of multi-temporal Landsat TM data are effective in the assessment of the health of the vegetation cover and in the identification of changes within these cover types. The results of the study indicate that, through the use of the NDVI temporal changes, the vegetation cover showed reasonable expansion in size for a larger number of restoration sites. However, few re-vegetated sites showed little or no progress. Areas in close proximity to the mining smelting activities are also displaying healthy progress in the time span covered by the image data. The study will continue to exploit the data set to address other issues of interest to the city of greater Sudbury. It is planned to use available multi-temporal hyperspectral data for the extraction of other environmental factors, such vegetation liquid water content, that will further aid in the assessment of the vegetation health. The integrated use of multi-spectral and hyperspectral temporal data can produce useful information that is key in evaluating the success of the restoration program in Sudbury.

### **Acknowledgements**

This work was funded through the Sustainable Development through Knowledge Integration (SDKI) Program of the Earth Science Sector (ESS) of Natural Resources Canada.

### **References**

Champagne, C., A.A. Abuelgasim, K. Staenz, S. Monet, H.P. White. 2004. Ecological restoration from space: The us of remote sensing for monitoring land reclamation in Sudbury. 16th Int. Conf. Soc. For Eco. Restoration, August 24- 26, 2004. Canada.

Hall, F. G., D. E. Strebel, J. E. Nickeson., S.J Goetz. 1991. Radiometric rectification: Toward a common radiometric response among multi-date, multi-sensor images. Remote Sensing of Environment, 35, 11 –27.

Natural Resources Canada, 2004. Landsat ETM+ Orthorectified Imagery over Canada. http://geogratis.cgdi.gc.ca.

Staenz, K. and D.J. Williams. 1997. Retrieval of surface reflectance from hyperspectral data using a look-up table approach. Canadian Journal of Remote Sensing, 23(4): 354- 368.

Winterhalder, K. 2002. The effects of the mining and smelting industry on Sudbury's landscape, in the The Physical Environment of the city of greater Sudbury, eds. D.H. Rousell and K.J. Jansons, OGS Special Volume 6, p145-174.