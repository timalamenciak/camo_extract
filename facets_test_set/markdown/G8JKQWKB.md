# **Evaluating Restoration Success on Lyell Island, British Columbia Using Oblique Videogrammetry**

Trevor J. Davis,<sup>1</sup> Brian Klinkenberg,<sup>2,3</sup> and C. Peter Keller<sup>4</sup>

### **Abstract**

In degraded ecosystems where the impact on wildlife and the destruction of natural systems is high, restoration becomes a critical component of recovery. Monitoring restoration activities plays a key role in determining end points for restoration and assessing effectiveness. Appropriate monitoring of major systems, particularly in assessing vegetation reestablishment and slope stabilization, requires a long-term commitment to annual assessment of change and improvement over time. However, intrinsic factors built into government or public management systems, such as budgeting and staffing limitations, limit the ability for long-term monitoring of critical restoration projects. In the research reported in this article, we devised and assessed a new remote method for assessing restoration success and tested it on restoration and monitoring requirements in Lyell Island, British Columbia. We developed a system (the oblique data fusion system [ODFS]) to extract spatial information from oblique aerial video imagery. The ODFS enables low-cost change detection and database updates at a range of operational scales. System tests show an absolute spatial accuracy on the order of ±2.1 m. The evaluation, based on digitized historical data, ground surveys, and the ODFS-derived data, indicates that the landslide rate (new area/year) tapered off following treatment; after 5 years it had been reduced by a factor of 3 relative to the background rate. The recovery is deemed sufficient to initiate secondary restoration tasks. The evaluation demonstrates the accuracy and utility of the ODFS for long-term monitoring of landscape restoration efforts, particularly in remote areas. In conclusion, this new innovative method shows considerable promise for park managers.

Key words: aerial video, British Columbia, data fusion, GIS, Gwaii Haanas, Lyell Island, oblique video, slope stabilization.

### Introduction

Canada has one of the largest land-to-population ratios in the world; yet, even so, there are few opportunities for the establishment of pristine, representative protected areas. Parks Canada, the national agency entrusted with protecting nationally significant areas of Canada's natural heritage (Government of Canada 2000) and maintaining their ecological integrity, has therefore become one of the most active agencies in restoration efforts. Based on a policy that provides for ecosystem restoration in the event of significant human damage (Parks Canada 1994), Parks Canada ecologists have pioneered a number of restoration programs across the country—from species-specific work (e.g., *Vulpes velox* reintroduction in the prairies; Smeeton & Weagle 2000) to landscape level restoration (e.g., deciduous forests in Ontario; McLachlan & Bazely 2001).

The larger restoration efforts have often suffered from a problem common to many long-term restorations: funding can be quite intermittent, particularly during the drawn-out phase of monitoring a project's success. The need to monitor restoration has been widely acknowledged (Berger 1991; Reay & Norton 1999). Its absence not only decreases the effectiveness of the restoration, but also provides little evidence of success (or failure) to spur further efforts in other regions or refine a methodology. This has been a particular problem in remote, protected areas, which have the highest logistic costs coupled with the lowest revenue from tourists.

In dealing with remote and difficult sites, remote sensing methods for evaluating and inventoring restoration success are clearly needed. To meet this challenge we have developed a change-detection system suitable for low-cost, long-term monitoring of vegetation and terrain restoration. It was developed to meet the requirements of a specific restoration project; yet it is applicable to a wide range of situations. Here we describe the system and its initial implementation in monitoring and evaluating the restoration of Lyell Island (Fig. 1), part of Gwaii Haanas National Park/Reserve, located 50 km off the north coast of British Columbia, Canada in the Queen Charlotte Islands (also commonly known as Haida Gwaii) at 52°40′N, 131°33′W.

<sup>&</sup>lt;sup>1</sup> University College of the Cariboo, P.O. Box 3010, 900 McGill Road, Kamloops, BC, Canada V2C 5N3

<sup>&</sup>lt;sup>2</sup> Department of Geography, University of British Columbia, 217-1984 West Mall, Vancouver, BC, Canada V6T 1Z2

Address correspondence to B. Klinkenberg, email brian@geog.ubc.ca

<sup>&</sup>lt;sup>4</sup>Department of Geography, University of Victoria, P.O. Box 3050, Victoria, BC, Canada V8W 3P5

<sup>© 2004</sup> Society for Ecological Restoration International

![](_page_1_Picture_1.jpeg)

Figure 1. Lyell Island (53 N, 132 E). Image based on LANDSAT Thematic Mapper data from April 1977. The black lines represent the logging road network (not visible on the LANDSAT image).

