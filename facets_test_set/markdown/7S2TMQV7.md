![](_page_0_Picture_1.jpeg)

# Canadian Journal of Fisheries and Aquatic Sciences

# Estimating the benefits of widespread floodplain reconnection for Columbia River Chinook salmon

| Journal:                                                          | Canadian Journal of Fisheries and Aquatic Sciences                                                                                                                                                              |  |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Manuscript ID                                                     | cjfas-2018-0108.R1                                                                                                                                                                                              |  |
| Manuscript Type:                                                  | Article                                                                                                                                                                                                         |  |
| Date Submitted by the Author:                                     | 15-Aug-2018                                                                                                                                                                                                     |  |
| Complete List of Authors:                                         | Bond, Morgan; Northwest Fisheries Science Center<br>Nodine, Tyler; Northwest Fisheries Science Center<br>Beechie, Tim; Northwest Fisheries Science Center<br>Zabel, Richard; Northwest Fisheries Science Center |  |
| Keyword:                                                          | Habitat Capacity, SALMON < Organisms, floodplain, river network                                                                                                                                                 |  |
| Is the invited manuscript for consideration in a Special Issue? : | Not applicable (regular submission)                                                                                                                                                                             |  |
|                                                                   |                                                                                                                                                                                                                 |  |

SCHOLARONE™ Manuscripts

| 1  | Running head: Predicting CRB side channels                                                                                   |
|----|------------------------------------------------------------------------------------------------------------------------------|
| 2  |                                                                                                                              |
| 3  | Estimating the benefits of widespread floodplain reconnection for Columbia River                                             |
| 4  | Chinook salmon                                                                                                               |
| 5  | Morgan H. Bond <sup>1</sup> , Tyler G. Nodine <sup>1,†</sup> , Tim J. Beechie <sup>2</sup> and Richard W. Zabel <sup>2</sup> |
| 6  | 1. Ocean Associates Inc.                                                                                                     |
| 7  | Under contract to: Northwest Fisheries Science Center,                                                                       |
| 8  | National Marine Fisheries Service, National Oceanic and Atmospheric Administration,                                          |
| 9  | 2725 Montlake Blvd. E., Seattle, WA 98112, USA                                                                               |
| 10 | 2. Fish Ecology Division                                                                                                     |
| 11 | Northwest Fisheries Science Center, National Marine Fisheries Service,                                                       |
| 12 | National Oceanic and Atmospheric Administration,                                                                             |
| 13 | 2725 Montlake Blvd. E., Seattle, WA 98112, USA                                                                               |
| 14 | †. Current Address: Department of Landscape Architecture and Environmental Planning,                                         |
| 15 | University of California, Berkeley, CA 94720, USA                                                                            |
| 16 |                                                                                                                              |
| 17 |                                                                                                                              |
| 18 |                                                                                                                              |
| 19 | Corresponding author: Morgan Bond, e-mail: morgan.bond@noaa.gov                                                              |
|    |                                                                                                                              |

|                       |     | 4  |   | 4  |
|-----------------------|-----|----|---|----|
| _                     | bs  | tr | o | ₽ŧ |
| $\boldsymbol{\Gamma}$ | เมอ | ш  | а | ·ι |

2.1

22

23

24

25

26

27

28

29

30

31

32

33

34

35

In the Pacific Northwest, widespread stream channel simplification has led to a loss of habitat area and diversity for rearing salmon. Subsequent efforts throughout the Columbia River Basin (CRB) have attempted to restore habitats altered through land development to recover imperiled salmon populations. However, there is scant evidence for demographic change in salmon populations following restoration. We used a process-based approach to estimate the potential benefit of floodplain reconnection throughout the CRB to Chinook salmon (Oncorhynchus tshawytscha) parr. Using satellite imagery, we measured stream habitats at 2093 CRB stream reaches to construct random forest models of habitat based on geomorphic and regional characteristics. Connected floodplain width was the most important factor for determining side channel presence. We estimated a current CRB-wide decrease in side channel habitat area of 26% from historical condition. Reconnection of historical floodplains currently used for agriculture could increase side channel habitat by 25% and spring Chinook salmon parr total rearing capacity by 9% over current estimates. Individual watersheds vary greatly in habitat factors that limit salmon recovery, and large-scale estimates of restoration potential like these are needed to make decisions about long-term restoration goals among imperiled populations.

36

37

38

39

**Key Words:** habitat capacity, salmon, random forest, river network, floodplain habitat

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

#### Introduction

Throughout decades of declining salmon population abundance in the Pacific Northwest, managers have taken considerable mitigation actions including hatchery operation, improved fish passage, and habitat restoration. Increasingly, hatchery programs are viewed skeptically, as their record as conservation tools is mixed (Naish et al. 2008). Mainstem river dam passage survival has substantially improved in recent years (Skalski et al. 2016), but recovery of Chinook salmon (Oncorhynchus tshawytscha) and other freshwater dependent salmon species has remained slow or non-existent (NOAA 2016b; a), expanding the number of evolutionarily significant units (ESU, Waples 1991) listed under the United States Federal Endangered Species Act (ESA). Currently, nearly all spring-run Chinook ESU's in the Columbia River basin are listed as either threatened (Snake River, Lower Columbia River, Upper Willamette River) or endangered (Upper Columbia River). Evidence of density dependent growth and survival of juvenile salmon in freshwater habitats, despite historically low adult abundances, has brought renewed focus on the condition of tributary habitats where spawning and primary rearing occur (Walters et al. 2013b; ISAB 2015; Bal et al. 2018). In addition, ESA listing recovery plans often indicate habitat degradation as a primary factor in declines in abundance, resulting in billions of dollars spent on restoration actions to date (Bernhardt et al. 2005; National Marine Fisheries Service 2018). Despite this immense investment, observed demographic responses to restoration actions are limited (Roni et al. 2008) because of inadequate monitoring, insufficient habitat actions (Roni et al. 2010), or survival limitations at other life stages. Recently, there has been a call for process-based approaches to stream restoration, which rely on reestablishing the appropriate functions of a stream, and, eventually the potential

diversity of habitats and biota given the constraints of the morphology and hydrology of the system (Beechie et al. 2010). Therefore, process-based restoration may seek to address the ultimate causes of stream degradation, rather than more proximate limitations on fish growth and survival. For example, floodplain reconnection may lead to channel and habitat complexity that is more persistent than engineered mainstem habitats.

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

Ecologists and fisheries resource managers have long recognized the value of habitat diversity for successive life stages of salmonids (Kiffney et al. 2006; Bisson et al. 2009). We observe ontogenetic shifts in habitat preference as the relative value of those environments changes with an individual's size, age, and physiological state (Bisson et al. 1988; Rosenfeld and Boss 2001). Further, studies have begun to demonstrate the demographic benefits of increased stream complexity for juvenile salmonids with extensive stream rearing (e.g. Chinook salmon; coho salmon, Oncorhynchus kisutch) (Morley et al. 2005; Rosenfeld et al. 2008; Bellmore et al. 2013). Therefore, stream habitat restoration occurs with an understanding that functioning freshwater habitats can promote increases in survival at all life stages of Chinook salmon (Quinn and Peterson 1996; Sommer et al. 2001; Ebersole et al. 2006). Implemented restoration actions vary widely in their scope, from in-stream wood placement and riparian plantings to improving seasonal access and flow, channel reorganization, or reclamation of floodplains (Roni et al. 2002; Bennett et al. 2016). However, the value of these actions for fish will depend upon the spatial scale of the restoration, the state of other components of the ecosystem, the persistence of the action, and the life history of the target population.

Although stream habitat complexity can be measured at small scales (e.g. streambed rugosity, large woody debris) or large (e.g. island braided channel networks), the hydrology and geomorphology of the system will determine the large scale channel heterogeneity on which

other attributes may further filter the rearing potential of a stream (e.g. primary productivity, predation, competition, etc.) (Beechie et al. 2006). Unfortunately, urbanization and agricultural development have resulted in simplification of stream channels by truncating floodplains, removing riparian vegetation, or moving streambeds (Sedell and Froggatt 1984). These processes restrict the ability of streams to produce their historical suite of habitats and biota (Allan 2004). In addition to a loss of multithread channel structure, mainstem channels can lose function by becoming either over-widened or incised (Kondolf et al. 2002; Beechie et al. 2006; Pollock et al. 2007; White et al. 2017). Therefore, to understand the potential value of widespread floodplain reconnection, we need estimates of the amount of existing habitat and its restoration potential. In the Columbia River basin (CRB), habitat modeling work has indicated that in areas with intact floodplains, channel pattern can be predicted from a few geomorphic and hydrological attributes (Beechie and Imaki 2014), validating the efficacy of estimating the historical state of streams in the CRB at large spatial scales with a fine resolution.

To make effective management recommendations about the relative benefit of various restoration scenarios affecting stream habitats, each resulting habitat type must be weighted by its value to the life stage of interest. Traditionally, habitats are weighted by capacity, or the maximum density of individuals that can be expected to reside in the habitat at that life stage, called habitat capacity. This forms the mechanism for identifying nursery habitats (Beck et al. 2001), and has been used in a number of studies to evaluate both habitat loss and the restoration potential of salmonid habitats (Beechie et al. 1994; Bartz et al. 2006; Beechie et al. 2012). An advantage of this approach is that it creates a snapshot capacity, or index, that can be compared among regions and restoration projects. Habitat capacity estimates may also benefit a limiting factors analysis with life-cycle models that track abundance and survival throughout the life

cycle (e.g. Scheuerell et al. 2006). Unfortunately, habitat capacity estimates for CRB Chinook salmon have not been produced at a scale needed for widespread restoration planning or comparison among restoration options.

Here, we employed satellite image-based measurements and empirically derived geomorphic attributes of stream habitats throughout the CRB to estimate the contribution of side channel habitats to juvenile salmon rearing area. We then computed spring-run Chinook salmon habitat capacity for each stream reach. We chose to estimate the side channel presence and restoration potential because floodplain habitats are extensively used by juvenile salmonids and are not well quantified by currently available GIS-based stream networks. Additionally, geomorphic controls on side channel habitat have shown their potential to be modeled at large spatial extents with a fine grain (Hall et al. 2007; Beechie and Imaki 2014). Finally, floodplain reconnection is a prominent, yet costly, restoration tool for imperiled stream-rearing salmon populations (Barnas et al. 2015), though the potential demographic benefit of widespread floodplain reconnection has not previously been estimated.

#### Methods

#### **Methods Overview**

To estimate the parr (young-of-the-year juvenile) Chinook salmon rearing capacity of Columbia River tributaries, we used geomorphic characteristics of stream reaches to extrapolate measurements of stream habitat area and condition from a large number of sample sites to the entire river network (Beechie and Imaki 2014; Hill et al. 2017). We measured habitat widths from recent satellite imagery at each of 2093 sample sites. We then used basin-wide estimates of topography, hydrography, geology, precipitation, and land use to estimate the discharge, slope, sediment supply, sinuosity, and confinement of each stream reach. These attributes were used to

predict mainstem stream habitat across the basin using a model that relates the variables driving channel planform (e.g. island-braided, meandering, etc.) to a stream's potential for providing high quality fish habitat (Beechie et al. 2014). Throughout habitats currently accessible to anadromous Chinook salmon, we examined alternative restoration scenarios to identify subwatersheds in which floodplain reconnection would likely create and maintain increased side channel habitats.

For streams < 8 m bankfull width (BFW), we assumed that all channels are single thread, as streams below this threshold do not have sufficient discharge and sediment supply to maintain side channels (Hall et al. 2007). In these small streams, we estimated pool and riffle area based on channel slope (Beechie et al. 1994; Beechie et al. 2001). For larger river segments (> 8 m wide) we estimated bank, bar, and mid-channel areas, as well as side channel area (Figure 1). Due to the importance of side channels in providing high quality rearing habitat and their vulnerability to floodplain modification (Morley et al. 2005; Bellmore et al. 2013), we made additional estimates of side channel habitat area under estimated historical floodplain widths and a restoration scenario that improves floodplain connectivity in agricultural regions. After habitat unit areas were estimated, we applied capacity parr densities to each distinct habitat unit, and then summed across all unit types to estimate reach- and basin-scale habitat capacities.

