![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

![](_page_0_Picture_2.jpeg)

Citation: Finnegan L, Pigeon KE, Cranston J, Hebblewhite M, Musiani M, Neufeld L, et al. (2018) Natural regeneration on seismic lines influences movement behaviour of wolves and grizzly bears. PLoS ONE 13(4): e0195480. https://doi.org/ 10.1371/journal.pone.0195480

**Editor:** Marco Festa-Bianchet, Université de Sherbrooke. CANADA

Received: November 7, 2017
Accepted: March 24, 2018
Published: April 16, 2018

Copyright: © 2018 Finnegan et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

**Data Availability Statement:** All data files are available from Dryad doi:10.5061/dryad.7687117.

Funding: Part of the National Conservation Plan, this project was undertaken with the financial support of the Government of Canada/Dans le cadre du Plan de conservation national, ce projet a été réalisé avec l'appui financier du gouvernement du Canada (HSP6617, 6699, 7195) [www.ec.gc.ca/hsp-pih/]. Additional support was provided by Alberta Environment and Parks [http://aep.alberta.ca/], the Foothills Landscape Management Forum

RESEARCH ARTICLE

# Natural regeneration on seismic lines influences movement behaviour of wolves and grizzly bears

Laura Finnegan<sup>1</sup>\*, Karine E. Pigeon<sup>1</sup>, Jerome Cranston<sup>2</sup>, Mark Hebblewhite<sup>3</sup>, Marco Musiani<sup>4</sup>, Lalenia Neufeld<sup>5</sup>, Fiona Schmiegelow<sup>6</sup>, Julie Duval<sup>7</sup>, Gordon B. Stenhouse<sup>8</sup>

1 Caribou Program, fRI Research, Hinton, Alberta, Canada, 2 Arctos Ecological Consultants, Edmonton, Alberta, Canada, 3 Wildlife Biology Program, Department of Ecosystem and Conservation Science, W.A. Franke College of Forestry and Conservation, University of Montana, Missoula, Montana, United States of America, 4 Department of Biological Sciences, Faculty of Science, University of Calgary, Calgary, Alberta, Canada, 5 Parks Canada, Jasper National Park, Jasper, Alberta, Canada, 6 Department of Renewable Resources, University of Alberta, Edmonton, Alberta, Canada, 7 GIS Program, fRI Research, Hinton, Alberta, Canada, 8 Grizzly Bear Program, fRI Research, Hinton, Alberta, Canada

\* Ifinnegan@friresearch.ca

# **Abstract**

Across the boreal forest of Canada, habitat disturbance is the ultimate cause of caribou (Rangifer tarandus caribou) declines. Habitat restoration is a focus of caribou recovery efforts, with a goal to finding ways to reduce predator use of disturbances, and caribou-predator encounters. One of the most pervasive disturbances within caribou ranges in Alberta, Canada are seismic lines cleared for energy exploration. Seismic lines facilitate predator movement, and although vegetation on some seismic lines is regenerating, it remains unknown whether vegetation regrowth is sufficient to alter predator response. We used Light Detection and Ranging (LiDAR) data, and GPS locations, to understand how vegetation and other attributes of seismic lines influence movements of two predators, wolves (Canis lupus) and grizzly bears (Ursus arctos). During winter, wolves moved towards seismic lines regardless of vegetation height, while during spring wolves moved towards seismic lines with higher vegetation. During summer, wolves moved towards seismic lines with lower vegetation and also moved faster near seismic lines with vegetation <0.7 m. Seismic lines with lower vegetation height were preferred by grizzly bears during spring and summer, but there was no relationship between vegetation height and grizzly bear movement rates. These results suggest that wolves use seismic lines for travel during summer, but during winter wolf movements relative to seismic lines could be influenced by factors additional to movement efficiency; potentially enhanced access to areas frequented by ungulate prey. Grizzly bears may be using seismic lines for movement, but could also be using seismic lines as a source of vegetative food or ungulate prey. To reduce wolf movement rate, restoration could focus on seismic lines with vegetation <1 m in height. However our results revealed that seismic lines continue to influence wolf movement behaviour decades after they were built, and even at later stages of regeneration. Therefore it remains unknown at what stage of natural regeneration, if any, wolves cease to respond to seismic lines. To

![](_page_1_Picture_1.jpeg)

[\[https://friresearch.ca/content/foothills-landscape](https://friresearch.ca/content/foothills-landscape-management-forum-flmf)[management-forum-flmf\]](https://friresearch.ca/content/foothills-landscape-management-forum-flmf), the Sustainable Forestry Initiative (2013-003) [[http://www.sfiprogram.org/\]](http://www.sfiprogram.org/), partners of the fRI Research Caribou and Grizzly Bear Programs, and fRI Research [\[www.](http://www.friresearch.ca) [friresearch.ca](http://www.friresearch.ca)]. Animal GPS data were collected as part of research supported by the Government of Alberta (GoA), fRI Research Grizzly Bear Program partners, and funders of graduate research at the University of Alberta and University of Montana. MH was also funded by NASA's Arctic Boreal Vulnerability Experiment (ABoVE) grant # NNX15AW71A [\[www.nasa.gov\]](http://www.nasa.gov). The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

**Competing interests:** The authors have declared that no competing interests exist.

reduce wolf response to seismic lines, active restoration tactics like blocking seismic lines and tree planting, along with management of alternate prey, could be evaluated.

## **Introduction**

Habitat disturbance and loss are recognised as key factors in the loss of global biodiversity [1,2]. Anthropogenic habitat disturbance can reduce the accessibility of natural resources for wildlife [1], directly and indirectly increase wildlife mortalities [3], and also have more subtle effects such as long-term reduction of habitat quality and function [4], and altered predatorprey dynamics [5]. However, not all anthropogenic disturbances are equal. In addition to environmental and biological factors that affect individual responses (e.g. reproductive status, season, and weather), wildlife can respond differently to disturbances with respect to the activity severity of the disturbance [6], and time since disturbance [7]. In areas where anthropogenic disturbances are years, or even decades old, natural regeneration (shrubs, grasses, and trees) may negate the need for active restoration, although it is unclear whether regenerative vegetation is sufficient to change wildlife responses. Given the widespread alteration of landscapes by humans, and the limited resources available, a triage approach may be required to direct restoration and management to areas that will have the most benefit for wildlife [8]. By identifying when regenerated areas no longer negatively impact wildlife species that are of conservation concern, we can direct mitigation activities where they are most needed.

The boreal forest of western Canada is fragmented by an extensive footprint of anthropogenic disturbance in the form of forest clear cuts, well sites, pipelines, power lines, seismic lines, and access roads [9,10]. The negative effects of habitat fragmentation on boreal wildlife are well documented [11,12], and of particular concern are boreal and central mountain woodland caribou (*Rangifer tarandus caribou*). Once widespread throughout the boreal forest and mountains of western Canada respectively, boreal and central mountain woodland caribou have declined across their range [13,14]. Ultimately, these declines are believed to be caused by habitat disturbances associated with land use and management activities [13,15]. Large areal disturbances like forestry, oil and gas, and mining activities have resulted in numerical responses by ungulates that prefer early seral forest (e.g. moose (*Alces alces*), deer (*Odocoileus* spp.), and elk (*Cervuscanadensis*)), and correspondingly increased the numerical response of shared predators such as wolves (*Canis lupus*) within caribou ranges [16–18]. Linear disturbances (roads, pipelines, and seismic lines) also increase functional overlap between these shared predators and caribou [19,20]. As a result, cumulative anthropogenic disturbance has increased apparent competition between caribou and ungulates that prefer early seral stages via increased predation [21,22].

Recognizing the negative effects of anthropogenic disturbances on the persistence of caribou, the Canadian federal government recovery strategies for boreal and southern mountain caribou state that at least 65% of the range of each caribou herd (low elevation winter and connectivity range for central mountain caribou) should be undisturbed [10,23]. In Alberta Canada, however, all caribou ranges currently exceed this threshold, populations are declining at an average of 8% per year [14,24], and there is an urgent need to implement habitat restoration as a measure to facilitate caribou recovery. Legacy seismic lines (linear features approximately 8 m wide that were cleared throughout the boreal forest during seismic soundwave mapping of oil reserves prior to 1990, hereafter seismic lines) have been a focus of scientific inquiry because they increase functional overlap between predators and caribou by facilitating predator movement and increasing caribou and predator encounters [20,25–27]. Specifically,

![](_page_2_Picture_1.jpeg)

predator movement rates on seismic lines can be up to double those in the forest interior [25], and even low densities of seismic lines increase predator use of habitats [28,29].

The extensive seismic line footprint within Alberta means that restoration will need to be prioritized [8]. Until recently, quantification of seismic line regeneration was not feasible at a large scale and corresponding investigations of wildlife response to regeneration were rare (but see [28,30,31]). Light Detection and Ranging Data (LiDAR) now facilitates detailed and broad scale assessments of habitat regeneration in three dimensional space, including measuring vegetation height on seismic lines [32]. We used animal Global Positioning System (GPS) data and LiDAR-based measurements of vegetation height on seismic lines to assess movement ecology of wolves and grizzly bears in relation to regenerating seismic lines. Our goals were 1) to determine whether natural regeneration on seismic lines is sufficient to make predator use of seismic lines indistinguishable from the surrounding landscape, and in the context of habitat restoration priorities for caribou, 2) to understand what specific characteristics of seismic lines make seismic lines most attractive to predators for movement.

At a broad scale, we assessed movement behaviour using step selection functions [33]. We predicted that at this broad scale, grizzly bears and wolves would move towards seismic lines that are attractive movement routes. Specifically that both species would move towards seismic lines i) with lower vegetation height, as seismic lines with lower vegetation height are more attractive movement routes when compared to seismic lines with higher vegetation height [30], ii) with dry soil, as seismic lines with dry soil likely facilitate faster movement rates than seismic lines with wet soil, and also likely have less vegetative cover to impede movement, iii) that fall within forest, as seismic lines that fall in forest are likely more attractive as movement routes than seismic lines in non-forest, and iv) that fall within areas with lower densities of seismic lines, as seismic lines that occur in areas where there are fewer seismic lines are likely more attractive as movement routes than seismic lines that fall within areas with more seismic lines. At a fine scale, as lower vegetation on seismic lines facilitates faster predator movement rates, we predicted that movement rates near seismic lines would increase with decreasing vegetation height of seismic lines [30]. Detailed predictions and associated models are described in Table 1. Improving our understanding of how regeneration of disturbed areas affects