Lyell consists of 17,300 ha of originally forested land. It is an area of extreme relief, with numerous 3545 slopes facing the ocean or lying above salmon spawning habitat (Fig. 2). While the west side of the island is relatively protected, the east side faces directly onto Hecate Strait. Numerous winter storms cross the strait, and it is considered by mariners to be one of the more dangerous passages in North America. These storms typically strike Lyell from the southeast and provide the precipitation (yearly mean 1,542 mm for the region, with peak years as high as 4,218 mm, 96% as rain) and winds that trigger a significant number of mass wastage events.

The native vascular plant communities on Lyell consist of a coastal temperate rainforest mix of Picea sitchensis (Sitka spruce), Thuja plicata (western redcedar), and

![](_page_1_Figure_5.jpeg)

Figure 2. A typical landslide on Lyell. Inset: Frequency of the distribution of slopes on the island.

Tsuga heterophylla (western hemlock), with an understory of Calamagrostis nutkaensis (Nootka reed grass) on the coast and moss or Gaultheria shallon (salal) inland. The ecosystems of Gwaii Haanas National Park/Reserve support a unique natural heritage due to their isolation from the mainland coast and the existence of glacial refugia (Josenhans et al. 1995). They support a large number of endemic flora and fauna that are distinct, at the subspecies level, from continental forms (Golumbia 2001).

The island has been the site of extensive clear-cut logging since about 1920, with the most recent round beginning in 1976. Between then and 1986, 22% of the island's land base was clear-cut, principally in the steep, eastern valleys. Over 140 km of roads were constructed to reach and extract 3,100 ha of timber, with a scaled volume of 2 million m3 (Ecosat Geobotanical Surveys 1989). The cutting locations and methods used by the contractor were so blatantly substandard and environmentally damaging as to trigger a local outcry, which later led to a highly publicized series of protests and arrests (Johnston 1987). The Canadian government responded by creating Gwaii Haanas National Park/Reserve in 1987, encompassing the southernmost 15% of the archipelago (147,000 ha).

One of the first major projects in this new park was the restoration of Lyell Island. This was envisioned as a longterm project, with an initial goal of stabilizing slopes to allow vegetation and stream recovery to begin. It was the first restoration work of its kind ever attempted in the region, and many of the techniques employed were based on informed guesses or extrapolation. Running from 1988 to 1992, it included full road decommissioning, bridge removal and stream rehabilitation, Alnus rubra (red alder) planting on exposed road surfaces, helicopter seeding on all landslide areas, and hand planting of 750 ha with P. sitchensis, T. heterophylla, and T. plicata. Although not documented in detail, a typical landslide area received 40 kg/ha of seed (primarily Lolium multiflorum [annual ryegrass] and Festuca rubra [red fescue]) and 250 kg/ha of fertilizer at an estimated cost of \$CA650/ha. These species were utilized due to their ready availability, with the intention that native species colonization would occur following slide stabilization. Both wet and dry seeding were utilized, and all treated areas were mapped and dated. Roads in potential landslide areas received particular attention—the original grade was restored where possible and over 1,000 waterbars were constructed.

The second stage of the restoration was envisioned as approximately 10 years of monitoring. This was to ensure that the principle restoration step—the elimination of causes of destabilization (Majer 1989; Hobbs & Norton 1996)—had been substantially completed (slopes had stabilized) before detailed stream restoration and other, less drastic, measures would be taken.

However, as is the case with many agencies, it was easier to fund large, short-term restorative work than to fund long-term monitoring. The methods typically employed for monitoring were deemed too problematic or expensive during reviews in later years. The principle issue in developing a monitoring program is the need to detect small events (landslides) and incremental growth of vegetation in some degree of detail, but over a very broad area. In addition, detecting landslides and change in surface area over time requires a spatial inventory; however, the cost of completing a new such inventory every few years through satellite or airphoto interpretation was deemed too high. Owing to the extremely rugged terrain, ground surveys to cover such a wide area were not an option. Complicating matters, this area has very few cloud-free days, leading to difficulty in image acquisition from both aforementioned optical image sources.

To address these issues we have developed a system to extract spatial information from a hitherto unutilized source: oblique aerial photos and video imagery. Digital aerial video has been used for inventory work in a number of applications, such as identifying shrubs on rangeland (Everitt et al. 1991), mapping forest vegetation (Graham 1993; Slaymaker et al. 1996), determining harp and hooded seal size and location on ice floes (Estep et al. 1994), and monitoring wetland restoration (Phinn et al. 1996). All of the above-mentioned vertical imagery is gathered in much the same way as aerial photographs. Although much easier to obtain, oblique images have previously been used only for descriptive or reference information. For example, large sections of the United States and Canadian west coast have been captured on oblique video, allowing rough estimates of shoreline type to be developed (Howes et al. 1994), and the USGS uses it for feature recognition tasks to document hurricane damage. Similarly, ground-based oblique images are commonly used to monitor landscape change through the use of periodically visited photo stations (Gobin et al. 2001).

