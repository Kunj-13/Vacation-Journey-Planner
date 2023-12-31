# Vacation-Journey-Planner       Final Project 463 - Kunj Patel, Shiv Patel

# Project Report: Vacation Journey Planner

## Project Goals

The primary objective of the Vacation Journey Planner application is to provide users with an efficient and interactive way to plan their journeys between different cities. The project aims to calculate the shortest path between two selected cities using Dijkstra's algorithm and recommend 'happy spots'—key attractions and destinations—within these cities, thereby enhancing the overall travel experience.

## Significance of the Project

Our Vacation Journey Planner application stands out for its meaningful contribution to enhancing the user's travel experience by recommending "happy spots" in destination cities. This unique feature elevates the application from being just a shortest route planner to an exciting travel guide, offering personalized and engaging travel suggestions. These recommendations not only cater to individual preferences but also promote a sense of happiness and joy, fostering a deeper connection with discovery of local attractions. This aspect of the project significantly amplifies the overall happiness and satisfaction of travelers, making it a valuable tool for anyone seeking a more fulfilling travel experience.

## Installation and Usage Instructions

1. **Installation**: To use the Vacation Journey Planner, users need to have any IDE that supports Python and the Tkinter library installed on their computers. They will not have to worry about installing Tkinter because it comes pre-installed with Python. 

2. **Usage**: Upon launching the program, users can select their starting and destination cities from drop-down menus. Clicking the "Find Path" button will display the shortest path, total distance, intermediate cities, and happy spots in the destination city.

## Code Structure

This code implements a vacation journey planner using Dijkstra's algorithm in Python with a graphical user interface (GUI) created using Tkinter. It allows users to select a starting city and a destination city, then calculates the shortest path and total distance between these cities.

## Code Structure and Explanation

1. **Class `CityGraph`:** Handles the graph data structure.
    - `__init__`: Initializes the graph with empty sets and dictionaries.
    - `add_city`: Adds a city to the graph.
    - `connect_cities`: Connects two cities with a given distance.
    - `calculate_shortest_distances`: Implements Dijkstra's algorithm to find the shortest path between two cities.

2. **Function `find_path`:** Interacts with the GUI to display the shortest path and distance.
    - Retrieves cities from the GUI.
    - Calls `calculate_shortest_distances` to get the path and distance.
    - Formats and displays the result on the GUI.

3. **Tkinter GUI Setup:**
    - Initializes the Tkinter window.
    - Sets up the `CityGraph` instance and adds cities and connections.
    - Defines happy spots for each city.
    - Creates UI elements like labels, combo boxes for city selection, a button to find paths, and a label to display results.

4. **Main Loop:**
    - `window.mainloop()` starts the Tkinter event loop.

## Dijkstra's Algorithm Explanation

Dijkstra's algorithm is used here in the `calculate_shortest_distances` method to find the shortest path between two cities. The steps are as follows:

**Initialization:** 
    - A priority queue (`priority_queue`) is used to efficiently retrieve the next city with the shortest known distance.
    - A dictionary (`distances`) tracks the shortest known distance to each city, initialized to infinity for all cities except the start city (set to 0).
    - Another dictionary (`previous_city`) tracks the previous city on the shortest path to each city.

**Algorithm Loop:** 
    - The city with the smallest known distance is popped from the priority queue.
    - If this city is the destination, the algorithm stops.
    - Otherwise, for each neighboring city, if the distance through the current city is shorter than the known distance, update the distance and add the neighbor to the priority queue.

**Path Reconstruction:**
    - Once the destination is reached or determined to be unreachable, the path is reconstructed in reverse using the `previous_city` dictionary.
    - The path and the total distance are returned.

Dijkstra's algorithm is very efficient and works well for applications like finding the shortest path in a network of cities. 

## Functionalities and Test Results

- **Path Calculation**: The Dijkstra algorithm accurately calculates the shortest paths between starting city and the destination.
- **UI Interaction**: Users can easily select cities using the dropdown box and view results.
- **Display of Travel Route:** Once a route is calculated, the application displays the path along with the total distance.
- **Happy Spots Recommendations**: Displays tourist attractions in the destination city.
  
Test results demonstrate accurate path calculations and responsive UI elements.
First picture demonstrates the interative GUI where users can use the dropdown feature to selection the starting city and the destination city.

<img width="606" alt="Screenshot 2023-11-22 at 12 58 07 PM" src="https://github.com/Kunj-13/Vacation-Journey-Planner/assets/143433713/2d40fefc-aefb-4c96-9005-834a514d57ff">

The picture below shows the results that users achieve after selecting the starting and destination cities. In this example, it shows the user selected Los Angeles as starting city and New York as destination city. After that, the application shows the users the shortest route in this case it was Los Angeles to Chicago to New York while showing the total miles distance after calculation. Also, it displays famous spots to visit in New York which are Times Square and Central Park. 

<img width="608" alt="Screenshot 2023-11-22 at 12 58 33 PM" src="https://github.com/Kunj-13/Vacation-Journey-Planner/assets/143433713/8918dbed-b933-43d0-a755-3a14cae6a3b2">



## Discussion and Conclusions

The project successfully meets its objectives by providing efficient travel planning and enhancing user happiness through travel recommendations. However, it faces some limitations like the static city and connection data, and the absence of real-time traffic or weather conditions. For instance, users are only provided limited selections of cities, however, it is still very valuable application that can help tremendously in planning trips. The learnings from the course were effectively applied in implementing the Dijkstra algorithm and creating a user-friendly GUI. Future enhancements could include dynamic data updates and integration with real-time travel APIs.
