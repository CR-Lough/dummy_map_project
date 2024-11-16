import geopandas as gpd
import folium

# Read the GeoJSON file
gdf = gpd.read_file('data/data.geojson')

# First, ensure we know what CRS we're working with
print(f"Original CRS: {gdf.crs}")

# Project to Web Mercator for accurate centroid calculation
gdf_projected = gdf.to_crs(epsg=3857)

# Calculate centroid in projected coordinates
centroid = gdf_projected.geometry.centroid

# Convert centroid back to lat/lon (EPSG:4326)
centroid_latlon = centroid.to_crs(epsg=4326)

# Get the mean center point
center_lat = centroid_latlon.y.mean()
center_lon = centroid_latlon.x.mean()

# Create the map
m = folium.Map(location=[center_lat, center_lon], zoom_start=10)

# Add the GeoJSON to the map
folium.GeoJson(
    gdf,  # Use original unprojected data for display
    name='geojson'
).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Save the map
m.save('map.html')