import matplotlib.pyplot as plt
from skyfield.api import load, EarthSatellite
import numpy as np
from datetime import datetime

# Load only TRUTH satellites from file
def load_truth_tles(filename):
    satellites = []
    with open(filename, 'r') as f:
        content = f.read()
    
    # Split by lines
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        if lines[i].strip() == 'TRUTH':
            # Found a TRUTH satellite
            if i + 2 < len(lines):
                line1 = lines[i+1].strip()
                line2 = lines[i+2].strip()
                # Check if these look like TLE lines
                if line1.startswith('1 ') and line2.startswith('2 '):
                    try:
                        satellite = EarthSatellite(line1, line2, 'TRUTH')
                        satellites.append(satellite)
                        print(f"Loaded TRUTH satellite {len(satellites)}")
                    except Exception as e:
                        print(f"Error loading TRUTH satellite: {e}")
                i += 3
            else:
                i += 1
        else:
            i += 1
    
    return satellites

# Load only TRUTH satellites
satellites = load_truth_tles('TLEs.txt')
print(f"Loaded {len(satellites)} TRUTH satellites")

if len(satellites) == 0:
    print("No TRUTH satellites found. Check the file format.")
    exit()

# Load timescale
ts = load.timescale()

# Specific time: 2025-08-24 12:26:33 UTC
target_time = datetime(2025, 8, 24, 12, 26, 33)
t = ts.utc(target_time.year, target_time.month, target_time.day,
           target_time.hour, target_time.minute, target_time.second)

# Calculate positions
lons, lats = [], []
for i, sat in enumerate(satellites):
    try:
        geocentric = sat.at(t)
        subpoint = geocentric.subpoint()
        lon = subpoint.longitude.degrees
        lat = subpoint.latitude.degrees
        lons.append(lon)
        lats.append(lat)
        print(f"TRUTH {i+1}: Lon={lon:.6f}, Lat={lat:.6f}")
    except Exception as e:
        print(f"Error calculating position for satellite {i+1}: {e}")

# Plot
plt.figure(figsize=(10, 8))
plt.scatter(lons, lats, s=100, alpha=0.7)
plt.title(f'TRUTH Constellation at 12:26:33 UTC')
plt.xlabel('Longitude (degrees)')
plt.ylabel('Latitude (degrees)')
plt.grid(True)

# Add labels to each point
for i, (lon, lat) in enumerate(zip(lons, lats)):
    plt.annotate(f'{i+1}', (lon, lat), xytext=(5, 5), textcoords='offset points')

# Zoom in on the constellation area if we have points
if lons and lats:
    plt.xlim(min(lons)-1, max(lons)+1)
    plt.ylim(min(lats)-1, max(lats)+1)

plt.tight_layout()
plt.savefig('truth_constellation_12_26_33.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"\nTotal TRUTH satellites at 12:26:33: {len(lons)}")
print(f"Longitude range: {min(lons):.2f} to {max(lons):.2f}")
print(f"Latitude range: {min(lats):.2f} to {max(lats):.2f}")