However, none of these applications make direct use of the spatial information in the image. To do so, we modified a geographic information system (GIS) so that a perspective view of the terrain could be registered to the aerial image. Data are then entered using three-dimensional digitizing directly on-screen. This integration/visualization process enables detection of spatial change, such as new mass wastage events or vegetation growth, as well as, in our opinion, providing better image interpretation than would be possible from vertical images. This system is termed the oblique data fusion system (ODFS).

An important aspect of the ODFS is the incorporation of spatial metadata—capturing and displaying the uncertainty in the location of lines. Although metadata is an important aspect of any data source, it has particular importance in oblique images due to the variable target distance. Elements in the foreground typically have much higher certainty than those located farther away. By capturing this metadata, and carrying it through to the resulting database, it is possible to calculate estimates of uncertainty in location, area, length, and any other spatial parameter.

# Methods

### The ODFS

Data for the ODFS are gathered using any standard commercial or high-end consumer video camera, synchronized with a GPS unit. GPS data can be stored on a data track or externally (the capture methodology is described fully in the following section). Individual video frames are captured from the tape and automatically tagged with a threedimensional GPS reference through time cross-referencing. The location reference is then used to initialize a GISbased perspective view of the terrain, which is displayed as an overlay on the video frame. The perspective view includes all pertinent available data from the GIS database, including (in the following study) the ground surface, roads, hydrology, and existing target information (e.g., cutblock boundaries or landslides.) The viewpoint is then interactively manipulated to bring the digital and the frame perspective into correspondence. A variety of methods can be used to visualize spatial metadata (Hearnshaw & Unwin 1994), allowing the user to determine when maximal registration accuracy has been achieved.

To summarize, the existing GIS data are displayed in a standard overlay on a perspective view. This imitates how the target area would look from the aircraft if the GIS data were actually on the ground. The viewpoint for the perspective view is set to coincide with the exact position of the aircraft at a particular point in time. Because GPS readings have some degree of error, a registration system is used to adjust the viewpoint coordinates until fixed features (e.g., roads and hilltops) line up.

The initial and final steps in image registration are presented in Figure 3a and 3b. The intervening steps include image rotation and changes to the virtual viewpoint including zooming, xy movement, and elevation change. These steps are accomplished interactively by a user, or may be automated through a search heuristic. In Figure 3b uncertainty in road location is visualized. It covers the image of the road, indicating that the operator is approaching maximum registration accuracy.

If changes in the scene are noted, new information is digitized directly on-screen (Fig. 4) using a ray-tracing algorithm developed for CAD/CAM and medical applications (Uenohara & Kanade 1995). This perspective-based information is then converted to planimetric data and entered into the database. In essence, the user draws with a mouse on the on-screen digitally enhanced photograph of the scene. The lines entered by the user are converted to map data by reversing the process that generates a perspective view. The accuracy of each newly entered line segment is determined in a separate procedure that quantifies the registration accuracy of the video image as compared with the computer-generated perspective view. Attribute data, such as species, ground cover, or surficial geology, can be entered into the database at this point.

![](_page_3_Picture_1.jpeg)

![](_page_3_Picture_2.jpeg)

Figure 3. Registration of a perspective view (linework) and a video image. The initial registration based on GPS data (a). In the final registered view (b), the uncertainty in road location (epsilon distance) is viewed as a blurred region around a center line. Note the new landslide that appears to the right of the large landslide in the middle of the image.

![](_page_3_Picture_4.jpeg)

Figure 4. On-screen digitizing to add the new landslide to the database.

A major issue in performing change detection and updates, as opposed to gathering a new dataset, is determining whether apparent change is "actual" change rather than an artifact of the process. For example, a landslide that appears to have grown by 5 m may have experienced no change at all if the spatial variability of the original data (or the newly collected data) is 5 m or more. To address this issue we also incorporated spatial metadata visualization into the digitizing process using a variety of userdefined methods (banding, cross-hatching, or variable opacity overlays). Metadata were drawn from published accuracy data for source layers, the highly specific results of airphoto registration during the creation of orthophotos. and from ground survey tests conducted during the pilot phases of this study. To facilitate accuracy assessment in future updates the new video images are also archived.

