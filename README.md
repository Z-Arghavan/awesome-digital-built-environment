# Awesome Digital Built Environment

A curated list of tools, standards, research groups, datasets, and platforms shaping the digital transformation of the built environment.

To add something to the list please either submit a pull request or submit your request in issues.

Topics include (and not limited to):

- BIM and openBIM
- Digital twins
- Ontologies and knowledge graphs
- Robotics and automation
- Smart cities
- Simulation and analytics
- AI for construction
- Data standards and interoperability

The goal is to provide a technical reference map of the digital built environment ecosystem. 

---

# Contents

* Open-source tools
* Proprietary and closed tools
* Ontologies and knowledge graphs
* Graph databases and data infrastructure
* Digital twin frameworks
* Robotics and AI for construction
* Standards and specifications
* Research groups and communities
* Conferences and workshops
* Datasets and benchmarks
* Learning resources

---

# Open-source tools

## Building modelling and BIM

* **IfcOpenShell** – Open-source IFC toolkit and geometry engine for working with BIM models.
* **BHoM** – Interoperability framework for sharing built-environment data.
* **Topologic** – Topological spatial modelling software for representing building spaces and relationships.
* **Rhino.Compute** – API enabling remote execution of Rhino and Grasshopper models.
* **Hypar** – Generative design platform for parametric BIM workflows.

---
## IFC tools

### Viewers – desktop (free)