**Table 1. Models and associated predictions used to explain movement behaviour and movement rates of wolves and grizzly bears in relation to seismic lines in west-central Alberta, Canada, between 2003 and 2009.**

| Model (M)                | Prediction                                                                                                                         |  |  |  |  |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| Step Selection Functions |                                                                                                                                    |  |  |  |  |
| M1.eDist                 | Null model                                                                                                                         |  |  |  |  |
| M2.eDistVeght            | A. Move towards (eDist) lower vegetation height (Veght) seismic lines.                                                             |  |  |  |  |
| M3.<br>eDistVeghteWAM    | B. Move towards (eDist) drier (eWAM), lower vegetation height (Veght) seismic lines.                                               |  |  |  |  |
| M4.eDistVeght<br>Density | C. Move towards (eDist) lower vegetation height (Veght) seismic lines in areas with lower<br>densities of seismic lines (Density). |  |  |  |  |
| M5.eDistVeghtfLand       | E. Move towards (eDist) lower vegetation height (Veght) seismic lines in forest (fLand<br>(Con), fLand(Mix)).                      |  |  |  |  |
| Movement Rate            |                                                                                                                                    |  |  |  |  |
| M6.Season                | Null Model                                                                                                                         |  |  |  |  |
| Season<br>M7.Veght       | G. Increased movement rate near lower vegetation height (Veght) seismic lines.                                                     |  |  |  |  |
| SeasonfFor<br>M8.Veght   | H. Increased movement rate near lower vegetation height (Veght) seismic lines in forest<br>(fFor(1)).                              |  |  |  |  |

Variables are further described in S1 Table.

<https://doi.org/10.1371/journal.pone.0195480.t001>

![](_page_3_Picture_1.jpeg)

movement ecology of two predators will help determine when regenerated disturbances no longer impact wildlife of conservation concern. In addition, by evaluating predator movement behaviour relative to regenerating seismic lines our research could be used to aid in recovery and conservation efforts for caribou.

## **Materials and methods**

## **Ethical statement**

Animal capture and handling protocols adhered to guidelines under the Canadian Council on Animal Care [34] and were approved by university animal care committees (University of Alberta Animal Care Committee Standards 99–69; University of Calgary Animal Use Protocol BI11R-17; University of Montana Animal Use Protocol 059-09MHWB-122209; University of Saskatchewan Animal Use Protocol 20010016) and the Alberta Department of Sustainable Resource Development Animal Care Committee. Capture occurred on public lands and in provincial parks, and permission for capture of animals was granted under the authority of the Government of Alberta.

## **Study area**

The study area was in west-central Alberta, Canada (Fig 1; -117˚W to -120˚W, 53˚N to 55˚N) and encompassed the entire range of one boreal woodland caribou herd (Little Smoky), the low elevation winter ranges of three central mountain woodland caribou herds (A La Peche, Narraway, and Redrock-Prairie Creek), one grizzly bear population unit (BMA 4 Grande Cache), and seven wolf packs (A La Peche, Berland, Kakwa, Muskeg, Narraway, Simonette, and Two Lakes). We did not consider areas in the mountainous portions of central mountain caribou ranges because these areas are largely within protected areas with low human footprint. The study area was 10,772 km2 and spanned two natural sub-regions (upper foothills and lower foothills [35]). There are 15,588 km of seismic lines within the study area and other industrial footprint includes forestry cut blocks, oil and gas pipelines, access roads, and well sites. Mean seismic line densities were 1.45 km/km<sup>2</sup> .

## **Animal location data**

The animal GPS-telemetry dataset consisted of multiyear wolf and grizzly bear locations. Between 2003 and 2004 wolves were captured using rubber-padded foothold traps and via aerial net-gunning [36], while between 2007 and 2009 wolves were captured using rubber-padded foothold traps [37]. Grizzly bears were captured using leg-hold snares, culvert traps, and aerial helicopter darting [38,39], with capture efforts focused on culvert traps and aerial darting from 2006 onwards [40].

For wolves, data were collected from 24 individuals (17 female, 7 male) from 7 packs (A La Peche n = 2, Berland n = 2, Kakwa n = 4, Muskeg n = 7, Narraway n = 1, Simonette n = 5, Two Lakes n = 2) between 2003 and 2007, or 2007 to 2009 inclusively. We rarefied GPS locations to 2-hour intervals (Lotek 2200/3300, Lotek Engineering Systems, Newmarket, Ontario, Canada or Televilt GPS Simplex, Lindesberg, Sweden). For grizzly bears, we used GPS locations rarefied to 1-hour intervals (Televilt Global Positioning System, Lindesberg, Sweden) collected between 2005 and 2009 from 19 individuals (9 male, 10 female). Because of divergent habitat selection patterns among reproductive status and sex, we divided grizzly bear data into male and female groups, and further partitioned adult females into those with cubs *<*1 year old, and those without cubs and with cubs *>*1 year old (female [7]). The presence of cubs was confirmed visually during telemetry flights or capture events, and females with no cub observed

![](_page_4_Picture_1.jpeg)

![](_page_4_Figure_2.jpeg)

**Fig 1. Vegetation height on seismic lines in west-central Alberta, Canada.** Legacy seismic line footprint (15,588 km) within the range of west-central Alberta, Canada, caribou herds attributed with vegetation heights (33%, 66% and 100% quantiles) using LiDAR.

![](_page_5_Picture_1.jpeg)

during at least two repeated observations were classified as lone females. We excluded females with cubs *<*1 year old from analyses because of small sample sizes (n = 3, fall season only). We did not partition wolf data into sex or reproductive status because patterns of resource selection are similar for males and females [41].

In addition, we partitioned data based on seasonal resource availability patterns of grizzly bears (spring 1 May to 15 June; summer 16 June to 31 July; fall 1 August to 15 October [42]) and wolves (denning 20 April to 30 June; rendezvous 1 July to 20 September; nomadic 21 September to 19 April [36]). Because we were using GPS locations from earlier-technology collars with low fix success rate (wolves mean 0.51 (range 0.24–0.79); grizzly bears mean 0.46 (range 0.28–0.72)), we weighted all locations with the inverse of the probability of obtaining a fix (PFix) using models developed by Frair et al. [43] and Hebblewhite et al. [44].

## **Step selection functions–broad scale movements**

Because linear features like seismic lines influence predator movement, we confined our analysis to GPS locations collected when animals were actively moving, rather than resting or feeding. We used a clustering tool developed using the ArcPy site package within ArcGIS 10.2.2 [45] to divide GPS locations into 'movement' and 'stationary' (when animals were resting or feeding on a kill). For wolves, we defined stationary locations as locations collected when animals spent more than 6 hours within a 300-m radius [46]. We defined grizzly bear stationary locations as locations collected when bears spent more than 7 hours within a 100-m radius to exclude bedding and kill sites, but include foraging and travel. We excluded stationary locations for both species and also excluded animals with less than 40 movement locations per season from the analysis dataset. The step selection function dataset included 4,667 wolf locations and 9,658 grizzly bear locations (S2 Table).

## **Movement rates–fine scale movements**

The relatively low number of GPS locations available for analysis in the study area, and associated location error of ± 30 m in forest stands for the earlier-technology collars we used [47] prevented us from assessing movement along seismic lines that are on average, only 8 m wide as reported by Dickie et al. [25,30]. Thus, to balance potential GPS measurement error while ensuring that we had a sufficient number of locations to model animal movement near seismic lines across all seasons, we used GPS locations from animals with at least 20 locations that fell within 100 m of seismic lines within each season, reflecting locations that were well within the zone of influence of movement of seismic lines [48]. We recognize that the fix-interval available for analysis (1 and 2 hour) may underestimate animal movement rates [49,50], however within our study area fine scale data (e.g. 5 min fixes) were not available that matched the time that the LiDAR were collected.

Previous research assessing wolf movement rates revealed significant differences between males and females [51], however we had insufficient data (1 male) to build male-specific seasonal models or to include sex as a factor within models, we therefore only included female wolves in the movement rate dataset, the grizzly bear movement rate dataset included males and females. The movement rate dataset included 813 wolf locations (17% of movement locations) and 2,973 grizzly bear locations (31% of movement locations; S2 Table).

## **Data analysis**

Prior to analyses, we screened data for non-linearity, collinearity, and correlations following Zuur et al. [52], and excluded one of two variables from the same model if correlation coefficients were greater than 0.6, or if variation inflation factors were greater than 3. We carried out

![](_page_6_Picture_1.jpeg)

data exploration and statistical analyses within R [53] and visualised results using the ggplot2 package [54].

## **Step selection functions–broad scale movements**

We used step selection functions to assess the effect of seismic line regeneration, landcover, and seismic line wetness on movement of wolves and grizzly bears. Step selection functions (SSF [33]) integrate analysis of movement in a used-available resource selection analysis framework, providing a movement-based definition of availability and improving the definition of availability from an explicit movement-modeling paradigm [55]. We used Geospatial Modelling Environment [56] and ArcGIS 10.2.2 [45] to summarise movement distances and turn angles between successive GPS locations, and tested for correlations between movement distance and turn angles of each used step for each species-sex group within each season. We found no significant correlations (*rs <*0.115 in all cases) and therefore generated 10 available steps for each used step by randomly drawing step lengths and turn angles from the observed movement distributions for each species-sex group within each season [57].

We analysed data using conditional logistic regression [58] in the survival package [59], with each stratum consisting of one used step and 10 available steps. For wolves, we controlled for correlated movements of pack members by randomly retaining only one step when wolves from the same pack travelled within 200 m of each other [60,61]. Also for both species, as successive steps by an individual can be correlated with one another [55], we calculated robust standard errors based on independent clusters of steps following Fortin et al. [33]. We considered wolf steps that occurred more than five days apart from one another as independent clusters [61], while grizzly bear steps were considered independent from one another after 24 hours [62]. This approach yielded 67 independent wolf clusters and 307 independent grizzly bear clusters (S2 Table).