Prior to implementing the study described below, we ran a number of accuracy tests on the system using ground surveys with GPS control. The boundaries between defined areas were determined to have an epsilon bandwidth of 2.3 m (the line containing 90% of offsets; see Blakemore 1983) as detailed in Figure 5. Epsilon bandwidth is a measure of spatial consistency between two representations of the same map object, typically used to indicate digitizing accuracy. Here we compare a highly accurate ground survey with the ODFS-generated lines. The perpendicular spatial offset of each new line segment (ODFS) is measured relative to the original line. The line lengths are then normalized (to enable comparison of different sized objects), and the results are plotted. The lines that bound 90% of the offsets provide an estimate of the epsilon bandwidth. If the bounds are centered on zero, no bias is indicated. In Figure 5 we present a random subset of the ODFS data (for clarity). Each line in the figure represents one of the polygon boundaries. After each line has been normalized the x-axis distance is the same for all lines. The y-axis value

![](_page_3_Figure_9.jpeg)

Figure 5. Perpendicular offsets of surveyed points from oblique data fusion system-generated lines. All lines (slide perimeters) have been normalized to a standard distance (*x*-axis). The dark line represents the epsilon bandwidth statistic, enclosing 90% of the offsets.

is the offset of the new line from the real line—essentially a graph of error over a linear distance. The data in Figure 5 indicate that there is no particular bias to the error (i.e., more on one side of the line than the other).

Similar tests replicating orthophoto-derived data using the ODFS resulted in an epsilon bandwidth of 3.1 m. Area comparisons between surveyed and ODFS polygons had a mean difference of *1*5% with a standard deviation of 10.2 ha; 90% of the comparisons fell within 17%. This compares favorably with 1 : 15,000 photogrammetry (620%, with considerable regional variability; Everitt et al. 1991). Full details of these tests are provided in Davis (1999).

### Lyell Island Study

We used six aerial photo series (both partial and complete), stretching back to 1977, to generate a set of historical orthophoto mosaics of Lyell Island. Image spatial resolution was on the order of 1 m, with an average spatial registration accuracy of 2.6 m relative to ground control. Slide zones were identified and digitized in each mosaic, providing a history of change for each landslide before the 1990 restoration effort. The date of occurrence for each event was estimated from photos, reports, plans, forestry maps, and interviews (Davis 1999).

Subsequently, each slide was examined in light of other data, and fields were coded based on the following criteria: source (natural or logging); impact on streams (scouring, side impact, or direct scouring of potential fish habitat); type of event (mass movement or road sidecast); and relation to roads (triggered by road or not). These items were not coded based on automated analytical criteria, but were coded individually taking all available data into consideration.

The data for the initial restoration monitoring exercise were gathered during a 2-hr helicopter flight in the summer of 1997, using a one-chip CCD standard commercial video camera, mounted in the doorframe. GPS data were captured within a GPS unit on 1-second intervals, and the two sources were tied together through clock synchronization. We limited the equipment to standard commercial units to emulate a typical reconnaissance or crew transfer flight.

The most useful images (in terms of their data-extraction potential) resulted from: (1) aircraft speeds under 25 knots (minimizing frame blurring), (2) a position that maintains a maximum number of terrain reference points while minimizing distance to target (simplifying registration), and (3) a camera technique utilizing a mix of wide shots to establish spatial reference points, coupled with zooms to capture detail (further simplifying registration).

Approximately 40 hr of work were required for an experienced technician to enter the flight-captured oblique videogrammetry data into the system using the ODFS. This consisted of 280 frames, 180 polygon updates, and data for each slide area such as ground cover, road stability, and vegetation or stream damage.

### Results

The restoration of Lyell Island had several goals: to decrease the slide rate as quickly as possible and to utilize several treatment types and assess their relative merits to facilitate future work. Table 1 and Figure 6 show a condensed summary of the restoration evaluation study results. The data indicate that slide levels have dropped off in the period following treatment, particularly when compared with the area that would be expected to slide if no treatment had occurred (''area available'' in Fig. 6). However, the results provide little evidence of the relative success of different treatment types. There are also additional factors discussed in the following section.

Overall, there have been 144 ha of mass wastage observed on Lyell Island since 1977 (0.75% of the land base), including areas visible at the onset of logging. Currently, 115 ha of the mass wastage remain visible. The 1997 update indicates that 21 ha of new slides have occurred since 1990, although approximately six of these occurred between 1990 and the onset of treatment in 1991. Of the 144 ha total, 11% are classified as naturally occurring; 21% of these natural slides existed before the 1976 (re)commencement of logging.

