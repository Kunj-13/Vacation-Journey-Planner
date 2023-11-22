# Vacation-Journey-Planner       Final Project 463 - Kunj Patel, Shiv Patel

# Project Report: Vacation Journey Planner

## Project Goals

The primary objective of the Vacation Journey Planner project is to provide users with an efficient and interactive way to plan their journeys between different cities. The project aims to calculate the shortest path between two selected cities and recommend 'happy spots'—key attractions and destinations—within these cities, thereby enhancing the overall travel experience.

## Significance of the Project

The project is significant in two main aspects: it facilitates efficient travel planning and enhances the happiness and satisfaction of travelers. By computing the shortest routes between cities and suggesting attractive landmarks and sites, the software not only saves time and resources but also enriches the travel experience. This aligns with the broader goal of improving happiness by providing joyful and stress-free travel experiences.

# Installation and Usage Instructions

1. **Installation**: To use the Vacation Journey Planner, users need to have Python and the Tkinter library installed on their computers. Tkinter comes pre-installed with Python.

2. **Usage**: Upon launching the program, users can select their starting and destination cities from drop-down menus. Clicking the "Find Path" button will display the shortest path, total distance, intermediate cities, and happy spots in the destination city.

## Code Structure

The code is structured around the `CityGraph` class, which manages city data and connections. The Dijkstra algorithm, implemented using the `heapq` module, calculates the shortest paths. The Tkinter library is utilized to create an interactive GUI. Key components include:

- `CityGraph` class for graph management.
- `find_path` function to handle path finding and GUI updates.
- Tkinter UI setup for user interaction.

## Functionalities and Test Results

- **Path Calculation**: The Dijkstra algorithm accurately calculates the shortest paths.
- **UI Interaction**: Users can easily select cities and view results.
- **Happy Spots Recommendations**: Displays tourist attractions in the destination city.
  
Test results demonstrate accurate path calculations and responsive UI elements.
First picture demonstrates the interative GUI where users can use the dropdown feature to selection the starting city and the destination city.

<img width="606" alt="Screenshot 2023-11-22 at 12 58 07 PM" src="https://github.com/Kunj-13/Vacation-Journey-Planner/assets/143433713/2d40fefc-aefb-4c96-9005-834a514d57ff">

The picture below shows the results that users achieve after selecting the starting and destination cities. In this example, it shows the user selected Los Angeles as starting city and New York as destination city. After that, the application shows the users the shortest route in this case it was Los Angeles to Chicago to New York while showing the total miles distance after calculation. Also, it displays famous spots to visit in New York which are Times Square and Central Park. 

<img width="608" alt="Screenshot 2023-11-22 at 12 58 33 PM" src="https://github.com/Kunj-13/Vacation-Journey-Planner/assets/143433713/8918dbed-b933-43d0-a755-3a14cae6a3b2">



## Discussion and Conclusions

The project successfully meets its objectives by providing efficient travel planning and enhancing user happiness through travel recommendations. However, it faces limitations like the static nature of city and connection data, and the absence of real-time traffic or weather conditions. The learnings from the course were effectively applied in implementing the Dijkstra algorithm and creating a user-friendly GUI. Future enhancements could include dynamic data updates and integration with real-time travel APIs.
