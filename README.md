# Awesome Digital Built Environment [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of tools, standards, datasets, platforms, and communities that are shaping the digital and intelligent transformation of the built environment.

Topics include (and are not limited to): BIM and openBIM, digital twins, ontologies and knowledge graphs, robotics and automation, smart cities, simulation and analytics, AI for construction, and data standards and interoperability. The goal is to provide a technical reference map of the digital built environment ecosystem in line with the Awesome list guidelines. 

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
- [Artificial intelligence and machine learning](#artificial-intelligence-and-machine-learning)
  - [AI for BIM and IFC](#ai-for-bim-and-ifc)
  - [LLM agents and natural-language interfaces](#llm-agents-and-natural-language-interfaces)
  - [Computer vision for construction](#computer-vision-for-construction)
  - [Generative design and spatial intelligence](#generative-design-and-spatial-intelligence)
  - [Building control and reinforcement learning](#building-control-and-reinforcement-learning)
  - [GeoAI and urban intelligence](#geoai-and-urban-intelligence)
  - [AI benchmarks and datasets](#ai-benchmarks-and-datasets)
  - [Foundation models for the built environment](#foundation-models-for-the-built-environment)
  - [Neuro-symbolic AI](#neuro-symbolic-ai)
  - [NLP for construction and the built environment](#nlp-for-construction-and-the-built-environment)
  - [RAG for AEC documents](#rag-for-aec-documents)
  - [Structural health monitoring and anomaly detection](#structural-health-monitoring-and-anomaly-detection)
  - [Time-series forecasting for building energy](#time-series-forecasting-for-building-energy)
  - [Multi-agent systems for construction](#multi-agent-systems-for-construction)
  - [Synthetic data generation](#synthetic-data-generation)
  - [AI bias and fairness in construction](#ai-bias-and-fairness-in-construction)
- [Datasets and benchmarks](#datasets-and-benchmarks)
  - [BIM and IFC](#bim-and-ifc)
  - [City models and geospatial](#city-models-and-geospatial)
  - [Point clouds and 3D scenes](#point-clouds-and-3d-scenes)
  - [Construction, energy, and mobility](#construction-energy-and-mobility)
  - [Sensors and smart cities](#sensors-and-smart-cities)
- [Standards and specifications](#standards-and-specifications)
- [Research groups and communities](#research-groups-and-communities)
- [Conferences and workshops](#conferences-and-workshops)
- [Initiatives and societies](#initiatives-and-societies)
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
- [GitHubDragonFly 3D viewers](https://github.com/GitHubDragonFly/GitHubDragonFly.github.io) - Collection of browser-based 3D viewers covering many formats including BIM and IFC.
- [Astral3D](https://github.com/mlt131220/Astral3D) - Open-source 3D engine and editor based on Vue3 and Three.js, with BIM lightweighting and CAD preview.
- [gemini-viewer-examples](https://github.com/pattern-x/gemini-viewer-examples) - Examples for a WebGL-based BIM viewer built on three.js, supporting DWG, glTF, OBJ, and IFC.
- [bimvie.ws](https://github.com/opensourceBIM/bimvie.ws) - JavaScript client for BIM using open standards including IFC, BCF, and BIMSie.
- [wl-bim-viewer](https://github.com/hql7/wl-bim-viewer) - BIM 3D model preview plugin for the Vue framework.
- [bim-ootb](https://github.com/red1oon/bim-ootb) - Browser-native IFC viewer paired with a local-first ERP kernel.

### Parsers and SDKs

- [IfcOpenShell](https://ifcopenshell.org/) - The primary open-source IFC toolkit and geometry engine, supporting Python and C++, with IFC2X3, IFC4, and IFC4X3.
- [web-ifc](https://github.com/ThatOpen/engine_web-ifc) - WebAssembly-based IFC parser in JavaScript for reading and writing IFC files at native speed; foundation of IFC.js.
- [xBIM Toolkit](https://docs.xbim.net/) - Open-source .NET toolkit for reading, creating, and viewing IFC files, with a geometry engine and COBie support.
- [IfcPlusPlus](https://github.com/ifcquery/ifcplusplus) - C++ library for reading and writing IFC files, with an OpenSceneGraph-based viewer.
- [IFC.js / web-ifc-three](https://github.com/ThatOpen/engine_three-ifc) - Official IFC loader for Three.js.
- [GeometryGym](https://github.com/jmirtsch/GeometryGym) - C# library for generating and parsing IFC and other openBIM standards.
- [xeokit-sdk](https://github.com/xeokit/xeokit-sdk) - Open-source WebGL-based 3D BIM/IFC viewer SDK for AEC applications, with real-world coordinates and double precision.
- [ifc-lite](https://github.com/LTplus-AG/ifc-lite) - Parse, view, query, edit, and export IFC, IDS, BCF, and point clouds in the browser, server, or desktop.
- [Microsoft IFC SDK](https://github.com/microsoft/ifc) - Microsoft's SDK for the IFC specification.
- [brepjs](https://github.com/andymai/brepjs) - Web CAD library with exact B-Rep geometry.
- [conway](https://github.com/bldrs-ai/conway) - High-performance IFC and STEP engine for web-based CAD applications.
- [XbimEssentials](https://github.com/xBimTeam/XbimEssentials) - .NET library for working with IFC data, the core component of the xBIM Toolkit.
- [XbimGeometry](https://github.com/xBimTeam/XbimGeometry) - Geometry engine computing 3D geometry for xBIM models.
- [specklepy](https://github.com/specklesystems/specklepy) - Python SDK for Speckle, an open-source data interoperability platform for AEC.
- [openskp](https://github.com/iamahsanmehmood/openskp) - Open-source parser for SketchUp (.skp) binary files.

### Validators and quality checking

- [buildingSMART Validation Service](https://validate.buildingsmart.org/) - Official online IFC validator by buildingSMART.
- [IfcDoc](https://github.com/buildingSMART/IfcDoc) - Tool for documenting and validating IFC schemas; used to author the official IFC specification.
- [IDS (Information Delivery Specification)](https://github.com/buildingSMART/IDS) - BuildingSMART standard for defining and checking model requirements; supported by several validators above.
- [COREY](https://github.com/JHJHJHJH/COREY) - Visually review IFC model data, configure clauses and rules, and validate.
- [ifc_checker](https://github.com/i-savelev/ifc_checker) - Simple tool for checking IFC models.

### Converters and pipelines

- [IfcConvert](https://ifcopenshell.org/ifcconvert) - Command-line tool (part of IfcOpenShell) for converting IFC to OBJ, DAE, GLB, SVG, and more.
- [IFC2CA](https://github.com/KC-Lab/IFC2CA) - Converts IFC structural models for use in structural analysis tools.
- [IFC to CityGML](https://github.com/tum-gis/ifc2citygml) - Converts IFC building models to CityGML format.
- [ifc-pipeline](https://github.com/AECgeeks/ifc-pipeline) - Processing queue and front-end for visualizing BIM models, built with IfcOpenShell, Docker Compose, and Flask.
- [xeokit-convert](https://github.com/xeokit/xeokit-convert) - Converts various AEC model formats for efficient viewing in the browser with xeokit.
- [cad2data](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN) - Automated conversion workflow for CAD files (RVT, IFC, DWG, DGN) using command-line converters.
- [blendit](https://github.com/lewismconte/blendit) - One-click Revit to Blender renderer.

---

## Building modelling and design

- [BHoM](https://github.com/BHoM/BHoM) - Interoperability framework for sharing built-environment data.
- [Topologic](https://topologic.app/) - Topological spatial modelling software for representing building spaces and relationships.
- [Rhino.Compute](https://compute.rhino3d.com/) - API enabling remote execution of Rhino and Grasshopper models.
- [Hypar](https://hypar.io/) - Generative design platform for parametric BIM workflows.
- [FreeCAD BIM Workbench](https://wiki.freecad.org/BIM_Workbench) - Open BIM modelling tools for FreeCAD.
- [Dynamo](https://github.com/DynamoDS/Dynamo) - Open-source graphical programming environment for computational design and automation.
- [Elements](https://github.com/hypar-io/Elements) - Lightweight, code-first BIM library for generating building geometry programmatically.
- [DynamoRevit](https://github.com/DynamoDS/DynamoRevit) - Dynamo libraries specifically for Revit.
- [Revit_Toolkit](https://github.com/BHoM/Revit_Toolkit) - Tools enabling exchange of information between BHoM and Revit.
- [Grevit](https://github.com/grevit-dev/Grevit) - Build BIM models in Grasshopper or SketchUp.
- [3dio-js](https://github.com/archilogic-com/3dio-js) - JavaScript toolkit for interior design applications.

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
- [FreeCAD](https://github.com/FreeCAD/FreeCAD) - Free and open-source multi-platform 3D parametric modeler, base platform for the FreeCAD BIM Workbench.
- [massing](https://github.com/ibuilder/massing) - Open, self-hosted, IFC-native AEC platform combining a web BIM viewer with a GC portal.
- [B45 Labs Coordination](https://github.com/B45Labs/B45Labs_Coordination) - Revit add-in for coordination, auditing, and QA/QC workflows.
- [multiconn_archicad](https://github.com/SzamosiMate/multiconn_archicad) - Python toolkit for multi-instance Archicad automation via its JSON API and Tapir Add-On.
- [CadAddinManager](https://github.com/chuongmep/CadAddinManager) - Updates .NET assemblies without restarting AutoCAD or Civil 3D during development.

---

## Digital twin platforms

- [Azure Digital Twins](https://azure.microsoft.com/en-us/products/digital-twins) - Cloud-based digital twin platform.
- [Bentley iTwin Platform](https://www.bentley.com/platform/itwin) - Infrastructure and digital twin platform.
- [Oracle IoT Digital Twin](https://docs.oracle.com/en/cloud/paas/iot-cloud/) - IoT and digital twin services on Oracle Cloud.
- [Dassault 3DEXPERIENCE](https://www.3ds.com/3dexperience) - Product and asset lifecycle digital twin platform.
- [Eclipse Ditto](https://www.eclipse.org/ditto/) - Open-source digital twin framework.
- [Asset Administration Shell](https://industrialdigitaltwin.org/) - Digital twin standard for Industry 4.0.
- [iTwin.js](https://github.com/iTwin/itwinjs-core) - Open-source library from Bentley for building infrastructure digital twin applications.

### Asset Administration Shell (AAS) tools

- [AASX Package Explorer](https://github.com/admin-shell-io/aasx-package-explorer) - C#-based viewer and editor for the Asset Administration Shell.
- [BaSyx Python SDK](https://github.com/eclipse-basyx/basyx-python-sdk) - Eclipse BaSyx implementation of the Asset Administration Shell for Industry 4.0 systems.
- [FA3ST Service](https://github.com/FraunhoferIOSB/FAAAST-Service) - Fraunhofer Advanced Asset Administration Shell Tools for digital twins.
- [openAAS](https://github.com/rwth-iat/openAAS) - Development repository for an open Asset Administration Shell implementation.
- [BaSyx AAS Web UI](https://github.com/eclipse-basyx/basyx-aas-web-ui) - Web-based interface for managing and interacting with Asset Administration Shells.
- [AAS Manager](https://github.com/rwth-iat/aas_manager) - Editor and viewer for Asset Administration Shells.
- [Twin4Build](https://github.com/JBjoernskov/Twin4Build) - Dynamic building simulation using differentiable data-driven models integrated with semantic models.
- [AASPortal](https://github.com/eclipse-aasportal/AASPortal) - Node.js-based web portal for visualizing and managing Asset Administration Shells.
- [aas-core3.0-csharp](https://github.com/aas-core-works/aas-core3.0-csharp) - Manipulate, verify, and serialize Asset Administration Shells in C#.
- [AAS Hub](https://github.com/aas-hub-org/aashub) - Web application for accessing and sharing Asset Administration Shells.

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
- [awatif](https://github.com/madil4/awatif) - AI-native platform for structural engineering automation.
- [VOSTOK](https://github.com/3dgeo-heidelberg/vostok) - Voxel Octree Solar Toolkit for computing detailed incoming solar radiation models.
- [OpenWind-AU](https://github.com/Elandu/OpenWind-AU) - Preliminary wind site terrain and topographic analysis for buildings using public geospatial datasets.

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
- [pystruct3d](https://github.com/humantecheu/pystruct3d) - Bounding box fitting and reconstruction library for scan-to-BIM workflows.
- [scan_to_model_pipeline](https://github.com/mac999/scan_to_model_pipeline) - Open-source pipeline that generates mesh models from point cloud scans.
- [ReUseX](https://github.com/pfmephisto/ReUseX) - Tool for processing 3D point cloud scans of building interiors to support reuse workflows.
- [pyhelios](https://github.com/chenzhaiyu/pyhelios) - Configurations of Helios++ for point cloud simulation on urban buildings.
- [SLAM2REF](https://github.com/MigVega/SLAM2REF) - Aligns and corrects LiDAR-based SLAM session data with a reference map or another session.
- [IGN LiDAR HD](https://github.com/imagodata/IGN_LIDAR_HD_DATASET) - Python library for processing IGN LiDAR HD data into machine-learning-ready datasets for buildings.

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
- [3D Tiles Renderer JS](https://github.com/NASA-AMMOS/3DTilesRendererJS) - Renderer for 3D Tiles in JavaScript using three.js, Babylon.js, or react-three-fiber.
- [3dtiles](https://github.com/fanvanzh/3dtiles) - Fast converter for generating 3D Tiles.
- [geo-three](https://github.com/tentone/geo-three) - Tile-based geographic world map visualization library for three.js.
- [loaders.gl](https://github.com/visgl/loaders.gl) - Loaders for large-scale geospatial and 3D data visualization.
- [objTo3d-tiles](https://github.com/PrincessGod/objTo3d-tiles) - Converts OBJ model files to 3D Tiles.
- [WorldWind Java](https://github.com/NASAWorldWind/WorldWindJava) - NASA SDK for building cross-platform 3D geospatial desktop applications.
- [OSM2World](https://github.com/tordanik/OSM2World) - Converts OpenStreetMap data into three-dimensional models.
- [3dfier](https://github.com/tudelft3d/3dfier) - Open-source tool for creating 3D city models from 2D GIS data, developed at TU Delft.
- [pg2b3dm](https://github.com/Geodan/pg2b3dm) - Creates 3D Tiles from PostGIS geometries.
- [3D Tiles Validator](https://github.com/CesiumGS/3d-tiles-validator) - Validator for the 3D Tiles specification.
- [3DCityDB Web Map](https://github.com/3dcitydb/3dcitydb-web-map) - Cesium-based 3D viewer and JavaScript API for the 3D City Database.
- [3DCityDB Importer/Exporter](https://github.com/3dcitydb/importer-exporter) - Client for high-performance import and export of 3D city model data.
- [Obj2Tiles](https://github.com/OpenDroneMap/Obj2Tiles) - Converts OBJ files to OGC 3D Tiles with splitting and decimation.
- [WorldWind Android](https://github.com/NASAWorldWind/WorldWindAndroid) - NASA SDK for building 3D geospatial applications on Android.
- [Building-Regulariser](https://github.com/DPIRD-DMA/Building-Regulariser) - Python library for cleaning and regularising building footprints in geospatial data.
- [three-geojson](https://github.com/gkjohnson/three-geojson) - Three.js shape loaders for GeoJSON and WKT formats.
- [mapbox-3d-tiles](https://github.com/yangjs6/mapbox-3d-tiles) - Integrates three.js with Mapbox GL to render 3D Tiles, 3D Gaussian Splats, and glTF.
- [3DGS-PLY-3DTiles-Converter](https://github.com/WilliamLiu-1997/3DGS-PLY-3DTiles-Converter) - Converts Gaussian Splatting PLY files into 3D Tiles.
- [open-buildings](https://github.com/opengeos/open-buildings) - Tools for working with open building footprint datasets.
- [citygml-tools](https://github.com/citygml4j/citygml-tools) - Command-line tools for processing and converting CityGML files.
- [ifcSQL_Tools for QGIS](https://github.com/MicheleBerlato/ifcSQL_Tools_for_QGIS) - QGIS plugin for loading and interacting with IFC data.
- [plateau-gis-converter](https://github.com/MIERUNE/plateau-gis-converter) - Converts PLATEAU 3D city models (CityGML) of Japan into various geospatial formats.
- [city2tabula](https://github.com/THD-Spatial-AI/city2tabula) - Extracts geometric attributes from 3D city models (CityGML/CityJSON) and classifies buildings.
- [cityjson-rs](https://github.com/3DGI/cityjson-rs) - CityJSON support in Rust with FFI, covering types, operations, and Arrow/Parquet formats.

---

## Data layer and standards

- Industry Foundation Classes (IFC) - Open BIM data model, see Standards and specifications section below.
- [CityGML](https://www.ogc.org/standard/citygml/) - Standard for 3D city models.
- [IndoorGML](https://www.ogc.org/standard/indoorgml/) - Indoor spatial information model.
- [buildingSMART Data Dictionary (bSDD)](https://www.buildingsmart.org/standards/bsi-standards/bsdd/) - Standardized terminology and properties.
- [dotbim](https://github.com/paireks/dotbim) - Minimalist, open file format for BIM.
- [bSDD (GitHub)](https://github.com/buildingSMART/bSDD) - Source repository for the buildingSMART Data Dictionary, including documentation and examples.

---

## Ontologies and knowledge graphs

- [BE-OLS](https://cyberbuildlab.github.io/BE-OLS/) - Built Environment Ontology Lookup Service.
- [LOV](https://lov.linkeddata.es/dataset/lov/) - Linked Open Vocabularies.

---

## Graph databases and data infrastructure

- [GraphDB](https://graphdb.ontotext.com/) - Knowledge graph database.
- [Neo4j](https://neo4j.com/) - Graph database.
- [Apache Jena](https://jena.apache.org/) - RDF framework and triple store.
- PostgreSQL / PostGIS - Spatial and relational database, see the GIS and geospatial tools section above.
- [TerminusDB](https://terminusdb.com/) - Distributed, collaborative database for building, versioning, and reasoning over knowledge graphs.

---

## Data spaces

### Frameworks and architectures

- [International Data Spaces (IDS)](https://internationaldataspaces.org/) - Reference architecture for secure data exchange between organisations.
- [GAIA-X](https://gaia-x.eu/) - European initiative for federated cloud and data infrastructure.
- [Eclipse Dataspace Components](https://github.com/eclipse-edc) - Open-source implementation of the IDS architecture.
- [FIWARE Data Spaces](https://www.fiware.org/data-spaces/) - Open ecosystem supporting domain-specific data spaces.
- [IDSA](https://github.com/International-Data-Spaces-Association/idsa) - Main repository of the International Data Spaces Association.
- [Trusted Connector](https://github.com/Fraunhofer-AISEC/trusted-connector) - IoT edge platform implementing the International Data Spaces connector, based on Spring Boot.
- [Dataspace Protocol specification](https://github.com/International-Data-Spaces-Association/ids-specification) - Specifications for interoperable data sharing between entities.
- [TRUE Connector](https://github.com/Engineering-Research-and-Development/true-connector) - TRUsted Engineering connector for the International Data Spaces ecosystem.
- [run-dsp](https://github.com/go-dataspace/run-dsp) - Open-source Go implementation of the IDSA dataspace protocol.
- [data-exchange-agreements](https://github.com/decentralised-dataexchange/data-exchange-agreements) - Specifications for data disclosure agreements.

### Domain data space initiatives

- [Manufacturing-X](https://www.manufacturing-x.de/) - Industrial data space initiative.
- [Mobility Data Space](https://mobility-dataspace.eu/) - European data-sharing ecosystem for mobility.
- [Catena-X](https://catena-x.net/) - Automotive data space ecosystem.
- Built Environment Data Spaces - Emerging data-sharing infrastructures for construction and infrastructure sectors.
- [mds-edc](https://github.com/Mobility-Data-Space/mds-edc) - Connector distribution based on Eclipse Dataspace Components, tailored for the Mobility Data Space.
- [dataspace-ecosystem](https://github.com/AmadeusITGroup/dataspace-ecosystem) - Amadeus dataspace connector built on Eclipse EDC components.
- [gx-credential-generator](https://github.com/SovereignCloudStack/gx-credential-generator) - Tools for creating Gaia-X credentials.
- [gaiax-credentials-tool](https://github.com/fundacionctic/gaiax-credentials-tool) - Tool for building and signing Gaia-X credentials.
- [federated-catalogue](https://github.com/eclipse-xfsc/federated-catalogue) - Federated catalogue for Gaia-X self-descriptions and service offerings.
- [gx-agent](https://github.com/Sphereon-Opensource/gx-agent) - Gaia-X participant agent and compliance server interactions.
- [ontology-management-base](https://github.com/GAIA-X4PLC-AAD/ontology-management-base) - Open, automated ontology management process for GAIA-X interoperable ecosystems.
- [mvg-portal](https://github.com/deltaDAO/mvg-portal) - Data space portal web application built on Ocean Protocol tooling.

---

## Robotics and AI for construction

- [OpenConstructionERP](https://github.com/datadrivenconstruction/OpenConstructionERP) - Open-source construction ERP covering BOQ and PDF/CAD/BIM takeoff with AI cost matching, across 42 regional catalogues and 21 languages.
- [DDC Skills for AI Agents in Construction](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction) - Collection of AI skills for construction covering BIM analysis, cost estimation, scheduling, and document control.
- [bimflowsuite](https://github.com/Nnamdi-Oniya/bimflowsuite) - Cloud-native platform for generating, analyzing, and managing IFC files.
- [FARKUS](https://github.com/modrobotics/FARKUS) - Robotic construction kit for factory automation.
- [M3-CRETE Firmware](https://github.com/sunnyday-technologies/M3-CRETE-FIRMWARE) - Firmware configuration for the M3-CRETE 3D concrete printing platform.

---

## Artificial intelligence and machine learning

Open-source tools, models, agents, benchmarks, and research implementations applying artificial intelligence to buildings, infrastructure, construction, cities, and the wider built environment.

### AI for BIM and IFC

- [Text2BIM](https://github.com/dcy0577/Text2BIM) - LLM-based multi-agent framework for generating editable BIM models from natural-language design instructions.
- [BIM LLM Code Agent](https://github.com/mac999/BIM_LLM_code_agent) - Research implementation for evaluating LLM reasoning, code generation, and task execution over BIM and IFC models.
- [BIM Graph Agent](https://github.com/mac999/BIM_graph_agent) - Converts IFC models into Neo4j graphs and provides natural-language querying through an LLM-based agent.
- [IFC-MCP](https://github.com/ekkodale/IFC-MCP) - Model Context Protocol server exposing IFC extraction, filtering, aggregation, and analysis tools to language models.
- [IFC Bonsai MCP](https://github.com/Show2Instruct/ifc-bonsai-mcp) - MCP server connecting language models to Bonsai for reading, creating, and editing IFC models.
- [AskSchema](https://github.com/Z-Arghavan/AskOntology2) - Schema-grounded retrieval and question-answering system using embeddings, vector search, subgraph expansion, and LLMs for ontology and information-model exploration.
- [BIM-NLQI](https://github.com/MengtianYin/BIM-NLQI) - Natural-language question and query dataset for evaluating interfaces to BIM models.
- [IfcBench](https://github.com/sylvainHellin/ifc-bench) - Benchmark for evaluating AI comprehension and reasoning over IFC models using curated models and question-answer pairs.
- [BimReq](https://github.com/dsd-sztaki-hu/BimReq) - Ontology-based representation of construction regulations and requirements that can support symbolic and neuro-symbolic BIM compliance systems.
- [pygaeb](https://github.com/frameIQ/pygaeb) - Python parser for GAEB construction data with support for LLM-assisted classification of construction items.
- [aware](https://github.com/aware-aeco/aware) - Open-source agentic substrate for AECO (Architecture, Engineering, Construction, Operations).
- [CAD2BIM](https://github.com/alvin528/CAD2BIM) - LLM and VLM agent skill for converting floor plans into IFC, GLB, OBJ, and STL.

### LLM agents and natural-language interfaces

- [ArchSight AIOS](https://github.com/ArchSightLabs/archsight-aios) - Agent and workflow toolkit for BIM, IFC, document retrieval, and RAG-based construction knowledge work.
- [Construction AI Agent](https://github.com/tayyabmughal676/Construction_AI_Agent) - Experimental agentic system for automating construction-industry workflows.
- [OpenConstructionEstimate](https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR) - Multilingual construction cost knowledge base designed for use with AI assistants and construction-estimation agents.
- [Geospatial Code Agent](https://github.com/aws-samples/sample-geospatial-code-agent) - Natural-language agent that generates and executes geospatial analysis workflows over satellite and spatial data.
- [SAP AAS MCP Server](https://github.com/SAP/aas-mcp-server) - MCP adapter exposing Asset Administration Shell APIs as Model Context Protocol tools for language models.
- [rhino-mcp](https://github.com/tanishqbhattad/rhino-mcp) - MCP server for controlling Rhino with Claude, ChatGPT, or any MCP client, exposing 3D modeling tools.
- [opentakeoff](https://github.com/Kentucky-ai/opentakeoff) - Open-source PDF takeoff engine for construction and flooring, built for AI agents to drive natively.
- [PLAXIS-MCP](https://github.com/yixuanzhong/PLAXIS-MCP) - MCP server for PLAXIS 2D geotechnical engineering remote scripting.
- [renoolab-agent-skills](https://github.com/mehdimicra/renoolab-agent-skills) - Agent skills for renovation and construction trades (BTP), connected via MCP.
- [Claude Skills for Computational Designers](https://github.com/marcinfinitesimal533/Claude-skills-for-Computational-Designers) - Claude Code skills for computational design, parametric modeling, simulation, and BIM scripting.

### Computer vision for construction

- [AECVision](https://github.com/PawelKinczyk/AECVision) - Computer-vision project for detecting construction and architectural elements in drawings and site imagery.
- [BD3 Dataset](https://github.com/Praveenkottari/BD3-Dataset) - Annotated building-defect image dataset for training and evaluating automatic inspection models.
- [Construction Site Image Dataset](https://github.com/pangyuteng/construction-site-image-dataset) - Annotated images of construction activities and objects for computer-vision research.
- [OpenConstruction Datasets](https://github.com/ruoxinx/OpenConstruction-Datasets) - Collection of datasets for construction-scene understanding and visual recognition.
- [Open3D-ML](https://github.com/isl-org/Open3D-ML) - Machine-learning extension to Open3D for semantic segmentation and object detection in 3D data.
- [MinkowskiEngine](https://github.com/NVIDIA/MinkowskiEngine) - Sparse tensor deep-learning library widely used for semantic segmentation and learning from large point clouds.
- [MMDetection3D](https://github.com/open-mmlab/mmdetection3d) - Open-source framework for 3D object detection and semantic segmentation using point clouds and multimodal data.
- [Torch Points3D](https://github.com/torch-points3d/torch-points3d) - PyTorch framework for machine learning on point clouds and 3D spatial data.
- [Segment Anything](https://github.com/facebookresearch/segment-anything) - Foundation segmentation model frequently adapted for buildings, defects, drawings, satellite imagery, and construction-site analysis.
- [Grounding DINO](https://github.com/IDEA-Research/GroundingDINO) - Open-set object detection model using text prompts, useful for construction and built-environment image analysis.
- [Ultralytics](https://github.com/ultralytics/ultralytics) - Computer-vision framework providing YOLO models for object detection, segmentation, tracking, and pose estimation.
- [Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection) - Enhances construction site safety using YOLO to detect hazards such as missing PPE.

### Generative design and spatial intelligence

- [House-GAN++](https://github.com/ennauata/houseganpp) - Graph-constrained generative model for producing residential floor plans.
- [Graph2Plan](https://github.com/HanHan55/Graph2plan) - Deep-learning method for generating floor plans from layout graphs and building boundaries.
- [Floor-SP](https://github.com/woodfrog/floor-sp) - Deep structured model for reconstructing floor plans from indoor point clouds.
- [RoomFormer](https://github.com/ywyue/RoomFormer) - Transformer-based model for reconstructing structured floor plans from point-cloud data.
- [HEAT](https://github.com/woodfrog/heat) - Holistic edge-attention transformer for reconstructing building wireframes and floor-plan geometry.
- [Structured3D](https://github.com/bertjiazheng/Structured3D) - Large synthetic dataset and tools for structured indoor scene understanding and layout reconstruction.
- [AI4CAD](https://github.com/gudo7208/awesome-ai4cad) - Curated collection of research and implementations covering AI for CAD, BIM, geometric modelling, and engineering design.
- [DeepCAD](https://github.com/ChrisWu1997/DeepCAD) - Generative deep-learning system for representing and generating CAD construction sequences.
- [cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot) - AI-native CAD/CAE workbench for AI agents, covering text-to-CAD and text-to-CAE workflows.
- [gcs](https://github.com/samsilverman/gcs) - Python library for generating 3D meshes of generalized cylindrical shells.

### Building control and reinforcement learning

- [CityLearn](https://github.com/intelligent-environments-lab/CityLearn) - Gymnasium environment for multi-agent reinforcement learning in building energy coordination and urban demand response.
- [BOPTEST](https://github.com/ibpsa/project1-boptest) - Standardised framework for testing and benchmarking advanced building-control strategies using detailed simulation models.
- [BOPTEST-Gym](https://github.com/ibpsa/project1-boptest-gym) - Gymnasium interface for training and evaluating reinforcement-learning controllers with BOPTEST building models.
- [Sinergym](https://github.com/ugr-sail/sinergym) - Gymnasium environment connecting reinforcement-learning algorithms with EnergyPlus building simulations.
- [GridLearn](https://github.com/apigott/GridLearn) - Multi-agent reinforcement-learning testbed for building energy coordination, demand response, and power-flow analysis.
- [HV-Ai-C](https://github.com/VectorInstitute/HV-Ai-C) - Reinforcement-learning framework and experiments for intelligent HVAC control.
- [RL Building Control](https://github.com/rdnfn/rl-building-control) - Curated collection of reinforcement-learning environments and projects for building automation and energy management.
- [Building Load Forecasting](https://github.com/climatechange-ai-tutorials/building-load-forecasting) - Reproducible tutorial for applying machine learning to building energy-demand forecasting.
- [Building Control with BOPTEST](https://github.com/climatechange-ai-tutorials/building-control-boptest) - Tutorial demonstrating reinforcement learning for building control using BOPTEST.
- [CityLearn Tutorial](https://github.com/climatechange-ai-tutorials/citylearn) - Practical introduction to reinforcement-learning control for grid-interactive buildings and communities.
- [Counterfactual Models for Energy Saving](https://github.com/climatechange-ai-tutorials/counterfactual-models-energy-saving) - Machine-learning workflow for measurement and verification of building energy savings.

### GeoAI and urban intelligence

- [TorchGeo](https://github.com/microsoft/torchgeo) - PyTorch library providing geospatial datasets, samplers, transforms, and pretrained models for machine learning.
- [GeoAI](https://github.com/opengeos/geoai) - Python package integrating artificial intelligence with satellite imagery, aerial photography, vector data, and geospatial analysis.
- [TerraTorch](https://github.com/IBM/terratorch) - Toolkit for fine-tuning and evaluating geospatial foundation models.
- [Prithvi](https://github.com/NASA-IMPACT/hls-foundation-os) - Foundation model and workflows for Earth-observation imagery developed around harmonised Landsat and Sentinel data.
- [Clay Foundation Model](https://github.com/Clay-foundation/model) - Open geospatial foundation model for extracting representations from Earth-observation data.
- [SatMAE](https://github.com/sustainlab-group/SatMAE) - Masked autoencoder for learning general representations from temporal and multispectral satellite imagery.
- [Scale-MAE](https://github.com/bair-climate-initiative/scale-mae) - Scale-aware masked autoencoder for learning from remote-sensing imagery at different spatial resolutions.
- [GeoSeg](https://github.com/WangLibo1995/GeoSeg) - Semantic-segmentation framework for buildings, roads, land cover, and other features in remote-sensing imagery.
- [GlobalBuildingAtlas](https://github.com/zhu-xlab/GlobalBuildingAtlas) - Resources associated with large-scale mapping of building footprints and heights.
- [Awesome Urban Foundation Models](https://github.com/usail-hkust/Awesome-Urban-Foundation-Models) - Curated literature and resources covering foundation models for urban planning, mobility, energy, environment, and public services.
- [Awesome Remote-Sensing Foundation Models](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models) - Collection of remote-sensing foundation models, benchmarks, datasets, and fine-tuning frameworks.
- [city2graph](https://github.com/c2g-dev/city2graph) - Transforms geospatial relations into graphs for graph neural networks and spatial network analysis.
- [rs-embed](https://github.com/cybergis/rs-embed) - One-line access to remote sensing foundation model embeddings for any place and time.
- [Geospatial Foundation Models on AWS](https://github.com/aws-samples/sample-geospatial-foundation-models-on-aws) - Reference implementations for using geospatial foundation models on AWS for earth-scale monitoring.
- [orthoseg](https://github.com/orthoseg/orthoseg) - Train neural networks to segment orthophotos.
- [CesiumJS AI Starter App](https://github.com/CesiumGS/cesiumjs-ai-starter-app) - Starter template for building LLM-powered 3D globe applications with CesiumJS and tool calling.
- [geoai-skills](https://github.com/muend/geoai-skills) - Agent skills for GeoAI and geospatial data science, covering remote sensing, spatial statistics, and PostGIS.

### AI benchmarks and datasets

- [IFCNet](https://ifcnet.e3d.rwth-aachen.de/) - IFC component dataset for machine-learning classification and representation learning.
- [BuildingNet](https://github.com/buildingnet/buildingnet_dataset) - Large-scale annotated building-model dataset for semantic segmentation and component understanding.
- [ArchShapesNet](https://i3l.seoultech.ac.kr/subList/20000005729) - Dataset of BIM elements for deep-learning-based component classification.
- [BIMNet](https://github.com/LydJason/BIMNet) - Benchmark for reconstructing BIM models from real-world point clouds.
- [SpaceNet](https://github.com/SpaceNetChallenge) - Benchmark datasets and challenges for building extraction, road detection, and geospatial machine learning.
- [Microsoft Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) - Global building-footprint dataset produced using machine-learning models over satellite imagery.
- [PANGAEA](https://github.com/VMarsocci/pangaea-bench) - Benchmark for evaluating geospatial foundation models across diverse Earth-observation tasks.
- [Japan Construction Cost Database](https://github.com/ogasurfproject-jpg/japan-construction-cost-database) - Open dataset of construction and renovation costs in Japan, based on 30 years of industry data.

### Foundation models for the built environment

#### Built-environment and AEC models

- [AECBench](https://github.com/ArchiAI-LAB/AECBench) - Open benchmark for evaluating large language models across architecture, engineering, and construction knowledge, reasoning, calculation, and professional application tasks.
- [AEC-Bench](https://github.com/nomic-ai/aec-bench) - Multimodal benchmark for evaluating agentic AI systems on real-world architecture, engineering, and construction tasks, including drawing understanding, cross-sheet reasoning, and project-level coordination.
- [LLMs for CAD Survey and Taxonomy](https://github.com/lichengzhanguom/LLMs-CAD-Survey-Taxonomy) - Collection of research on large language models for CAD generation, editing, understanding, and engineering-design workflows.
- [TRELLIS](https://github.com/microsoft/TRELLIS) - Large-scale pretrained model for generating and editing structured 3D assets from text and images.

#### Urban and geospatial foundation models

- [Awesome Location Intelligence](https://github.com/CityMind-Lab/Awesome-Location-Intelligence) - Collection of urban and geospatial representation-learning models, including UrbanCLIP, CityFM, ReFound, and urban vision-language models.

### Neuro-symbolic AI

#### Built-environment applications

- [IDPO](https://github.com/RUB-Informatik-im-Bauwesen/idpo) - Information Delivery Processes Ontology for formally representing information exchanges and delivery processes in construction.
- [LOIN Ontology](https://github.com/RUB-Informatik-im-Bauwesen/loin-ontology) - Formal representation of Levels of Information Need, aligned with EN 17412-1 and buildingSMART IDS.
- [IoC Process Ontology](https://github.com/Internet-of-Construction/IoC-Process-Ontology) - Ontological representation of construction processes and associated process data.
- [Digital Buildings](https://github.com/google/digitalbuildings) - Ontology and software tools for representing building systems, equipment, relationships, and telemetry.

#### Supporting semantic web and neuro-symbolic frameworks

- [SymbolicAI](https://github.com/ExtensityAI/symbolicai) - Framework for combining large language models with symbolic expressions, constraints, computation, and structured reasoning.
- [DeepProbLog](https://github.com/ML-KULeuven/deepproblog) - Neuro-symbolic framework combining neural networks with probabilistic logic programming.
- [Logic Tensor Networks](https://github.com/logictensornetworks/logictensornetworks) - Framework integrating neural learning with first-order logical constraints.
- [Neural Theorem Provers](https://github.com/uclnlp/ntp) - Differentiable reasoning system for learning and inference over knowledge bases.
- [PyReason](https://github.com/lab-v2/pyreason) - Explainable temporal and graph-based symbolic reasoning framework.
- [SHACL](https://github.com/w3c/data-shapes) - W3C resources for validating RDF knowledge graphs against formal constraints.
- [pySHACL](https://github.com/RDFLib/pySHACL) - Python validator for applying SHACL constraints and rules to RDF knowledge graphs.

### NLP for construction and the built environment

#### Language models and evaluation

- [DesignQA](https://github.com/AutodeskAILab/DesignQA) - Multimodal benchmark for evaluating machine understanding of engineering drawings and technical documentation.

#### Supporting NLP frameworks

- [spaCy](https://github.com/explosion/spaCy) - Industrial NLP framework for named-entity recognition, text classification, dependency parsing, and custom domain pipelines.
- [Flair](https://github.com/flairNLP/flair) - NLP framework supporting named-entity recognition, classification, relation extraction, and contextual embeddings.
- [Haystack](https://github.com/deepset-ai/haystack) - Framework for retrieval-augmented generation, document search, question answering, and agent pipelines.
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data and retrieval framework for connecting LLMs to documents, databases, knowledge graphs, and structured project information.
- [LangChain](https://github.com/langchain-ai/langchain) - Framework for developing LLM applications involving retrieval, tools, structured outputs, and agents.
- [GraphRAG](https://github.com/microsoft/graphrag) - Graph-based retrieval framework for extracting entities, relationships, communities, and grounded answers from document collections.

### RAG for AEC documents

- [les_rag_public](https://github.com/proovcme/les_rag_public) - Local-first engineering RAG with CAD/BIM JSON exporters and a standalone viewer.

### Structural health monitoring and anomaly detection

- [sgsim](https://github.com/Sajad-Hussaini/sgsim) - Simulation and analysis of ground motions for structural and earthquake engineering.

### Time-series forecasting for building energy

- [ha-energy-forecast](https://github.com/m-zenker/ha-energy-forecast) - Home Assistant app forecasting household electricity consumption 48 hours ahead.
- [gridsense](https://github.com/PrajitMittal16/gridsense) - 7-day building energy forecasting using a stacked LSTM and XGBoost model with SHAP explanations.
- [hass.tibber_prices](https://github.com/jpawlowski/hass.tibber_prices) - Home Assistant integration providing detailed electricity price sensors for demand-response use cases.

### Multi-agent systems for construction

- [AssetOpsBench](https://github.com/IBM/AssetOpsBench) - Industry 4.0 benchmark and framework for building, orchestrating, and evaluating asset-operations agents.

### Synthetic data generation

#### Built-environment synthetic datasets

- [ResBIM](https://github.com/RogerLiang0725/ResBIM) - Synthetic dataset containing more than 1,000 paired parametric BIM models and annotated 2D floor plans for BIM automation and 2D-to-BIM reconstruction.
- [InteriorNet](https://github.com/InteriorNet/InteriorNet) - Large synthetic indoor dataset for scene understanding, localisation, depth estimation, and visual navigation.
- [Hypersim](https://github.com/apple/ml-hypersim) - Photorealistic synthetic indoor-scene dataset with geometry, depth, surface normals, semantic labels, and lighting information.
- [SceneNet RGB-D](https://github.com/jmccormac/SceneNetRGB-D) - Synthetic RGB-D dataset for indoor semantic segmentation and scene understanding.
- [Synthinel-1](https://github.com/tum-lmf/Synthinel-1) - Synthetic overhead imagery dataset for building segmentation and remote-sensing research.
- [SYNTHIA](https://github.com/AndresCarranza/Extended-SYNTHIA) - Synthetic urban imagery dataset with pixel-level semantic annotations.

#### Synthetic-data generation tools

- [BlenderProc](https://github.com/DLR-RM/BlenderProc) - Procedural Blender pipeline for generating photorealistic, automatically annotated computer-vision training data.
- [BlenderSynth](https://github.com/OllieBoyne/BlenderSynth) - Python framework for generating synthetic image datasets and labels through Blender.
- [Kubric](https://github.com/google-research/kubric) - Scalable pipeline for generating synthetic image and video datasets with object, depth, optical-flow, and segmentation annotations.
- [Omniverse Replicator](https://github.com/NVIDIA-Omniverse/Replicator) - Synthetic-data generation framework for physically based simulation, sensor data, robotics, and computer vision.
- [Unity Perception](https://github.com/Unity-Technologies/com.unity.perception) - Tools for creating labelled synthetic image datasets using configurable Unity environments.
- [CARLA](https://github.com/carla-simulator/carla) - Open urban-driving simulator capable of producing synthetic sensor, traffic, pedestrian, building, and street-scene data.
- [AirSim](https://github.com/microsoft/AirSim) - Simulation environment for drones, vehicles, cameras, LiDAR, and autonomous-system training.
- [HELIOS++](https://github.com/3dgeo-heidelberg/helios) - Virtual laser-scanning simulator for producing synthetic airborne, mobile, terrestrial, and indoor point clouds.
- [BlenSor](https://github.com/jg-rosenfeld/blensor) - Blender-based sensor simulator for generating synthetic LiDAR, depth-camera, and point-cloud data.
- [Salingo Virtual 3D Scanner](https://github.com/salingo/virtual-3d-scanner) - Virtual scanner for producing synthetic RGB-D observations and point clouds from 3D models.
- [SynthCity](https://github.com/vanderschaarlab/synthcity) - General synthetic-data generation framework for tabular and sequential datasets, potentially applicable to building energy, asset, and operational data.

### AI bias and fairness in construction

Research, datasets, auditing tools, and methods for identifying and mitigating unfair or systematically distorted AI outcomes affecting construction workers, professionals, organisations, communities, building occupants, and urban populations. For built-environment-specific resources relevant to geographic and representation bias, see Awesome Urban Foundation Models and Awesome Location Intelligence under Foundation models, and Microsoft Global ML Building Footprints and SpaceNet under AI benchmarks and datasets, above.

#### Fairness auditing and mitigation tools

- [Google Open Buildings Detection](https://github.com/google-research/google-research/tree/master/building_detection) - Building-detection methods and resources that can support analysis of regional performance disparities in satellite-derived building datasets.
- [AI Fairness 360](https://github.com/Trusted-AI/AIF360) - Toolkit containing fairness metrics, bias-detection methods, datasets, and mitigation algorithms.
- [Fairlearn](https://github.com/fairlearn/fairlearn) - Python toolkit for evaluating and mitigating unfair outcomes in machine-learning systems.
- [Aequitas](https://github.com/dssg/aequitas) - Bias-audit toolkit for examining disparities between demographic and population groups.
- [FairBench](https://github.com/mever-team/FairBench) - Fairness-evaluation framework providing a large collection of metrics and structured audit reports.
- [Holistic AI](https://github.com/holistic-ai/holisticai) - Toolkit for evaluating bias, fairness, explainability, robustness, security, and model efficacy.
- [What-If Tool](https://github.com/PAIR-code/what-if-tool) - Interactive tool for inspecting model behaviour, subgroup performance, counterfactuals, and fairness metrics.
- [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) - Collection of tools for error analysis, interpretability, fairness assessment, causal analysis, and responsible model development.
- [Folktables](https://github.com/socialfoundations/folktables) - Benchmark datasets derived from US Census data for evaluating fairness and distribution shifts across demographic and geographical groups.
- [LLM Fairness](https://github.com/junxu-ai/LLM_fairness) - Collection of datasets, methods, papers, and evaluation resources for studying bias and fairness in large language models.

---

## Datasets and benchmarks

### BIM and IFC

- [Example IFC Files Dataset](https://www.kaggle.com/datasets/claytonmiller/example-ifc-file) - Collection of IFC models used in BIM tutorials.
- [BIMData IFC dataset](https://github.com/bimdata/BIMData-Research-and-Development/blob/master/pages/IFC_FILES.md) - Collection of IFC models for development and testing.
- [buildingSMART IFC Datasets](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/ifc-datasets/) - BIM model datasets in IFC format.
- [IfcBench](https://huggingface.co/datasets/sylvainHellin/ifc-bench) - Benchmark dataset for IFC-based machine learning.
- [BuildingNet](https://buildingnet.org/) - Building model dataset for machine learning.
- [3DFacilities Dataset](https://www.sciencedirect.com/science/article/pii/S0926580524002942) - Dataset of structural and MEP BIM elements for research.
- [Open IFC Model Repository](https://github.com/opensourceBIM/TestFiles) - IFC test files for openBIM development.
- [xBIM Toolkit Examples](https://github.com/xBimTeam/XbimSamples) - BIM models used for xBIM development and tutorials.
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
- [EduBIM 2026](https://edubim2026.sciencesconf.org/) - Conference on BIM education and training in architecture, engineering, and construction.
- [ECPPM - European Conference on Product and Process Modelling](https://www.ecppm.org/) - Biennial conference on product and process modelling in the building and construction industry.

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
- [Linked Building Data Community Group](https://github.com/w3c-lbd-cg/lbd) - W3C Community Group site and resources for linked building data.

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
