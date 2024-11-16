# Geographic Data Visualization Project

A Python-based project for visualizing geographic data using GeoJSON files and interactive maps.

## Overview

This project provides tools to visualize geographic data points and polygons on an interactive map using Python. It currently supports visualization of New York City landmarks and areas as a demonstration.

## Prerequisites

- Python 3.8 or higher
- Required Python packages (install via pip):
  - geopandas
  - folium
  - pandas

## Project Structure

    map_project/
    ├── data/
    │   └── data.geojson      # Sample geographic data
    ├── geomapping.py         # Main mapping logic
    ├── map.html             # Generated interactive map
    ├── pyproject.toml       # Project dependencies
    └── README.md           # This file

## Installation

1. Clone the repository:
```
git clone <repository-url>
cd map_project
```
2. Set up a Python virtual environment (optional but recommended):

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies:
```
pip install -r requirements.txt
```
## Usage

1. Run the mapping script:

    python geomapping.py

2. Open `map.html` in your web browser to view the interactive map.

## Data Format

The project uses GeoJSON files for geographic data. The sample data (`data/data.geojson`) includes:
- Points of interest (e.g., Central Park, Times Square)
- Area polygons (e.g., Manhattan District)

Each feature in the GeoJSON file includes:
- Geometry (Point or Polygon)
- Properties (name, type, area, etc.)

