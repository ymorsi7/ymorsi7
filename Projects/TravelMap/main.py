import folium
from folium.plugins import MarkerCluster
from folium.features import CustomIcon

# List of routes with modes of travel
routes = [
    ("SAN", "SFO", "drive"),
    ("SFO", "SAN", "drive"),
    ("LAX", "MDW", "fly"),
    ("MDW", "LGA", "fly"),
    ("NYC", "ORF", "train"),
    ("ORF", "BWI", "fly"),
    ("BWI", "BOS", "fly"),
    ("BOS", "BNA", "fly"),
    ("BNA", "LAX", "fly"),
    ("SAN", "AUS", "fly"),
    ("AUS", "ATL", "fly"),
    ("ATL", "HOU", "fly"),
    ("HOU", "SAN", "fly"),
    ("SAN", "SFO", "drive"),
    ("SFO", "SAN", "drive"),
    ("LAX", "MDW", "fly"),
    ("MDW", "LAX", "fly"),
    ("SAN", "ORF", "fly"),
    ("ORF", "SAN", "fly"),
    ("LAX", "IST", "fly"),
    ("IST", "HBE", "fly"),
    ("HBE", "IST", "fly"),
    ("IST", "JFK", "fly"),
    ("JFK", "SAN", "fly"),
    ("SAN", "SFO", "drive"),
    ("SFO", "SAN", "drive"),
    ("SAN", "SFO", "drive"),
    ("SFO", "SAN", "drive"),
    ("SAN", "SFO", "drive"),
    ("SFO", "SAN", "drive"),
    ("SJC", "PDX", "fly"),
    ("PDX", "SJC", "fly"),
    ("SFO", "SAN", "fly"),
    ("SAN", "BWI", "fly"),
    ("BWI", "DC", "train"),
    ("BWI", "SAN", "fly"),
    ("SAN", "LHR", "fly"),
    ("LHR", "CAI", "fly"),
    ("CAI", "VIE", "fly"),
    ("VIE", "SFO", "fly"),
    ("SFO", "SAN", "fly"),
    ("SNA", "ORD", "fly"),
    ("ORD", "SNA", "fly"),
    ("SAN", "SJC", "fly"),
    ("SJC", "SAN", "fly"),
    ("LAX", "WSW", "fly"),
    ("WSW", "CAI", "fly"),
    ("HBE", "JED", "fly"),
    ("JED", "MED", "drive"),
    ("MED", "JED", "drive"),
    ("JED", "DXB", "fly"),
    ("DXB", "RUH", "fly"),
    ("RUH", "HBE", "fly")
]

# Initialize map centered at SAN
map_center = (32.7157, -117.1611)  # SAN coordinates
my_map = folium.Map(location=map_center, zoom_start=5)
marker_cluster = MarkerCluster().add_to(my_map)

# Predefined coordinates for locations to avoid SSL issues
coordinates = {
    "SAN": (32.7157, -117.1611),
    "SFO": (37.7749, -122.4194),
    "LAX": (33.9416, -118.4085),
    "MDW": (41.7868, -87.7522),
    "LGA": (40.7769, -73.8740),
    "NYC": (40.7128, -74.0060),
    "ORF": (36.8508, -76.2859),
    "ORF": (36.8946, -76.2012),
    "BWI": (39.1754, -76.6684),
    "BOS": (42.3601, -71.0589),
    "BNA": (36.1627, -86.7816),
    "AUS": (30.2672, -97.7431),
    "ATL": (33.7490, -84.3880),
    "HOU": (29.7604, -95.3698),
    "IST": (41.0082, 28.9784),
    "HBE": (31.2001, 29.9187),
    "JFK": (40.6413, -73.7781),
    "SJC": (37.3382, -121.8863),
    "PDX": (45.5152, -122.6784),
    "LHR": (51.4700, -0.4543),
    "CAI": (30.0444, 31.2357),
    "VIE": (48.2082, 16.3738),
    "WSW": (26.0, 50.55),
    "JED": (21.4858, 39.1925),
    "MED": (24.5247, 39.5692),
    "DXB": (25.276987, 55.296249),
    "RUH": (24.7136, 46.6753),
    "DC": (38.9072, -77.0369),
    "ORD": (41.9742, -87.9073),
    "SNA": (33.6757, -117.8678)
}

# Icons for modes of travel
icons = {
    "fly": "https://cdn-icons-png.flaticon.com/512/194/194918.png",
    "drive": "https://cdn-icons-png.flaticon.com/512/194/194932.png",
    "train": "https://cdn-icons-png.flaticon.com/512/194/194933.png"
}

for start, end, mode in routes:
    start_coords = coordinates.get(start)
    end_coords = coordinates.get(end)

    if start_coords and end_coords:
        # Add markers for start and end locations with custom icons
        folium.Marker(location=start_coords, popup=start, icon=CustomIcon(icons[mode], icon_size=(30, 30))).add_to(marker_cluster)
        folium.Marker(location=end_coords, popup=end, icon=CustomIcon(icons[mode], icon_size=(30, 30))).add_to(marker_cluster)

        # Add animated line
        line_color = "blue" if mode == "fly" else "green" if mode == "drive" else "red"
        folium.PolyLine(locations=[start_coords, end_coords], color=line_color, weight=2.5).add_to(my_map)

# Save map
my_map.save("Projects/TravelMap/flight_routes.html")
print("Map saved as flight_routes.html")