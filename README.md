# WFS Fetcher

A tool to fetch, process, and save features from a WFS (Web Feature Service) into various formats.

## Installation

1. **Install Poetry** if you haven't already:
   ```bash
   sudo apt install python3-poetry
2. **Clone the repository** (if you haven't already):


3. **Install dependencies:**
Poetry will automatically handle the installation of dependencies, including the necessary packages and their versions:
```bash
poetry lock
poetry install
```

## Usage
To run the tool:
```bash
poetry run wfs-fetcher --url <WFS_URL> --format <FORMAT> --output-dir <OUTPUT_DIR>
```

Replace **<WFS_URL>** with the URL of the WFS service, **<FORMAT>** with the desired output format (GeoJSON, GeoPackage, or Shapefile), and **<OUTPUT_DIR>** with the directory where you want to save the output files.


This setup ensures that the project is well-organized, modular, and easy to maintain, with dependency management handled by Poetry.