Figure 6 is a condensed summary of the entire dataset, showing the correspondence between logging and landslide area over time. The ''area available'' represents the logged areas that have experienced sufficient root degeneration to enable landslides to take place should a weather event of sufficient severity occur (Hammond et al. 1992). To the right of the graph, this area decreases as natural regeneration builds new root systems (assuming no restoration). In comparison, the background natural slide rate (referring to actual slides in undisturbed areas) has changed little over time. Approximately 75 ha of landslide areas were treated with aerial seeding (77% of all slides visible in 1990). Of these, there was a net change of 0.3 ha between the treatment date and 1997. This involved a slide expansion of 1 ha, and a grow-back of 0.7 ha. The bulk of the 1-ha expansion was one 0.7-ha slide in one of the most destabilized areas on the island. In addition, this slide was apparently not triggered from within the area seeded.

Given the relatively few slide events in treated areas, there is little evidence to judge the relative success of different treatment types. Slide expansion in dry-seeded areas amounted to 0.95% (increase in area), while expansion in the wet-seeded areas (generally considered to be a more successful treatment method; Hammond et al. 1992) totaled 1.6%.

Owing to the uneven application and patchy documentation, it is impossible to quantitatively assess the effect of road deactivation (by far the most costly part of treatment) on slide rates. The percentage of slides that were induced by road cuts actually increased in the post-treatment period (34%, up from 20%), but the absolute value dropped from 18 to 7 ha.

Table 1. Summary of project results for Lyell Island at the four principal update periods, based on historical data (airphotos), ground observation, and the new oblique data fusion system.

|                                                              | 1977         | 1980         | 1990            | 1997         |
|--------------------------------------------------------------|--------------|--------------|-----------------|--------------|
| Study area (ha)                                              | 10,390.4     | 13,990.2     | 14,550.9        | 19,036.8     |
| Total area logged (visible)                                  | 214.7        | 991.8        | 3,517.2         | 3,517.2      |
| As percentage of Lyell                                       | 1.1          | 5.2          | 18.5            | 18.5         |
| As percentage of study area                                  | 2.1          | 7.1          | 24.2            | 18.5         |
| Area logged during previous period<br>As percentage of Lyell | 214.7<br>1.1 | 777.1<br>4.1 | 2,525.4<br>13.3 | 0.0<br>0.0   |
| Slide area showing                                           | 9.1          | 27.0         | 97.7            | 115.3        |
| As percentage of Lyell                                       | 0.05         | 0.14         | 0.51            | 0.61         |
| As percentage of study area                                  | 0.09         | 0.19         | 0.67            | 0.61         |
| As percentage of total cut area                              | 4.2          | 2.7          | 2.8             | 3.3          |
| Recovery since previous date                                 |              | 5.3          | 19.2            | 3.9          |
| New slides                                                   | 9.1          | 23.2         | 89.8            | 21.6         |
| As percentage of study area                                  | 0.09         | 0.17         | 0.62            | 0.11         |
| Treated slides<br>As percentage of 1990 slides               |              |              |                 | 75.0<br>76.8 |
| New slides                                                   |              |              |                 |              |
| Cause                                                        |              |              |                 |              |
| Logging                                                      | 5.8          | 17.7         | 83.4            | 21.1         |
| Natural                                                      | 3.3          | 5.4          | 6.8             | 3.0          |
| As percentage of unlogged                                    | 0.03         | 0.04         | 0.06            | 0.02         |
| Type                                                         |              |              |                 |              |
| Mass wastage                                                 | 8.8          | 22.0         | 85.9            | 20.3         |
| As percentage of all landslides<br>Sideslip                  | 96.8<br>0.3  | 91.7<br>2.0  | 95.6<br>7.2     | 92.6<br>4.9  |
| Stream                                                       |              |              |                 |              |
| Scouring<br>As percentage of all landslides                  | 7.3<br>80.3  | 19.7<br>85.0 | 54.2<br>60.4    | 4.3<br>19.8  |
| Main                                                         | 0.0          | 0.2          | 0.0             | 0.0          |
| Road induced                                                 | 1.3          | 6.5          | 18.2            | 7.3          |
| As percentage of all landslides                              | 14.6         | 28.1         | 20.2            | 33.8         |
| Total slides                                                 |              |              |                 |              |
| Cause                                                        |              |              |                 |              |
| Logging                                                      | 5.8          | 18.6         | 89.1            | 106.6        |
| Natural                                                      | 3.3          | 8.4          | 8.6             | 8.7          |
| Type                                                         |              |              |                 |              |
| Mass wastage                                                 | 8.8          | 25.9         | 93.3            | 109.6        |
| Sideslip                                                     | 0.3          | 2.0          | 0.8             | 12.5         |
| Stream<br>Scouring                                           | 7.3          | 22.7         | 60.3            | 62.1         |
| Main                                                         | 0.0          | 0.2          | 0.0             | 0.7          |
| Road induced                                                 | 1.3          | 6.5          | 20.3            | 26.7         |
| Treated slides                                               |              |              |                 |              |
| Cause                                                        |              |              |                 |              |
| Logging                                                      |              |              |                 | 75.0         |
| Natural                                                      |              |              |                 | 0.0          |
| Type                                                         |              |              |                 |              |
| Mass wastage<br>Sideslip                                     |              |              |                 | 74.5<br>3.5  |
| Stream                                                       |              |              |                 |              |
| Scouring                                                     |              |              |                 | 49.4         |
| Main                                                         |              |              |                 | 0.0          |
| Road induced                                                 |              |              |                 | 16.0         |

