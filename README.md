# Mapillary Extensions API

A FastAPI-based extension for the Mapillary Python SDK.

## Live API
**Production URL:** `https://mapillary-extensions.vercel.app`

## Features
- **Random Image Lookup**: Find a mapillary image ID within a specific radius of given coordinates.

## Endpoints

### `GET /random-image`
Fetches a random image ID near a location.

**Parameters:**
- `token`: Your Mapillary Access Token.
- `lat`: Latitude of the center point.
- `lng`: Longitude of the center point.
- `radius` (Optional): Search radius in meters (default: 500).

---

## Local Setup

1. **Create and activate virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run the development server:**
   ```powershell
   python main.py
   ```
   The API will be available at `http://localhost:5001`.
   Documentation is available at `http://localhost:5001/docs`.

## Deployment
This project is configured for Vercel using `pyproject.toml`. To deploy, push your changes to GitHub or use the Vercel CLI.