We fit conditional logistic regression models using a general estimating equation [59], and thus used the quasi-likelihood under the independence model criterion (QICU [63]) to assess which model(s) (Table 1) best explained observed animal steps (MuMIn package [64]). Because we were interested in typical selection patterns within the study area, we carried out QICU model selection at the population level [65], and chose the best model based on the lowest population QICU and highest model weight (*ωi*).

To calculate population-level coefficients, we fit the best model to each individual and then inverse-weighted coefficients across individuals [66]. We report results as beta (β) coefficients ± 95% confidence intervals (95% CI), and as the relative probability (logit (P)) of step selection as a function of exp (β<sup>1</sup> <sup>+</sup>. . . <sup>β</sup>x)/(1+exp(β<sup>1</sup> <sup>+</sup>. . . <sup>β</sup>x)).

We evaluated models with k-fold cross validation [67] using the hab package [68]. We randomly partitioned our strata into 80% training data and 20% testing data, and calculated the correlation (rs) between the relative probabilities of observed and predicted data for each used and available step. We repeated the process 100 times and report the average and range of rs values for used (rs1) and available (rs0) steps across all 100 comparisons; with better model performance indicated by higher values of rs1 when compared to rs0.

## **Movement rates–fine scale movements**

We used linear mixed models within the lme4 package [69] to assess movement rates of wolves and grizzly bears in relation to vegetation height and habitat intersecting seismic lines (S1 Table). Movement rates were exponentially distributed for both species, we therefore loge transformed movement rate and modeled movement rate as a Gaussian distribution. For wolves, we built a single model that included season as an interaction and identified the best

![](_page_7_Picture_1.jpeg)

random effect structure for the model (individual, individual nested within pack) using Akaike's Information Criterion corrected for small sample sizes (AIC $_{\rm C}$  [70]). To ease interpretation, we divided distances travelled by wolves between consecutive 2 hour locations by a value of 2, therefore converting the units to m/hour. For grizzly bears we built models for each sex and included season as an interaction. Vegetation height data were Poisson distributed, we therefore  $\log_{\rm e}$  transformed the vegetation height variable (Veght) after adding a constant of 1 to meet the linearity assumption for linear predictors.

We identified which model (Table 1) best explained movement rates using AIC<sub>C</sub> calculated in the AICcmodavg package [71]. We assessed the fit of the best model using marginal ( $R^2_{LMM(m)}$ ) and conditional  $R^2$  ( $R^2_{LMM(c)}$ ) values for linear mixed models calculated using the MuMIn package [64], where  $R^2_{LMM(m/c)}$  is the proportion of variance explained by the fixed effects, and combined random and fixed effects, within the model respectively [72].

When the best model revealed that there was a relationship between vegetation height and movement rate, we used piecewise regression to identify breakpoints where the relationship between vegetation height, and movement rate for each species, sex, and season changed. We carried out piecewise regression with the SiZer package [73] and estimated confidence intervals using 1,000 bootstrap replicates with  $\alpha$  set at 0.05.

#### **Environmental data**

Our motivation was to assess the overall influence of seismic lines on animal movement, therefore, we only included distance to seismic lines and environmental attributes of seismic lines within our analysis. Detailed SSF-based habitat models for wolves and grizzly bears can be found elsewhere [74,75].

#### Attributes of seismic lines

We used LiDAR data collected between 2005 and 2007 during the leaf-on period to attribute vegetation height to 15,588 km of seismic lines within the study area (Fig 1); calculating mean vegetation height (variable names in italics: Veght) along approximately 100 m length segments of seismic lines using a least-cost approach which identified and quantified the lowest vegetation along the seismic line (i.e. game trails; S1 File). We measured seismic line wetness, as represented by mean depth to water of each seismic line segment, using wet areas mapping data (WAM [76]). To represent the diminishing effect of the depth to water on vegetation growth we transformed WAM using an exponential decay function (eWAM: 1-exp<sup>-1.55\*WAM(m)</sup>) that caused the effect of depth to water to rapidly decrease at depths greater than 2 m, and to become constant at depths greater than 3 m (mean root depth of boreal forest vegetation  $2 \pm 0.3$  m [77]).

Using landcover derived from Moderate Resolution Imaging Spectroradiometer (MODIS) and Landsat imagery mapped at a 30 m x 30 m resolution [78], we determined the landcover (*fLand*) that intersected the longest length of each 100 m seismic line segment. For step selection function analysis, we classified landcover into three categories: Conifer (*fLand:Con*), Mixed (*fLand:Mix*), and Non-forest (*fLand:NF*). For movement rate analysis we classified landcover into a binary variable (*fFor*: 1 Forest, 0 Non-forest). For step selection function analyses, we also used a 1 km moving window with a 30 m cell size to calculate the density (*Density*) of seismic lines across our study area (km/km²). We attributed 100 m seismic line segments with mean *Veght*, *eWAM*, and *Density* values, and with the landcover (*fLand, fFor*) that intersected the majority of the seismic section using Geospatial Modelling Environment [56] and ArcGIS 10.2.2 [45,57]. Attributes of seismic lines are described in S1 Table.

![](_page_8_Picture_1.jpeg)

## **Attributes of animal steps**

For step-selection function analyses, to represent the diminishing effect of seismic lines and attributes of seismic lines on movement behaviour with increasing distance to seismic lines, we used an exponential decay function as the measure of distance from the end of each step to each seismic line segment (*eDist*; 1-exp-0.002Distance(m); S1 Table). As outlined by Thurfjell [57] because linear features are narrower than the step length of the animal only a small portion of each step will contain the linear feature, so using metrics calculated along the step might underestimate selection. Therefore, we used the end of the step to avoid underestimating selection for narrow seismic lines [57]. The exponential decay function caused the effect of distance to decrease rapidly beyond 500 m, and to become constant at distances greater than 2 km [42].

## **Results**

## **Vegetation height**

Mean vegetation height along seismic lines within the study area was 0.81 m (range 0–15 m; standard deviation 1.3 m; Fig 1). 11,755 km (75%) of the seismic line footprint had a mean vegetation height less than 1 m (S1 Fig).

## **Step selection functions–broad scale movements**

**Wolves.** During the denning season, the model including an interaction between distance to the nearest seismic line (*eDist*), seismic line vegetation height (*Veght*), and landcover intersecting the seismic line (*fLand*) best explained wolf steps (M5, ω<sup>i</sup> = 1). During the rendezvous season the model including an interaction between distance to the nearest seismic line, seismic line vegetation height, and seismic line wetness (*eWAM*) best explained wolf steps (M3, ω<sup>i</sup> = 0.85), and during the nomadic season the model including distance to the nearest seismic line best explained wolf steps (M1, ω<sup>i</sup> = 0.99; Table A in S2 File). Averaged inverse-weighted coefficients for the best models for each season are in Table A in S3 File.

During the denning season M5 indicated that wolf steps brought them closer to seismic lines (Fig 2). Specifically, wolf steps brought them closer to lower vegetation height seismic lines in non-forest, and closer to higher vegetation height seismic lines in mixed and conifer forest (Fig 2). During the rendezvous season M3 indicated that regardless of seismic line wetness, wolf steps brought them closer to lower vegetation height seismic lines (Fig 3). During the nomadic season M1 indicated that wolf steps brought them closer to seismic lines (β*eDist* = -0.33, 95% CI = 0.01). Means and ranges of Spearman rank correlations from k-fold cross validation suggested that M5 accurately predicted wolf steps during the denning season (mean rs1 0.806, range 0.414–0.975; mean rs0 0.015, range -0.695–0.709), but that M3 and M1 failed to completely predict wolf steps during the rendezvous (mean rs1 0.559, range -0.253–0.924; mean rs0 0.002, range -0.765–0.914) and nomadic (mean rs1 0.226, range -0.314–0.799; mean rs0−0.003, range -0.887–0.768) seasons.

**Grizzly bears.** The model including an interaction between distance to the nearest seismic line (*eDist*), seismic line vegetation height (*Veght*), and landcover intersecting the seismic line (*fLand*) best explained female grizzly bear steps across all seasons, and also best explained male grizzly bear steps during fall (M5, ω<sup>i</sup> = 1). During spring, the models including an interaction between distance to the nearest seismic line, seismic line vegetation height, seismic line wetness (*eWAM*), and landcover intersecting the seismic line best explained male grizzly bear steps (M3, ω<sup>i</sup> = 0.65; M5, ω<sup>i</sup> = 0.33). During summer, the model including distance to the nearest seismic line best explained male grizzly bear steps (M1, ω<sup>i</sup> = 0.68; Tables B and C in S2

![](_page_9_Figure_2.jpeg)

**Fig 2. Relative probability of step selection by wolves in west-central Alberta during the denning season.** Relative probability of step selection by wolves in west-central Alberta between 2003 and 2009 during the denning season in relation to distance to seismic lines (represented as an exponential decay (1-exp-0.002 Distance (m))), seismic line vegetation height (visualised using the mean of the lower (Low), middle (Mod), and upper (High) quantiles), and landcover intersecting seismic lines (Non-forest, Mixed, Conifer). Shaded areas are 95% confidence intervals around relative predicted probabilities of step selection.

File). Averaged inverse-weighted coefficients for the best models for each season are in Tables B and C in S3 File.

During spring, M5 indicated that female grizzly bear steps brought them closer to higher vegetation height seismic lines in non-forest, closer to lower vegetation height seismic lines in conifer forest, and further from higher vegetation height seismic lines in conifer forest (Fig 4). M3 indicated that during spring, regardless of seismic line wetness, male grizzly bear steps brought them closer to lower vegetation height seismic lines and further from higher vegetation height seismic lines (Fig 5). M5 indicated that during spring male grizzly bear steps brought them closer to seismic lines in non-forest and conifer forest, specifically closer to higher vegetation height seismic lines in non-forest, and closer to lower vegetation height seismic lines in conifer forest. M5 also indicated that, regardless of vegetation height, male grizzly bear steps brought them further from seismic lines in mixed forest (Fig 4).

