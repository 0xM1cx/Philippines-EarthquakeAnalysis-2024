import folium


ph_lat = 12.8797
ph_lon = 121.7740


earthquake_data = [
    {'lat': 14.6042, 'lon': 121.0444, 'magnitude': 6.3},  # Luzon
    {'lat': 10.3000, 'lon': 125.1500, 'magnitude': 5.4},  # Visayas
    {'lat': 5.0000, 'lon': 120.0000, 'magnitude': 4.2},  # Mindanao
    # Add more entries as needed, ensuring each has a 'magnitude' key
    {'lat': 18.1500, 'lon': 122.3333, 'magnitude': 4.8},  # Sample entry
]


map = folium.Map(location=[ph_lat, ph_lon], zoom_start=5)


earthquake_markers = folium.FeatureGroup(name="Earthquakes")


for earthquake in earthquake_data:
  
  folium.CircleMarker(
      location=[earthquake['lat'], earthquake['lon']],
      radius=earthquake['magnitude'] * 3,  # Adjust scaling factor for marker size
      popup=f"Magnitude: {earthquake['magnitude']:.1f}",  # Format magnitude to one decimal
      color='red',
      fill_color='red',
      fill_opacity=0.7,
  ).add_to(earthquake_markers)


earthquake_markers.add_to(map)


try:
  map.add_layer_control()  
except AttributeError:
  
  layer_control = folium.LayerControl(positions='topleft')
  layer_control.add_to(earthquake_markers)  
  map.add_to(layer_control)


map