* [Bonsai / BlenderBIM](https://bonsaibim.org/) – open-source BIM authoring and viewing environment built on Blender. Already listed above.
* [xBIM Xplorer](https://xbim.net/xbim-xplorer/) – free and open-source IFC viewer written in C#, with stand-alone and web versions. Demonstrates the capabilities of the xBIM Toolkit.
* [FZK Viewer](https://www.iai.kit.edu/english/1648.php) – developed by Karlsruhe Institute of Technology (KIT); good at displaying IFC data that other viewers skip.
* [BIMvision](https://bimvision.eu/) – freeware IFC viewer supporting IFC 2×3 and 4.0, with a plugin interface. Not open-source.
* [Open IFC Viewer](https://openifcviewer.com/) – free professional-grade viewer by the Open Design Alliance, supporting IFC 2x3 to 4.1 with clash detection and validation. Not open-source.
* [Solibri Anywhere](https://www.solibri.com/solibri-anywhere) – free registration-required viewer; widely regarded as the benchmark IFC viewer for quality checking. Not open-source.
* [BIMcollab ZOOM](https://www.bimcollab.com/en/go/free-ifc-viewer/) – free viewer with smart views, dynamic filtering, BCF issue management, and point cloud support. Not open-source.
* [Dalux BIM Viewer](https://www.dalux.com/bim-viewer/) – free IFC viewer with desktop and mobile support.

### Viewers – web / browser (free)

* [That Open / IFC.js](https://ifcjs.github.io/info/) – open-source browser-based IFC viewer and toolkit built on Three.js, with clipping planes, 2D plan generation, and dimensions.
* [web-ifc-viewer](https://github.com/ThatOpen/web-ifc-viewer) – extension of web-ifc-three; provides a full API for building BIM tools in the browser.
* [xeokit BIM Viewer](https://github.com/xeokit/xeokit-bim-viewer) – open-source WebGL viewer built on the xeokit SDK; supports IFC, point clouds, and double-precision coordinates.
* [Flinker IFC Viewer](https://viewer.flinker.app/) – free browser viewer with fully local processing (no upload), supporting IFC 2x3/4/4x3, BCF 2.1/3, and IDS 1.0 validation.
* [Sortdesk IFC Viewer](https://viewer.sortdesk.com/) – free browser-based viewer with built-in IDS rule editor.

### Parsers and SDKs

* [IfcOpenShell](https://ifcopenshell.org/) – the primary open-source IFC toolkit and geometry engine, supporting Python and C++. Supports IFC2X3, IFC4, IFC4X3.
* [web-ifc](https://github.com/ThatOpen/engine_web-ifc) – WebAssembly-based IFC parser in JavaScript for reading and writing IFC files at native speed. Foundation of IFC.js.
* [xBIM Toolkit](https://docs.xbim.net/) – open-source .NET toolkit for reading, creating, and viewing IFC files, with geometry engine and COBie support.
* [IfcPlusPlus](https://github.com/ifcquery/ifcplusplus) – C++ library for reading and writing IFC files, with an OpenSceneGraph-based viewer.
* [IFC.js / web-ifc-three](https://github.com/ThatOpen/engine_three-ifc) – official IFC loader for Three.js.
* [GeometryGym](https://github.com/jmirtsch/GeometryGym) – C# library for generating and parsing IFC and other open BIM standards.

### Validators and quality checking

* [buildingSMART Validation Service](https://validate.buildingsmart.org/) – official online IFC validator by buildingSMART.
* [IfcDoc](https://github.com/buildingSMART/IfcDoc) – tool for documenting and validating IFC schemas; used to author the official IFC specification.
* [IDS (Information Delivery Specification)](https://github.com/buildingSMART/IDS) – buildingSMART standard for defining and checking model requirements; supported by several validators above.

### Converters and pipelines

* [IfcConvert](https://ifcopenshell.org/ifcconvert) – command-line tool (part of IfcOpenShell) for converting IFC to OBJ, DAE, GLB, SVG, and more.
* [IFC2CA](https://github.com/KC-Lab/IFC2CA) – converts IFC structural models for use in structural analysis tools.
* [IFC to CityGML](https://github.com/tum-gis/ifc2citygml) – converts IFC building models to CityGML format.

---

## Data layer

Core data structures and models used to represent the built environment.

* [Industry Foundation Classes (IFC)](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/) – open BIM data model.
* [CityGML](https://www.ogc.org/standard/citygml/) – standard for 3D city models.
* [IndoorGML](https://www.ogc.org/standard/indoorgml/) – indoor spatial information model.
* [buildingSMART Data Dictionary (bSDD)](https://www.buildingsmart.org/standards/bsi-standards/bsdd/) – standardized terminology and properties.


## Application layer

# Proprietary and closed tools

## BIM and CAD platforms

* [Autodesk Revit](https://www.autodesk.com/products/revit/) – widely used BIM authoring platform with extensible APIs.
* [Autodesk AutoCAD](https://www.autodesk.com/products/autocad/) – widely used CAD platform with extensible APIs.
* [Bentley iTwin](https://www.bentley.com/platform/itwin/) – infrastructure and digital twin platform.
* [Graphisoft Archicad](https://graphisoft.com/solutions/archicad) – BIM platform with developer extensions.
* [Trimble Tekla](https://www.tekla.com/) – structural BIM platform.
* [Nemetschek Allplan](https://www.allplan.com/) – BIM platform for architecture and engineering.
* [Dassault CATIA](https://www.3ds.com/products-services/catia/) – CAD and BIM platform for complex projects.
* [Autodesk Civil 3D](https://www.autodesk.com/products/civil-3d/) – civil engineering design software.
* [Autodesk InfraWorks](https://www.autodesk.com/products/infraworks/) – infrastructure design and visualization platform.
* [Autodesk Navisworks](https://www.autodesk.com/products/navisworks/) – project review and clash detection software.
* [Autodesk BIM 360](https://www.autodesk.com/bim-360/) – cloud-based construction management platform.
* [Autodesk Forge](https://forge.autodesk.com/) – cloud platform for building custom applications and integrations.* [Bentley OpenBuildings](https://www.bentley.com/en/products/brands/openbuildings) – building design and analysis software.
* [Bentley OpenRoads](https://www.bentley.com/en/products/brands/openroads) – road design and analysis software.
* [Bentley OpenRail](https://www.bentley.com/en/products/brands/openrail) – rail design and analysis software.
* [Bentley OpenBridge](https://www.bentley.com/en/products/brands/openbridge) – bridge design and analysis software.
* [Bentley OpenUtilities](https://www.bentley.com/en/products/brands/openutilities) – utility network design and analysis software. 
* [Bentley OpenFlows](https://www.bentley.com/en/products/brands/openflows) – water infrastructure design and analysis software.

## Digital twin platforms

* [Azure Digital Twins](https://azure.microsoft.com/en-us/products/digital-twins)
* [Oracle IoT Digital Twin](https://docs.oracle.com/en/cloud/paas/iot-cloud/)
* [Dassault 3DEXPERIENCE](https://www.3ds.com/3dexperience)
* [Bentley iTwin Platform](https://www.bentley.com/platform/itwin)

## Simulation and analysis

* [EnergyPlus](https://energyplus.net/) – building energy simulation.
* [OpenStudio](https://www.openstudio.net/) – energy modelling platform.
* [ANSYS](https://www.ansys.com/) – engineering simulation.

  
# Open-source tools

## Building modelling and BIM
Tools used to create, manipulate, and analyse digital built environment models.

* [IfcOpenShell](https://ifcopenshell.org/) – Open-source IFC toolkit and geometry engine for working with BIM models.
* [BHoM](https://github.com/BHoM/BHoM) – Interoperability framework for sharing built-environment data.
* [Topologic](https://topologic.app/) – Topological spatial modelling software for representing building spaces and relationships.
* [Rhino.Compute](https://compute.rhino3d.com/) – API enabling remote execution of Rhino and Grasshopper models.
* [Hypar](https://hypar.io/) – Generative design platform for parametric BIM workflows.
* [BlenderBIM / Bonsai](https://bonsaibim.org/) – Open-source BIM authoring environment built on Blender.
* [FreeCAD BIM Workbench](https://wiki.freecad.org/BIM_Workbench) – Open BIM modelling tools for FreeCAD.

## BIM and CAD platforms

* **Autodesk Revit** – widely used BIM authoring platform with extensible APIs.
* **Bentley OpenBuildings / iTwin** – infrastructure and digital twin platform.
* **Graphisoft Archicad** – BIM platform with developer extensions.
* 

Systems for integrating data, simulation, and monitoring of built assets.

* [Eclipse Ditto](https://www.eclipse.org/ditto/) – open digital twin framework.
* [Azure Digital Twins](https://azure.microsoft.com/en-us/products/digital-twins) – cloud-based digital twin platform.
* [Asset Administration Shell](https://industrialdigitaltwin.org/) – digital twin standard for Industry 4.0.

## Simulation and analysis



---

## Ontologies
- [BE-OLS](https://cyberbuildlab.github.io/BE-OLS/) - Built Environment Ontology Lookup Service
- [LOV](https://lov.linkeddata.es/dataset/lov/) - Linked Open Vocabularies


---
# Data spaces

Architectures and platforms for **secure and interoperable data sharing across organisations**.
Data spaces are increasingly used for **built environment, smart city, and industrial digital twin ecosystems**.

## Frameworks and architectures

* [International Data Spaces (IDS)](https://internationaldataspaces.org/) – reference architecture for secure data exchange between organisations.
* [GAIA-X](https://gaia-x.eu/) – European initiative for federated cloud and data infrastructure.
* [Eclipse Dataspace Components](https://github.com/eclipse-edc) – open-source implementation of the IDS architecture.
* [FIWARE Data Spaces](https://www.fiware.org/data-spaces/) – open ecosystem supporting domain-specific data spaces.

## Domain data space initiatives

* [Manufacturing-X](https://www.manufacturing-x.de/) – industrial data space initiative.
* [Mobility Data Space](https://mobility-dataspace.eu/) – European data-sharing ecosystem for mobility.
* [Catena-X](https://catena-x.net/) – automotive data space ecosystem.
* [Built Environment Data Spaces (emerging initiatives)] – data sharing infrastructures for construction and infrastructure sectors.
  
---
# Graph databases and data infrastructure


## Graph databases and RDF triple stores

* [GraphDB](https://graphdb.ontotext.com/) – knowledge graph database.
* [Neo4j](https://neo4j.com/) – graph database.
* [Apache Jena](https://jena.apache.org/) – RDF framework and triple store.

  
## Spatial and relational databases

* **PostgreSQL / PostGIS**

---

# Digital twin 


---

# Robotics and AI for construction

* tbc


---

# Standards and specifications

## Standards

* [BIM Standards Landscape Explorer](https://ec-3.org/BIM-Standards-Landscape-Explorer.html)
* [buildingSMART standards](https://www.buildingsmart.org/standards/)
* [IFC](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/)
* [OGC standards](https://www.ogc.org/standards) – including CityGML, IndoorGML, and 3D Tiles.

## Semantic Web standards

* [RDF](https://www.w3.org/RDF/)
* [RDFS](https://www.w3.org/TR/rdf-schema/)
* [OWL](https://www.w3.org/OWL/)
* [SHACL](https://www.w3.org/TR/shacl/)
* [SPARQL](https://www.w3.org/TR/sparql11-query/)

---

# Research groups and communities

* [Information Systems in the Built Environment](https://isbe.bwk.tue.nl/) - Research group @ Eindhoven University of Technology (TU/e), The Netherlands

---

# Conferences and workshops

# Conferences and workshops

Known conferences and workshops related to **digital construction, BIM, digital twins, AI and semantic technologies for the built environment**.

## Digital construction and BIM

* [CIB W78 – Information Technology in Construction](https://www.cibw78.org/) – leading conference on digital technologies for construction.
* [EC3 – European Conference on Computing in Construction](https://ec-3.org/) – major European conference on computational approaches in construction.
* [ASCE International Conference on Computing in Civil Engineering](https://www.asce.org/cce) – conference on computing applications in civil engineering.
* [eCAADe – Education and Research in Computer Aided Architectural Design in Europe](https://ecaade.org/) – conference on computational design and digital architecture.
* [CAAD Futures](https://caadfutures.org/) – international conference on computer-aided architectural design.
* [ISARC – International Symposium on Automation and Robotics in Construction](https://www.isarc.org/) – flagship conference on robotics in construction.
* [IEEE CASE](https://ieee-ras.org/conferences-workshops/fully-sponsored/case) – IEEE conference on automation science and engineering.
* [LDAC – Linked Data in Architecture and Construction](http://www.linkedbuildingdata.net/ldac/) – workshop on semantic web technologies in the built environment.
* [SEMANTiCS Conference](https://2024-eu.semantics.cc/) – conference on semantic technologies and knowledge graphs.
* [Digital Twin Consortium Events](https://www.digitaltwinconsortium.org/) – workshops and conferences on digital twin technologies.
* [TwinArch – Digital Twin Architecture Workshop](https://www.iese.fraunhofer.de/en/twinarch.html) – workshop on digital twin architectures.
* [ACM BuildSys](https://buildsys.acm.org/) – conference on systems for smart buildings and cities.
* [IEEE Smart Cities](https://smartcities.ieee.org/) – conference series on smart city technologies.
* [TUM GNI Symposium 2026](https://events.gni.tum.de/ai-symposium-2026/) – symposium on digital transformation in the built environment organized by TUM.
* [ICSA2027 - 7th International Conference on Structures and Architecture](https://www.linkedin.com/company/icsa-2027-milano/)


##National Conferences and Workshops

* [UK BIM Conference](https://www.ukbimconference.com/) – annual conference on BIM in the UK.
* [BIM World](https://www.bim-world.com/) – global conference with regional editions in Europe, Asia, and the Americas.
* [AIA Conference on Architecture](https://conferenceonarchitecture.com/) – major US conference on architecture and design, including digital technologies.
* [BILT Conference](https://bilt-conference.com/) – conference on BIM and digital construction with global editions.
* [BIM Forum](https://bimforum.org/) – annual conference on BIM in the US.
* [BIM Nordic](https://bimnordic.com/) – conference on BIM in the Nordic countries.
* [BIM Summit](https://bimsummit.es/) – annual conference on BIM in Spain.
* [BIM World Munich](https://www.bim-world.com/munich/) – conference on BIM and digital construction in Germany.
* [BIM World Paris](https://www.bim-world.com/paris/) – conference on BIM and digital construction in France.
* [Digital Construction Week](https://www.digitalconstructionweek.com/) – UK-based conference on digital construction technologies.
* [Smart Building Conference](https://www.smartbuildingconference.com/) – conference on smart building technologies in the US.
* [Smart Cities Expo World Congress](https://www.smartcityexpo.com/) – global conference on smart city technologies.
* [Smart City Expo](https://www.smartcityexpo.com/) – conference on smart city technologies in Spain.
* [4TU-14UAS Research Day on Digitalisation of the Built Environment](https://www.4tu.nl/agenda/5th-research-day-on-digitalization/) – workshop on digitalisation in the built environment organized by 4TU and 14UAS in the Netherlands.






---

# Inititives ans societies
- [BIMe](https://bimexcellence.org/) - BIM Excellence Initiative
- [CIB – International Council for Research and Innovation in Building and Construction](https://www.cibworld.org/) - global network of researchers and practitioners in the built environment
- [Modelling & Standards committee](https://ec-3.org/governance/technical-committees/modelling-standards-committee/) - a permanent committee of the EC3
- [BuildingSMART International Ltd](https://www.buildingsmart.org/) - international organization developing open BIM standards
- [Digital Twin Consortium](https://www.digitaltwinconsortium.org/) - global ecosystem for digital twin technologies
- [International Data Spaces Association](https://internationaldataspaces.org/) - organization promoting secure data exchange through data spaces
- 
-


# Datasets and benchmarks

* [Example IFC Files Dataset](https://www.kaggle.com/datasets/claytonmiller/example-ifc-file) – collection of IFC models used in BIM tutorials
* [BIMData IFC dataset](https://github.com/bimdata/BIMData-Research-and-Development/blob/master/pages/IFC_FILES.md) – collection of IFC models for development and testing
* [BuildingSmart IFC Datasets](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/ifc-datasets/) – BIM model datasets in IFC format
* [IFCNet](https://ifcnet.e3d.rwth-aachen.de/) – BIM model dataset for machine learning
* [IfCBench](https://huggingface.co/datasets/sylvainHellin/ifc-bench) – benchmark dataset for IFC-based machine learning
* [BuildingNet](https://buildingnet.org/) – building model dataset for machine learning
* [ArchShapesNet](https://i3l.seoultech.ac.kr/subList/20000005729) – BIM elements dataset for deep learning classification of building components
* [3DFacilities Dataset](https://www.sciencedirect.com/science/article/pii/S0926580524002942) – dataset of structural and MEP BIM elements for research
* [Microsoft Global Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) – dataset of building footprints extracted from satellite imagery
* [Global Building Atlas](https://arxiv.org/abs/2506.04106) – global dataset of building footprints and heights
* [Habitat-Matterport 3D (HM3D)](https://aihabitat.org/datasets/hm3d/) – dataset of indoor environments used for embodied AI and robotics research
* [Brick Building Dataset](https://brickschema.org/resources/) – datasets for building systems modelling using the Brick ontology
* [Open IFC Model Repository](https://github.com/opensourceBIM/TestFiles) – IFC test files for openBIM development
* [xBIM Toolkit Examples](https://github.com/xBimTeam/XbimSamples) – BIM models used for xBIM development and tutorials
* [BIM-NLQ Dataset for NLQ4BIM]https://github.com/MengtianYin/BIM-NLQI)
* [Dataset Schependomlaan](https://github.com/jakob-beetz/DataSetSchependomlaan) - IFC dataset for a residential building in the Netherlands
* [BIM Whale](https://github.com/andrewisen/bim-whale-ifc-samples?tab=readme-ov-files) - a collection of IFC sample files for the BIM Whale project
* [The nation-scale fine-GrAined 3D BuiLding modEl (GABLE)](https://github.com/AICyberTeam/GABLE) - large-scale building model dataset for machine learning (Beijing, China)
* [Awesome CityGML](https://github.com/OloOcki/awesome-citygml) – curated list of CityGML datasets and resources of different cities
* [3D City Database](https://github.com/3dcitydb/3dcitydb) - open-source database for storing and managing 3D city models with example datasets
* [Open City Mdodel](https://github.com/opencitymodel/opencitymodel) - an initiative to provide open cityGML data for all the buildings in the USA
* [Ifc Sample files](https://github.com/youshengCode/IfcSampleFiles) – sample IFC files for testing and benchmarking
* [Tokyo SpatialID Dataset](https://github.com/tlab-wide/SpatialID) - large-scale csv dataset for Tokyo, Japan
* [Polygon City Berlin](https://github.com/polygon-city/polygon-city-berlin-export) - CityGML dataset for Berlin, Germany
* [Matterport3D](https://niessner.github.io/Matterport/) – indoor scanning dataset
* [Stanford Computational and Geometry Lab Vision](https://cvgl.stanford.edu/resources.html) – several datasets
* [KITTI](http://www.cvlibs.net/datasets/kitti/) – autonomous driving dataset with 3D point clouds
* [ModelNet](http://modelnet.cs.princeton.edu/) – 3D CAD model dataset
* [ShapeNet](https://www.shapenet.org/) – large-scale 3D model dataset
* [ScanNet](http://www.scan-net.org/) – 3D scene dataset
* [S3DIS](http://buildingparser.stanford.edu/dataset.html) – indoor scene dataset
* [NIST IFC Repository](https://www.nist.gov/services-resources/software/ifc) – BIM model datasets
* [3D Warehouse](https://3dwarehouse.sketchup.com/) – 3D model repository with many building models
* [CityGML 3D City Model Repository](https://www.ogc.org/standards/citygml#datasets) – repository of 3D city models in CityGML format
* [3D Tiles](https://github.com/CesiumGS/3d-tiles) – 3D geospatial data format with example datasets
* [Semantic3D](http://www.semantic3d.net/) – large-scale outdoor LiDAR point cloud dataset
* [Toronto3D](https://github.com/WeikaiTan/Toronto-3D) – mobile LiDAR dataset for urban environments
* [Paris-Lille-3D](https://npm3d.fr/paris-lille-3d) – urban LiDAR dataset with semantic labels
* [DALES](https://udayton.edu/engineering/centers/vision_lab/research/dales.php) – aerial LiDAR dataset for urban object segmentation
* [Structured3D](https://structured3d-dataset.org/) – large-scale dataset of synthetic indoor scenes with detailed room layouts
* [InteriorNet](https://interiornet.org/) – photorealistic dataset for indoor scene understanding
* [Replica Dataset](https://github.com/facebookresearch/Replica-Dataset) – high-quality 3D indoor environments for robotics and AIns
* [OpenStreetMap](https://www.openstreetmap.org/) – global open geospatial dataset
* [Microsoft Global Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) – global building footprint dataset
* [Google Open Buildings Dataset](https://sites.research.google/open-buildings/) – large-scale building footprint dataset derived from satellite imagery
* [Urban Atlas](https://land.copernicus.eu/en/products/urban-atlas) – European land-use and urban spatial dataset
* [NYC Open Data](https://opendata.cityofnewyork.us/) – large collection of urban infrastructure datasets
* [SemanticKITTI](http://semantic-kitti.org/) – LiDAR dataset with semantic annotations
* [AHN3 / AHN4](https://www.ahn.nl/) – Dutch national LiDAR dataset
* [USGS 3D Elevation Program](https://www.usgs.gov/3d-elevation-program) – national LiDAR datasets for the United States
* [OpenTopography](https://opentopography.org/) – repository of LiDAR datasets
* [Building Change Detection Dataset](https://study.rsgis.whu.edu.cn/pages/download/building_dataset.html) – dataset for monitoring construction and urban change
* [SpaceNet Building Dataset](https://github.com/spacenetchallenge) – satellite imagery dataset for building detection
* [Inria Aerial Image Labeling Dataset](https://project.inria.fr/aerialimagelabeling/) – aerial imagery dataset with building annotation
* [ASHRAE Great Energy Predictor Dataset](https://www.kaggle.com/c/ashrae-energy-prediction) – dataset for building energy prediction
* [Building Data Genome Project](https://github.com/buds-lab/building-data-genome-project-2) – large dataset of building energy consumption
* [Construction Site Image Dataset](https://github.com/pangyuteng/construction-site-image-dataset) – construction site image dataset for computer vision
* [Open Construction Dataset](https://github.com/ruoxinx/OpenConstruction-Datasets) – dataset for construction scene understanding
* [Building Change Detection Dataset](https://study.rsgis.whu.edu.cn/pages/download/building_dataset.html) – dataset for detecting construction changes from aerial imagery
* [Open Transport Data](https://data.europa.eu/data/datasets?query=transport) – European transportation datasets
* [OpenTraffic](https://opentraffic.io/) – traffic and mobility datasets
* [Uber Movement](https://www.kaggle.com/datasets/ishandutta/uber-travel-movement-data-2-billion-trips) – urban mobility datasets for cities worldwide
* [Google Open Building](https://sites.research.google/gr/open-buildings/) – large-scale building footprint dataset derived from satellite imagery
* [Inria Aerial Image Labeling Dataset](https://project.inria.fr/aerialimagelabeling/) – aerial imagery dataset with building annotations
* [DeepGlobe Building Dataset](https://deepglobe.org/challenge.html) – satellite dataset for building extraction
* [xView Dataset](https://xviewdataset.org/) – satellite imagery dataset for object detection including buildings
* [ABC Dataset (Architecture, Buildings, Construction)](https://deep-geometry.github.io/abc-dataset/) – large dataset of CAD models used for geometric deep learning
* [Natural Earth](https://www.naturalearthdata.com/) – public domain map dataset
* [Copernicus Urban Atlas](https://land.copernicus.eu/en/products/urban-atlas) – European urban land use, buiding height, trees
* [Eurostat GISCO datasets](https://ec.europa.eu/eurostat/web/gisco/geodata) – European geospatial datasets
* [Global Human Settlement Layer (GHSL)](https://human-settlement.emergency.copernicus.eu/GHSLWeGenerateData.php) – global dataset describing human settlements
* [SmartSantander Dataset](https://github.com/Predictia/smartsantander) – IoT sensor data for smart city experiments
* [Array of Things Sensor Dataset](https://github.com/waggle-sensor/waggle/blob/master/data/README.md) – urban sensor network dataset
* [CityPulse Dataset](https://iot.ee.surrey.ac.uk:8080/datasets.html) – smart city IoT data streams
* [Urban Observatory Newcastle](https://urbanobservatory.ac.uk/) – large urban sensor dataset
* [Open Power System Data](https://open-power-system-data.org/) – energy infrastructure datasets
* [IDEAS Building Energy Dataset](https://github.com/open-ideas/IDEAS) – building energy modelling datasets
---

# Learning resources

## Books

## Courses

* BIM and digital twin courses on **Coursera** and **edX**


---

# Contributing

Contributions are welcome.

To contribute:

1. Ensure the resource fits one of the categories above.
2. Provide a short description.
3. Link directly to the official source.
4. Submit a pull request. (Please :D )

---

# License

This repository follows the structure of the **awesome-list ecosystem** and is open for community contributions.
