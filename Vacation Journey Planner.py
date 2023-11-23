import tkinter as tk
from tkinter import ttk
import heapq
from collections import defaultdict

class CityGraph:
    def __init__(self):
        # Initialize the graph with sets and dictionaries to store cities and connections
        self.cities = set()
        self.connections = defaultdict(list)

    def add_city(self, name):
        self.cities.add(name)

    def connect_cities(self, city_a, city_b, distance):
        self.connections[city_a].append((city_b, distance))
        self.connections[city_b].append((city_a, distance))

    # Calculate the shortest distance between two cities using Dijkstra's algorithm
    def calculate_shortest_distances(self, start, end):
        if start not in self.cities or end not in self.cities:
            return float('inf'), []

        # Initialize distances and set up priority queue
        distances = {city: float('inf') for city in self.cities}
        distances[start] = 0
        priority_queue = [(0, start)]
        previous_city = {city: None for city in self.cities}

        while priority_queue:
            # Pop the city with the shortest distance from the queue
            current_distance, current_city = heapq.heappop(priority_queue)

            # Break if the end city is reached
            if current_city == end:
                break
                        
            # Update distances for neighboring cities
            for neighbor, neighbor_distance in self.connections[current_city]:
                distance = current_distance + neighbor_distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_city[neighbor] = current_city
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Construct the path from start to end
        path = []
        current = end
        if distances[current] == float('inf'):
            return float('inf'), path  # No path found

        while current is not None:
            path.append(current)
            current = previous_city[current]
        path.reverse()

        return distances[end], path

# Function to handle finding path and updating the GUI
def find_path():
    starting_city = start_city_var.get()
    destination_city = end_city_var.get()
    total_distance, path = city_graph.calculate_shortest_distances(starting_city, destination_city)

    result_text = ""
    if total_distance == float('inf'):
        result_text = f"No path found from {starting_city} to {destination_city}.\n"
    else:
        result_text = (f"Journey from {starting_city} to {destination_city}\n" +
                       "-" * 40 + "\n" +
                       f"Shortest path: {' -> '.join(path)}\n" +
                       f"Total distance: {total_distance} miles\n")

        if len(path) > 2:
            intermediate_cities = path[1:-1]
            result_text += "\nIntermediate Cities:\n"
            for city in intermediate_cities:
                result_text += f"  - {city}\n"
        else:
            result_text += "\nNo intermediate cities on this route.\n"

        if destination_city in happy_spots:
            result_text += f"\nSpots to enhance your happiness in {destination_city}:\n"
            for spot in happy_spots[destination_city]:
                result_text += f"  - {spot}\n"
        else:
            result_text += "  No happy spots listed for this city.\n"
        result_text += "-" * 40

    result_label.config(text=result_text)

# Create Tkinter window
window = tk.Tk()
window.title("Vacation Journey Planner")

# Create and set up city graph
city_graph = CityGraph()
cities = ["New York", "San Francisco", "Los Angeles", "Chicago", 
          "Seattle", "Miami", "Denver", "Boston", "Austin"]
for city in cities:
    city_graph.add_city(city)

# Connect cities
city_graph.connect_cities("New York", "San Francisco", 3000)
city_graph.connect_cities("New York", "Chicago", 1000)
city_graph.connect_cities("Los Angeles", "San Francisco", 500)
city_graph.connect_cities("Los Angeles", "Chicago", 2000)
city_graph.connect_cities("New York", "Seattle", 2500)
city_graph.connect_cities("San Francisco", "Miami", 3500)

# Define happy spots for each city
happy_spots = {
    "New York": ["Central Park", "Times Square"],
    "San Francisco": ["Golden Gate Park", "Fisherman's Wharf"],
    "Los Angeles": ["Griffith Observatory", "Santa Monica Pier"],
    "Chicago": ["Millennium Park", "Navy Pier"],
    "Seattle": ["Space Needle", "Pike Place Market"],
    "Miami": ["South Beach", "Art Deco Historic District"],
    "Denver": ["Red Rocks Park", "Denver Zoo"],
    "Boston": ["Freedom Trail", "Harvard University"],
    "Austin": ["Sixth Street", "Lady Bird Lake"]
               }

# UI Elements
start_city_var = tk.StringVar()
end_city_var = tk.StringVar()

tk.Label(window, text="Starting City:").grid(row=0, column=0, padx=10, pady=10)
start_city_entry = ttk.Combobox(window, textvariable=start_city_var, values=cities)
start_city_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Destination City:").grid(row=1, column=0, padx=10, pady=10)
end_city_entry = ttk.Combobox(window, textvariable=end_city_var, values=cities)
end_city_entry.grid(row=1, column=1, padx=10, pady=10)

find_path_button = tk.Button(window, text="Find Path", command=find_path)
find_path_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="", justify=tk.LEFT)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