Areas are expressed in hectares.

![](_page_6_Figure_1.jpeg)

Figure 6. Summary of study results. The most recent logging activity ran from 1976 to 1986. The right y-axis refers to the ''area available'' curve only (the slide activity expected if no treatment were undertaken). The ''treatment period'' is the duration of the rehabilitation work (there has been no subsequent treatment).

# Discussion

An evaluation of restoration success is the principle purpose of this study, with the central question being: ''Have landslides stabilized since the treatment period?'' Such an evaluation is considerably hampered by a lack of valid control areas for comparison. However, even in such a case, the number of areas required for statistical validity would be quite high if the focus were on individual slides as single events. To help overcome this problem, we focused the evaluation on change in area over time (i.e., change in physical area of existing slides or the area of new slides). This temporal focus of the study used a substantial quantity of data. Even so, there is no possible way to provide statistical rigor for any of the conclusions, given (1) the number of variable influences on each slide area, (2) data dependence due to spatial contiguity, and (3) the limited time span of the study. Nevertheless, there are a number of apparent trends.

To establish a background natural landslide rate for comparison, we enumerated all slides on Lyell Island outside of the disturbed areas over the study period. This represents an initial sample area of 17,300 ha, which gradually shrinks during the 20 years of activity (i.e., the percentage of Lyell Island undisturbed decreases from 98.9% in 1977 to 81.5% by 1990; see Table 1). Though not an ideal data source (as the areas removed are not random), it contains many areas quite similar to the disturbed zones. The slide rate established, as shown in Figure 6, shows a small, gradual decrease over the study period. To reduce the statistical impact of specific heavy rainfall events, this line has been smoothed using a 5-year average (based on orthogonal polynomials).

The new slide rate, superimposed on Figure 6, shows a considerably different trend when subjected to the same averaging. The rate begins to taper off following the treatment period. Because of a lack of comparative control areas, we are forced to fall back on comparisons with (1) the background natural rate and (2) the theoretical rate. Hammond et al. (1992) summarize studies of stability over time on logged slopes. They conclude that, assuming regeneration occurs immediately, a balance between root decay and root growth will begin to reduce the danger of landslides after 1215 years. This estimated landslide danger (superimposed on Fig. 6, based on yearly logging figures) remains high far into the post-treatment period.

Does this represent general success of the initial restoration? Overall, it appears quite successful. Landslide rates (new slides) have been reduced by a factor of 3, during a period when slide rates theoretically should have increased. Although there was a decrease in activity in the control (natural slide) areas, the treated areas experienced more than twice the decrease observed in the control area despite the fact that they should be far more susceptible to mass movement.

The treatment of slide areas through aerial seeding and road decommissioning has contributed to reducing the expansion rate of existing slides from a high of 2.6 ha/ year in the 19841990 period to less than 0.1 ha/year in the post-treatment period. However, again, there is no control segment for direct comparison, making it impossible to separate out the effects of seeding from those of road decommissioning on these numbers. As noted above, the percentage of slides induced by road cuts actually went up in the post-treatment period. This may be due to other areas stabilizing faster than decommissioned roads, where green-up is delayed due to compaction. This supposition was borne out by qualitative ground observations.

An additional function of the restoration work was to stabilize siltation and direct damage to salmon-bearing streams due to mass wasting (Parks Canada 1987). While the number of slides that directly affect the known salmon streams is small, the upstream effects have been considerable, with up to 85% of all landslides in the period around 1980 directly impacting watercourses. Although this percentage was already on the decline before the treatment, the post-treatment values also decreased in line with the overall slide rate.

A number of other relevant observations were made by crews during the ground survey phase of this study that, while not contributing to the numerical analysis, have additional bearing on restoration success.