During summer, M5 indicated that female grizzly bear steps brought them closer to lower vegetation height seismic lines in non-forest, further from higher vegetation height seismic lines in non-forest, neither closer to nor further from seismic lines in mixed forest, and regardless of vegetation height, female grizzly bear steps brought them further from seismic lines in conifer forest (Fig 6). M1 indicated that during summer, male grizzly bear steps brought them further from seismic lines (β*eDist* = 0.18, 95% CI = 0.14).

During fall, M5 indicated that female grizzly bear steps brought them closer to lower vegetation height seismic lines in non-forest and regardless of vegetation height, neither closer to nor further from seismic lines in mixed and conifer forest (Fig 6). M5 also indicated that male

![](_page_10_Picture_1.jpeg)

![](_page_10_Figure_2.jpeg)

**Fig 3. Relative probability of step selection by wolves in west-central Alberta during the rendezvous season.** Relative probability of step selection by wolves in west-central Alberta between 2003 and 2009 during the rendezvous season in relation to distance to seismic lines (represented as an exponential decay  $(1-\exp^{-0.002^* \text{ Distance (m)}})$ ) and seismic line vegetation height (visualised using the mean of the lower (Low), middle (Mod), and upper (High) quantiles). Seismic line wetness (*eWAM*) was held at the mean for prediction. Shaded areas are 95% confidence intervals around relative predicted probabilities of step selection.

grizzly bear steps brought them closer to lower vegetation height seismic lines regardless of landcover (Fig 7). Means and ranges of spearman rank correlations from k-fold cross validation suggested that all models failed to completely predict step selection of grizzly bears (Spring: Female mean  $\rm r_{s1}$  0.478, range -0.262–0.862; mean  $\rm r_{s0}$ –0.018, range -0.652–0.693, Male M3 mean  $\rm r_{s1}$  0.610, range 0.037–0.894; mean  $\rm r_{s0}$ –0.031, range -0.781–0.845, M5 mean  $\rm r_{s1}$  0.496, range -0.051–0.941; mean  $\rm r_{s0}$ –0.005, range -0.878–0.740; Summer: Female mean  $\rm r_{s1}$  0.483, range -0.027–0.902;  $\rm r_{s0}$  0.015, range -0.886–0.668, Male mean  $\rm r_{s1}$  0.-0.069, range -0.603–0.551;  $\rm r_{s0}$ –0.001, range -0.705–0.739; Fall: Female mean  $\rm r_{s}$  0.611, range 0.032–0.956,  $\rm r_{s}$  0.017, range -0.612–0.661, Male mean  $\rm r_{s1}$  0.529, range 0.018–0.945,  $\rm r_{s0}$  0.005, range -0.877–0.685).

## Movement rates-fine scale movements

**Wolves.** The best model explaining wolf movement rate included an interaction between vegetation height (*Veght*), season (*fSeason*), and landcover (*fFor*; M8; Table A in S4 File), and random effect for individual (Table B in S4 File). M8 indicated that during the rendezvous season, wolf movement rate increased near lower vegetation height seismic lines in forest, but there was no relationship between wolf movement rate and vegetation height of seismic lines in non-forest, or between movement rate and vegetation height of seismic lines during other seasons (Table 2,  $R^2_{LMM(m)}$  0.06,  $R^2_{LMM(c)}$  0.07). *Post-hoc* piecewise linear regression comparing movement rate of wolves in the rendezvous season and vegetation height of seismic lines in forest revealed a decrease in wolf movement rate above vegetation heights of 0.7 m (95% CI = 0.06).

![](_page_11_Picture_1.jpeg)

![](_page_11_Figure_2.jpeg)

Fig 4. Relative probability of step selection by grizzly bears in west-central Alberta during spring. Relative probability of step selection by grizzly bears in west-central Alberta between 2005 and 2009 during spring in relation to distance to seismic lines (represented as an exponential decay (1-exp<sup>-0.002\*</sup> Distance (m))), seismic line vegetation height (visualised using the mean of the lower (Low), middle (Mod), and upper (High) quantiles), and landcover intersecting seismic lines (Non-forest, Mixed, Conifer). Shaded areas are 95% confidence intervals around relative predicted probabilities of step selection.

https://doi.org/10.1371/journal.pone.0195480.g004

**Grizzly bears.** The best model explaining female grizzly bear movement rate included an interaction between vegetation height (*Veght*), season (*fSeason*), and landcover (*fFor*; M8; Table A in S4 File). M8 indicated that during spring and summer, there was no relationship between female grizzly bear movement rate and vegetation height of the nearest seismic line. However, during fall, female grizzly bear movement rate increased near higher vegetation height seismic lines in non-forest (Table 2;  $R^2_{LMM(m)}$  0.02,  $R^2_{LMM(c)}$  0.04). The best model explaining male grizzly bear movement rate was the null model (M6; Table A in S4 File). M6 indicated that male grizzly bear movement rates were higher during spring (reference category) when compared to summer (β<sub>Summer</sub> = -0.770, 95% CI = 0.393) and fall (β<sub>Fall</sub> = -1.054, 95% CI = 0.381;  $R^2_{LMM(m)}$  0.09,  $R^2_{LMM(c)}$  0.14).

### **Discussion**

Unravelling the mechanisms driving wildlife response to regenerating anthropogenic disturbance is essential to understand the spatiotemporal effects of anthropogenic activity on wildlife, and could be used to direct habitat restoration efforts to benefit species of conservation concern. In Alberta, Canada, the primary focus of recovery efforts for threatened woodland caribou is restoration of habitat, and specifically, identifying linear features that should be prioritized for restoration within caribou ranges. We found stronger selection of seismic lines by wolves when compared to grizzly bears, but responses to seismic lines varied seasonally and were dependent on regeneration stage (i.e. vegetation height) and landcover. During the rendezvous season, wolves are likely using low vegetation height seismic lines to increase travel

![](_page_12_Picture_1.jpeg)

![](_page_12_Figure_2.jpeg)

