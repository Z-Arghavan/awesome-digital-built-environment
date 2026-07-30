# Awesome Digital Built Environment [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of tools, standards, research groups, datasets, and platforms shaping the digital transformation of the built environment.

Topics include (and are not limited to): BIM and openBIM, digital twins, ontologies and knowledge graphs, robotics and automation, smart cities, simulation and analytics, AI for construction, and data standards and interoperability. The goal is to provide a technical reference map of the digital built environment ecosystem.

To add something to the list, please submit a pull request or open an issue.

## Contents

- [BIM and IFC tools](#bim-and-ifc-tools)
  - [Desktop viewers](#desktop-viewers)
  - [Web and browser viewers](#web-and-browser-viewers)
  - [Parsers and SDKs](#parsers-and-sdks)
  - [Validators and quality checking](#validators-and-quality-checking)
  - [Converters and pipelines](#converters-and-pipelines)
- [Building modelling and design](#building-modelling-and-design)
- [BIM and CAD platforms](#bim-and-cad-platforms)
- [Digital twin platforms](#digital-twin-platforms)
- [Simulation and analysis](#simulation-and-analysis)
- [Point cloud and scan-to-BIM](#point-cloud-and-scan-to-bim)
- [GIS and geospatial tools](#gis-and-geospatial-tools)
- [Data layer and standards](#data-layer-and-standards)
- [Ontologies and knowledge graphs](#ontologies-and-knowledge-graphs)
- [Graph databases and data infrastructure](#graph-databases-and-data-infrastructure)
- [Data spaces](#data-spaces)
- [Robotics and AI for construction](#robotics-and-ai-for-construction)
- [Standards and specifications](#standards-and-specifications)
- [Research groups and communities](#research-groups-and-communities)
- [Conferences and workshops](#conferences-and-workshops)
- [Initiatives and societies](#initiatives-and-societies)
- [Datasets and benchmarks](#datasets-and-benchmarks)
- [Learning resources](#learning-resources)

---

## BIM and IFC tools

### Desktop viewers

- [Bonsai / BlenderBIM](https://bonsaibim.org/) - Open-source BIM authoring and viewing environment built on Blender.
- [xBIM Xplorer](https://xbim.net/xbim-xplorer/) - Free, open-source IFC viewer written in C#, with stand-alone and web versions.
- [FZK Viewer](https://www.iai.kit.edu/english/1648.php) - Developed by Karlsruhe Institute of Technology (KIT); displays IFC data that other viewers often skip.
- [BIMvision](https://bimvision.eu/) - Freeware IFC viewer supporting IFC 2x3 and 4.0, with a plugin interface. Not open-source.
- [Open IFC Viewer](https://openifcviewer.com/) - Free professional-grade viewer by the Open Design Alliance, supporting IFC 2x3 to 4.1 with clash detection and validation. Not open-source.
- [Solibri Anywhere](https://www.solibri.com/solibri-anywhere) - Free registration-required viewer, widely regarded as a benchmark for IFC quality checking. Not open-source.
- [BIMcollab ZOOM](https://www.bimcollab.com/en/go/free-ifc-viewer/) - Free viewer with smart views, dynamic filtering, BCF issue management, and point cloud support. Not open-source.
- [Dalux BIM Viewer](https://www.dalux.com/bim-viewer/) - Free IFC viewer with desktop and mobile support.

### Web and browser viewers

- [That Open / IFC.js](https://ifcjs.github.io/info/) - Open-source browser-based IFC viewer and toolkit built on Three.js, with clipping planes, 2D plan generation, and dimensions.
- [web-ifc-viewer](https://github.com/ThatOpen/web-ifc-viewer) - Extension of web-ifc-three, providing a full API for building BIM tools in the browser.
- [xeokit BIM Viewer](https://github.com/xeokit/xeokit-bim-viewer) - Open-source WebGL viewer built on the xeokit SDK; supports IFC, point clouds, and double-precision coordinates.
- [Flinker IFC Viewer](https://viewer.flinker.app/) - Free browser viewer with fully local processing (no upload), supporting IFC 2x3/4/4x3, BCF 2.1/3, and IDS 1.0 validation.
- [Sortdesk IFC Viewer](https://viewer.sortdesk.com/) - Free browser-based viewer with a built-in IDS rule editor.
- [Share](https://github.com/bldrs-ai/Share) - Browser-based BIM and CAD viewer and collaboration platform supporting IFC, STEP, STL, OBJ, and GLTF.
- [BIMsurfer](https://github.com/opensourceBIM/BIMsurfer) - WebGL viewer for IFC models.
- [bim-viewer](https://github.com/thingraph/bim-viewer) - WebGL-based BIM viewer built on three.js and Vue, viewing glTF, IFC, OBJ, DAE, and STL models.

### Parsers and SDKs

- [IfcOpenShell](https://ifcopenshell.org/) - The primary open-source IFC toolkit and geometry engine, supporting Python and C++, with IFC2X3, IFC4, and IFC4X3.
- [web-ifc](https://github.com/ThatOpen/engine_web-ifc) - WebAssembly-based IFC parser in JavaScript for reading and writing IFC files at native speed; foundation of IFC.js.
- [xBIM Toolkit](https://docs.xbim.net/) - Open-source .NET toolkit for reading, creating, and viewing IFC files, with a geometry engine and COBie support.
- [IfcPlusPlus](https://github.com/ifcquery/ifcplusplus) - C++ library for reading and writing IFC files, with an OpenSceneGraph-based viewer.
- [IFC.js / web-ifc-three](https://github.com/ThatOpen/engine_three-ifc) - Official IFC loader for Three.js.
- [GeometryGym](https://github.com/jmirtsch/GeometryGym) - C# library for generating and parsing IFC and other openBIM standards.
- [xeokit-sdk](https://github.com/xeokit/xeokit-sdk) - Open-source WebGL-based 3D BIM/IFC viewer SDK for AEC applications, with real-world coordinates and double precision.
- [ifc-lite](https://github.com/LTplus-AG/ifc-lite) - Parse, view, query, edit, and export IFC, IDS, BCF, and point clouds in the browser, server, or desktop.

### Validators and quality checking

- [buildingSMART Validation Service](https://validate.buildingsmart.org/) - Official online IFC validator by buildingSMART.
- [IfcDoc](https://github.com/buildingSMART/IfcDoc) - Tool for documenting and validating IFC schemas; used to author the official IFC specification.
- [IDS (Information Delivery Specification)](https://github.com/buildingSMART/IDS) - BuildingSMART standard for defining and checking model requirements; supported by several validators above.

### Converters and pipelines

- [IfcConvert](https://ifcopenshell.org/ifcconvert) - Command-line tool (part of IfcOpenShell) for converting IFC to OBJ, DAE, GLB, SVG, and more.
- [IFC2CA](https://github.com/KC-Lab/IFC2CA) - Converts IFC structural models for use in structural analysis tools.
- [IFC to CityGML](https://github.com/tum-gis/ifc2citygml) - Converts IFC building models to CityGML format.
- [ifc-pipeline](https://github.com/AECgeeks/ifc-pipeline) - Processing queue and front-end for visualizing BIM models, built with IfcOpenShell, Docker Compose, and Flask.
- [xeokit-convert](https://github.com/xeokit/xeokit-convert) - Converts various AEC model formats for efficient viewing in the browser with xeokit.

---

## Building modelling and design

- [BHoM](https://github.com/BHoM/BHoM) - Interoperability framework for sharing built-environment data.
- [Topologic](https://topologic.app/) - Topological spatial modelling software for representing building spaces and relationships.
- [Rhino.Compute](https://compute.rhino3d.com/) - API enabling remote execution of Rhino and Grasshopper models.
- [Hypar](https://hypar.io/) - Generative design platform for parametric BIM workflows.
- [FreeCAD BIM Workbench](https://wiki.freecad.org/BIM_Workbench) - Open BIM modelling tools for FreeCAD.
- [Dynamo](https://github.com/DynamoDS/Dynamo) - Open-source graphical programming environment for computational design and automation.
- [Elements](https://github.com/hypar-io/Elements) - Lightweight, code-first BIM library for generating building geometry programmatically.

---

## BIM and CAD platforms

- [Autodesk Revit](https://www.autodesk.com/products/revit/) - Widely used BIM authoring platform with extensible APIs.
- [Autodesk AutoCAD](https://www.autodesk.com/products/autocad/) - Widely used CAD platform with extensible APIs.
- [Autodesk Civil 3D](https://www.autodesk.com/products/civil-3d/) - Civil engineering design software.
- [Autodesk InfraWorks](https://www.autodesk.com/products/infraworks/) - Infrastructure design and visualization platform.
- [Autodesk Navisworks](https://www.autodesk.com/products/navisworks/) - Project review and clash detection software.
- [Autodesk BIM 360](https://www.autodesk.com/bim-360/) - Cloud-based construction management platform.
- [Autodesk Forge](https://forge.autodesk.com/) - Cloud platform for building custom applications and integrations.
- [Bentley OpenBuildings](https://www.bentley.com/en/products/brands/openbuildings) - Building design and analysis software.
- [Bentley OpenRoads](https://www.bentley.com/en/products/brands/openroads) - Road design and analysis software.
- [Bentley OpenRail](https://www.bentley.com/en/products/brands/openrail) - Rail design and analysis software.
- [Bentley OpenBridge](https://www.bentley.com/en/products/brands/openbridge) - Bridge design and analysis software.
- [Bentley OpenUtilities](https://www.bentley.com/en/products/brands/openutilities) - Utility network design and analysis software.
- [Bentley OpenFlows](https://www.bentley.com/en/products/brands/openflows) - Water infrastructure design and analysis software.
- [Graphisoft Archicad](https://graphisoft.com/solutions/archicad) - BIM platform with developer extensions.
- [Trimble Tekla](https://www.tekla.com/) - Structural BIM platform.
- [Nemetschek Allplan](https://www.allplan.com/) - BIM platform for architecture and engineering.
- [Dassault CATIA](https://www.3ds.com/products-services/catia/) - CAD and BIM platform for complex projects.
- [BIMserver](https://github.com/opensourceBIM/BIMserver) - Open-source BIM server platform for managing and querying IFC models.
- [EF-Tools](https://github.com/ErikFrits/EF-Tools) - Free collection of pyRevit-based tools for automating repetitive tasks in Revit.

---

## Digital twin platforms

- [Azure Digital Twins](https://azure.microsoft.com/en-us/products/digital-twins) - Cloud-based digital twin platform.
- [Bentley iTwin Platform](https://www.bentley.com/platform/itwin) - Infrastructure and digital twin platform.
- [Oracle IoT Digital Twin](https://docs.oracle.com/en/cloud/paas/iot-cloud/) - IoT and digital twin services on Oracle Cloud.
- [Dassault 3DEXPERIENCE](https://www.3ds.com/3dexperience) - Product and asset lifecycle digital twin platform.
- [Eclipse Ditto](https://www.eclipse.org/ditto/) - Open-source digital twin framework.
- [Asset Administration Shell](https://industrialdigitaltwin.org/) - Digital twin standard for Industry 4.0.
- [iTwin.js](https://github.com/iTwin/itwinjs-core) - Open-source library from Bentley for building infrastructure digital twin applications.

---

## Simulation and analysis

- [EnergyPlus](https://energyplus.net/) - Open-source whole-building energy simulation engine developed by the US DOE.
- [OpenStudio](https://openstudio.net/) - Open-source platform wrapping EnergyPlus for energy modelling and analysis workflows.
- [Ladybug Tools](https://www.ladybug.tools/) - Open-source suite for environmental analysis in Grasshopper and Rhino; covers daylight, solar, wind, and thermal comfort.
- [OpenFOAM](https://www.openfoam.com/) - Open-source CFD toolkit widely used for airflow, wind, and thermal simulations around and within buildings.
- [OpenSees](https://opensees.berkeley.edu/) - Open-source framework for structural and geotechnical earthquake engineering simulation.
- [FEniCS](https://fenicsproject.org/) - Open-source platform for solving partial differential equations, used in structural and fluid analysis.
- [TEASER](https://github.com/RWTH-EBC/TEASER) - Tool for energy analysis and simulation for early retrofit planning of building stocks.
- [RC_BuildingSimulator](https://github.com/architecture-building-systems/RC_BuildingSimulator) - Simplified thermal building simulation based on the ISO 13790 resistance-capacitance model.
- [ANSYS](https://www.ansys.com/) - General-purpose engineering simulation platform. Not open-source.
- [adapy](https://github.com/Krande/adapy) - Python library for structural analysis and design.
- [bim2sim](https://github.com/BIM2SIM/bim2sim) - Python tool for creating simulation models across different domains based on BIM IFC models.

---

## Point cloud and scan-to-BIM

- [CloudCompare](https://www.cloudcompare.org/) - Open-source 3D point cloud and mesh processing software; widely used for scan-to-BIM workflows.
- [Open3D](http://www.open3d.org/) - Open-source library for 3D data processing including point clouds, meshes, and RGBD data.
- [PDAL](https://pdal.io/) - Open-source point cloud data abstraction library for reading, filtering, and writing point cloud data.
- [Potree](https://potree.github.io/) - Open-source WebGL-based renderer for large point clouds in the browser.
- [py3dtiles](https://gitlab.com/py3dtiles/py3dtiles) - Python library for creating and manipulating 3D Tiles from point clouds and other data.
- [lidR](https://github.com/r-lidar/lidR) - R package for airborne LiDAR data processing and analysis.
- [OPALS](https://opals.geo.tuwien.ac.at/) - Software for processing and analysing airborne laser scanning data; developed at TU Wien.
- [Cloud2BIM](https://github.com/VaclavNezerka/Cloud2BIM) - Codes for automatic point-cloud-to-BIM conversion.

---

## GIS and geospatial tools

- [QGIS](https://qgis.org/) - Open-source desktop GIS platform with an extensive plugin ecosystem, including BIM and CityGML support.
- [GDAL](https://gdal.org/) - Open-source library for reading and writing raster and vector geospatial data formats.
- [PostGIS](https://postgis.net/) - Open-source spatial extension for PostgreSQL; widely used for storing and querying geospatial data.
- [GeoServer](https://geoserver.org/) - Open-source server for sharing geospatial data via OGC standards (WMS, WFS, WCS).
- [CesiumJS](https://cesium.com/cesiumjs/) - Open-source JavaScript library for 3D geospatial visualisation in the browser; supports 3D Tiles and IFC.
- [deck.gl](https://deck.gl/) - Open-source WebGL-powered large-scale data visualisation framework by Uber; widely used for urban analytics.
- [Kepler.gl](https://kepler.gl/) - Open-source geospatial analysis tool for large-scale datasets, built on deck.gl.
- [OpenLayers](https://openlayers.org/) - Open-source JavaScript library for interactive web maps.
- [Leaflet](https://leafletjs.com/) - Lightweight open-source JavaScript library for mobile-friendly interactive maps.
- [3DCityDB](https://www.3dcitydb.org/) - Open-source database solution for storing and managing 3D city models in CityGML format.
- [citygml4j](https://github.com/citygml4j/citygml4j) - Open-source Java library for reading, writing, and processing CityGML datasets.
- [py3dtilers](https://github.com/Oslandia/py3dtilers) - Tilers accepting OBJ, 3DCityDB, GeoJSON, and IFC input to produce 3D Tiles tilesets.
- [mago-3d-tiler](https://github.com/Gaia3D/mago-3d-tiler) - Java-based 3D Tiles generator.

---

## Data layer and standards

- Industry Foundation Classes (IFC) - Open BIM data model, see Standards and specifications section below.
- [CityGML](https://www.ogc.org/standard/citygml/) - Standard for 3D city models.
- [IndoorGML](https://www.ogc.org/standard/indoorgml/) - Indoor spatial information model.
- [buildingSMART Data Dictionary (bSDD)](https://www.buildingsmart.org/standards/bsi-standards/bsdd/) - Standardized terminology and properties.
- [dotbim](https://github.com/paireks/dotbim) - Minimalist, open file format for BIM.

---

## Ontologies and knowledge graphs

- [BE-OLS](https://cyberbuildlab.github.io/BE-OLS/) - Built Environment Ontology Lookup Service.
- [LOV](https://lov.linkeddata.es/dataset/lov/) - Linked Open Vocabularies.
- [Digital Buildings](https://github.com/google/digitalbuildings) - Ontology and SDK used by Google internally to manage its own buildings.

---

## Graph databases and data infrastructure

- [GraphDB](https://graphdb.ontotext.com/) - Knowledge graph database.
- [Neo4j](https://neo4j.com/) - Graph database.
- [Apache Jena](https://jena.apache.org/) - RDF framework and triple store.
- PostgreSQL / PostGIS - Spatial and relational database, see the GIS and geospatial tools section above.

---

## Data spaces

### Frameworks and architectures
- [International Data Spaces (IDS)](https://internationaldataspaces.org/) - Reference architecture for secure data exchange between organisations.
- [GAIA-X](https://gaia-x.eu/) - European initiative for federated cloud and data infrastructure.
- [Eclipse Dataspace Components](https://github.com/eclipse-edc) - Open-source implementation of the IDS architecture.
- [FIWARE Data Spaces](https://www.fiware.org/data-spaces/) - Open ecosystem supporting domain-specific data spaces.

### Domain data space initiatives

- [Manufacturing-X](https://www.manufacturing-x.de/) - Industrial data space initiative.
- [Mobility Data Space](https://mobility-dataspace.eu/) - European data-sharing ecosystem for mobility.
- [Catena-X](https://catena-x.net/) - Automotive data space ecosystem.
- Built Environment Data Spaces - Emerging data-sharing infrastructures for construction and infrastructure sectors.

---

## Robotics and AI for construction

- [OpenConstructionERP](https://github.com/datadrivenconstruction/OpenConstructionERP) - Open-source construction ERP covering BOQ and PDF/CAD/BIM takeoff with AI cost matching, across 42 regional catalogues and 21 languages.
- [DDC Skills for AI Agents in Construction](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction) - Collection of AI skills for construction covering BIM analysis, cost estimation, scheduling, and document control.
- [bimflowsuite](https://github.com/Nnamdi-Oniya/bimflowsuite) - Cloud-native platform for generating, analyzing, and managing IFC files.

---

## Standards and specifications

### Standards

- [BIM Standards Landscape Explorer](https://ec-3.org/BIM-Standards-Landscape-Explorer.html)
- [buildingSMART standards](https://www.buildingsmart.org/standards/)
- [IFC](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/)
- [OGC standards](https://www.ogc.org/standards) - Including CityGML, IndoorGML, and 3D Tiles.
- [IFC4.x-development](https://github.com/buildingSMART/IFC4.x-development) - Repository tracking updates to the IFC4.3 specification.
- [IFC5-development](https://github.com/buildingSMART/IFC5-development) - Development repository for the next generation of Industry Foundation Classes.

### Semantic web standards

- [RDF](https://www.w3.org/RDF/)
- [RDFS](https://www.w3.org/TR/rdf-schema/)
- [OWL](https://www.w3.org/OWL/)
- [SHACL](https://www.w3.org/TR/shacl/)
- [SPARQL](https://www.w3.org/TR/sparql11-query/)

---

## Research groups and communities

- [Information Systems in the Built Environment (ISBE)](https://isbe.bwk.tue.nl/) - Research group at Eindhoven University of Technology (TU/e), The Netherlands.

---

## Conferences and workshops

Known conferences and workshops related to digital construction, BIM, digital twins, AI, and semantic technologies for the built environment.

### International

- [CIB W78 - Information Technology in Construction](https://www.cibw78.org/) - Leading conference on digital technologies for construction.
- [EC3 - European Conference on Computing in Construction](https://ec-3.org/) - Major European conference on computational approaches in construction.
- [ASCE International Conference on Computing in Civil Engineering](https://www.asce.org/cce) - Conference on computing applications in civil engineering.
- [eCAADe - Education and Research in Computer Aided Architectural Design in Europe](https://ecaade.org/) - Conference on computational design and digital architecture.
- [CAAD Futures](https://caadfutures.org/) - International conference on computer-aided architectural design.
- [ISARC - International Symposium on Automation and Robotics in Construction](https://www.isarc.org/) - Flagship conference on robotics in construction.
- [IEEE CASE](https://ieee-ras.org/conferences-workshops/fully-sponsored/case) - IEEE conference on automation science and engineering.
- [LDAC - Linked Data in Architecture and Construction](http://www.linkedbuildingdata.net/ldac/) - Workshop on semantic web technologies in the built environment.
- [SEMANTiCS Conference](https://2024-eu.semantics.cc/) - Conference on semantic technologies and knowledge graphs.
- [TwinArch - Digital Twin Architecture Workshop](https://www.iese.fraunhofer.de/en/twinarch.html) - Workshop on digital twin architectures.
- [ACM BuildSys](https://buildsys.acm.org/) - Conference on systems for smart buildings and cities.
- [IEEE Smart Cities](https://smartcities.ieee.org/) - Conference series on smart city technologies.
- [TUM GNI Symposium](https://events.gni.tum.de/ai-symposium-2026/) - Symposium on digital transformation in the built environment, organized by TUM.
- [ICSA - International Conference on Structures and Architecture](https://www.linkedin.com/company/icsa-2027-milano/)

### National and regional

- [UK BIM Conference](https://www.ukbimconference.com/) - Annual conference on BIM in the UK.
- [BIM World](https://www.bim-world.com/) - Global conference with regional editions in Europe, Asia, and the Americas.
- [AIA Conference on Architecture](https://conferenceonarchitecture.com/) - Major US conference on architecture and design, including digital technologies.
- [BILT Conference](https://bilt-conference.com/) - Conference on BIM and digital construction with global editions.
- [BIM Forum](https://bimforum.org/) - Annual conference on BIM in the US.
- [BIM Nordic](https://bimnordic.com/) - Conference on BIM in the Nordic countries.
- [BIM Summit](https://bimsummit.es/) - Annual conference on BIM in Spain.
- [Digital Construction Week](https://www.digitalconstructionweek.com/) - UK-based conference on digital construction technologies.
- [Smart Building Conference](https://www.smartbuildingconference.com/) - Conference on smart building technologies in the US.
- [Smart Cities Expo World Congress](https://www.smartcityexpo.com/) - Global conference on smart city technologies.
- [4TU / 14UAS Research Day on Digitalisation of the Built Environment](https://www.4tu.nl/agenda/5th-research-day-on-digitalization/) - Workshop on digitalisation in the built environment, organized by 4TU and 14UAS in the Netherlands.

---

## Initiatives and societies

- [BIMe](https://bimexcellence.org/) - BIM Excellence Initiative.
- [CIB - International Council for Research and Innovation in Building and Construction](https://www.cibworld.org/) - Global network of researchers and practitioners in the built environment.
- [EC3 Modelling & Standards Committee](https://ec-3.org/governance/technical-committees/modelling-standards-committee/) - A permanent technical committee of the EC3.
- [buildingSMART International](https://www.buildingsmart.org/) - International organization developing open BIM standards.
- [Digital Twin Consortium](https://www.digitaltwinconsortium.org/) - Global ecosystem for digital twin technologies.

---

## Datasets and benchmarks

### BIM and IFC

- [Example IFC Files Dataset](https://www.kaggle.com/datasets/claytonmiller/example-ifc-file) - Collection of IFC models used in BIM tutorials.
- [BIMData IFC dataset](https://github.com/bimdata/BIMData-Research-and-Development/blob/master/pages/IFC_FILES.md) - Collection of IFC models for development and testing.
- [buildingSMART IFC Datasets](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/ifc-datasets/) - BIM model datasets in IFC format.
- [IFCNet](https://ifcnet.e3d.rwth-aachen.de/) - BIM model dataset for machine learning.
- [IfcBench](https://huggingface.co/datasets/sylvainHellin/ifc-bench) - Benchmark dataset for IFC-based machine learning.
- [BuildingNet](https://buildingnet.org/) - Building model dataset for machine learning.
- [ArchShapesNet](https://i3l.seoultech.ac.kr/subList/20000005729) - BIM elements dataset for deep learning classification of building components.
- [3DFacilities Dataset](https://www.sciencedirect.com/science/article/pii/S0926580524002942) - Dataset of structural and MEP BIM elements for research.
- [Open IFC Model Repository](https://github.com/opensourceBIM/TestFiles) - IFC test files for openBIM development.
- [xBIM Toolkit Examples](https://github.com/xBimTeam/XbimSamples) - BIM models used for xBIM development and tutorials.
- [BIM-NLQ Dataset for NLQ4BIM](https://github.com/MengtianYin/BIM-NLQI) - Natural language query dataset for BIM models.
- [Dataset Schependomlaan](https://github.com/jakob-beetz/DataSetSchependomlaan) - IFC dataset for a residential building in the Netherlands.
- [BIM Whale](https://github.com/andrewisen/bim-whale-ifc-samples) - Collection of IFC sample files for the BIM Whale project.
- [GABLE](https://github.com/AICyberTeam/GABLE) - Nation-scale fine-grained 3D building model dataset for machine learning (Beijing, China).
- [Ifc Sample Files](https://github.com/youshengCode/IfcSampleFiles) - Sample IFC files for testing and benchmarking.
- [NIST IFC Repository](https://www.nist.gov/services-resources/software/ifc) - BIM model datasets.
- [Sample-Test-Files](https://github.com/buildingSMART/Sample-Test-Files) - Official buildingSMART sample files across various formats and schema versions.

### City models and geospatial

- [Awesome CityGML](https://github.com/OloOcki/awesome-citygml) - Curated list of CityGML datasets and resources for different cities.
- [3D City Database](https://github.com/3dcitydb/3dcitydb) - Open-source database for storing and managing 3D city models, with example datasets.
- [Open City Model](https://github.com/opencitymodel/opencitymodel) - Initiative providing open CityGML data for buildings in the USA.
- [Tokyo SpatialID Dataset](https://github.com/tlab-wide/SpatialID) - Large-scale CSV dataset for Tokyo, Japan.
- [Polygon City Berlin](https://github.com/polygon-city/polygon-city-berlin-export) - CityGML dataset for Berlin, Germany.
- [CityGML 3D City Model Repository](https://www.ogc.org/standards/citygml#datasets) - Repository of 3D city models in CityGML format.
- [3D Tiles](https://github.com/CesiumGS/3d-tiles) - 3D geospatial data format with example datasets.
- [Microsoft Global Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) - Building footprints extracted from satellite imagery.
- [Google Open Buildings](https://sites.research.google/open-buildings/) - Large-scale building footprint dataset derived from satellite imagery.
- [Global Building Atlas](https://arxiv.org/abs/2506.04106) - Global dataset of building footprints and heights.
- [Urban Atlas](https://land.copernicus.eu/en/products/urban-atlas) - European urban land use, building height, and tree data.
- [Eurostat GISCO datasets](https://ec.europa.eu/eurostat/web/gisco/geodata) - European geospatial datasets.
- [Global Human Settlement Layer (GHSL)](https://human-settlement.emergency.copernicus.eu/GHSLWeGenerateData.php) - Global dataset describing human settlements.
- [OpenStreetMap](https://www.openstreetmap.org/) - Global open geospatial dataset.
- [Natural Earth](https://www.naturalearthdata.com/) - Public domain map dataset.

### Point clouds and 3D scenes

- [Habitat-Matterport 3D (HM3D)](https://aihabitat.org/datasets/hm3d/) - Dataset of indoor environments used for embodied AI and robotics research.
- [Matterport3D](https://niessner.github.io/Matterport/) - Indoor scanning dataset.
- [Stanford Computational and Geometry Lab Vision](https://cvgl.stanford.edu/resources.html) - Several 3D vision datasets.
- [KITTI](http://www.cvlibs.net/datasets/kitti/) - Autonomous driving dataset with 3D point clouds.
- [ModelNet](http://modelnet.cs.princeton.edu/) - 3D CAD model dataset.
- [ShapeNet](https://www.shapenet.org/) - Large-scale 3D model dataset.
- [ScanNet](http://www.scan-net.org/) - 3D scene dataset.
- [S3DIS](http://buildingparser.stanford.edu/dataset.html) - Indoor scene dataset.
- [3D Warehouse](https://3dwarehouse.sketchup.com/) - 3D model repository with many building models.
- [Semantic3D](http://www.semantic3d.net/) - Large-scale outdoor LiDAR point cloud dataset.
- [Toronto3D](https://github.com/WeikaiTan/Toronto-3D) - Mobile LiDAR dataset for urban environments.
- [Paris-Lille-3D](https://npm3d.fr/paris-lille-3d) - Urban LiDAR dataset with semantic labels.
- [DALES](https://udayton.edu/engineering/centers/vision_lab/research/dales.php) - Aerial LiDAR dataset for urban object segmentation.
- [Structured3D](https://structured3d-dataset.org/) - Large-scale dataset of synthetic indoor scenes with detailed room layouts.
- [InteriorNet](https://interiornet.org/) - Photorealistic dataset for indoor scene understanding.
- [Replica Dataset](https://github.com/facebookresearch/Replica-Dataset) - High-quality 3D indoor environments for robotics and AI.
- [SemanticKITTI](http://semantic-kitti.org/) - LiDAR dataset with semantic annotations.
- [AHN3 / AHN4](https://www.ahn.nl/) - Dutch national LiDAR dataset.
- [USGS 3D Elevation Program](https://www.usgs.gov/3d-elevation-program) - National LiDAR datasets for the United States.
- [OpenTopography](https://opentopography.org/) - Repository of LiDAR datasets.

### Construction, energy, and mobility

- [ASHRAE Great Energy Predictor Dataset](https://www.kaggle.com/c/ashrae-energy-prediction) - Dataset for building energy prediction.
- [Building Data Genome Project](https://github.com/buds-lab/building-data-genome-project-2) - Large dataset of building energy consumption.
- [Construction Site Image Dataset](https://github.com/pangyuteng/construction-site-image-dataset) - Annotated images of active construction sites for computer vision tasks.
- [Open Construction Dataset](https://github.com/ruoxinx/OpenConstruction-Datasets) - Dataset for construction scene understanding.
- [Building Change Detection Dataset](https://study.rsgis.whu.edu.cn/pages/download/building_dataset.html) - Dataset for monitoring construction and urban change from aerial imagery.
- [SpaceNet Building Dataset](https://github.com/spacenetchallenge) - Satellite imagery dataset for building detection.
- [Inria Aerial Image Labeling Dataset](https://project.inria.fr/aerialimagelabeling/) - Aerial imagery dataset with building annotations.
- [DeepGlobe Building Dataset](https://deepglobe.org/challenge.html) - Satellite dataset for building extraction.
- [xView Dataset](https://xviewdataset.org/) - Satellite imagery dataset for object detection, including buildings.
- [ABC Dataset (Architecture, Buildings, Construction)](https://deep-geometry.github.io/abc-dataset/) - Large dataset of CAD models used for geometric deep learning.
- [Open Transport Data](https://data.europa.eu/data/datasets?query=transport) - European transportation datasets.
- [OpenTraffic](https://opentraffic.io/) - Traffic and mobility datasets.
- [Uber Movement](https://www.kaggle.com/datasets/ishandutta/uber-travel-movement-data-2-billion-trips) - Urban mobility datasets for cities worldwide.
- [Open Power System Data](https://open-power-system-data.org/) - Energy infrastructure datasets.
- [IDEAS Building Energy Dataset](https://github.com/open-ideas/IDEAS) - Building energy modelling datasets.

### Sensors and smart cities

- [Brick Building Dataset](https://brickschema.org/resources/) - Datasets for building systems modelling using the Brick ontology.
- [SmartSantander Dataset](https://github.com/Predictia/smartsantander) - IoT sensor data for smart city experiments.
- [Array of Things Sensor Dataset](https://github.com/waggle-sensor/waggle/blob/master/data/README.md) - Urban sensor network dataset.
- [CityPulse Dataset](https://iot.ee.surrey.ac.uk:8080/datasets.html) - Smart city IoT data streams.
- [Urban Observatory Newcastle](https://urbanobservatory.ac.uk/) - Large urban sensor dataset.
- [NYC Open Data](https://opendata.cityofnewyork.us/) - Large collection of urban infrastructure datasets.

---

## Learning resources

### Books

_This section is a work in progress. Contributions welcome._

### Courses

- BIM and digital twin courses on **Coursera** and **edX**.

---

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the maintainer has waived all copyright and related or neighboring rights to this list. See [LICENSE](LICENSE) for details.