Although increases in slide area have been minimal since surface stabilization efforts occurred, there is still the issue of surface erosion. The imagery used in this project did not have sufficient resolution to establish the degree of grass and legume growth on seeded landslides (recent modifications to the system incorporate a wideangle 35 mm camera with the video and would enable such estimates). During the ground-truthing exercise, it was noted that some landslides, though not visibly expanding in area, were being gradually stripped of soil through surface runoff from upslope. Though stable in size, these areas would still produce significant siltation, contributing to stream damage.

The most visibly successful slide-stabilization efforts occurred in experimental areas where aerial hydroseeding was combined with ''biotechnical stabilization'' in the form of Alnus rubra (red alder) planting. Areas with repeated slope failures were rehabilitated in this manner and, after 15 years, all were stable. This expensive and time-consuming restoration technique would be appropriate in the areas subject to soil stripping through erosion.

Waterbar construction may have been somewhat excessive in certain areas (over 1,100 were constructed). Many of the waterbars located on shallow slopes show little evidence of winter water flow, indicating that the placement density may have been too high. On steep slopes, however, most waterbars contained some flow even through a dry August. The apparent stability of these slopes indicates that the combination of seeding and waterbar construction is (likely) successful.

In conclusion, the 1997 update indicates that the initial restoration effort has been successful to that point in time. Given the episodic nature of weather in the Queen Charlotte region, this apparent success will still require monitoring over the next 10 years to ensure that slide rates have returned to their background level. Currently, the stability of the landscape indicates that further restoration efforts would now be justified.

These further efforts, as documented in the original restoration plan (Parks Canada 1987), include the following items in the list of secondary stage restoration tasks:

- (1) Continue slope-stability monitoring;
- (2) Compare site characteristics and evaluate natural vegetation regeneration;
- (3) Determine the effects of the herbivore Odocoileus hemionus sitkensis (Sitka black-tailed deer) browsing on regeneration (introduction of herbivores in this area has affected the balance of native species);
- (4) Begin monitoring siltation levels in streams and begin detailed surveys;
- (5) Start plots in control areas on other islands to compare community structure and monitor recovery.

# ODFS Performance

The oblique data fusion system developed for this study allowed us to perform a restoration database update for less than 1/20th the cost of comparable low-altitude aerial photography (Davis 1999). The update required \$1,100 in helicopter time and 40 hours of technician time, using commonly available hardware (total \$3,500). A single airphoto mission with orthophoto creation for this area (similar useable resolution) was priced at a minimum of \$110,000. Orthocorrected satellite imagery at a similar resolution would range from \$10,000 (IKONOS satellite imagery) to \$15,000 (Quickbird satellite imagery). As noted earlier, both satellite imagery and aerial photography are highly problematic in an area covered with clouds for over 90% of the year.

For an agency with a limited budget, this system made the process of restoration monitoring possible, when it otherwise might be indefinitely delayed. The system was designed with a particular type of task in mind: updates to an existing database on a periodic basis with a userspecified level of accuracy. In concert with other sources of data, such as satellite imagery or existing aerial photography, the system is useful for monitoring fast-changing environments (such as encroachments on the boundary of protected areas, road building, etc.), or for monitoring the details of change over a broad area.

Our system tests indicate that the ODFS can perform with accuracy on the order of the underlying database being updated and, used properly, contributes minimally to data uncertainty. The system is designed to be a lowcost, variable-accuracy update tool, operating in areas of either high data density or considerable topographic relief.

# Conclusions

An evaluation of a large restoration project can be an extremely long-term procedure, particularly in areas where damage extends to the soil and alters the hydrology. We have used the Lyell Island study to develop and evaluate a monitoring tool that, through low cost and ease of data acquisition, enables on-going evaluation of specific types of restoration work. The tool works best in areas of high relief or high existing data density, although performance can be improved in low data density areas by reducing scale (also reducing accuracy). The ODFS depends on an existing spatial database for a baseline to perform the updates, rather than recreating the entire dataset. Because of this limitation, it cannot be used for initial surveys. It also depends upon the accuracy of the existing data and cannot increase the accuracy of the database.

On-going development work includes studying the system's capabilities for performing detailed measurements (e.g., tree heights and buffer sizes) in areas of variable relief and at very fine scales.

In this initial study, data obtained from the system and from archived information indicate that the combination of road deactivation, aerial seeding, and planting used on Lyell Island has reduced the rate of mass wastage over a 7-year period relative to the background rate. Gwaii Haanas National Park/Reserve management plans to continue monitoring the area indefinitely to ensure the full restoration of Lyell Island's ecosystems.

### Acknowledgments

The authors thank the Gwaii Haanas Archipelago Management Board and Parks Canada staff, in particular Todd Golumbia, Debbie Gardiner, Dennie Chretien, and Pat Bartier, for their assistance in the field and in providing data. Data and assistance were also provided by staff from Macmillan Bloedel, Western Forest Products, and the Malcolm Knapp Research Forest. The project was funded in part by Forest Renewal British Columbia (project HQ96078-RE).