**Fig 5. Relative probability of step selection by male grizzly bears in west-central Alberta during spring.** Relative probability of step selection by male grizzly bears in west-central Alberta between 2005 and 2009 during spring in relation to distance to seismic lines (represented as an exponential decay (1-exp-0.002 Distance (m))), seismic line vegetation height (visualised using the mean of the lower (Low), middle (Mod), and upper (High) quantiles), and seismic lines wetness (represented as an exponential decay (1-exp-1.55WAM(m)) and visualised using the mean of the lower (Wet), middle (Mesic), and upper (Dry) quantiles. Shaded areas are 95% confidence intervals around relative predicted probabilities of step selection.

efficiency, but as wolves moved towards seismic lines regardless of vegetation height, our results suggest that seismic lines may not only be attractive to wolves as movement routes. For grizzly bears, movements in relation to seismic lines do not appear to increase travel efficiency. Combined, our results suggest that low vegetation height seismic lines primarily benefit wolves, facilitating movement, increasing wolf-ungulate encounters, and leading to a more rapid saturation of the wolf functional response [20].

As predicted, we found that wolves moved towards seismic lines with lower vegetation height during the rendezvous seasons. We also found that wolves moved faster near seismic lines with vegetation *<*0.7m, a result which is accordance with that of Dickie et al. [30], despite the comparatively coarse fix rates available for our analysis (2 hour vs. 5 min). Whether seismic lines with low vegetation are used to minimise the energetic costs of travel during the puprearing season [41, 79], or whether wolves move faster along low vegetation seismic lines because they are in areas with less ungulate prey, would require further investigation. Still, regardless of the mechanisms, seismic lines with lower vegetation heights likely provide movement routes for wolves during the rendezvous season, consistent with previous studies [25,26,74]. As prey are more diffuse and more difficult to encounter during the rendezvous season [41], the observed varations in movement behaviour among individual wolves are not suprising, and likely explain why we did not observe a cohesive response in movement behaviour relative to seismic lines during that season.

![](_page_13_Picture_1.jpeg)

![](_page_13_Figure_2.jpeg)

**Fig 6. Relative probability of step selection by female grizzly bears in west-central Alberta during summer and fall.** Relative probability of step selection by female grizzly bears in west-central Alberta between 2005 and 2009 during summer and fall in relation to distance to seismic lines (represented as an exponential decay (1-exp-0.002 Distance (m))), seismic line vegetation height (visualised using the mean of the lower (Low), middle (Mod), and upper (High) quantiles), and landcover intersecting seismic lines (Non-forest, Mixed, Conifer). Shaded areas are 95% confidence intervals around relative predicted probabilities of step selection.

Seismic lines with lower vegetation may be attractive movement routes during snow-free months, however, when snow is on the ground during the nomadic season and part of the denning season, snowpack depth and compaction can hinder or benefit movement on seismic lines [79,80]. Snow depth and compaction data were unavailable for the ~15,000 km of seismic lines in this study but may explain why we found no relationship between wolf movement rates and vegetation height during the nomadic and denning seasons.

Contrary to our prediction, we found that, wolves moved towards higher vegetation seismic lines during the denning season, and regardless of vegetation height, wolves moved towards seismic lines during the nomadic season. One potential explanation is that despite the high horizontal resolution of LiDAR (1 m), we were unable to identify narrow game trails or even all-terrain vehicle (ATV) trails underneath broad tree canopies that could have been established at earlier stages of regeneration and maintained through continued animal use; Tigner et al. [28] reported game trails on seismic lines with high levels of regeneration. It also possible that altered understory communities caused by soil compaction during construction [81,82] make seismic lines attractive to wolves regardless of vegetation height, as they contain the combination of early seral stage vegetation and cover preferred by their ungulate prey [82–84]. The proposed link between wolf habitat selection, prey, and vegetation preferred by prey has been reported previously [85–87], and assessing moose, deer, and elk response to regenerating seismic lines in would help confirm our interpretations of wolf movement.

Movement of wolves towards seismic lines regardless of vegetation height during the denning and nomadic seasons is especially important because most wolf-caused mortality on

![](_page_14_Picture_1.jpeg)

![](_page_14_Figure_2.jpeg)

**Fig 7. Relative probability of step selection by male grizzly bears in west-central Alberta during fall.** Relative probability of step selection by male grizzly bears in west-central Alberta between 2005 and 2009 during fall in relation to distance to seismic lines (represented as an exponential decay (1-exp-0.002 Distance (m))) and seismic line vegetation height (visualised using the mean of the lower (Low), middle (Mod), and upper (High) quantiles). Results are shown for the reference category of landcover intersecting seismic lines (Non-forest). Shaded areas are 95% confidence intervals around relative predicted probabilities of step selection.

**Table 2. Coefficient estimates (β) and 95% confidence intervals (CI) for the best model (M8) explaining female wolf and grizzly bear movement rate in west-central Alberta, Canada, between 2003 and 2009.**

|                                           |        | Wolves  |        | Female grizzly bears |  |
|-------------------------------------------|--------|---------|--------|----------------------|--|
|                                           | β      | ±95% CI | β      | ±95% CI              |  |
| log(Veght)                                | -0.386 | 1.110   | -0.434 | 0.614                |  |
| fSeason(Rendezvous Summer)1               | 0.184  | 0.997   | -0.317 | 0.247                |  |
| fSeason(Nomadic Fall)2                    | 0.770  | 0.835   | -0.114 | 0.255                |  |
| fFor                                      | -0.271 | 0.708   | 0.347  | 0.321                |  |
| log(Veght)fSeason(Rendezvous Summer)1     | 0.697  | 2.207   | 0.179  | 0.691                |  |
| log(Veght)fSeason(Nomadic Fall)2          | -0.237 | 0.674   | 0.742  | 0.363                |  |
| log(Veght) fForest                        | 2.109  | 1.111   | 0.151  | 0.707                |  |
| fForfSeason(Rendezvous Summer)1           | 2.041  | 0.876   | -0.057 | 0.372                |  |
| fForfSeason(Nomadic Fall)2                | -0.673 | 1.482   | -0.303 | 0.373                |  |
| log(Veght)fForfSeason(Rendezvous Summer)1 | -4.189 | 3.063   | -0.054 | 0.816                |  |
| log(Veght)fForfSeason(Nomadic Fall)2      | -1.695 | 2.331   | -0.240 | 0.853                |  |

Significant relationships are shown in bold. Denning and Spring were the reference categories for fSeason for wolves, and grizzly bears respectively. Variables are described in S1 Table.

<https://doi.org/10.1371/journal.pone.0195480.t002>

**<sup>1</sup>** Results for wolves are for the Rendezvous season, and results for grizzly bears are for the Summer season.

**<sup>2</sup>** Results for wolves are for the Nomadic season, and results for grizzly bears are for the Fall season.

![](_page_15_Picture_1.jpeg)

caribou occurs during those seasons [88]. Our results suggest that with the goal of restoring ecosystem function for caribou, natural regeneration of seismic lines may be insufficient to successfully restore seismic lines [30], at least in the time-frames examined in this study. More active restoration activities such as tree planting or seismic line blocking (felling trees across seismic lines) could be required to reduce use of seismic lines by wolves. However, Neufeld [36] showed that even moderately large-scale seismic line restoration activities such as line blocking and tree falling failed to appreciably affect wolf selection for seismic lines. Thus, with respect to our question of when wolf use of seismic lines is indistinguishable from the surrounding landscape, our analyses suggest that there may not be a clear threshold at which this occurs, and that adaptive restoration treatments (e.g. line blocking, tree planting) combined with management of alternate prey [89] are likely required to reduce wolf selection for and continued use of seismic lines.

We found significant associations between grizzly bear selection and seismic lines that were in accordance with previous research on black bears (*U*. *americanus*) [28,29,90]. As predicted, we found that grizzly bears moved away from seismic lines with higher vegetation height, moved towards seismic lines with lower vegetation height during spring, and male grizzly bears also moved towards seismic lines with lower vegetation height during fall. However, contrary to our prediction we found no relationship between grizzly bear movement rates and vegetation height of seismic lines. As omnivores, movement of grizzly bears while feeding on vegetation or while hunting ungulates are difficult to separate from travelling or seeking mates, making interpretations more challenging. Therefore, it is possible that during spring grizzly bears are using seismic lines for travel, or to search for and pursue mates [91], and male grizzly bears may also be using seismic lines with lower vegetation height for travel during fall. However, it is also possible that grizzly bears are using lower vegetation height seismic lines not only as movement routes, but also to access herbaceous food and woody shrubs [82, 92– 95]. Linking wildlife forage on seismic lines to LiDAR measurements of regeneration, combined with aforementioned assessments of moose, deer, and elk response to regenerating seismic lines, would confirm these potential explanations.

Within the exception of wolf models during the denning season, the poor cross validation results of suggest that seismic lines are not the only landscape feature influencing movements of wolves and grizzly bears within our study area. For grizzly bears, that forage in large areal disturbances such as forestry clear cuts and burned areas [7], and whose movements are driven by the availability of vegetative food [7], opportunistic hunting [96], and searching for mates [91], this result was not surprising. For wolves, although there is a link between seismic lines and movement [20,88], hunting behaviour is dependent on a range of additional factors such as prey density [97] and snow cover [80], which we were unable to include in our models. However, as ungulate specialists, wolf movement and habitat selection is driven by ungulate encounters [41, 87], therefore the strong cross validation of our denning models suggest that during that season seismic lines with higher vegetation height may be a source of ungulate prey. Habitat selection analysis of ungulate prey would confirm this interpretation.

## **Conclusions**

Based on our results and those of Dickie et al. [30], if restoration of linear features is soley focused on impeding wolf movement rate, then seismic lines with vegetation of less than 1 m could be prioritized for restoration. However, although regeneration did reduce grizzly bear response to seismic lines, because we found that wolves also moved towards seismic lines irrespective of vegetation height, in accordance with Dickie et al. [30], we caution the use of vegetation height alone as a metric to quantify habitat recovery. Instead, effective

![](_page_16_Picture_1.jpeg)

prioritization of habitat restoration, and ultimately, restoring ecosystem function for caribou will likely require a coordinated approach targeting disturbances preferred by alternate prey and shared-predators while considering the cumulative effects of disturbances across caribou ranges [98–100]. Ultimately, our results reveal that seismic lines continue to influence wolf movement behaviour decades after they are built, and even at later stages of regeneration, and it remains unknown at what stage of natural regeneration, if any, seismic lines cease to affect wolf movement. Considering that seismic lines may take up to 60 years to regenerate naturally in low productivity sites [32], it is likely that seismic lines are a longterm legacy within the boreal forest in western Canada. Avoiding new construction of these high-impact linear disturbance features elsewhere may help mitigate the long-term effects of anthropogenic activity on wildlife.

## **Supporting information**

**S1 [File.](http://www.plosone.org/article/fetchSingleRepresentation.action?uri=info:doi/10.1371/journal.pone.0195480.s001) Description of LiDAR processing used to attribute vegetation height to legacy seismic lines within the ranges of the Little Smoky, A La Peche, Redrock Prairie Creek and Narraway caribou herds in west-central Alberta, Canada.** (DOCX)

**S2 [File.](http://www.plosone.org/article/fetchSingleRepresentation.action?uri=info:doi/10.1371/journal.pone.0195480.s002) Quasi-likelihood under the independence model criterion for candidate models used to identify factors determining broad scale movement behaviour of wolves and grizzly bears in west-central Alberta, Canada, between 2003 and 2009.** (DOCX)

**S3 [File.](http://www.plosone.org/article/fetchSingleRepresentation.action?uri=info:doi/10.1371/journal.pone.0195480.s003) Population-level coefficient estimates and 95% confidence intervals for the best models explaining broad scale movement behaviour of wolves and grizzly bears in westcentral Alberta, Canada, between 2003 and 2009.** (DOCX)

**S4 [File.](http://www.plosone.org/article/fetchSingleRepresentation.action?uri=info:doi/10.1371/journal.pone.0195480.s004) Akaike under the independence model criterion for candidate models determining fine scale movement rates of wolves and grizzly bears in west-central Alberta, Canada, between 2003 and 2009.**

(DOCX)

**S1 [Table.](http://www.plosone.org/article/fetchSingleRepresentation.action?uri=info:doi/10.1371/journal.pone.0195480.s005) Variables used to explain broad scale movement behaviour (Step Selection Functions; SSF) and fine scale movement rates of wolves and grizzly bears in west-central Alberta, Canada, between 2003 and 2009.** (DOCX)

**S2 [Table.](http://www.plosone.org/article/fetchSingleRepresentation.action?uri=info:doi/10.1371/journal.pone.0195480.s006) Number of individual wolves and grizzly bears (N), steps, clusters, and steps within 100 m of seismic lines used to explain broad scale movement behaviour (Step Selection Functions; SSF) and fine scale movement rates in west-central Alberta, Canada, between 2003 and 2009.** Wolf clusters were successive steps taken *<* 5 days of one another while grizzly bear clusters were successive steps taken *<* 24 hours of one another. Wolf data were partitioned into denning, rendezvous, and nomadic seasons, while grizzly bear data were partitioned into males and females, and into spring, summer, and fall seasons. (DOCX)

**S1 [Fig](http://www.plosone.org/article/fetchSingleRepresentation.action?uri=info:doi/10.1371/journal.pone.0195480.s007). Histogram showing mean vegetation height (m) along 100 m segments of seismic lines in west-central Alberta, Canada, measured using LiDAR.** (DOCX)

![](_page_17_Picture_1.jpeg)

**S2 [Fig](http://www.plosone.org/article/fetchSingleRepresentation.action?uri=info:doi/10.1371/journal.pone.0195480.s008). Graphical abstract to accompany Finnegan et al. Natural regeneration on seismic lines influences movement behaviour of wolves and grizzly bears.** (TIFF)

## **Acknowledgments**

The Government of Alberta provided LiDAR and we are grateful to J. Stadt and D. Stepnisky for facilitating this process. D. Ghikas, C. Calihoo and G. Wilson (Environment and Climate Change Canada) provided support and guidance for this project. D. MacNearney, T. McKay, J. Crough, and K. Myles at fRI Research assisted with data management, GIS, and data analysis. We also acknowledge all of the individuals involved with project management, capture, collaring and field data collection of the extensive animal GPS datasets used for this analysis. We would like to thank the editor and anonymous reviewers for constructive comments that helped us to improve this manuscript. Jennifer Hird created the graphical abstract to illustrate this research (S2 Fig).

# **Author Contributions**

**Conceptualization:** Laura Finnegan, Karine E. Pigeon, Jerome Cranston, Gordon B. Stenhouse.

**Data curation:** Jerome Cranston, Mark Hebblewhite, Marco Musiani, Lalenia Neufeld, Fiona Schmiegelow, Julie Duval, Gordon B. Stenhouse.

**Formal analysis:** Laura Finnegan.

**Funding acquisition:** Laura Finnegan, Jerome Cranston, Gordon B. Stenhouse.

**Investigation:** Laura Finnegan, Jerome Cranston, Mark Hebblewhite, Marco Musiani, Lalenia Neufeld, Fiona Schmiegelow, Gordon B. Stenhouse.

**Methodology:** Laura Finnegan, Karine E. Pigeon.

**Project administration:** Laura Finnegan.

**Resources:** Laura Finnegan, Mark Hebblewhite, Marco Musiani, Lalenia Neufeld, Fiona Schmiegelow, Gordon B. Stenhouse.

**Software:** Jerome Cranston, Julie Duval.

**Supervision:** Laura Finnegan. **Validation:** Laura Finnegan.

**Visualization:** Laura Finnegan, Julie Duval.

**Writing – original draft:** Laura Finnegan, Karine E. Pigeon.

**Writing – review & editing:** Laura Finnegan, Jerome Cranston, Mark Hebblewhite, Marco Musiani, Lalenia Neufeld, Fiona Schmiegelow, Gordon B. Stenhouse.

## **References**

- **1.** Fischer J, Lindenmayer DB. Landscape modification and habitat fragmentation: a synthesis. Glob Ecol Biogeogr. 2007; 16: 265–280. <https://doi.org/10.1111/j.1466-8238.2006.00287.x>
- **2.** Haddad NM, Brudvig LA, Clobert J, Davies KF, Gonzalez A, Holt RD, et al. Habitat fragmentation and its lasting impact on Earth's ecosystems. Sci Adv. 2015; 1: 1–9. [https://doi.org/10.1126/sciadv.](https://doi.org/10.1126/sciadv.1500052) [1500052](https://doi.org/10.1126/sciadv.1500052) PMID: [26601154](http://www.ncbi.nlm.nih.gov/pubmed/26601154)

![](_page_18_Picture_1.jpeg)

- **3.** Nielsen S, McDermid G, Stenhouse G, Boyce M. Dynamic wildlife habitat models: Seasonal foods and mortality risk predict occupancy-abundance and habitat selection in grizzly bears. Biol Conserv. 2010; 143: 1623–1634.
- **4.** Singh NJ, Grachev IA, Bekenov AB, Milner-Gulland EJ. Saiga antelope calving site selection is increasingly driven by human disturbance. Biol Conserv. 2010; 143: 1770–1779. [http://dx.doi.org/10.](http://dx.doi.org/10.1016/j.biocon.2010.04.026) [1016/j.biocon.2010.04.026](http://dx.doi.org/10.1016/j.biocon.2010.04.026)
- **5.** Wittmer HU, McLellan BN, Serrouya R, Apps CD. Changes in landscape composition influence the decline of a threatened woodland caribou population. J Anim Ecol. 2007; 76: 568–579. [https://doi.org/](https://doi.org/10.1111/j.1365-2656.2007.01220.x) [10.1111/j.1365-2656.2007.01220.x](https://doi.org/10.1111/j.1365-2656.2007.01220.x) PMID: [17439473](http://www.ncbi.nlm.nih.gov/pubmed/17439473)
- **6.** McKay T, Sahle´n E, Støen O-G, Swenson JE, Stenhouse GB. Wellsite selection by grizzly bears Ursus arctos in west-central Alberta. Wildlife Biol. 2014; 20: 310–319. [https://doi.org/10.2981/wlb.](https://doi.org/10.2981/wlb.00046) [00046](https://doi.org/10.2981/wlb.00046)
- **7.** Nielsen SE, Boyce MS, Stenhouse GB. Grizzly bears and forestry I. Selection of clearcuts by grizzly bears in west-central Alberta, Canada. For Ecol Manage. 2004; 199: 51–65. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.foreco.2004.04.014) [foreco.2004.04.014](https://doi.org/10.1016/j.foreco.2004.04.014)
- **8.** Noss R, Nielsen S, Vance-Borland K. Prioritizing Ecosystems, Species, and Sites for Restoration. In: Moilanen A, Wilson K, Possingham H, editors. Spatial Conservation Prioritization: Quantitative Methods and Computational Tools. London: Oxford University Press; 2009. pp. 158–171.
- **9.** Sorensen T, McLoughlin PD, Hervieux D, Dzus E, Nolan J, Wynes B, et al. Determining sustainable levels of cumulative effects for boreal caribou. J Wildl Manage. 2008; 72: 900–905. [https://doi.org/10.](https://doi.org/10.2193/2007-079) [2193/2007-079](https://doi.org/10.2193/2007-079)
- **10.** Environment Canada. Recovery strategy for the Woodland Caribou (Rangifer tarandus caribou), Boreal population, in Canada. Species at Risk Act Recovery Strategy Series. Ottawa; 2012.
- **11.** Nielsen SE, Herrero S, Boyce MS, Mace RD, Benn B, Gibeau ML, et al. Modeling the spatial distribution of human-caused grizzly bear mortalities in the Central Rockies Ecosystem of Canada. Biol Conserv. 2004; 120: 101–113.
- **12.** Bowman J, Ray J, Magoun A, Johnson D, Dawson F. Roads, logging, and the large-mammal community of an eastern Canadian boreal forest. Can J Zool. 2010; 88: 545–567.
- **13.** Vors LS, Boyce MS. Global declines of caribou and reindeer. Glob Chang Biol. 2009; 15: 2626–2633.
- **14.** Hervieux D, Hebblewhite M, Decesare NJ, Russell M, Smith K, Robertson S, et al. Widespread declines in woodland caribou (Rangifer tarandus caribou) continue in Alberta. Can J Zool. 2013; 91: 872–882. <https://doi.org/10.1139/cjz-2013-0123>
- **15.** Bradley M, Neufeld LM. Climate and management interact to explain the decline of woodland caribou (Rangifer tarandus caribou) in Jasper National Park. Rangifer. 2010; 32: 183–192. [https://doi.org/10.](https://doi.org/10.7557/2.32.2.2268) [7557/2.32.2.2268](https://doi.org/10.7557/2.32.2.2268)
- **16.** Latham ADM, Latham MC, McCutchen NA, Boutin S. Invading white-tailed deer change wolf-caribou dynamics in northeastern Alberta. J Wildl Manage. 2011; 75: 204–212. [https://doi.org/10.1002/jwmg.](https://doi.org/10.1002/jwmg.28) [28](https://doi.org/10.1002/jwmg.28)
- **17.** James ARC, Boutin S, Hebert DM, Rippin AB. Spatial separation of caribou from moose and its relation to predation by wolves. J Wildl Manage. 2004; 68: 799–809.
- **18.** DeCesare NJ, Hebblewhite M, Robinson HS, Musiani M. Endangered, apparently: The role of apparent competition in endangered species conservation. Anim Conserv. 2010; 13: 353–362. [https://doi.](https://doi.org/10.1111/j.1469-1795.2009.00328.x) [org/10.1111/j.1469-1795.2009.00328.x](https://doi.org/10.1111/j.1469-1795.2009.00328.x)
- **19.** Wittmer HU, Sinclair ARE, McLellan BN. The role of predation in the decline and extirpation of woodland caribou. Oecologia. 2005; 144: 257–267. <https://doi.org/10.1007/s00442-005-0055-y> PMID: [15891849](http://www.ncbi.nlm.nih.gov/pubmed/15891849)
- **20.** McKenzie HW, Merrill EH, Spiteri RJ, Lewis MA. How linear features alter predator movement and the functional response. Interface Focus. 2012; 2: 205–16. <https://doi.org/10.1098/rsfs.2011.0086> PMID: [22419990](http://www.ncbi.nlm.nih.gov/pubmed/22419990)
- **21.** Hebblewhite M, Musiani M, DeCesare N, Hazenberg S, Peters W, Robinson H, et al. Linear features, forestry and wolf predation of caribou and other prey in west central Alberta. Final report to the Ptroleum Technology Alliance of Canada (PTAC). 84 pp. 2010.
- **22.** Gustine DD, Parker KL, Lay RJ, Gillingham MP, Heard DC, Vn BC. Interpreting resource selection at different scales for woodland caribou in winter. J Wildl Manage. 2006; 70: 1601–1614.
- **23.** Environment Canada. Recovery Strategy for the Woodland Caribou, Southern Mountain population (Rangifer tarandus caribou) in Canada. Ottawa, Ontario, Canada: Species at Risk Act Recovery Strategy Series. Environment Canada, Ottawa.; 2014.

![](_page_19_Picture_1.jpeg)

- **24.** Environment Canada. Scientific assessment to inform the identification of critical habitat for Woodland Caribou (Rangifer tarandus caribou), Boreal Population, in Canada: 2011 update. Ottawa; 2011. p. 102.
- **25.** Dickie M, Serrouya R, McNay S, Boutin S. Faster and farther: Wolf movements on linear features and implications for hunting behaviour. J Appl Ecol. 2017; 54: 253–263.
- **26.** DeCesare NJ. Separating spatial search and efficiency rates as components of predation risk. Proc R Soc B. 2012; 279: 4626–33. <https://doi.org/10.1098/rspb.2012.1698> PMID: [22977145](http://www.ncbi.nlm.nih.gov/pubmed/22977145)
- **27.** Mumma MA, Gillingham MP, Johnson CJ, Parker KL. Understanding predation risk and individual variation in risk avoidance for threatened boreal caribou. Ecol Evol. 2017; 10266–10277. [https://doi.org/](https://doi.org/10.1002/ece3.3563) [10.1002/ece3.3563](https://doi.org/10.1002/ece3.3563) PMID: [29238553](http://www.ncbi.nlm.nih.gov/pubmed/29238553)
- **28.** Tigner J, Bayne EM, Boutin S. Black bear use of seismic lines in Northern Canada. J Wildl Manage. 2014; 78: 282–292. <https://doi.org/10.1002/jwmg.664>
- **29.** DeMars CA, Boutin S. Nowhere to hide: Effects of linear features on predator-prey dynamics in a large mammal system. J Anim Ecol. 2017; <https://doi.org/10.1111/13>
- **30.** Dickie M, Serrouya R, DeMars C, Cranston J, Boutin S. Evaluating functional recovery of habitat for threatened woodland caribou. Ecosphere. 2017; 8: e01936. <https://doi.org/10.1002/ecs2.1936>
- **31.** Tigner J, Bayne EM, Boutin S. American marten respond to seismic lines in northern Canada at two spatial scales. PLoS One. 2015; 10: e0118720. <https://doi.org/10.1371/journal.pone.0118720> PMID: [25768848](http://www.ncbi.nlm.nih.gov/pubmed/25768848)
- **32.** van Rensen CK, Nielsen SE, White B, Vinge T, Lieffers VJ. Natural regeneration of forest vegetation on legacy seismic lines in boreal habitats in Alberta's oil sands region. Biol Conserv. Elsevier Ltd; 2015; 184: 127–135. <https://doi.org/10.1016/j.biocon.2015.01.020>
- **33.** Fortin D, Beyer HL, Boyce MS, Smith DW, Duchesne T, Mao JS. Wolves influence elk movements: Behavior shapes a trophic cascade in Yellowstone National Park. Ecology. 2005; 86: 1320–1330. <https://doi.org/10.1890/04-0953>
- **34.** Canadian Council on Animal Care. CCAC guidelines on the care and use of wildlife. Ottawa, Ontario, Canada; 2003.
- **35.** Natural Regions Committee. Natural Regions and Subregions of Alberta. Compiled by D.J. Downing and W.W. Pettapiece. Government of Alberta. Pub. No. T/852.; 2006.
- **36.** Neufeld LM. Spatial dynamics of wolves and woodland caribou in an industrial forest landscape in west-central Alberta. MSc. University of Alberta. 2006.
- **37.** DeCesare NJ. Resource selection, predation risk, and population dynamics of Woodland caribou. PhD. University of Montana. 2012.
- **38.** Cattet MMRL, Caulkett NA, Stenhouse GB. Anesthesia of grizzly bears using xylazine-zolazepam-tiletamine or zolazepam-tiletamine. Ursus. 2003; 14: 88–93.
- **39.** Cattet MR, Christison K, Caulkett N a, Stenhouse GB. Physiologic responses of grizzly bears to different methods of capture. J Wildl Dis. 2003; 39: 649–54. <https://doi.org/10.7589/0090-3558-39.3.649> PMID: [14567227](http://www.ncbi.nlm.nih.gov/pubmed/14567227)
- **40.** Cattet M, Boulanger J, Stenhouse GB, Powell RA, Reynolds-Hogland MJ. An evaluation of long-term capture effects in ursids: Implications for wildlife welfare and research. J Mammal. 2008; 89: 973–990.
- **41.** Mech LD, Boitani L. Wolves. Behaviour, Ecology and Conservation. Chicago: University of Chicago Press; 2003.
- **42.** Nielsen S, Cranston J, Stenhouse G. Identification of Priority Areas for Grizzly Bear Conservation and Recovery in Alberta, Canada. J Conserv Plan. 2009; 5: 38–60.
- **43.** Frair JL, Nielsen SE, Merrill EH, Lele SR, Boyce MS, Munro RHM, et al. Removing GPS collar bias in habitat selection studies. J Appl Ecol. 2004; 41: 201–212. [https://doi.org/10.1111/j.0021-8901.2004.](https://doi.org/10.1111/j.0021-8901.2004.00902.x) [00902.x](https://doi.org/10.1111/j.0021-8901.2004.00902.x)
- **44.** Hebblewhite M, Percy M, Merrill EH. Are All Global Positioning System Collars Created Equal? Correcting Habitat-Induced Bias Using Three Brands in the Central Canadian Rockies. J Wildl Manage. 2007; 71: 2026–2033. <https://doi.org/10.2193/2006-238>
- **45.** Environmental Systems Research Institute (ESRI). ArcGIS Desktop: Release 10. Redlands, California. Redlands, California; 2015.
- **46.** Webb N, Hebblewhite M, Merril E. Statistical methods for identifying wolf kill sites using global positioning system locations. J Wildl Manag. 2008; 72: 1798–1804.
- **47.** Frair JL, Fieberg J, Hebblewhite M, Cagnacci F, DeCesare NJ, Pedrotti L. Resolving issues of imprecise and habitat-biased locations in ecological analyses using GPS telemetry data. Philos Trans R Soc Lond B Biol Sci. 2010; 365: 2187–200. <https://doi.org/10.1098/rstb.2010.0084> PMID: [20566496](http://www.ncbi.nlm.nih.gov/pubmed/20566496)

![](_page_20_Picture_1.jpeg)

- **48.** McKenzie HW, Jerde CL, Visscher DR, Merrill EH, Lewis M a. Inferring linear feature use in the presence of GPS measurement error. Environ Ecol Stat. 2009; 16: 531–546. [https://doi.org/10.1007/](https://doi.org/10.1007/s10651-008-0095-7) [s10651-008-0095-7](https://doi.org/10.1007/s10651-008-0095-7)
- **49.** Mills KJ, Patterson BR, Murray DL. Effects of variable sampling frequencies on GPS transmitter efficiency and estimated wolf home range size and movement distance. Wildl Soc Bull. 2006; 34: 1463– 1469.
- **50.** Rowcliffe JM, Carbone C, Kays R, Kranstauber B, Jansen PA. Bias in estimating animal travel distance: The effect of sampling frequency. Methods Ecol Evol. 2012; 3: 653–662. [https://doi.org/10.](https://doi.org/10.1111/j.2041-210X.2012.00197.x) [1111/j.2041-210X.2012.00197.x](https://doi.org/10.1111/j.2041-210X.2012.00197.x)
- **51.** Jędrzejewski W, Schmidt K, Theuerkauf J, Jędrzejewska B, Okarma H. Daily movements and territory use by radio-collared wolves (Canis lupus) in Bialowieza Primeval Forest in Poland. Can J Zool. 2001; 79: 1993–2004.
- **52.** Zuur AF, Ieno EN, Elphick CS. A protocol for data exploration to avoid common statistical problems. Methods Ecol Evol. 2010; 1: 3–14. <https://doi.org/10.1111/j.2041-210X.2009.00001.x>
- **53.** R Development Core Team. R: A Language and Environment for Statistical Computing. R Foundation for Statistical Computing. 2017. <https://doi.org/10.1007/978-3-540-74686-7>
- **54.** Wickham H. ggplot2: elegant graphics for data analysis. New York: Springer; 2009.
- **55.** Duchesne T, Fortin D, Rivest LP. Equivalence between step selection functions and biased correlated random walks for statistical inference on animal movement. PLoS One. 2015; 10: 1–12. [https://doi.org/](https://doi.org/10.1371/journal.pone.0122947) [10.1371/journal.pone.0122947](https://doi.org/10.1371/journal.pone.0122947) PMID: [25898019](http://www.ncbi.nlm.nih.gov/pubmed/25898019)
- **56.** Beyer H. Geospatial Modelling Environment (version 0.7.2.1) [Internet]. 2012. Available: [http://www.](http://www.spatialecology.com/gme) [spatialecology.com/gme](http://www.spatialecology.com/gme)
- **57.** Thurfjell H, Ciuti S, Boyce MS. Applications of step-selection functions in ecology and conservation. Mov Ecol. 2014; 2: 1–12. <https://doi.org/10.1186/2051-3933-2-1>
- **58.** Duchesne T, Fortin D, Courbin N. Mixed conditional logistic regression for habitat selection studies. J Anim Ecol. 2010; 79: 548–55. <https://doi.org/10.1111/j.1365-2656.2010.01670.x> PMID: [20202010](http://www.ncbi.nlm.nih.gov/pubmed/20202010)
- **59.** Therneau T. A package for survival analysis in S. version 2.38 [Internet]. 2015. Available: [http://cran.r](http://cran.r-project.org/package=survival)[project.org/package=survival.](http://cran.r-project.org/package=survival)
- **60.** Courbin N, Fortin D, Dussault C, Courtois R. Landscape management for woodland caribou: the protection of forest blocks influences wolf-caribou co-occurrence. Landsc Ecol. 2009; 24: 1375–1388. Available: isi:000271809800009
- **61.** Courbin N, Fortin D, Dussault C, Courtois R. Logging-induced changes in habitat network connectivity shape behavioural interactions in the wolf-caribou-moose system. Ecol Monogr. 2014; 84: 265–285.
- **62.** Nielsen SE, Boyce MS, Stenhouse GB, Munro RHM. Modeling Grizzly Bear Habitats in the Yellowhead Ecosystem of Alberta: Taking Autocorrelation Seriously. Ursus. 2002; 13: 45–56.
- **63.** Pan W. Akaike's information criterion in generalized estimating equations. Biometrics. 2001; 57: 120– 125. PMID: [11252586](http://www.ncbi.nlm.nih.gov/pubmed/11252586)
- **64.** Barto´n K. MuMIn: Multi-Model Inference ver 1.13.4 [Internet]. 2015. Available: [http://cran.r-project.org/](http://cran.r-project.org/package=MuMIn) [package=MuMIn](http://cran.r-project.org/package=MuMIn)
- **65.** Fieberg J, Matthiopoulos J, Hebblewhite M, Boyce M, Frair J. Correlation and studies of habitat selection: problem, red herring, or opportunity? Philos Trans R Soc Lond B Biol Sci. 2010; 365: 2233–2244. <https://doi.org/10.1098/rstb.2010.0079> PMID: [20566500](http://www.ncbi.nlm.nih.gov/pubmed/20566500)
- **66.** Murtaugh P. Simplicity and complexity in ecological data analysis. Ecology. 2007; 88: 56–62. PMID: [17489454](http://www.ncbi.nlm.nih.gov/pubmed/17489454)
- **67.** Boyce MS, Vernier PR, Nielsen SE, Schmiegelow FKA. Evaluating resource selection functions. Ecol Modell. 2002; 157: 281–300. [https://doi.org/10.1016/S0304-3800\(02\)00200-4](https://doi.org/10.1016/S0304-3800(02)00200-4)
- **68.** Basille M. hab: Habitat and movement functions ver 1.7 [Internet]. 2015. Available: [http://ase](http://ase-research.org/basille/hab)[research.org/basille/hab](http://ase-research.org/basille/hab)
- **69.** Bates D, Maechler M, Bolker B, Walker S. Fitting Linear Mixed-Effects Models Using lme4. J Stat Softw. 2015; 67: 1–48.
- **70.** Burnham KP, Anderson DR. Model selection and multi-model inference: a practical information-theoretic approach. New York: Spring-Verlag; 2002.
- **71.** Mazerolle M. AICcmodavg: Model selection and mutlimodel inference based on (Q)AIC(c) [Internet]. 2013. Available: <http://cran.r-project.org/web/packages/AICcmodavg/AICcmodavg.pdf>
- **72.** Nakagawa S, Schielzeth H. A general and simple method for obtaining R2 from generalized linear mixed-effects models. Methods Ecol Evol. 2013; 4: 133–142.
- **73.** Sonderegger D. siZer: Significant Zero Crossings. 2012.

![](_page_21_Picture_1.jpeg)

- **74.** Latham ADM, Latham MC, Boyce MS, Boutin S. Movement responses by wolves to industrial linear features and their effect on woodland caribou in northeastern Alberta. Ecol Appl. 2011; 21: 2854– 2865. <https://doi.org/10.1890/11-0666.1>
- **75.** Roever CL, Boyce MS, Stenhouse GB. Grizzly bear movements relative to roads: application of step selection functions. Ecography (Cop). 2010; 33: 1113–1122. [https://doi.org/10.1111/j.1600-0587.](https://doi.org/10.1111/j.1600-0587.2010.06077.x) [2010.06077.x](https://doi.org/10.1111/j.1600-0587.2010.06077.x)
- **76.** White B, Ogilvie J, Campbell D, Hiltz D, Gauthier B, Chrisholm H, et al. Using the cartographic depthto-water index to locate small streams and associated wet areas across landscapes. Can Water Resour J. 2012; 37: 333–347.
- **77.** Canadell J, Jackson R, Ehleringer J, Mooney HA, Sala OE, Schulze E-D. Maximum rooting depth of vegetation types at the global scale. Oecologia. 1996; 108: 583–595. [https://doi.org/10.1007/](https://doi.org/10.1007/BF00329030) [BF00329030](https://doi.org/10.1007/BF00329030) PMID: [28307789](http://www.ncbi.nlm.nih.gov/pubmed/28307789)
- **78.** McDermid GJ, Hall RJ, Sanchez-Azofeifa G a., Franklin SE, Stenhouse GB, Kobliuk T, et al. Remote sensing and forest inventory for wildlife habitat assessment. For Ecol Manage. 2009; 257: 2262–2269. <https://doi.org/10.1016/j.foreco.2009.03.005>
- **79.** Metz MC, Smith DW, Vucetich JA, Stahler DR, Peterson RO. Seasonal patterns of predation for gray wolves in the multi-prey system of Yellowstone National Park. J Anim Ecol. 2012; 81: 553–563. [https://](https://doi.org/10.1111/j.1365-2656.2011.01945.x) [doi.org/10.1111/j.1365-2656.2011.01945.x](https://doi.org/10.1111/j.1365-2656.2011.01945.x) PMID: [22260633](http://www.ncbi.nlm.nih.gov/pubmed/22260633)
- **80.** Droghini A, Boutin S. Snow conditions influence grey wolf (Canis lupus) travel paths: the effect of human-created linear features. Can J Zool. 2017;cjz-2017-0. <https://doi.org/10.1139/cjz-2017-0041>
- **81.** Lee P, Boutin S. Persistence and developmental transition of wide seismic lines in the western Boreal Plains of Canada. J Environ Manage. 2006; 78: 240–250. [https://doi.org/10.1016/j.jenvman.2005.03.](https://doi.org/10.1016/j.jenvman.2005.03.016) [016](https://doi.org/10.1016/j.jenvman.2005.03.016) PMID: [16112795](http://www.ncbi.nlm.nih.gov/pubmed/16112795)
- **82.** Finnegan L, MacNearney D, Pigeon KE. Divergent patterns of understory forage growth after seismic line exploration: Implications for caribou habitat restoration. For Ecol Manage. Elsevier; 2018; 409: 634–652. <https://doi.org/10.1016/j.foreco.2017.12.010>
- **83.** Visscher DR, Merrill EH, Fortin D, Frair JL. Estimating woody browse availability for ungulates at increasing snow depths. For Ecol Manage. 2006; 222: 348–354.
- **84.** Melin M, Packale´n P, Matala J, Mehta¨talo L, Pusenius J. Assessing and modeling moose (Alces alces) habitats with airborne laser scanning data. Int J Appl Earth Obs Geoinf. 2013; 23: 389–396. [https://doi.](https://doi.org/10.1016/j.jag.2012.11.004) [org/10.1016/j.jag.2012.11.004](https://doi.org/10.1016/j.jag.2012.11.004)
- **85.** Hebblewhite M, Merrill E, McDonald T. Spatial decomposition of predation risk using resource selection functions: an example in a wolf-elk predator-prey system. Oikos. 2005; 111: 101–111.
- **86.** Hebblewhite M, Munro RH, Merrill EH. Trophic consequences of postfire logging in a wolf-ungulate system. For Ecol Manage. 2009; 257: 1053–1062.
- **87.** Roffler GH, Gregovich DP, Larson KR. Resource selection by coastal wolves reveals the seasonal importance of seral forest and suitable prey habitat. For Ecol Manage. 2017; 409: 190–201. [https://doi.](https://doi.org/10.1016/j.foreco.2017.11.025) [org/10.1016/j.foreco.2017.11.025](https://doi.org/10.1016/j.foreco.2017.11.025)
- **88.** Whittington J, Hebblewhite M, DeCesare NJ, Neufeld L, Bradley M, Wilmshurst J, et al. Caribou encounters with wolves increase near roads and trails: a time-to-event approach. J Appl Ecol. 2011; 48: 1535–1542. <https://doi.org/10.1111/j.1365-2664.2011.02043.x>
- **89.** Serrouya R, Mclellan BN, Boutin S. Testing predator-prey theory using broad-scale manipulations and independent validation. J Anim Ecol. 2015; 84: 1600–1609. <https://doi.org/10.1111/1365-2656.12413> PMID: [26101058](http://www.ncbi.nlm.nih.gov/pubmed/26101058)
- **90.** Latham ADM, Latham MC, Boyce MS. Habitat selection and spatial relationships of black bears (Ursus americanus) with woodland caribou (Rangifer tarandus caribou) in northeastern Alberta. Can J Zool. 2011; 89: 267–277. <https://doi.org/10.1139/Z10-115>
- **91.** Stenhouse GB, Boulanger J, Lee J, Graham K, Duval J, Cranston J. Grizzly bear associations along the eastern slopes of Alberta. Ursus. 2005; 16: 31–40.
- **92.** Revel RD, Dougherty TD, Downing DJ. Forest growth and revegetation along seismic lines. Calgary, Alberta, Canada: University of Calgary Press; 1984.
- **93.** Roever CL, Boyce MS, Stenhouse GB. Grizzly bears and forestry I: Road vegetation and placement as an attractant to grizzly bears. For Ecol Manage. 2008; 256: 1253–1261. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.foreco.2008.06.040) [foreco.2008.06.040](https://doi.org/10.1016/j.foreco.2008.06.040)
- **94.** Munro RHM, Nielsen SE, Price MH, Stenhouse GB, Boyce MS. Seasonal and Diel Patterns of Grizzly Bear Diet and Activity in West-Central Alberta. J Mammal. 2006; 87: 1112–1121. [https://doi.org/10.](https://doi.org/10.1644/05-MAMM-A-410R3.1) [1644/05-MAMM-A-410R3.1](https://doi.org/10.1644/05-MAMM-A-410R3.1)

![](_page_22_Picture_1.jpeg)

- **95.** Dawe C, Filicetti A, Nielsen S. Effects of Linear Disturbances and Fire Severity on Velvet Leaf Blueberry Abundance, Vigor, and Berry Production in Recently Burned Jack Pine Forests. Forests. 2017; 8: 398. <https://doi.org/10.3390/f8100398>
- **96.** Cristescu B, Stenhouse GB, Boyce M. Grizzly bear diet shifting on reclaimed mines. Glob Ecol Conserv. 2015; 4: 207–220.
- **97.** Je¸drzejewski W, Jędrzejewska B, Okarma H, Schmidt K, Zub K, Musiani M. Prey Selection and predation by wolves in Bialowieża primeval forest, Poland. J Mammal. 2000; 81: 197–212. [https://doi.org/10.](https://doi.org/10.1644/1545-1542(2000)081<0197:PSAPBW>2.0.CO;2) [1644/1545-1542\(2000\)081](https://doi.org/10.1644/1545-1542(2000)081<0197:PSAPBW>2.0.CO;2)<0197:PSAPBW>2.0.CO;2
- **98.** Serrouya R, McLellan BN, Boutin S, Seip DR, Nielsen SE. Developing a population target for an overabundant ungulate for ecosystem restoration. J Appl Ecol. 2011; 48: 935–942. [https://doi.org/10.1111/](https://doi.org/10.1111/j.1365-2664.2011.01998.x) [j.1365-2664.2011.01998.x](https://doi.org/10.1111/j.1365-2664.2011.01998.x)
- **99.** Serrouya R, McLellan B, van Oort H, Mowat G, Boutin S. Experimental moose reduction lowers wolf density and stops decline of endangered caribou. PeerJ. 2017; 5: e3736. [https://doi.org/10.7717/peerj.](https://doi.org/10.7717/peerj.3736) [3736](https://doi.org/10.7717/peerj.3736) PMID: [28875080](http://www.ncbi.nlm.nih.gov/pubmed/28875080)
- **100.** Hebblewhite M. Billion dollar woodland caribou and the biodiversity impacts of the global oil and gas industry. Biol Conserv. 2017; 206: 102–111.