Uncertainty in habitat-specific parr capacity densities led us to make three contemporary capacity estimates that each utilized independent parr density data sources with our modeled habitat area estimates.

#### **CRB** stream network

Our hydrography data set spanned the entire CRB, and included reach characteristics developed by Beechie and Imaki (2014). This stream layer consists of two merged hydrography

datasets; the National Hydrography Dataset Plus (NHDplus 2.10, mapped at 1:100,000 scale (U.S. Geological Survey 2007-2014) for U.S. streams and The Watershed Atlas (mapped at 1:50,000 scale) for Canadian streams (Figure 2). The stream network is broken into 200 m segments, and each segment is designated small stream (< 8 m bankfull width) or large river (> 8 m BFW). We joined fish distribution data from the StreamNet Project (2012) to the stream layer and reaches were designated as being accessible or inaccessible to spring Chinook salmon, and whether they were utilized for rearing.

#### Habitat area estimates in small streams

In small streams (< 8 m BFW), we estimated reach area as the product of the reach length and the estimated stream width (Beechie and Imaki 2014). We accounted for heterogeneity in rearing habitat availability among reaches by estimating a pool to riffle ratio for each 200 m stream segment as a function of slope (Beechie et al. 2001). The pool:riffle ratio was used to estimate the proportion of pool and riffle habitat areas in each reach.

#### Habitat area estimates in large streams

Habitat measurement site selection

We used a Generalized Random Tessellation Stratified approach (GRTS, Kincaid 2016) to draw a spatially balanced sample of reaches from the total of 243,544 large river (> 8 m BFW) segments in the CRB. We stratified by land cover (5 types), channel type (5 types), and stream width (3 types), resulting in 75 unique strata (Table 1). Dominant land cover was assigned to each reach using a 250 m resolution continuous land cover dataset for North America (Commission for Environmental Cooperation, Land Cover 2010). We aggregated the dataset's land cover types into five classes (urban, cropland, grassland, shrubland, and forest) and calculated the dominant land cover class (class with highest frequency) that occurred in a 100 m

radius of the midpoint of each stream segment. Using channel patterns predicted by Beechie and Imaki (2014), we also stratified by the following channel types: straight, meandering, island-braided, braided, and confined. Finally, to ensure all stream sizes were represented we used estimated bankfull width (Beechie and Imaki 2014) to stratify by streams 8-20 m, 20-50 m, and >50 m BFW (Table 1). We sampled 50 sites from all island-braided strata, where we expected to find the most side channel habitat, and for all other strata we sampled 25 sites or as many sites as were available for rare combinations (e.g. >50 m, braided, urban), totaling a sample size of 2,093 reaches (Figure 2).

#### *Measurement of response variables*

We measured habitat area at each of 2093 stream segments using the highest quality aerial satellite available from Google and Microsoft. We used an imagery integration extension (Arc2Earth) to view this imagery in ArcMap 10.3 and digitize habitat characteristics. Satellite images were primarily taken during summer months between June and August. Although flow conditions, and thus wetted area, may vary among images, the relationship between main channel and side channel wetted area should be well maintained over the range of stream sizes and conditions evaluated. When we encountered images with snowfall or poor image quality obscuring habitats, we skipped that site and moved on the next site in our random draw of sites.

At each sample site we measured wetted habitat features along three transects.

Measurement transects were drawn perpendicular to valley axis with 100 m spacing. Our validation exercises showed that measuring habitat features at three transects at this spacing adequately characterized a 200 m reach (see S1-S3). Transects spanned the width of the valley floor and wherever wetted habitat was crossed the width of the feature was digitized and stored in a geodatabase with a common reach identifier.

202

203

204

205

206

207

208

209

210

211

212

213

214

215

216

217

218

219

220

221

222

223

Our primary response variables were side channel width and mainstem wetted width, but other habitat features were also digitized including bankfull width, braids, off-channels (sloughs and backwaters), and ditches as well as historical and contemporary floodplain widths (Table 2). We defined a side channel as an unmodified or minimally modified channel connected to the mainstem on two sides and separated from the mainstem by a vegetated island (Beechie et al. 2017). However, we also included side channels that were disconnected from the main channel on one end due to flow levels when the imagery was taken. If the side channel was heavily altered or degraded from its natural state and not considered to be suitable salmonid habitat it was classified as a modified channel or ditch. Channels separated from the mainstem by an unvegetated gravel bar were classified separately as braids (Beechie et al. 2017). Habitat feature widths were digitized along the transect axis except for bankfull width, which was measured perpendicular to the direction of flow. Aside from the bankfull width metric which spanned the entire width of the main channel including unvegetated bars and islands, only wetted habitats were measured; if a transect crossed a dry side channel or slough the feature was not digitized. Estimate of predictor variables We estimated side channel and mainstem habitat area for each reach in our large river network using geomorphic reach attributes calculated by Beechie and Imaki (2014) (Table 3) and additional metrics developed for this analysis. Variables developed by Beechie and Imaki (2014) include bankfull width, bankfull depth, slope, elevation, discharge, stream segment position in a reach, and sediment supply. Slopes and elevations were derived from a basin-wide 10 m digital elevation model (DEM) that was created by merging U.S. (NED) and Canadian (CDED) elevation datasets. Bankfull width, depth, and discharge were estimated based on DEM derived drainage area and mean annual precipitation models (PRISM, ClimateBC). We used two

sediment supply surrogates that were derived from flow accumulation, drainage area in alpine terrain, and flow accumulation weighted by fine sediment source. For more detail on the calculation of these reach attributes see Beechie and Imaki (2014). We also considered the variable "ecoregion", assigned to reaches using EPA level III ecoregion classes.

We estimated historical floodplain width perpendicular to the valley axis by filling valley-floor polygons derived from a detrended DEM to 5 m above main-channel elevation (Beechie and Imaki 2014). In many streams however, floodplain width has effectively been reduced due to development and land modification. Therefore, we developed an additional predictor variable of "contemporary" floodplain width, which was the historical floodplain truncated by "modified" land-use categories: urban, agriculture, and rangeland. Using a 30-m resolution land-cover datasets and road layers (Homer et al. 2015)(LU2010 Agriculture and Agri-Food Canada, USGS National Transportation Dataset, Canada National Road Network) we mapped floodplain modification and used these modified zones to restrict the historical floodplain width assigned to each reach.

To make historical side channel habitat area predictions we substituted the contemporary floodplain width used in model development with estimated historical floodplain widths and predicted side channel area for all stream segments. Although historical side-channel area provides a useful benchmark, it is not a practical restoration target as floodplain is unlikely to be reconnected in urbanized areas, including paved roads. To estimate what salmon rearing habitat may be gained by reclaiming floodplains in less urbanized areas, we used the same procedure to estimate the side channel habitat area that could be gained by reconnection in areas where floodplains are currently restricted by rangeland, cropland, and unimproved roads.

Habitat models

Because our goal was to make accurate predictions of habitat area from the available data, rather than evaluate the statistical relationship of the factors governing or correlated with side channel habitat, we elected to use random forest prediction models instead of more traditional statistical approaches like binomial/gamma hurdle models. Random forest models work well with very large datasets that include many correlated predictors and, unlike classification and regression trees, are resistant to overfitting by constructing thousands of trees with a random subset of predictors, rather than a single large tree (Cutler et al. 2012). In addition, random forest models perform equally well for both classification (presence or absence of habitat) and regression (habitat amount). We used this approach to model four important aspects of fluvial habitats for rearing salmonids: mainstem wetted width, bank and bar edge amount, presence of side channel, and total amount of side channel (in areas with a predicted presence).

To estimate mainstem habitat area, we first modeled wetted widths for each stream segment using a random forest regression. The model included eight predictors: current floodplain width, sediment accumulation, discharge, bankfull width, bankfull depth, slope, sinuosity, and elevation. Predicted wetted widths were then multiplied by stream segment length to estimate total mainstem wetted habitat area.

To account for differences in juvenile salmonid capacity among mainstem edge habitats, we measured the bank to bar ratio of both banks at a subset of 70 sites throughout the CRB with satellite imagery. We then used a random forest model to estimate the bank to bar ratio for each 200 m stream segment. The random forest regression model included slope, historical floodplain width, current floodplain width, and sediment accumulation. The resulting bank to bar ratio was used to estimate the total stream edge length occupied by banks or bars in each reach. To estimate usable bank and bar area we used regressions of bar (Eq 1.) and bank (Eq 2.) width on

total stream width developed from measurements of the Chehalis River in Washington State
 (Tim Beechie, unpublished data).

- 272 Eq 1.  $B_{rw} = 0.0872 \text{ x } W_w + 2.114$
- 273 Eq 2.  $B_{kw} = 0.0837 \text{ x } W_w + 0.328$
- Where B<sub>rw</sub> is the bar width, B<sub>kw</sub> is the bank width, and W<sub>w</sub> is the predicted stream segment
  wetted width. Mainstem habitat area not encompassed by bank and bar area was considered to be\nmid-channel area, which is not preferred habitat by salmon parr, and receives a unique density
  during fish capacity estimation.

Following measurement of satellite imagery for side and off channel area at the 2093 sample sites, side channels were present in 35% of sites, while off channel habitats were found at 2% of sites. Low rates of the presence of any side or off channel habitat indicated a hurdle model approach would be the most effective at estimating habitat areas (Potts and Elith 2006). A hurdle model is used for count data where separate processes may govern the presence and magnitude of the response, and where the zeros cannot be effectively modeled with standard probability distributions (Martin et al. 2005). Therefore, the presence/absence is modeled first, and sites where the presence of habitat is predicted are placed into a second model to estimate the magnitude.

To construct predictive models we created a binary classification of side and off channel habitats, 0 where no habitat was present, and 1 where any side or off channel was measured. Therefore, the entire suite of 2093 sites were used to construct the classification model. We randomly selected 80% of sites to be included in training the model, with the remaining 20% reserved for testing model accuracy. To train the random forest model we included 12 predictors: current floodplain width, historical floodplain width, discharge, flow by precipitation, sediment,

sediment accumulation, average elevation, watershed position, flow accumulation, ecoregion, slope and hydrologic regime (Table 3). We constructed models with the randomForest and caret packages in the R statistical software platform version 3.2.3 (R Development Core Team 2011). During the training phase we used 10-fold cross-validation and tuned two parameters: the number of trees constructed, and the number of variables randomly drawn to include at each tree node. We used the kappa tuning metric, and evaluated the final model for balanced accuracy. Our final model included 2000 trees and two variables at each node. A second regression random forest model was constructed with only the 874 sites that had side channels present, using the same suite of predictors used in the side channel presence classification model. We used the same training procedure employed in the classification model but tuned the regression model by maximizing the receiver operating characteristic (ROC).

Once both models were sufficiently tuned, we used the classification model to predict the presence or absence of side channel habitat for all CRB stream segments. For all sites with a predicted side channel presence, the regression model was used to predict side channel area. The effect of floodplain width on side channel presence and area in our models allows for the prediction of side channels with a novel floodplain width. Therefore, to estimate historical side channel area and floodplain restoration potential, we made new predictions with both models where floodplain width was updated to historical or restoration width values.

#### **Fish Capacity Estimation**

A key uncertainty in translating habitat area to habitat capacity lies in choosing appropriate fish densities to populate each stream segment. Problems can arise with differences in scale between habitat estimates and fish density data that misrepresent capacity. Additionally, much of the empirical fish density data available has been collected at historically low

abundances, and may only characterize capacity at the smallest spatial scales. In light of these difficulties, we chose to apply three independent data sources of spring Chinook parr density to our modeled habitat areas at scales appropriate for each data source, effectively producing three separate capacity estimates.

- 1. A habitat expansion based on the total area of each habitat type multiplied by habitat-specific fish densities for small and large streams (Table 4).
- A coarser expansion based on reach-level habitat characteristics, total wetted area of each large stream reach, and a quantile regression of observed reach-level fish densities in the CRB.
- 3. A single, empirically derived parr capacity estimate based on observed average fish densities from mid-summer snorkel surveys in the Salmon River and total habitat area estimates for large stream reaches (Thorson et al. 2014).

We used densities from review and re-analysis of published and unpublished habitat specific capacities spring Chinook parr (Beechie and Thompson, unpublished data, Table 4). These data were derived primarily from repeated beach seining or electrofishing specific habitat types over a range of stream flows and spawner abundances in the Skagit River, the most abundant Chinook salmon population in the ESA listed Puget Sound ESU. Skagit River Chinook densities have been used in previous habitat capacity studies (Beechie et al. 2015) because of an abundance of habitat-specific juvenile densities derived from extensive monitoring in that system (Beechie et al. 2005a; Zimmerman et al. 2015). The average maximum observed parr density was applied to each habitat type: side channel, mainstem bank, mainstem bar, mainstem mid-channel, small stream pool, and small stream riffle.

339

340

341

342

343

344

345

346

347

348

349

350

351

352

353

354

355

356

357

358

359

360

The quantile regression approach is also an expansion approach, but the fish density data were for entire stream reaches and not separated by habitat type. Therefore, a single abundance and wetted area were used to calculate density. The Integrated Status and Effectiveness Monitoring Program (ISEMP) has been electrofishing stream reaches previously sampled by the Columbia River Habitat Monitoring Program (CHaMP) for several years. The ISEMP data have the advantage of being measured over a range of spawner abundances. However, the observed fish density at a given site may vary from zero to several fish per m<sup>2</sup> over the period of record. Therefore, a mean or median density may not accurately reflect capacity. To account for these differences we used a quantile random forest procedure, which allows for the modeling of any percentile of fish density (Cade and Noon 2003). We indexed the ISEMP sample densities for spring Chinook to the sites used in our habitat model construction and used the same suite of predictors to model fish capacity. We created and tuned quantile random forest models with the R package quantregForest using similar tuning procedures to the habitat estimation. After tuning, we predicted the 90th percentile fish density for each stream segment, and multiplied those densities by the sum of mainstem and side channel habitat for that reach. Finally, we employed the spring Chinook capacity estimated from a hierarchical stockrecruit model of spawner and mid-summer parr densities in the Salmon River (Thorson et al. 2014). Thorson et al. (2014) used decades of snorkel survey data to estimate an average capacity of 5200 parr/hectare. To estimate capacity we multiplied the total habitat area (mainstem bars, mainstem banks, side channel) in hectares by 5200, regardless of reach characteristics or habitat types. Because of data limitations, both quantile regression and snorkel estimated capacities were made for streams greater than 8 m BFW only, and small streams were characterized by the pool and riffle specific fish densities.

362

363

364

365

366

367

368

369

370

371

372

373

374

375

376

377

378

379

380

381

382

383

#### Results

#### Habitat area prediction

We estimated large river (>8m BFW) mainstem habitat areas with two random forest models, one for wetted width of the main channel and one for bank to bar edge habitat ratios. Regression of predicted versus measured wetted widths indicated that the wetted width model performed well, with slope near one and intercept near zero, and an  $R^2$  of 0.86 (n = 419, Figure 3). Estimated stream discharge was the most important variable in the model predicting wetted width (Figure 4). Bank to bar ratios were also relatively accurately estimated (regression slope and intercept near one and zero, respectively), but with lower precision ( $R^2 = 0.58$ , n = 70). Off channel habitats were too rare in our dataset to make useful landscape level predictions. Although the model had a high sensitivity (true positive rate, 99%), the specificity (true negative rate, 81%) led to vast overestimates of off channel habitat. While we measured only 46 sites with off channel habitat, our model predicted 407 sites with off channel habitat. In contrast, our model predicting the presence of any side channel had a balanced accuracy (correct positive and negative detections) of 75% when tested on the 20% of sites withheld from model development, although there was some bias between specificity (true negative rate, 86%) and sensitivity (true positive rate, 60%) of the classification. Overall, the model tended to under-predict side channel presence; 640 of 2093 reaches were predicted to have side channels, fewer than the 732 we measured. Floodplain width was the most important predictor in determining side channel presence (Figure 5) with the prevalence of side channels increasing rapidly as floodplain width increased from 0 m to 500 m, then remaining relatively flat with increasing floodplain width (Figure 6). A regression of predicted on measured total side channel area had an R<sup>2</sup> of 0.52, when predicting

sites not included in model development. The most important predictor in the side channel area model was river discharge (Figure 7). While floodplain width was less important in the model, side channel area increases with increasing floodplain width up to floodplain width of about 2 km (Figure 8). However, the largest effect of floodplain width on side channel area occurs in the first 250 m of floodplain width.

Across all HUC-8 watersheds (US Geological Survey level 8 hydrologic unit) containing spring Chinook (Table 5) we estimated approximately 45,270 hectares of contemporary juvenile rearing habitat. Contemporary side channel habitat comprises 13.6% of the total wetted habitat area. However, contemporary side channels comprise over 42% of the high value juvenile rearing habitat (i.e., all habitat excluding mid-channel area). Across the CRB, the contemporary area of side channel habitat was 26% lower than historical estimates, although individual HUC-8's range from 0% to 78% loss in side channel area. Our model predicted that restoration of floodplain connectivity in rangeland, cropland, and areas currently restricted by small roads could increase side channel habitat by as much as 25% across the CRB, although individual HUC-8's could see increases of none, to as much as 333% above current side channel area.

#### Fish capacity estimates

Estimates of contemporary Chinook parr capacity using the habitat expansion method varied substantially among watersheds, totaling 96.6 million parr across the entire currently accessible portion of the CRB (Table 5, Figure 10). As a percentage of total reach production, contemporary side channel habitat accounted for 40% of total parr capacity, although the percentage varied widely among watersheds, from 0-59% (Figure 11). The quantile random forest method of assigning capacity to each stream segment predicted fewer fish in most watersheds, but many more at a few sites (e.g. Middle and Upper Willamette). In total, the

quantile regression method estimates a higher Chinook parr capacity than habitat expansion (105.8 million parr) (Table 5). Chinook parr capacity estimated from applying 5,200 fish per hectare to the total wetted area for each reach produced a lower total capacity than either expansion or quantile random forests (76 million parr across all watersheds). However, the Upper Willamette HUC-8 watershed alone accounted for much of the difference between the methods, with over 16 million parr predicted using quantile random forest, compared to 7.4 million and 5.8 million for habitat expansion and 5200/hectare, respectively. For many watersheds, the estimates were very similar among methods; the coefficient of variation among was less than 20% for 27 of 57 watersheds. There was a small but significant ( $R^2 = 0.11$ , F(1, 56) = 6.82, P = 0.011) increase in CV with increasing proportion of side channel area, but no increase in CV with increasing total habitat area ( $R^2 = 0.01$ , F(1, 56) = 0.39, P = 0.53).

Using the habitat expansion approach we estimated potential changes in Chinook parr capacity due to restoration by increasing the current floodplain width to include rangeland and cropland. This scenario increased CRB-wide capacity by 9.4% over contemporary estimates, although there were a few watersheds with increases of 50% or more, notably the Lemhi R. (81%), and Upper Grande Ronde (70%, Table 5, Figure 12).

#### **Discussion**

Currently, multiple CRB Chinook salmon population trends suggest density dependent processes may be limiting freshwater growth and survival despite historically low population abundances, indicating that habitat quality or quantity may be limiting recovery (Walters et al. 2013b; ISAB 2015). One important constraint to population recovery may be loss of side channels that often provide high quality rearing habitat for juvenile salmon and other stream fishes. However, despite widespread urbanization and agricultural development, loss of

431

432

433

434

435

436

437

438

439

440

441

442

443

444

445

446

447

448

449

450

451

floodplain habitat has not been ubiquitous in the CRB. Our analysis demonstrates that watersheds vary widely in historical, contemporary, and restoration potential of side channel habitats. In many watersheds, side channels were likely never prominent habitats, as valley confinement has limited their creation or maintenance, restricting their potential for floodplain habitat restoration. For example, tributaries of the upper Columbia River and Clearwater River have few areas where widespread floodplain reconnection would provide additional side channel habitat because those streams are naturally confined (Figure 12). However, we note that areas with little floodplain restoration potential should not be viewed as without other restoration opportunities. Naturally confined stream channels operate as collectors of allocthonous material that increases the productivity and diversity of more complex habitats downstream (Bellmore and Baxter 2014). In these areas, other process-based restoration options are available to restore stream complexity and function (e.g. natural flow patterns, wood delivery, or riparian function, Beechie et al. 2010). Additionally, the importance of discharge in our models indicates that sufficient stream flow is needed to create or maintain side channels regardless of floodplain width. Although we did not distinguish between flow regulated and flow unregulated river reaches, deviations form a natural flow regime in many watersheds may reduce the connection and ecological function of floodplain habitats which would limit their restoration value (Galat et al. 1998). In watersheds with more extensive historical floodplains, our model suggests that there are widespread floodplain restoration opportunities. While reconnecting entire floodplains is

are widespread floodplain restoration opportunities. While reconnecting entire floodplains is impractical in many areas, our analysis demonstrates that in many streams a modest increase in active channel width is likely to substantially increase the amount of side channel. On average,

the greatest improvement in side channel presence and area was found with a floodplain width increase of ca. 250 m (Figures 6 and 8).

Where feasible, large-scale floodplain restoration activities can lead to increases in productivity (Bellmore et al. 2017), and Chinook salmon populations experiencing density dependence at contemporary spawner numbers may benefit from increases in rearing habitat (Walters et al. 2013b). Floodplains are known to contain a variety of prominent rearing habitats for salmon parr (Beechie et al. 1994; Morley et al. 2005; Bellmore et al. 2013). Within floodplains, side channels can provide increased growth opportunities (Sommer et al. 2001; Giannico and Hinch 2003; Jeffres et al. 2008), as well as refuge from predation because shallower side channels are generally unoccupied by larger piscivorous species (Bellmore et al. 2013). While we found no studies that empirically evaluated the benefit of constructed or reconnected side channels for Chinook salmon, studies of natural systems showed that densities of Chinook salmon during winter were an order of magnitude higher than in the adjacent mainstem or nearby tributaries (Martens and Connolly 2014). Moreover, seasonally inundated floodplain habitats have demonstrated higher growth and survival of juvenile Chinook salmon (Sommer et al. 2001), indicating a potential value to salmon beyond habitat capacity.

Mainstem habitats comprise the majority of wetted habitat in our model, and their value for rearing fish cannot be understated. However, there are several potential improvements in the estimation of mainstem habitat area that could be made. First, we were not able to measure the width of favorable flow and depth from satellite imagery, so our estimates rely on measurements of bar and bank edge widths from the Chehalis River in coastal Washington State. Bank and bar forming processes are likely similar in the Chehalis River and CRB, but measuring bar and bank widths at various locations in the CRB would increase confidence in the model estimates of edge

habitat area. Second, we were unable to address other habitat types such as hydromodified banks and backwaters, which decrease and increase rearing capacity, respectively (Beamer and Henderson 1998; Beechie et al. 2005a). Measurement of these features may improve model accuracy, although total capacities of these habitat types at the watershed and larger spatial scale are likely very small relative to the capacity of natural banks and bars.

Although we estimated the potential for increases in rearing habitat resulting from floodplain reconnection, the benefits of floodplain reconnection extend beyond the creation and maintenance of side channels. Floodplain habitats tend to increase the overall heterogeneity of riverine habitats through periodic inundation (Ward et al. 1999; Tockner and Stanford 2002), which produces a diverse and productive link between aquatic and terrestrial ecosystems (Junk et al. 1989). Therefore, where geomorphologically appropriate, allowing floodplain reconnection will directly benefit riverine vertebrates and invertebrates through increased growth and survival (Galat et al. 1998; Tockner et al. 2010). However, successful floodplain reconnection requires that appropriate flow, sediment supply, and wood delivery, along with intact riparian habitat in the reconnected area to allow the diversity of biotic and abiotic function needed for their long-term viability. Unfortunately, in many parts of the CRB impoundments or water diversions may sufficiently restrict flow and sediment such that the dynamism of stream channels might continue to be reduced, despite floodplain reconnection.

Our habitat capacity estimates result from several separate habitat models and sources of parr density data. Therefore, multiple sources and scales of uncertainty exist in our modeling process. At the smallest spatial scale, previous work has shown a high degree of accuracy (e.g. R2 = 0.98, Beechie et al. 2005b) measuring stream widths from aerial photography of similar resolution to our satellite imagery. A larger source of error is the variation in image collection

dates, as stream widths and side channel inundation will vary with seasonal flows. Although varying image dates add error in our analysis, a time series of images over a range of discharges will eventually lead to better estimates of bank slopes and edge habitat. We also chose to measure wetted habitat along three evenly spaced transects perpendicular to each reach, rather than digitizing all habitats in each sample reach reach. This faster method classified habitats well (see S1-S3), although very small side channels may have been missed. The benefit of this streamlined approach is that it allowed us to measure 2093 sites stratified across the entire CRB. Although there is uncertainty in our predictions of mainstem and side channel habitats in unmeasured reaches, there appears to be little bias in our estimates (Figures 3 and 9). Ultimately we were not able to propagate the error from all of these sources to create a confidence interval for our aggregated estimates, but the goal of our approach was large scale estimates of habitat capacity, not reach specific estimates that would be better served by on the ground site visits. Our watershed scale estimates would benefit from validation with independent measures of habitat area that are currently unavailable at comparable scales.

A larger source of uncertainty in habitat capacity analyses likely arises from variation in available fish density data. Although a review of published and unpublished fish density data by Beechie and Thompson resulted in habitat-specific (i.e., bank, bar, mid-channel, side channel) capacity estimates, these data were primarily collected outside of the CRB, in Puget Sound rivers that may not be representative of CRB habitats. The most extensive CRB spring Chinook fish density data come from ISEMP, and were included in our quantile random forest approach to applying parr densities to each reach. Although these data include electrofishing densities from hundreds of sites throughout the CRB, even the 90<sup>th</sup> percentile of data may not represent capacity in populations that are far below their historical spawner density. Additionally, ISEMP densities

are aggregated at the reach scale, and separate densities for habitats within a reach are not available. Average parr capacity of 5200 parr per hectare from Thorson et al.'s (2014) hierarchical model of several decades of snorkel based fish counts in Idaho streams provided another independently derived parr capacity. However, their model selection indicated a population specific capacity was warranted, possibly owing to differences in habitat quality among streams. The mild increase in CV we observed among capacity estimates with increasing proportion of side channel habitat is likely a factor of the higher value placed on side channel habitats in habitat expansion compared to the single value applied to all habitats in a reach with quantile regression and fixed density approaches.

One important assumption of the habitat capacity approach is that all habitats are at a fully seeded capacity, a state that is unlikely to occur in the wild at larger spatial scales, but provides a useful index for comparisons. In this sense habitat capacity is distinct from population capacity, which is an asymptotic or long-term average capacity, derived from fitting demographic data to models that assume density-dependence (Ricker 1954; Beverton and Holt 1957; Barrowman and Myers 2000). This important difference between habitat and population capacity makes validation of habitat capacity estimates from monitoring data impractical, as observations of abundance at the population level are a composite of fully seeded and underseeded habitats and density dependent processes therein. It is our expectation, therefore, that habitat capacity estimates exceed population capacity estimates in most circumstances. That said, comparisons between habitat capacity and population capacity could inform us whether limitations on the population are occurring at the spawning or pre-parr stage (population capacity << habitat capacity) or at the overwintering, smolt, or marine survival stage (population capacity habitat capacity). Estimation of habitat capacity, and the change in habitat capacity that may

result from management or restoration actions, allows for a direct comparison of the benefit of various options independent of contemporary population dynamics (Walters et al. 2013a).

Often, individual restoration projects may be too small to detect a beneficial response, or other limiting factors in the watershed constrain their benefits (Roni et al. 2002, Beechie et al. 2008). Recently, monitoring and modeling efforts have been used to quantitatively evaluate the potential benefits of habitat restoration at larger spatial scales (e.g., Bartz et al. 2006; Wall et al. 2016; Justice et al. 2017; Wheaton et al. 2018). Similarly, our estimates of floodplain restoration potential are a first step to providing managers with guidance for focusing floodplain restoration efforts on areas with the greatest potential for increasing salmon abundance and survival. These results can be further combined with life-cycle models to demonstrate the potential benefits of restoration for increases in adult salmon abundance (Bartz et al. 2006; Scheuerell et al. 2006), as well as to identify target reaches of high floodplain restoration potential within watersheds. Both types of studies are underway in the CRB, and the combination of our results with those of other studies should increase the cost-effectiveness of restoration efforts.

We recognize that reconnecting side channels and other floodplain habitats is only one of many habitat restoration actions that are needed for salmon recovery. A thorough body of work has related increased abundance of wood in streams to higher habitat quality for salmonids (Montgomery et al. 2003; Whiteway et al. 2010; Roni et al. 2015). Additional studies highlight the importance of riparian restoration for decreasing summer stream temperatures and ameliorating climate change effects on stream temperature (Beechie et al. 2000; Beechie et al. 2013). While these types of actions are important for realizing the full benefits of side channel restoration, these actions without floodplain restoration will likely achieve a more limited benefit

and provide less resilience to future climate change effects (Beechie et al. 2013; Bellmore et al. 2017).

In addition to ecosystem needs, restoration project selection relies on available funding, feasibility, and level of interest by practitioners. Funding for habitat restoration in Pacific Northwest streams is generally top-down, originating with a handful of Federal agencies; yet decision-making about habitat actions is often bottom-up and decentralized, with projects chosen by local entities at scales smaller than ESUs. This piecemeal project selection process has resulted in a lack of coordination and planning for restoration at population scales, resulting in potential mismatch between ecological need and funded projects (Beechie et al. 2008; Barnas et al. 2015). Further studies estimating the restoration potential and resulting potential demographic response for other restoration types throughout the CRB are needed. This approach would allow for a more formal analysis of the relative or synergistic effects of each restoration option and a cost-benefit analysis to focus restoration funds toward more effective projects.

#### Acknowledgements

Funding for this study was provided by NOAA Fisheries. Hiroo Imaki provided landscape characteristics included in our model. Aimee Fullerton provided comments on earlier versions of the manuscript. Martin Liermann provided comments on the manuscript and assisted with GRTS sampling design. This manuscript benefitted from thorough reviews by two anonymous reviewers.

586 Literature Cited

Allan, J.D. 2004. Landscapes and Riverscapes: The Influence of Land Use on Stream

Ecosystems. Annual Review of Ecology, Evolution, and Systematics 35(1): 257-284.

| 590 | Bal, G., Scheuerell, M.D., and Ward, E.J. 2018. Characterizing the strength of density          |
|-----|-------------------------------------------------------------------------------------------------|
| 591 | dependence in at-risk species through Bayesian model averaging. Ecological Modelling            |
| 592 | <b>381</b> : 1-9.                                                                               |
| 593 | Barnas, K.A., Katz, S.L., Hamm, D.E., Diaz, M.C., and Jordan, C.E. 2015. Is habitat restoration |
| 594 | targeting relevant ecological needs for endangered species? Using Pacific Salmon as a           |
| 595 | case study. Ecosphere <b>6</b> (7): 1-42.                                                       |
| 596 | Barrowman, N.J., and Myers, R.A. 2000. Still more spawner-recruitment curves: the hockey        |
| 597 | stick and its generalizations. Canadian Journal of Fisheries and Aquatic Sciences 57(4):        |
| 598 | 665-676.                                                                                        |
| 599 | Bartz, K.K., Lagueux, K.M., Scheuerell, M.D., Beechie, T., Haas, A.D., and Ruckelshaus, M.H.    |
| 600 | 2006. Translating restoration scenarios into habitat conditions: an initial step in             |
| 601 | evaluating recovery strategies for Chinook salmon (Oncorhynchus tshawytscha).                   |
| 602 | Canadian Journal of Fisheries and Aquatic Sciences 63(7): 1578-1595.                            |
| 603 | Beamer, E.M., and Henderson, R. 1998. Juvenile salmonid use of natural and hydromodified        |
| 604 | stream bank habitat in the mainstem Skagit River, northwest Washington. Report                  |
| 605 | prepared for US Army Corps of Engineers Seattle District, Skagit System Cooperative,            |
| 606 | LaConner, WA.                                                                                   |
| 607 | Beck, M.W., Heck, K.L., Jr., Able, K.W., Childers, D.L., Eggleston, D.B., Gillanders, B.M.,     |
| 608 | Halpern, B., Hays, C.G., Hoshino, K., Minello, T.J., Orth, R.J., Sheridan, P.F., and            |
| 609 | Weinstein, M.P. 2001. The identification, conservation, and management of estuarine and         |
| 610 | marine nurseries for fish and invertebrates. Bioscience <b>51</b> (8): 633-641.                 |

| 611 | Beechie, T., Beamer, E., and Wasserman, L. 1994. Estimating Coho Salmon Rearing Habitat and      |
|-----|--------------------------------------------------------------------------------------------------|
| 612 | Smolt Production Losses in a Large River Basin, and Implications for Habitat                     |
| 613 | Restoration. North American Journal of Fisheries Management 14(4): 797-811.                      |
| 614 | Beechie, T., and Imaki, H. 2014. Predicting natural channel patterns based on landscape and      |
| 615 | geomorphic controls in the Columbia River basin, USA. Water Resour Res <b>50</b> (1): 39-57.     |
| 616 | Beechie, T., Pess, G., and Imaki, H. 2012. Estimated changes to Chinook salmon (Oncorhynchus     |
| 617 | tshawytscha) and steelhead (Oncorhynchus mykiss) habitat carrying capacity from                  |
| 618 | rehabilitation actions for the Trinity River, North Fork Trinity to Lewiston Dam.                |
| 619 | Beechie, T., Pess, G., Morley, S., Butler, L., Downs, P., Maltby, A., Skidmore, P., Clayton, S., |
| 620 | Muhlfeld, C., and Hanson, K. 2013. Chapter 3: Watershed assessments and identification           |
| 621 | of restoration needs. In Stream and Watershed Restoration: A Guide to Restoring                  |
| 622 | Riverine Processes and Habitats. Edited by P. Roni and T. Beechie. Wiley-Blackwell,              |
| 623 | Chichester, UK. pp. 50-113.                                                                      |
| 624 | Beechie, T., Pess, G., and Roni, P. 2008. Setting river restoration priorities: a review of      |
| 625 | approaches and a general protocol for identifying and prioritizing actions. North                |
| 626 | American Journal of Fisheries Management 28(3): 891-905.                                         |
| 627 | Beechie, T.J., Collins, B.D., and Pess, G.R. 2001. Holocene and recent geomorphic processes,     |
| 628 | land use, and salmonid habitat in two north Puget Sound river basins. Geomorphic                 |
| 629 | processes and riverine habitat, Water Science and Application 4: 37-54.                          |
| 630 | Beechie, T.J., Liermann, M., Beamer, E.M., and Henderson, R. 2005a. A classification of habitat  |
| 631 | types in a large river and their use by juvenile salmonids. Transactions of the American         |
| 632 | Fisheries Society <b>134</b> (3): 717-729.                                                       |

| 633 | Beechie, T.J., Liermann, M., Pollock, M.M., Baker, S., and Davies, J. 2006. Channel pattern and |
|-----|-------------------------------------------------------------------------------------------------|
| 634 | river-floodplain dynamics in forested mountain river systems. Geomorphology <b>78</b> (1-2):    |
| 635 | 124-141.                                                                                        |
| 636 | Beechie, T.J., Pess, G., Kennard, P., Bilby, R.E., and Bolton, S. 2000. Modeling Recovery Rates |
| 637 | and Pathways for Woody Debris Recruitment in Northwestern Washington Streams.                   |
| 638 | North American Journal of Fisheries Management 20(2): 436-452.                                  |
| 639 | Beechie, T.J., Pess, G.R., Imaki, H., Martin, A., Alvarez, J., and Goodman, D.H. 2015.          |
| 640 | Comparison of potential increases in juvenile salmonid rearing habitat capacity among           |
| 641 | alternative restoration scenarios, Trinity River, California. Restoration Ecology 23(1): 75-    |
| 642 | 84.                                                                                             |
| 643 | Beechie, T.J., Sear, D.A., Olden, J.D., Pess, G.R., Buffington, J.M., Moir, H., Roni, P., and   |
| 644 | Pollock, M.M. 2010. Process-based Principles for Restoring River Ecosystems.                    |
| 645 | Bioscience <b>60</b> (3): 209-222.                                                              |
| 646 | Beechie, T.J., Timpane-Padgham, B., Stefankiv, O., Hall, J., Pess, G., Liermann, M., Rowse, M., |
| 647 | Fresh, K., and Ford, M. 2017. Monitoring salmon habitat status and trends in Puget              |
| 648 | Sound: development of sample designs, monitoring metrics, and sampling protocols for            |
| 649 | large river, floodplain, delta, and nearshore environments. Edited by U.S. Department of        |
| 650 | Commerce. NOAA Technical Memorandum NMFS-NWFSC-137.                                             |
| 651 | Beechie, T.J., Veldhuisen, C.N., Beamer, E.M., Schuett-Hames, D.E., Conrad, R.H., and           |
| 652 | DeVries, P. 2005b. Monitoring treatments to reduce sediment and hydrologic effects              |
| 653 | from roads. In Monitoring stream and watershed restoration. American Fisheries Society,         |
| 654 | Bethesda, Maryland. Edited by P. Roni. pp. 35-66.                                               |

655 Bellmore, J.R., and Baxter, C.V. 2014. Effects of Geomorphic Process Domains on River 656 Ecosystems: A Comparison of Floodplain and Confined Valley Segments. River 657 Research and Applications **30**(5): 617-630. 658 Bellmore, J.R., Baxter, C.V., Martens, K., and Connolly, P.J. 2013. The floodplain food web 659 mosaic: a study of its importance to salmon and steelhead with implications for their 660 recovery. Ecological Applications **23**(1): 189-207. 661 Bellmore, J.R., Benjamin, J.R., Newsom, M., Bountry, J.A., and Dombroski, D. 2017. 662 Incorporating food web dynamics into ecological restoration: a modeling approach for 663 river ecosystems. Ecological Applications 27(3): 814-832. Bennett, S., Pess, G., Bouwes, N., Roni, P., Bilby, R.E., Gallagher, S., Ruzycki, J., Buehrens, T., 664 Krueger, K., Ehinger, W., Anderson, J., Jordan, C., Bowersox, B., and Greene, C. 2016. 665 666 Progress and Challenges of Testing the Effectiveness of Stream Restoration in the Pacific 667 Northwest Using Intensively Monitored Watersheds. Fisheries **41**(2): 92-103. Bernhardt, E.S., Palmer, M.A., Allan, J.D., Alexander, G., Barnas, K., Brooks, S., Carr, J., 668 669 Clayton, S., Dahm, C., Follstad-Shah, J., Galat, D., Gloss, S., Goodwin, P., Hart, D., Hassett, B., Jenkinson, R., Katz, S., Kondolf, G.M., Lake, P.S., Lave, R., Meyer, J.L., 670 671 O'Donnell, T.K., Pagano, L., Powell, B., and Sudduth, E. 2005. Ecology - Synthesizing 672 US river restoration efforts. Science **308**(5722): 636-637. 673 Beverton, R.J., and Holt, S.J. 1957. On the dynamics of exploited fish populations. Fish. Invest. 674 Ministry Agric. Fish. Food (GB) Ser. II. Bisson, P.A., Dunham, J.B., and Reeves, G.H. 2009. Freshwater Ecosystems and Resilience of 675 676 Pacific Salmon: Habitat Management Based on Natural Variability. Ecology and Society 677 **14**(1).

| 678 | Bisson, P.A., Sullivan, K., and Nielsen, J.L. 1988. Channel hydraulics, habitat use and body form |
|-----|---------------------------------------------------------------------------------------------------|
| 679 | of juvenile coho salmon, steelhead and cutthroat trout in streams. Trans. Am. Fish. Soc.          |
| 680 | <b>117</b> : 262-273.                                                                             |
| 681 | Cutler, A., Cutler, D.R., and Stevens, J.R. 2012. Random Forests. Ensemble Machine Learning:      |
| 682 | Methods and Applications: 157-175.                                                                |
| 683 | Ebersole, J.L., Wigington, P.J., Baker, J.P., Cairns, M.A., Church, M.R., Hansen, B.P., Miller,   |
| 684 | B.A., LaVigne, H.R., Compton, J.E., and Leibowitz, S.G. 2006. Juvenile Coho Salmon                |
| 685 | Growth and Survival across Stream Network Seasonal Habitats. Transactions of the                  |
| 686 | American Fisheries Society 135(6): 1681-1697.                                                     |
| 687 | Galat, D.L., Fredrickson, L.H., Humburg, D.D., Bataille, K.J., Bodie, J.R., Dohrenwend, J.,       |
| 688 | Gelwicks, G.T., Havel, J.E., Helmers, D.L., Hooker, J.B., Jones, J.R., Knowlton, M.F.,            |
| 689 | Kubisiak, J., Mazourek, J., McColpin, A.C., Renken, R.B., and Semlitsch, R.D. 1998.               |
| 690 | Flooding to restore connectivity of regulated, large-river wetlands - Natural and                 |
| 691 | controlled flooding as complementary processes along the lower Missouri River.                    |
| 692 | Bioscience <b>48</b> (9): 721-733.                                                                |
| 693 | Giannico, G.R., and Hinch, S.G. 2003. The effect of wood and temperature on juvenile coho         |
| 694 | salmon winter movement, growth, density and survival in side-channels. River Research             |
| 695 | and Applications <b>19</b> (3): 219-231.                                                          |
| 696 | Hall, J.E., Holzer, D.M., and Beechie, T.J. 2007. Predicting river floodplain and lateral channel |
| 697 | migration for salmon habitat conservation. J Am Water Resour As 43(3): 786-797.                   |
| 698 | Hill, R.A., Fox, E.W., Leibowitz, S.G., Olsen, A.R., Thornbrugh, D.J., and Weber, M.H. 2017.      |
| 699 | Predictive Mapping of the Biotic Condition of Conterminous-USA Rivers and Streams.                |
| 700 | Ecological Applications in press: n/a-n/a.                                                        |

701 Homer, C.G., Dewitz, J.A., Yang, L., Jin, S., Danielson, P., Xian, G., Coulston, J., Herold, N.D., 702 Wickham, J., and Megown, K. 2015. Completion of the 2011 National Land Cover 703 Database for the conterminous United States-Representing a decade of land cover change 704 information. Photogrammetric Engineering and Remote Sensing 81(5): 345-354. 705 ISAB. 2015. Density dependence and its implications for fish management and restoration 706 programs in the Columbia River basin. ISAB 2015-1. 707 Jeffres, C.A., Opperman, J.J., and Moyle, P.B. 2008. Ephemeral floodplain habitats provide best 708 growth conditions for juvenile Chinook salmon in a California river. Environmental 709 Biology of Fishes **83**(4): 449-458. 710 Junk, W.J., Bayley, P.B., and Sparks, R.E. 1989. The flood pulse concept in river-floodplain 711 systems, Canadian Special Publication of Fisheries and Aquatic Science 106:110-127. 712 Justice, C., White, S.M., McCullough, D.A., Graves, D.S., and Blanchard, M.R. 2017. Can 713 stream and riparian restoration offset climate change impacts to salmon populations? 714 Journal of Environmental Management **188**: 212-227. 715 Kiffney, P.M., Greene, C.M., Hall, J.E., and Davies, J.R. 2006. Tributary streams create spatial 716 discontinuities in habitat, biological productivity, and diversity in mainstem rivers. 717 Canadian Journal of Fisheries and Aquatic Sciences **63**(11): 2518-2530. 718 Kondolf, G.M., Piégay, H., and Landon, N. 2002. Channel response to increased and decreased bedload supply from land use change: contrasts between two catchments. 719 720 Geomorphology **45**(1): 35-51. 721 Martens, K.D., and Connolly, P.J. 2014. Juvenile Anadromous Salmonid Production in Upper 722 Columbia River Side Channels with Different Levels of Hydrological Connection. 723 Transactions of the American Fisheries Society **143**(3): 757-767.

| 124 | Montgomery, D.R., Collins, B.D., Buffington, J.M., and Abbe, 1.B. 2003. Geomorphic effects of    |
|-----|--------------------------------------------------------------------------------------------------|
| 725 | wood in rivers. Ecology and Management of Wood in World Rivers 37: 21-47.                        |
| 726 | Morley, S.A., Garcia, P.S., Bennett, T.R., and Roni, P. 2005. Juvenile salmonid (Oncorhynchus    |
| 727 | spp.) use of constructed and natural side channels in Pacific Northwest rivers. Canadian         |
| 728 | Journal of Fisheries and Aquatic Sciences 62(12): 2811-2821.                                     |
| 729 | Naish, K.A., Taylor, J.E., Levin, P.S., Quinn, T.P., Winton, J.R., Huppert, D., and Hilborn, R.  |
| 730 | 2008. An evaluation of the effects of conservation and fishery enhancement hatcheries on         |
| 731 | wild populations of salmon. In Advances in Marine Biology. Edited by D.W. Sims. pp.              |
| 732 | 61-194.                                                                                          |
| 733 | National Marine Fisheries Service. 2018. Pacific Northwest salmon habitat project database.      |
| 734 | National Marine Fisheries Service, Northwest Fisheries Science Center. Available from            |
| 735 | https://www.webapps.nwfsc.noaa.gov/pnshp/ [accessed 5/30/2018 2018].                             |
| 736 | NOAA. 2016a. 2016 5-Year Review: Summary & Evaluation of Snake River Sockeye, Snake              |
| 737 | River Spring-Summer Chinook, Snake River Fall-Run Chinook, Snake River Basin                     |
| 738 | Steelhead, Portland, OR.                                                                         |
| 739 | NOAA. 2016b. 2016 5-Year Review: Summary & Evaluation of Upper Columbia River                    |
| 740 | Steelhead and Upper Columbia River Spring-run Chinook Salmon, Portland, OR.                      |
| 741 | Pollock, M.M., Beechie, T.J., and Jordan, C.E. 2007. Geomorphic changes upstream of beaver       |
| 742 | dams in Bridge Creek, an incised stream channel in the interior Columbia River basin,            |
| 743 | eastern Oregon. Earth Surface Processes and Landforms 32(8): 1174-1185.                          |
| 744 | Quinn, T.P., and Peterson, N.P. 1996. The influence of habitat complexity and fish size on over- |
| 745 | winter survival and growth of individually marked juvenile coho salmon (Oncorhynchus             |

| 746 | kisutch) in Big Beef creek, Washington. Canadian Journal of Fisheries and Aquatic                |
|-----|--------------------------------------------------------------------------------------------------|
| 747 | Sciences <b>53</b> (7): 1555-1564.                                                               |
| 748 | Ricker, W.E. 1954. Stock and recruitment. Journal of the Fisheries Board of Canada 11(5): 559-   |
| 749 | 623.                                                                                             |
| 750 | Roni, P., Beechie, T., Pess, G., and Hanson, K. 2015. Wood placement in river restoration: fact, |
| 751 | fiction, and future direction. Canadian Journal of Fisheries and Aquatic Sciences 72(3):         |
| 752 | 466-478.                                                                                         |
| 753 | Roni, P., Beechie, T.J., Bilby, R.E., Leonetti, F.E., Pollock, M.M., and Pess, G.R. 2002. A      |
| 754 | review of stream restoration techniques and a hierarchical strategy for prioritizing             |
| 755 | restoration in Pacific northwest watersheds. North American Journal of Fisheries                 |
| 756 | Management <b>22</b> (1): 1-20.                                                                  |
| 757 | Roni, P., Hanson, K., and Beechie, T. 2008. Global review of the physical and biological         |
| 758 | effectiveness of stream habitat rehabilitation techniques. North American Journal of             |
| 759 | Fisheries Management 28(3): 856-890.                                                             |
| 760 | Roni, P., Pess, G., Beechie, T., and Morley, S. 2010. Estimating Changes in Coho Salmon and      |
| 761 | Steelhead Abundance from Watershed Restoration: How Much Restoration Is Needed to                |
| 762 | Measurably Increase Smolt Production? North American Journal of Fisheries                        |
| 763 | Management <b>30</b> (6): 1469-1484.                                                             |
| 764 | Rosenfeld, J.S., and Boss, S. 2001. Fitness consequences of habitat use for juvenile cutthroat   |
| 765 | trout: energetic costs and benefits in pools and riffles. Canadian Journal of Fisheries and      |
| 766 | Aquatic Sciences <b>58</b> (3): 585-593.                                                         |

| /6/ | Rosenfeld, J.S., Raeburn, E., Carrier, P.C., and Johnson, R. 2008. Effects of side channel    |
|-----|-----------------------------------------------------------------------------------------------|
| 768 | structure on productivity of floodplain habitats for juvenile coho salmon. North American     |
| 769 | Journal of Fisheries Management 28(4): 1108-1119.                                             |
| 770 | Scheuerell, M.D., Hilborn, R., Ruckelshaus, M.H., Bartz, K.K., Lagueux, K.M., Haas, A.D., and |
| 771 | Rawson, K. 2006. The Shiraz model: a tool for incorporating anthropogenic effects and         |
| 772 | fish-habitat relationships in conservation planning. Canadian Journal of Fisheries and        |
| 773 | Aquatic Sciences 63(7): 1596-1607.                                                            |
| 774 | Sedell, J.R., and Froggatt, J.L. 1984. Importance of streamside forests to large rivers: the  |
| 775 | isolation of the Willamette River, Oregon, USA, from its floodplain by snagging and           |
| 776 | streamside forest removal. Verhandlungen der Internationalen Vereiningung für                 |
| 777 | Theoretische und Angewandte Limnologie 22: 1828-1834.                                         |
| 778 | Skalski, J.R., Weiland, M.A., Ham, K.D., Ploskey, G.R., McMichael, G.A., Colotelo, A.H.,      |
| 779 | Carlson, T.J., Woodley, C.M., Eppard, M.B., and Hockersmith, E.E. 2016. Status after 5        |
| 780 | Years of Survival Compliance Testing in the Federal Columbia River Power System               |
| 781 | (FCRPS). North American Journal of Fisheries Management 36(4): 720-730.                       |
| 782 | Sommer, T.R., Nobriga, M.L., Harrell, W.C., Batham, W., and Kimmerer, W.J. 2001. Floodplain   |
| 783 | rearing of juvenile chinook salmon: evidence of enhanced growth and survival. Canadian        |
| 784 | Journal of Fisheries and Aquatic Sciences 58(2): 325-333.                                     |
| 785 | StreamNet Project. 2012. StreamNet Generalized Fish Distribution, Fall Chinook In             |
| 786 | ftp://ftp.streamnet.org/pub/streamnet/gisdata/map_data_biological/StreamNet_FishDist_J        |
| 787 | uly2010.zip.                                                                                  |

| 788 | Thorson, J.T., Scheuerell, M.D., Buhle, E.R., and Copeland, T. 2014. Spatial variation buffers |
|-----|------------------------------------------------------------------------------------------------|
| 789 | temporal fluctuations in early juvenile survival for an endangered Pacific salmon. Journal     |
| 790 | of Animal Ecology <b>83</b> (1): 157-167.                                                      |
| 791 | Tockner, K., Lorang, M.S., and Stanford, J.A. 2010. River Flood Plains Are Model Ecosystems    |
| 792 | to Test General Hydrogeomorphic and Ecological Concepts. River Research and                    |
| 793 | Applications <b>26</b> (1): 76-86.                                                             |
| 794 | Tockner, K., and Stanford, J.A. 2002. Riverine flood plains: present state and future trends.  |
| 795 | Environ Conserv <b>29</b> (3): 308-330.                                                        |
| 796 | U.S. Geological Survey. 2007-2014. National Hydrography Dataset available on the World Wide    |
| 797 | Web (https://nhd.usgs.gov), accessed 11/01/2015.                                               |
| 798 | Wall, C.E., Bouwes, N., Wheaton, J.M., Saunders, W.C., and Bennett, S.N. 2016. Net rate of     |
| 799 | energy intake predicts reach-level steelhead (Oncorhynchus mykiss) densities in diverse        |
| 800 | basins from a large monitoring program. Canadian Journal of Fisheries and Aquatic              |
| 801 | Sciences <b>73</b> (7): 1081-1091.                                                             |
| 802 | Walters, A.W., Bartz, K.K., and McClure, M.M. 2013a. Interactive Effects of Water Diversion    |
| 803 | and Climate Change for Juvenile Chinook Salmon in the Lemhi River Basin (U.S.A.).              |
| 804 | Conservation Biology <b>27</b> (6): 1179-1189.                                                 |
| 805 | Walters, A.W., Copeland, T., and Venditti, D.A. 2013b. The density dilemma: limitations on     |
| 806 | juvenile production in threatened salmon populations. Ecology of Freshwater Fish 22(4):        |
| 807 | 508-519.                                                                                       |
| 808 | Waples, R.S. 1991. Pacific Salmon, Oncorhynchus spp., and the Definition of "Species" Under    |
| 809 | the Endangered Species Act. Marine Fisheries Review 53(3): 11-22.                              |

| 810 | Ward, J.V., Tockner, K., and Schiemer, F. 1999. Biodiversity of floodplain river ecosystems: |
|-----|----------------------------------------------------------------------------------------------|
| 811 | Ecotones and connectivity. Regul River <b>15</b> (1-3): 125-139.                             |
| 812 | Wheaton, J.M., Bouwes, N., McHugh, P., Saunders, C., Bangen, S., Bailey, P., Nahorniak, M.,  |
| 813 | Wall, E., and Jordan, C. 2018. Upscaling site-scale ecohydraulic models to inform            |
| 814 | salmonid population-level life cycle modeling and restoration actions - Lessons from the     |
| 815 | Columbia River Basin. Earth Surface Processes and Landforms 43(1): 21-44.                    |
| 816 | White, S.M., Justice, C., Kelsey, D.A., McCullough, D.A., and Smith, T. 2017. Legacies of    |
| 817 | stream channel modification revealed using General Land Office surveys, with                 |
| 818 | implications for water temperature and aquatic life. Elem Sci Anth 5.                        |
| 819 | Whiteway, S.L., Biron, P.M., Zimmermann, A., Venter, O., and Grant, J.W.A. 2010. Do in-      |
| 820 | stream restoration structures enhance salmonid abundance? A meta-analysis. Canadian          |
| 821 | Journal of Fisheries and Aquatic Sciences 67(5): 831-841.                                    |
| 822 | Zimmerman, M.S., Kinsel, C., Beamer, E., Connor, E.J., and Pflug, D.E. 2015. Abundance,      |
| 823 | Survival, and Life History Strategies of Juvenile Chinook Salmon in the Skagit River,        |
| 824 | Washington. Transactions of the American Fisheries Society 144(3): 627-641.                  |
| 825 |                                                                                              |

# 826 Table 1. Parameters governing the stratification of sites randomly chosen for satellite image 827 analysis of channel habitat characteristics.

| Sample Strata  |                |  |
|----------------|----------------|--|
|                | Urban          |  |
| Land cover     | Cropland       |  |
|                | Grassland      |  |
|                | Shrubland      |  |
|                | Forest         |  |
|                | Straight       |  |
|                | Meandering     |  |
| Channel type   | Island-braided |  |
|                | Braided        |  |
|                | Confined       |  |
| Bankfull width | 8-20 m         |  |
|                | 20-50 m        |  |
|                | > 50 m         |  |

828

831

### Table 2. Descriptions of stream habitat types measured with satellite imagery at each of

#### 2093 reaches and standardized orientation of measurements.

| 3.7 1     | TT 1    | 3.6     |
|-----------|---------|---------|
| Measured  | Habitat | Matrice |
| Micasurcu | Habitat | Michies |

| Name                  | Description                                                                                                        | Measurement Axis             |  |  |  |
|-----------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------|--|--|--|
| Side channel          | Channel regularly connected to mainstem on both sides and separated from the mainstem by a vegetated island        | perpendicular to valley axis |  |  |  |
| Off channel           | Feature only connected to mainstem on one end with little or no flow (slough, backwater)                           | perpendicular to valley axis |  |  |  |
| Braid                 | Channel regularly connected to mainstem on both sides and separated from the mainstem by an unvegetated gravel bar | perpendicular to valley axis |  |  |  |
| Modified side channel | Highly modified or degraded side channel determined to be inaccessable to fish or unsuitable for rearing           | perpendicular to valley axis |  |  |  |
| Ditch                 | Artificial channel determined to be inaccessable to fish or unsuitable for rearing                                 | perpendicular to valley axis |  |  |  |
| Wetted width          | Wetted width of main channel                                                                                       | perpendicular to valley axis |  |  |  |
| Bankfull width        | Width of stream at bankfull flows                                                                                  | perpendicular to stream flow |  |  |  |
| Historical floodplain | Width of valley bottom defined by rise in elevation > 5 m above main channel elevation using DEM                   | perpendicular to valley axis |  |  |  |
| Current floodplain    | Width of unmodified floodplain; same as historic floodplain if no modification exists same as                      | perpendicular to valley axis |  |  |  |

## Table 3. Predictor variables and data sources used to predict the presence of side and off channel

# habitat throughout the Columbia River basin.

| <b>Predictor Variables</b>                  | Description                                                                                                                                                                                                            | <b>Data Source</b>                                                                                                                                                  |  |  |  |  |  |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|
| Bankfull width  Discharge                   | Stream channel width at bankfull flows estimated from drainage area and mean annual precipitation upstream of each reach 2 year flood discharge estimated from drainage area and mean annual precipitation upstream of | Beechie and Imaki 2014  Beechie and Imaki 2014                                                                                                                      |  |  |  |  |  |
| Flow accumulation by precipitation/sediment | each reach Estimated from DEM derived drainage area. Flow accumulation weighted by precipitation and fine sediment source also included                                                                                | Beechie and Imaki 2014                                                                                                                                              |  |  |  |  |  |
| Slope                                       | Reach slope estimated from digital elevation and hydrography models                                                                                                                                                    | Beechie and Imaki 2014                                                                                                                                              |  |  |  |  |  |
| Bankfull width                              | Estimated bankfull width in meters                                                                                                                                                                                     | Beechie and Imaki 2014                                                                                                                                              |  |  |  |  |  |
| Bankfull depth                              | Estimated bankfull depth in meters                                                                                                                                                                                     | Beechie and Imaki 2014                                                                                                                                              |  |  |  |  |  |
| Elevation                                   | Estimated from digital elevation and hydrography models                                                                                                                                                                | Beechie and Imaki 2014                                                                                                                                              |  |  |  |  |  |
| Sinuosity                                   | Shortest distance between reach endnodes divided by reach length                                                                                                                                                       | Beechie and Imaki 2014                                                                                                                                              |  |  |  |  |  |
| Hydrologic Regime  Sediment supply          | Categorical variable indicating if reach belongs to a snow-melt dominated, rain dominated or transitional drainage Sediment supply surrogates estimated from flow accumulation,                                        | Beechie and Imaki 2014  Beechie and Imaki 2014                                                                                                                      |  |  |  |  |  |
| Position                                    | fine sediment sources and relative<br>slope<br>Segment number upstream from<br>confluence                                                                                                                              | Beechie and Imaki 2014                                                                                                                                              |  |  |  |  |  |
| Historical floodplain width                 | Valley bottom width estimated from DEM and hydrography                                                                                                                                                                 | Beechie and Imaki 2014; National<br>Hydrography Dataset (NHD),                                                                                                      |  |  |  |  |  |
| Current floodplain width                    | models Width of currently unmodified floodplain estimated from DEM, hydrography models and land use                                                                                                                    | https://nhd.usgs.gov/data.html; National Land<br>Cover Database 2011 (NLCD 2011),<br>http://www.mrlc.gov/nlcd2011.php;<br>Agriculture and Agri-Food Canada Land Use |  |  |  |  |  |
| Restored floodplain width.                  | data Width of floodplain assuming reclamation of cropland, rangeland, and small roads                                                                                                                                  | 2010,<br>http://www.agr.gc.ca/eng/?id=134306645696;<br>USGS National Transportation Dataset,<br>Canada National Road Network                                        |  |  |  |  |  |
| Ecoregion                                   | Level III EPA Ecoregions                                                                                                                                                                                               | EPA, https://www.epa.gov/eco-research/ecoregions                                                                                                                    |  |  |  |  |  |

834

838

![](_page_41_Picture_5.jpeg)

- 840 Table 4. Densities of Chinook parr used to estimate capacity with habitat expansion approach
- 841 (From Beechie and Thompson unpublished review).

|                     | Chinook parr · |
|---------------------|----------------|
| Habitat             | hectare-1      |
| Mainstem bank       | 8884           |
| Mainstem bar        | 4720           |
| Mainstem mid        |                |
| channel             | 100            |
| Side channel        | 6000           |
| Small stream pool   | 452            |
| Small stream riffle | 4              |

![](_page_42_Picture_7.jpeg)

Table 5. Spring Chinook parr habitat area and rearing capacity by HUC-8 subbasin. *Main* indicates bank, bar, mid-channel area. *Current side channel* indicates contemporary side channel area. *Historical side channel* indicates side channel area with unrestricted floodplains.

\*Restoration side channel indicates side channel area for floodplain reconnection in agricultural lands and areas with small roads. \*Current >8m BFW streams\* indicates the expansion method sum of bank, bar, mid-channel, and contemporary side channel capacity. \*Restoration >8m BFW streams\* indicates the sum of mainstem and restored side channel capacity. \*Quantile regression >8m BFW\* indicates estimates from quantile random forest model (90th percentile) of ISEMP fish survey data and habitat area. Both historical and contemporary estimates are limited to habitats defined as rearing habitat by StreamNet.

|                   |                               |        |                                    | Habitat ar                            | ea (Hectares)                   |                                                      |                                                                                | Chinook parr capacity<br>(individuals) |                                    |                                                             |                                    |                                             |                                   |
|-------------------|-------------------------------|--------|------------------------------------|---------------------------------------|---------------------------------|------------------------------------------------------|--------------------------------------------------------------------------------|----------------------------------------|------------------------------------|-------------------------------------------------------------|------------------------------------|---------------------------------------------|-----------------------------------|
| нис 6             | HUC 8                         | Main   | Curre<br>nt<br>side<br>chann<br>el | Histori<br>cal<br>side<br>channe<br>1 | Restorat<br>ion side<br>channel | % side<br>chann<br>el loss<br>from<br>histori<br>cal | side<br>channel<br>%<br>increase<br>from<br>current<br>with<br>restorati<br>on | Current >8 m<br>BFW streams            | Restoration >8<br>m BFW<br>streams | %<br>increase<br>with<br>side<br>channel<br>restorati<br>on | Quantile<br>regression >8 m<br>BFW | 5200 parr<br>per<br>hectare,<br>>8 m<br>BFW | Current<br><8 m<br>BFW<br>streams |
| Lower<br>Columbia | Lewis                         | 141.5  | 12.5                               | 19.0                                  | 14.0                            | -34.3                                                | 12.2                                                                           | 285,931                                | 295,087                            | 3.2                                                         | 319,336                            | 218,374                                     | 28,771                            |
| Lower<br>Columbia | Lower Columbia-<br>Clatskanie | 254.8  | 17.8                               | 20.1                                  | 17.8                            | -11.7                                                | 0.0                                                                            | 495,212                                | 495,212                            | 0.0                                                         | 467,483                            | 364,884                                     | 43,193                            |
| Lower<br>Columbia | Lower Columbia-<br>Sandy      | 580.7  | 66.2                               | 73.7                                  | 67.6                            | -10.1                                                | 2.0                                                                            | 1,266,072                              | 1,269,993                          | 0.3                                                         | 1,102,423                          | 976,322                                     | 33,101                            |
| Lower<br>Columbia | Lower Cowlitz                 | 454.7  | 57.7                               | 85.7                                  | 67.6                            | -32.7                                                | 17.2                                                                           | 978,276                                | 1,037,951                          | 6.1                                                         | 1,177,151                          | 743,042                                     | 33,168                            |
| Lower<br>Columbia | Upper Cowlitz                 | 678.6  | 169.0                              | 192.3                                 | 185.5                           | -12.1                                                | 9.8                                                                            | 1,974,635                              | 2,073,544                          | 5.0                                                         | 1,792,603                          | 1,574,004                                   | 10,663                            |
| Willamette        | Clackamas                     | 890.6  | 124.6                              | 140.6                                 | 131.7                           | -11.3                                                | 5.7                                                                            | 2,086,128                              | 2,128,863                          | 2.0                                                         | 2,477,358                          | 1,611,201                                   | 21,188                            |
| Willamette        | Coast Fork<br>Willamette      | 278.7  | 47.1                               | 120.3                                 | 90.3                            | -60.8                                                | 91.5                                                                           | 713,440                                | 971,851                            | 36.2                                                        | 1,245,196                          | 557,368                                     | 2,310                             |
| Willamette        | Lower Willamette              | 29.3   | 0.3                                | 1.0                                   | 0.3                             | -69.4                                                | 0.0                                                                            | 41,485                                 | 41,485                             | 0.0                                                         | 41,686                             | 29,328                                      | 23,475                            |
| Willamette        | Mckenzie                      | 1444.4 | 507.8                              | 574.6                                 | 559.1                           | -11.6                                                | 10.1                                                                           | 5,207,995                              | 5,503,421                          | 5.7                                                         | 5,443,837                          | 4,199,754                                   | 127,283                           |
| Willamette        | Middle Fork<br>Willamette     | 976.9  | 259.3                              | 295.9                                 | 283.9                           | -12.4                                                | 9.5                                                                            | 3,085,220                              | 3,230,568                          | 4.7                                                         | 3,009,425                          | 2,470,267                                   | 131,771                           |
| Willamette        | Middle Willamette             | 2113.8 | 471.0                              | 659.0                                 | 615.2                           | -28.5                                                | 30.6                                                                           | 5,708,246                              | 6,573,509                          | 15.2                                                        | 9,112,475                          | 4,480,042                                   | 65,055                            |
| Willamette        | Molalla-Pudding               | 797.3  | 63.4                               | 97.3                                  | 105.1                           | -34.8                                                | 65.7                                                                           | 1,671,132                              | 1,911,317                          | 14.4                                                        | 2,532,000                          | 1,273,057                                   | 31,219                            |
| Willamette        | North Santiam                 | 1082.2 | 321.0                              | 385.8                                 | 361.2                           | -16.8                                                | 12.5                                                                           | 3,499,640                              | 3,737,892                          | 6.8                                                         | 4,922,581                          | 2,801,469                                   | 47,428                            |
| Willamette        | South Santiam                 | 885.7  | 173.2                              | 253.3                                 | 240.7                           | -31.6                                                | 38.9                                                                           | 2,412,919                              | 2,817,661                          | 16.8                                                        | 4,017,124                          | 1,907,205                                   | 26,642                            |
| Willamette        | Upper Willamette              | 2253.5 | 695.8                              | 1173.3                                | 1065.8                          | -40.7                                                | 53.2                                                                           | 7,399,446                              | 9,618,055                          | 30.0                                                        | 16,479,084                         | 5,894,195                                   | 41,321                            |
| Deschutes         | Lower Crooked                 | 321.2  | 17.6                               | 75.8                                  | 67.3                            | -76.8                                                | 282.4                                                                          | 605,335                                | 903,662                            | 49.3                                                        | 800,183                            | 461,405                                     | NA                                |
| Deschutes         | Lower Deschutes               | 1740.3 | 114.0                              | 152.0                                 | 136.4                           | -25.0                                                | 19.7                                                                           | 3,203,425                              | 3,337,836                          | 4.2                                                         | 2,537,810                          | 2,456,100                                   | 14,817                            |
| Deschutes         | Trout                         | 0.4    | 0.1                                | 0.2                                   | 0.1                             | -29.3                                                | 0.0                                                                            | 1,534                                  | 1,534                              | 0.0                                                         | 494                                | 1,286                                       | NA                                |

| Deschutes          | Upper Deschutes                    | 203.1  | 10.4  | 14.6  | 13.3  | -28.9 | 28.0  | 406,081    | 423,505     | 4.3  | 458,014     | 317,094                | 2,739     |
|--------------------|------------------------------------|--------|-------|-------|-------|-------|-------|------------|-------------|------|-------------|------------------------|-----------|
| John Day           | Lower John Day<br>Middle Fork John | 2077.5 | 338.6 | 367.7 | 361.0 | -7.9  | 6.6   | 4,952,420  | 5,085,956   | 2.7  | 4,815,557   | 3,870,168              | 45        |
| John Day           | Day                                | 243.7  | 19.4  | 25.4  | 25.3  | -23.9 | 30.5  | 548,997    | 584,463     | 6.5  | 245,816     | 436,931                | 94,416    |
| John Day           | North Fork John Day                | 724.6  | 43.2  | 59.3  | 55.3  | -27.1 | 27.8  | 1,435,191  | 1,507,341   | 5.0  | 1,560,261   | 1,097,226              | 88,239    |
| John Day           | Upper John Day                     | 491.7  | 96.2  | 138.1 | 121.7 | -30.4 | 26.5  | 1,429,236  | 1,578,939   | 10.5 | 1,930,852   | 1,176,785              | 32,296    |
| Middle<br>Columbia | Klickitat                          | 620.0  | 92.3  | 103.4 | 93.0  | -10.7 | 0.7   | 1,483,469  | 1,487,247   | 0.3  | 1,460,173   | 1,158,633              | 7,745     |
| Middle<br>Columbia | Middle Columbia-<br>Hood           | 409.9  | 67.1  | 72.0  | 69.2  | -6.8  | 3.2   | 1,064,312  | 1,077,158   | 1.2  | 918,031     | 839,490                | 106,043   |
| Middle<br>Columbia | Umatilla                           | 552.9  | 92.1  | 226.1 | 195.7 | -59.3 | 112.5 | 1,444,628  | 2,066,039   | 43.0 | 1,203,297   | 1,159,626              | 38,983    |
| Middle<br>Columbia | Walla Walla                        | 162.8  | 4.8   | 21.0  | 11.0  | -77.0 | 128.0 | 342,033    | 379,040     | 10.8 | 364,072     | 274,270                | 21,345    |
| Yakima             | Lower Yakima,<br>Washington        | 1880.6 | 585.1 | 647.8 | 597.8 | -9.7  | 2.2   | 6,078,184  | 6,129,889   | 0.9  | 6,807,410   | 4,935,626              | 50,341    |
| Yakima             | Naches                             | 444.3  | 105.4 | 115.4 | 107.8 | -8.6  | 2.2   | 1,341,240  | 1,352,140   | 0.8  | 737,197     | 1,084,655              | 40,522    |
| Yakima             | Upper Yakima                       | 1221.8 | 282.6 | 345.6 | 301.5 | -18.2 | 6.7   | 3,499,068  | 3,610,038   | 3.2  | 1,801,625   | 2,817,275              | 37,807    |
| Upper<br>Columbia  | Chief Joseph                       | 1.6    | 0.0   | 0.0   | 0.0   | NA    | NA    | 3,619      | 3,619       | 0.0  | 2,348       | 3,119                  | 169       |
| Upper<br>Columbia  | Methow                             | 1267.4 | 225.8 | 251.4 | 232.0 | -10.2 | 2.7   | 3,198,422  | 3,233,536   | 1.1  | 1,443,710   | 2,605,905              | 21,557    |
| Upper              | Upper Columbia-                    |        |       |       |       |       |       |            |             |      |             |                        |           |
| Columbia<br>Upper  | Entiat                             | 175.1  | 27.6  | 38.8  | 31.4  | -28.9 | 13.9  | 443,959    | 465,883     | 4.9  | 139,736     | 359,595                | 9,498     |
| Columbia<br>Lower  | Wenatchee                          | 1115.7 | 203.4 | 263.0 | 218.6 | -22.7 | 7.4   | 2,862,676  | 2,950,188   | 3.1  | 1,215,227   | 2,294,165              | 40,374    |
| Snake<br>Lower     | Hells Canyon                       | 22.9   | 0.0   | 0.0   | 0.0   | NA    | NA    | 34,690     | 34,690      | 0.0  | 29,995      | 25,875                 | 40,291    |
| Snake<br>Lower     | Imnaha                             | 448.9  | 17.1  | 19.2  | 19.2  | -10.9 | 12.2  | 885,426    | 897,954     | 1.4  | 513,132     | 687,420                | 62,733    |
| Snake<br>Lower     | Lower Grande Ronde<br>Lower Snake- | 510.8  | 15.6  | 15.6  | 15.6  | 0.0   | 0.0   | 869,559    | 869,559     | 0.0  | 629,576     | 650,744                | 70,300    |
| Snake              | Tucannon                           | 99.4   | 6.3   | 9.1   | 8.6   | -31.1 | 36.9  | 217,884    | 231,740     | 6.4  | 197,826     | 170,438                | 8,420     |
| Lower<br>Snake     | Upper Grande Ronde                 | 709.1  | 52.5  | 240.5 | 227.2 | -78.2 | 332.5 | 1,503,877  | 2,551,121   | 69.6 | 2,176,811   | 1,160,457              | 86,611    |
| Lower<br>Snake     | Wallowa                            | 595.7  | 41.9  | 91.5  | 81.3  | -54.3 | 94.2  | 1,262,398  | 1,499,071   | 18.7 | 1,153,676   | 966,512                | 35,964    |
| Clearwater         | Clearwater                         | 1482.6 | 92.5  | 111.0 | 102.0 | -16.7 | 10.3  | 2,778,192  | 2,829,467   | 1.8  | 1,486,872   | 2,146,813              | 277,559   |
| Clearwater         | Lochsa                             | 1009.8 | 29.5  | 35.3  | 30.5  | -16.4 | 3.5   | 1,761,151  | 1,767,298   | 0.3  | 1,591,429   | 1,304,017              | 165,793   |
| Clearwater         | Lower North Fork<br>Clearwater     | 22.5   | 2.5   | 2.7   | 2.5   | -7.7  | 0.3   | 46,199     | 46,237      | 0.1  | 21,859      | 36,123                 | NA        |
| Clearwater         | Lower Selway                       | 769.3  | 12.5  | 12.5  | 12.5  | 0.0   | 0.0   | 1,274,586  | 1,274,586   | 0.0  | 801,184     | 944,119                | 98,923    |
| Clearwater         | Middle Fork<br>Clearwater          | 484.8  | 37.8  | 25.7  | 39.4  | 47.2  | 4.4   | 884,637    | 894,521     | 1.1  | 376,147     | 684,528                | 56,743    |
| Clearwater         | South Fork<br>Clearwater           | 667.2  | 26.1  | 33.9  | 31.2  | -23.1 | 19.6  | 1,240,573  | 1,271,289   | 2.5  | 858,797     | 927,369                | 254,070   |
| Clearwater         | Upper Selway                       | 547.0  | 17.8  | 17.8  | 18.2  | 0.0   | 2.1   | 1,026,048  | 1,028,315   | 0.2  | 819,270     | 765,741                | 190,910   |
| Salmon             | Lemhi                              | 210.9  | 31.9  | 120.9 | 108.9 | -73.6 | 241.6 | 570,307    | 1,032,635   | 81.1 | 156,898     | 458,452                | 43,315    |
| Salmon             | Little Salmon                      | 234.2  | 9.7   | 11.9  | 10.7  | -18.0 | 10.2  | 458,438    | 464,389     | 1.3  | 541,245     | 351,697                | 33,937    |
| Salmon             | Lower Middle Fork<br>Salmon        | 795.7  | 19.8  | 20.8  | 21.0  | -4.9  | 5.9   | 1,392,105  | 1,399,065   | 0.5  | 1,735,069   | 1,014,904              | 268,377   |
| Salmon             | Lower Salmon                       | 150.1  | 2.4   | 3.0   | 3.1   | -17.3 | 25.9  | 285,715    | 289,523     | 1.3  | 222,679     | 216,448                | 81,506    |
| Salmon             | Middle Salmon-<br>Chamberlain      | 235.6  | 7.3   | 7.3   | 7.3   | 0.0   | 0.0   | 467,715    | 467,715     | 0.0  | 414,904     | 353,698                | 194,336   |
| Salmon             | Middle Salmon-<br>Panther          | 704.2  | 137.0 | 161.4 | 153.8 | -15.1 | 12.3  | 1,921,854  | 2,018,837   | 5.0  | 2,490,330   | 1,518,733              | 209,370   |
| Salmon             | Pahsimeroi                         | 85.8   | 32.1  | 37.8  | 37.3  | -14.9 | 16.2  | 349,497    | 380,685     | 8.9  | 184,292     | 289,469                | NA        |
| Salmon             | South Fork Salmon                  | 889.5  | 39.8  | 42.0  | 41.9  | -5.3  | 5.2   | 1,679,670  | 1,692,004   | 0.7  | 2,044,231   | 1,263,941              | 253,775   |
| Salmon             | Upper Middle Fork<br>Salmon        | 555.2  | 87.9  | 90.9  | 90.7  | -3.3  | 3.2   | 1,516,197  | 1,533,195   | 1.1  | 1,742,764   | 1,209,109              | 380,324   |
|                    |                                    |        |       |       |       |       |       |            |             |      |             |                        |           |
| Salmon             | Upper Salmon                       | 1328.5 | 160.3 | 235.0 | 216.8 | -31.8 | 35.3  | 3,060,223  | 3,392,352   | 10.9 | 3,118,350   | 2,402,031<br>75,998,50 | 572,012   |
| Total              |                                    | 39,077 | 6,193 | 8,355 | 7,724 | -25.9 | 24.7  | 96,656,545 | 105,750,668 | 9.4  | 105,888,913 | 1                      | 4,658,794 |

#### Figure Legends

Figure 1. Flow chart of habitat capacity modeling process. Grey boxes indicate random forest models and dotted boxes indicate steps where we applied estimates to make decisions in branch direction or used established relationships to achieve outputs. All model outputs are in boxes with solid black lines.

Figure 2. Locations of 2093 sample sites selected with a generalized random tesselation stratified (GRTS) sample design. At each site, mainstem and off channel wetted habitat widths were measured from satellite imagery.

Figure 3. A comparison of wetted width measurements from satellite imagery (x-axis) and predicted wetted width from a random forest model. Solid line indicates a 1:1 relationship.

Figure 4. The relative importance of each input variable included in the random forest model predicting the wetted width of mainstem stream segments. Importance is estimated from the gini impurity criterion based on the number of nodes that a given variable is included in the model. *Flow by precip*. indicates accumulated flow by precipitation source. *Curr. Floodplain* indicates the current floodplain width.

Figure 5. The importance of predictors in side channel presence. The x-axis indicates scaled mean decrease in classification accuracy when each variable is permuted over all random forest trees. *Curr. Floodplain* indicates the current floodplain width. *Hist. floodplain* indicates the historical unrestricted floodplain width. *Flow acc.* indicates total flow accumulation. *Flow by sed.* indicates flow accumulation by sediment source.

Figure 6. Vote influence of floodplain width on predictions of the presence of side channel habitat. Increasingly positive values of vote influence predict the presence of side channel habitat more strongly. Similarly, decreasing vote influence values indicate a stronger prediction of no

side channel. Small ticks on the x-axis indicate deciles of floodplain width for all measured reaches.

Figure 7. The relative importance of each input variable in predicting the average side channel width (m) at each reach where side channels were present. Importance is estimated from the gini impurity criterion based on the number of nodes that a given variable is included in the model.

Figure 8. Partial dependence plot of the marginal effect of floodplain width on side channel width prediction. The influence of floodplain width becomes saturated at ca. 2000 m floodplain width. Small ticks on the x-axis indicate deciles of floodplain width for all measured stream segments.

Figure 9. A comparison of measured side channel width (x –axis) and predicted side channel width (y-axis) from the random forest regression model for 128 novel sites that were not included in model development. Solid line indicates 1:1 correspondence between measurements and model output.

Figure 10. Contemporary summer parr rearing capacity of Spring Chinook within the domain currently accessible to anadromous fishes as determined by the habitat expansion approach of estimating mainstem and side channel habitat and assigning fish densities to each habitat at the 200 m stream segment scale. For graphical purposes, estimates are aggregated at the HUC-10 watershed boundary spatial scale. Black lines indicate regional HUC-6 watershed boundaries.

Figure 11. Contemporary percentage of total estimated spring Chinook parr rearing capacity attributed to side channel habitat. Estimates were made with the habitat expansion approach and aggregated at the HUC-10 watershed spatial scale.

 Figure 12**.** Estimated increase in spring Chinook parr capacity from contemporary conditions resulting from floodplain reconnection in historical floodplain currently occupied by rangeland, cropland, and small unimproved roads. Estimates were made with the habitat expansion approach and aggregated at the HUC-10 watershed spatial scale.

![](_page_47_Picture_3.jpeg)

![](_page_48_Figure_3.jpeg)

908

909 Figure 1.

![](_page_49_Figure_2.jpeg)

912 Figure 2.

![](_page_50_Figure_2.jpeg)

915 Figure 3.

![](_page_51_Figure_3.jpeg)

918

919 Figure 4.

![](_page_51_Picture_7.jpeg)

![](_page_52_Figure_2.jpeg)

922 Figure 5.

![](_page_53_Figure_2.jpeg)

925 Figure 6.

![](_page_54_Figure_3.jpeg)

928

929 Figure 7.

![](_page_54_Picture_7.jpeg)

![](_page_55_Figure_2.jpeg)

932 Figure 8.

933

![](_page_56_Figure_2.jpeg)

936 Figure 9.

![](_page_57_Figure_2.jpeg)

939 Figure 10.

![](_page_58_Figure_2.jpeg)

942

943 Figure 11.

![](_page_59_Figure_2.jpeg)

945 Figure 12**.** 

946