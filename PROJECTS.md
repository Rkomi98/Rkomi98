# Project guide

[← Back to my profile](README.md)

A deeper look at the applications, research, teaching materials, and experiments behind my public work.

## Public repository catalogue

The catalogue below covers **all 35 public repositories owned by this account as of 9 October 2026: 31 non-fork repositories and 4 forks**. It includes applications, research, teaching materials, personal experiments, and this profile repository. Non-fork repositories also include collaborative projects and adapted learning materials; project context and upstream attribution are described where relevant.

Descriptions reflect the published default-branch documentation and files. Each repository remains the reference for setup, requirements, datasets, and project status.

## AI applications and agent workflows

### [datapizzaAI-RAG](https://github.com/Rkomi98/datapizzaAI-RAG) — Documentation and FAQ assistant

A Retrieval-Augmented Generation chatbot for questions about **Datapizza-AI**. It combines local Markdown FAQs with an optional official-documentation integration through MCP, separating document ingestion from retrieval and answer generation.

The project includes semantic search, query rewriting, conversation memory, multilingual interface options, debugging tools, and both web and terminal entry points. Its stack centres on **Python, datapizza-ai, Streamlit, Qdrant, and Google Gemini**, with an OpenAI embedding path for the documentation integration. This is a practical example of connecting a knowledge base to a conversational application.

### [Retrieval-Challenge](https://github.com/Rkomi98/Retrieval-Challenge) — Learn retrieval through experiments

A guided exercise on **chunking, ingestion, embeddings, and retrieval**, using an Italian corpus about Qdrant and Pinecone. Participants complete a starter pipeline, compare fixed-size and structure-aware chunking, and experiment with local multilingual embedding models or OpenAI embeddings.

A separate evaluator reports **`hit@1`, `hit@2`, and `hit@3`** against questions with expected source files. The repository includes starter code, a reference solution, configuration, and a gold set. The focus is finding the right sources before adding answer generation, using **Python and Qdrant**.

### [VibeTalking](https://github.com/Rkomi98/VibeTalking) — Audio recording, transcription, and analysis

A terminal application for **Linux/Fedora** that records microphone audio through ALSA/`arecord`, then sends it through a **datapizza-ai/Gemini** pipeline for transcription, tone analysis, and summarisation. Results are saved as structured JSON alongside recording metadata.

It supports fixed-duration and interactive recording, plus a demo/local fallback for exercising the workflow without a working cloud configuration. The published implementation is a **Python CLI**, with separate audio, analysis, and configuration modules.

### [senior-blender-designer-plugin](https://github.com/Rkomi98/senior-blender-designer-plugin) — A staged AI workflow for Blender

A **Claude Code plugin/skill** targeting the official Blender MCP Server. It organises 3D work into brief, planning, blockout, modelling, UV/texturing, materials, lighting, rendering, critique, refinement, and export, with inspection between stages.

The repository combines workflow references with **Python/`bpy` QA scripts** for geometry, UVs, transforms, printability, and pre-export checks. It also covers FDM constraints and delivery formats, and documents how it works alongside the upstream `ra100/blender-claude-plugin`. The emphasis is on an inspectable creative process and destination-specific output.

## Education and AI adoption

### [Datapizza](https://github.com/Rkomi98/Datapizza) — Training materials, demonstrations, and workshop tools

A broad collection of public materials for **AI training and adoption**. It contains notebooks, tutorials, presentations, practical exercises, and demonstrations organised across training contexts.

Notable parts include:

