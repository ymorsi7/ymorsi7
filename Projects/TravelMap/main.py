import folium
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster

# List of routes with modes of travel
routes = [
    ("SAN", "SFO", "drive"),
    ("SFO", "SAN", "drive"),
    ("LAX", "MDW", "fly"),
    ("MDW", "LGA", "fly"),
    ("NYC", "Norfolk Virginia", "train"),
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
    ("JED", "Medina", "drive"),
    ("Medina", "JED", "drive"),
    ("JED", "DXB", "fly"),
    ("DXB", "Riyadh", "fly"),
    ("Riyadh", "HBE", "fly")
]

# Initialize map centered at SAN
map_center = (32.7157, -117.1611)  # SAN coordinates
my_map = folium.Map(location=map_center, zoom_start=5)
marker_cluster = MarkerCluster().add_to(my_map)

def get_coordinates(location):
    """Geocodes a location to get its latitude and longitude."""
    geolocator = Nominatim(user_agent="flight_mapper")
    try:
        location_obj = geolocator.geocode(location)
        return (location_obj.latitude, location_obj.longitude)
    except:
        return None

for start, end, mode in routes:
    start_coords = get_coordinates(start)
    end_coords = get_coordinates(end)

    if start_coords and end_coords:
        # Add markers for start and end locations
        folium.Marker(location=start_coords, popup=start).add_to(marker_cluster)
        folium.Marker(location=end_coords, popup=end).add_to(marker_cluster)

        # Add route line
        line_color = "blue" if mode == "fly" else "green" if mode == "drive" else "red"
        folium.PolyLine(locations=[start_coords, end_coords], color=line_color, weight=2.5).add_to(my_map)

# Save map
my_map.save("flight_routes.html")
print("Map saved as flight_routes.html")