### LITERATURE CITED

- Berger, J. J. 1991. A generic framework for evaluating complex restoration and conservation projects. Environmental Professional 13:254262.
- Blakemore, M. 1983. Generalization and error in spatial databases. Cartographica 21:131139.
- Davis, T. J. 1999. Toward verification of a natural resource uncertainty model. Ph.D. dissertation. Department of Geography, University of British Columbia, Vancouver.
- Ecosat Geobotanical Surveys. 1989. Forest harvesting activities and LANDSAT Thematic Mapper analysis of Lyell Island. Report, submitted to Parks Canada, Queen Charlotte City, British Columbia.
- Estep, K. W., F. MacIntyre, and T. T. Noji. 1994. Seal sizes and habitat conditions assessed from aerial photography and video analysis. International Council for the Exploration of the Sea Journal of Marine Science 51:253261.
- Everitt, J. H., D. E. Escobar, and F. W. Judd. 1991. Evaluation of airborne video imagery for distinguishing black mangrove (Avicennia germinans) on the Lower Texas Gulf Coast. Journal of Coastal Research 7:11691173.
- Gobin, A., P. Campling, and J. Feyen. 2001. Spatial analysis of rural land ownership. Landscape and Urban Planning 55:185194.
- Golumbia, T. E. 2001. Classification of plant communities in Gwai Haanas National Park Reserve and Haida Heritage Site. M.Sc. Thesis. Department of Forest Sciences, University of British Columbia, Vancouver.
- Government of Canada. 2000. National Parks Act. Statutes of Canada 2000. Chapter 32. Ottawa, Canada.
- Graham, L. A. 1993. Airborne video for near-real-time vegetation mapping. Journal of Forestry 91:2834.
- Hammond, C., D. Hall, S. Miller, and P. Swetik. 1992. Level I stability analysis documentation. Intermountain Research Station. General Technical Report INT-285. United States Forest Service Department of Agriculture, Ogden, Utah.

- Hearnshaw, H. M., and D. J. Unwin, editors. 1994. Visualization in geographical information systems. Wiley, New York.
- Hobbs, J. R., and D. A. Norton. 1996. Towards a conceptual framework for restoration ecology. Restoration Ecology 4:93100.
- Howes, D., J. Harper, and E. Owens. 1994. British Columbia physical shore-zone mapping system. Resources Inventory Committee, Victoria, British Columbia.
- Johnston, D. 1987. Greening the leftthe fight for Lyell Island. New Internationalist 171:6571.
- Josenhans, H. W., D. W. Fedje, K. W. Conway, and J. V. Barrie. 1995. Post glacial sea levels on the Western Canadian continental shelf: evidence for rapid change, extensive subaerial exposure, and early human habitation. Marine Geology 125:7394.
- Majer, J. D. 1989. Animals in primary succession: the role of fauna in reclaimed lands. Cambridge University Press, Cambridge, United Kingdom.
- McLachlan, S. M., and D. R. Bazely. 2001. Recovery patterns of understory herbs and their use as indicators of deciduous forest regeneration. Conservation Biology 15:98110.
- Parks Canada. 1987. Lyell Island restoration terms of reference. Internal Parks Canada Report, Queen Charlotte City, British Columbia.
- Parks Canada. 1994. Parks Canada guiding principles and operational policies. Minister of Supply and Services, Ottawa Canada.
- Phinn, S. R., D. A. Stow, and J. B. Zedler. 1996. Monitoring wetland restoration using airborne multispectral video data in southern California. Restoration Ecology 4:412422.
- Reay, S. D., and D. A. Norton. 1999. Assessing the success of restoration plantings in a temperate New Zealand forest. Restoration Ecology 7:298308.
- Slaymaker, D. M., K. M. L. Jones, C. R. Griffin, and J. T. Finn. 1996. Mapping deciduous forests in southern New England using aerial videography and hyperclustered multi-temporal LANDSAT TM imagery. Pages 87101 in J. M. Scott, T. H. Tear, and F. W. Davis, editors. Gap analysis: a landscape approach to biodiversity planning. American Society for Photogrammetry and Remote Sensing, Bethesda, Maryland.
- Smeeton, C., and K. Weagle. 2000. The reintroduction of the swift fox Vulpes velox to South Central Saskatchewan, Canada. Oryx 34:171179.
- Uenohara, M., and T. Kanade. 1995. Vision-based object registration for real-time image overlay. Computers in Biology and Medicine 25:249.