- **[Datapizza-AI examples](https://github.com/Rkomi98/Datapizza/tree/main/DatapizzAI/PizzAI):** clients, multimodal calls, structured responses, conversation memory, tools, agents, and multi-agent examples.
- **[Ducati tutorials](https://github.com/Rkomi98/Datapizza/tree/main/Ducati):** introductory notebooks, chatbot/tool examples, and RAG materials with a reproducible Python environment.
- **[Training assessment](https://github.com/Rkomi98/Datapizza/tree/main/Assessment%20aula):** a bilingual Streamlit survey analyser with column detection, charts, optional AI insights, and spreadsheet export.
- **[Dashboard RAG](https://github.com/Rkomi98/Datapizza/tree/main/Mondadori/datapizza_dashboard_rag):** visual CSV exploration combined with natural-language questions, SQLite, local Qdrant, dataset-specific memory, and source previews.
- **Hackathon voting:** the root web application manages host/player roles, rooms, weighted voting criteria, timed rounds, and live leaderboards using **JavaScript and Firebase Realtime Database**.

Across the repository, the recurring stack includes **Python, Jupyter, datapizza-ai, Streamlit, Plotly, and web technologies**. The root README describes the voting application; the folders provide the wider teaching and demonstration context.

### [PrePostAula](https://github.com/Rkomi98/PrePostAula) — Training feedback and learning assessment

A bilingual **Streamlit** dashboard for analysing pre/post training survey exports from Microsoft Forms and similar tools. It accepts CSV/XLSX inputs, recognises changing column labels through keyword and fuzzy matching, and supports manual overrides.

It combines familiarity-transition Sankey charts, macro/micro quality analysis, time-to-apply views, optional AI summaries of open responses, and **Excel/CSV/Flourish-ready exports**. The stack includes **Python, pandas, Plotly, RapidFuzz, openpyxl, and optional OpenAI/Anthropic integrations**. It makes training outcomes easier to inspect and communicate.

### [Claude-101](https://github.com/Rkomi98/Claude-101) — An Italian learning notebook for Claude

An independent editorial learning site based on public Anthropic courses. It organises Italian notes into chapters with reading progress, light/dark themes, bookmarks, personal notes, and text-to-speech through the Web Speech API.

Markdown content is turned into a static payload for publication through **GitHub Actions/GitHub Pages**, with **JavaScript and React** in the interface. The public site provides course and chapter navigation, reading aids, and source attribution. It is an independent project, unaffiliated with Anthropic.

### [LearnSQL](https://github.com/Rkomi98/LearnSQL) — Purrfessor Cocoa, an AI-assisted SQL mentor

A playful SQL learning prototype themed around cats and chocolate. Learners write queries and receive reviews through a **Google Gemini** integration, with dedicated components for input, feedback, and a user profile.

Built with **React, TypeScript, Vite, and the Google GenAI SDK**, it explores a more approachable interface for technical learning. The repository includes local development instructions and documents its AI Studio origin.

### [DevPath](https://github.com/Rkomi98/DevPath) — Adaptive practice for Python coding interviews

A full-stack **MVP** that diagnoses a learner's starting point, selects daily coding challenges, and provides progressive help. Its documented catalogue contains **100 Python challenges across 25 algorithmic archetypes**, with ten levels, thirteen skills, visible/hidden tests, and seven levels of assistance.

The architecture combines **Next.js, React, TypeScript, Monaco Editor, Supabase Auth/PostgreSQL**, and an isolated Python runner using **Fastify/Docker**, with Judge0 as an alternative execution provider. It includes local setup, deployment guides, migrations, and validation tools. The learning design emphasises transferring reasoning between problems and reducing repeated patterns.

### [Mondadori](https://github.com/Rkomi98/Mondadori) — AI and data-science course proposals

Static web presentations of proposed training programmes for the publishing sector. The six-day programme covers AI literacy, prompt engineering, tool selection, ETL/data quality, anomaly detection, feature engineering, data visualisation, and governance or RAG/agents.

A separate proposal focuses on **AI-assisted data analysis, dashboards, and storytelling**. These **HTML/CSS/JavaScript** artefacts communicate a learning path and hands-on activities.

### [Unicredit](https://github.com/Rkomi98/Unicredit) — Showcase materials and an investigative learning game

Materials for the **Datapizza × Unicredit showcase of 23 June 2026**, with two independent deliverables. The first is a browser-based restaurant investigation in three phases: operational analysis, market context, and an investigation supported by documents and narrative evidence.

The second is a pair of Italian **Claude Code installation/configuration guides for Windows**, generated as Word documents with **Python and python-docx**. The repository brings together an interactive **HTML game**, exercise assets, and practical setup documentation.

## Geospatial research and environmental data

### [Point-Clouds-Data-Cleaning](https://github.com/Rkomi98/Point-Clouds-Data-Cleaning) — Master's thesis research on 6D point clouds

Research on removing **outliers, noise, and vegetation occlusions** from point clouds to support illegal-landfill detection and waste-volume estimation. The thesis context connects camera/LiDAR data processing to the European **PERIVALLON** project.

The published files include **Python scripts** for synthetic data generation and comparisons of methods such as SOR, ROR, DBSCAN, bilateral filtering, and other anomaly-detection approaches. The thesis abstract also discusses **RandLA-Net and PointNeXt** for vegetation segmentation and synthetic Blender datasets. It represents the research side of my work: data preparation, method comparison, and environmental applications.

### [Landslide](https://github.com/Rkomi98/Landslide) — Landslide susceptibility around Como

A collaborative academic project studying landslide susceptibility around Como and the southern Lake Como area. It uses **QGIS, spatial datasets, and Random Forest in R** to produce susceptibility maps and explore their relationship with exposed population.

The repository includes GIS projects, clipped raster/vector inputs, output maps, evaluation artefacts, and an **HTML/OpenLayers** presentation of the methodology and results. It documents the path from spatial predictors to a modelled environmental-risk map.

### [DECODE](https://github.com/Rkomi98/DECODE) — Flood damage exploration for buildings

**Damage Evaluation with Comprehensive Observation Data on Earth:** a dashboard prototype for exploring potential flood damage to insured buildings. It brings building attributes together with flood-related geographic layers, maps, damage categories, histograms, and data export.

Built with **Python, Dash, Plotly, and GeoPandas**, the published project uses synthetic building data to demonstrate the workflow. Its documentation distinguishes that demonstration from a planned user-upload flow. It connects spatial analysis with a concrete insurance-domain interface.

### [S4GEO](https://github.com/Rkomi98/S4GEO) — Air-quality information and analysis

A collaborative project for **Software Engineering for Geoinformatics** at Politecnico di Milano. The web application explores air-pollution observations and forecasts for **Skopje, Belgrade, Krakow, Paris, and London**.

Users can register, choose a city and data type, inspect stations on a map, query/filter observations, and access statistical analysis and exports. The implementation combines a **Python/Flask backend, PostgreSQL/PostGIS, notebooks, and HTML templates**, bringing spatial storage, data access, and analysis into one application.

### [AI4Good](https://github.com/Rkomi98/AI4Good) — GeoAI workshop experiments

A learning repository containing experiments from an **AI for Good workshop**, including a notebook adapted from upstream GeoAI/PDFM tutorial material. It explores **Population Dynamics Foundation Model embeddings**, Zillow housing data, regression/KNN models, and geographic visualisation.

The public files include the notebook, county boundaries, and county embeddings. Source context and tutorial attribution are provided in the notebook.

## Volleyball and sports technology

### [VolleyRef](https://github.com/Rkomi98/VolleyRef) — From official scoresheets to structured match data

An application that turns volleyball **PDF scoresheets** into structured starting line-ups, rotations, and service turns. Users compare extracted values with the original PDF, correct readings, validate volleyball rules, and export **Excel/CSV** results.

It separates a **Next.js/TypeScript frontend** from a **FastAPI backend** using PyMuPDF, OpenCV, Tesseract, Pydantic, and SQLite. Text-layer and raster/OCR extraction converge into a domain parser and validator. The repository also contains an **Electron desktop package** for running the interface and OCR backend locally. The central idea is a reviewable document-to-data workflow with human correction.

### [AppPedanaVolley](https://github.com/Rkomi98/AppPedanaVolley) — Force-platform acquisition and jump-test analysis

A **Python desktop MVP** for collecting signals from a BTS force platform through a **National Instruments USB-6211**. It displays vertical channels in real time, aggregates platform signals, records short tests, and exports raw measurements and metadata to CSV/Excel.

The stack includes **PySide6, pyqtgraph, nidaqmx, pandas, and openpyxl**, with both hardware and simulated acquisition. A terminal analysis flow supports SJ/CMJ/DJ tests, event detection, flight-time-based jump-height estimates, and asymmetry summaries. The README makes the current calibration boundary explicit: signals remain in volts, and actual NI acquisition requires a supported hardware environment.

### [AceDashboard](https://github.com/Rkomi98/AceDashboard) — Interactive volleyball match analysis

A **Dash** application for exploring match data from a **SQLite** scouting database. It visualises player efficiency, positivity, and action counts for attack, reception, and serve, alongside setter distribution on a court diagram.

Team, skill, and setter-position filters connect the underlying event/player/team tables to interactive views. The project combines **Python, Dash/Plotly, and SQL** to make scouting data readable through both statistical summaries and spatial representations.

### [CuneoWebsite.io](https://github.com/Rkomi98/CuneoWebsite.io) — Volleyball statistics portal and scouting tools

A collection centred on **Cuneo Granda Volley statistics**, with web pages for match/statistical views, scouting datasets, and supporting analysis tools. It includes **R/Shiny dashboards**, `datavolley` processing, Plotly visualisations, and Python scoreboard-related scripts.

The public tree spans A2/B1 statistics, team/player analysis, distribution views, and match-data utilities. Its **HTML/CSS/JavaScript, R, and Python** components show several stages of the scouting workflow.

### [TrainingApp](https://github.com/Rkomi98/TrainingApp) — Training exercise monitoring

A **React** web application for recording daily exercise scores and following progress over time. The documented flow includes user authentication, exercise logging, a dashboard, and progress visualisation.

Built with **JavaScript, React Router, and Chart.js**, with GitHub Pages deployment configuration, it focuses on recording training activities and following their evolution.

### [VolleyTorch](https://github.com/Rkomi98/VolleyTorch) — Volleyball action-recognition project presentation

A public presentation of a neural-network project for **volleyball action recognition**. The README explains the project and states that training data is not provided for privacy reasons.

The current public default branch contains the **README and licence**, so this entry describes the project context; model code, training data, and a reproducible training pipeline are not currently published in that branch.

### [Concorezzo](https://github.com/Rkomi98/Concorezzo) — Volleyball experience and visual storytelling

A presentation repository documenting work connected to **ASD Concorezzo Volley**, with a video reference and a linked **Flourish story**. It reflects the communication and visual-storytelling side of sports analysis.

The current public tree contains the README and licence, with media references in the presentation.

## Web applications and product experiments

### [NASA-NEO](https://github.com/Rkomi98/NASA-NEO) — Near-Earth Object data explorer

A full-stack dashboard developed for the **Arkemis NASA-NEO challenge**, turning **NASA NeoWs** data into a filterable object list, charts, and individual detail views. Its interface includes an Earth-centric orbital view, distance/time scatter plots, size distributions, and dark/light themes.

The **Next.js/TypeScript/ECharts** frontend talks to a **Python/FastAPI** proxy that handles NASA's seven-day request windows, file-based caching, retries, error mapping, and Prometheus metrics. The repository includes architecture/API documentation, screenshots, and a development wiki.

### [FAME](https://github.com/Rkomi98/FAME) — AI-assisted meal-planning exercise and prototype

A teaching/product experiment for turning a nutritionist's guidelines into weekly meal plans, recipes, and shopping lists. The repository includes workshop briefs and prompts for comparing AI-assisted application-building approaches, plus an implementation under **`Soluzione/`**.

That published solution uses **Python, Flask, SQLAlchemy, Flask-Login, PDF parsing, and web assets**, with documented integrations for AI-generated plans. The root brief proposes a FastAPI/React architecture, while the solution is Flask-based. This distinction captures both sides of the repository: the intended exercise and the implemented prototype.

### [VenTour](https://github.com/Rkomi98/VenTour) — Venture-capital hypermedia application

A collaborative **Politecnico di Milano Hypermedia Web Application project, academic year 2022/23**, created with Emma Lodetti and Nikolina Zallemi. It models a venture-capital company through investment areas, companies, team members, and their relationships.

The repository contains **Vue/Nuxt frontend components, a Node.js backend, database-related code**, and extensive design/implementation documentation. It connects information architecture, reusable interfaces, relational content, and desktop/mobile navigation.

## Personal lab and writing

### [PersonalProjects](https://github.com/Rkomi98/PersonalProjects) — A lab for small applications and deeper experiments

A multi-project workspace spanning geospatial data engineering, AI automation, volleyball logistics, interactive learning, games, and hardware documentation. The projects live in separate folders and have different scopes and maturity levels.

<details>
<summary><strong>Explore the projects inside PersonalProjects</strong></summary>

| Project or folder | What it explores |
| --- | --- |
| **[EO Notebook](https://github.com/Rkomi98/PersonalProjects/tree/main/EO%20Notebook)** | Sentinel-2 dataset engineering: STAC discovery, signed COG access, cloud masking, tiling, train/validation splits, Zarr/Parquet outputs, quality reports, and a lazy PyTorch data loader. Uses Python, xarray, Rasterio, GeoPandas, and PyTorch. |
| **[EO](https://github.com/Rkomi98/PersonalProjects/tree/main/EO)** | An educational InSAR web presentation covering complex SAR pixels, phase, line-of-sight displacement, coregistration, interferograms, topographic phase, and coherence. |
| **[Slide Generator](https://github.com/Rkomi98/PersonalProjects/tree/main/Slide%20Generator)** | Generates branded PowerPoint decks from a brief using datapizza-ai/OpenAI structured output, Pydantic slide models, python-pptx, and SVG-to-image conversion. |
| **[T2S con Mistral](https://github.com/Rkomi98/PersonalProjects/tree/main/T2S%20con%20Mistral)** | A terminal Markdown-to-speech pipeline using datapizza-ai and Voxtral, with reference-audio voice cloning, a local Linux/GPU runtime, and a documented Mistral API fallback. |
| **[MedStudent](https://github.com/Rkomi98/PersonalProjects/tree/main/MedStudent)** | A browser-based educational gastroenterology RPG: narrative scenes, exam-style quizzes, guided reasoning, progress persistence, and references to the source study material. |
| **[Scacchi](https://github.com/Rkomi98/PersonalProjects/tree/main/Scacchi)** | Two-player local chess on a shared device, with opposing player controls, legal moves, material advantage, and an optional clock. Built with React, Vite, chess.js, and react-chessboard. |
| **[chess-openings](https://github.com/Rkomi98/PersonalProjects/tree/main/chess-openings)** | An offline-capable opening trainer focused on plans and structures. It uses a JSON opening book and conceptual feedback; the Italian opening has an initial move tree and other openings are extensible stubs. |
| **[IrrigatoreSmart](https://github.com/Rkomi98/PersonalProjects/tree/main/IrrigatoreSmart)** | A documented DIY 24 VAC irrigation-controller project, with Arduino code, an Uno-to-ESP32 migration path, a control dashboard, bills of materials, cost sheets, and verification guides. |
| **[Dashboard partite](https://github.com/Rkomi98/PersonalProjects/tree/main/Dashboard%20partite)** | Volleyball schedules and logistics, with calendar data, venue maps, travel-distance summaries, and team-oriented web views. |
| **[Arkemis](https://github.com/Rkomi98/PersonalProjects/tree/main/Arkemis)** | Python experiments on path finding and sorting comparisons. |
| **[Experiments](https://github.com/Rkomi98/PersonalProjects/tree/main/Experiments)** | Small browser experiments across algorithms, ML, gradients, games, and interactive visual explanations. |
| **[SecretSanta](https://github.com/Rkomi98/PersonalProjects/tree/main/SecretSanta)** | A static gift microsite with a passport-style quiz, saved progress, and downloadable reading/audio material unlocked through the game. |
| **[Cernusco](https://github.com/Rkomi98/PersonalProjects/tree/main/Cernusco)** | A local catalogue presented as an HTML page. |
| **[Dieta](https://github.com/Rkomi98/PersonalProjects/tree/main/Dieta)** | A personal meal-plan HTML presentation. |
| **[Estate26](https://github.com/Rkomi98/PersonalProjects/tree/main/Estate26)** | Personal summer/birthday web pages. |
| **[Presentazioni](https://github.com/Rkomi98/PersonalProjects/tree/main/Presentazioni)** | A personal introduction web presentation. |

</details>

### [MyBlog](https://github.com/Rkomi98/MyBlog) — Articles and a bilingual publishing pipeline

The repository behind my **[personal blog](https://rkomi98.github.io/MyBlog/)**. A static generator turns Markdown source articles into an index and per-language pages, while preserving a separate landing page and supporting assets/PDFs.

Its **Node.js** tooling supports building and publishing to GitHub Pages, article metadata, and optional **Gemini-assisted Italian-to-English translation**. Translations are saved as regular Markdown files so subsequent builds can reuse them. It connects writing with a reproducible publication workflow.

### [Rkomi98](https://github.com/Rkomi98/Rkomi98) — This profile and portfolio index

The special GitHub profile repository whose **`README.md`** appears on my account overview. It brings together my background, technical interests, project catalogue, writing, and contact links as a single entry point into the other repositories.

## IoT and embedded systems

### [Ch04](https://github.com/Rkomi98/Ch04) — Wireless request/response simulation

An academic IoT challenge at Politecnico di Milano using **TinyOS/nesC**. Two motes exchange periodic requests and delayed responses, with message counters, acknowledgements, timer logic, and a fake sensor.

The repository includes message definitions, component wiring, application logic, and a **Python simulation script**. It documents event-driven embedded programming and how communication behaviour is exercised in simulation.

### [IoT_Ch03](https://github.com/Rkomi98/IoT_Ch03) — From mote events to an IoT dashboard

A Politecnico di Milano challenge that converts a numeric identifier into ternary digits and represents them through three LEDs in a **TinyOS** application. A **Cooja** simulation streams LED states over a serial connection.

**Node-RED** parses the values and publishes them through **MQTT to ThingSpeak**, where they are charted. The project covers the path from an embedded timer/event to a networked visualisation.

## Forks and upstream projects

These four repositories are **forks**, with their upstream projects and original authors credited below. They extend the catalogue into 3D annotation, mobile mapping, embedded systems, and Flutter interfaces.

| My fork | Original project | Purpose and technologies |
| --- | --- | --- |
| **[3d-bat](https://github.com/Rkomi98/3d-bat)** | [walzimmer/3d-bat](https://github.com/walzimmer/3d-bat) | 3D Bounding Box Annotation Tool for point-cloud and image labelling; a TypeScript-based tool relevant to 3D data annotation. |
| **[flutter_map](https://github.com/Rkomi98/flutter_map)** | [fleaflet/flutter_map](https://github.com/fleaflet/flutter_map) | A Dart/Flutter mapping widget inspired by Leaflet, for interactive maps in mobile applications. |
| **[SmartBracelet](https://github.com/Rkomi98/SmartBracelet)** | [POLIMI-Project/SmartBracelet](https://github.com/POLIMI-Project/SmartBracelet) | A collaborative academic smart-bracelet simulation with pairing, child/parent communication, and falling/missing alerts using TinyOS, Cooja, and Node-RED. The fork's default branch is `help`. |
| **[Flutter_Login_Registration_UI](https://github.com/Rkomi98/Flutter_Login_Registration_UI)** | [RajatPalankar8/Flutter_Login_Registration_UI](https://github.com/RajatPalankar8/Flutter_Login_Registration_UI) | A Flutter/Dart login and registration interface example, useful as a mobile UI reference. |

---

<sub>Reviewed: 9 October 2026. Private work is summarised by capability in the profile; this guide links to public projects only.</sub>
