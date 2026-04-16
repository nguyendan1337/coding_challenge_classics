"""
Proximity Routing System

You are building a proximity-based routing system for datacenters.

Each datacenter has:
- id (string)
- latitude (float)
- longitude (float)
- capacity (int): maximum number of requests it can handle
- current_load (int): number of requests currently being handled

-----------------------
Part 1: Registry
-----------------------
Implement a way to register datacenters.

-----------------------
Part 2: Distance Function
-----------------------
Implement a function to compute the distance between two coordinates.

Use Euclidean distance:
    d = sqrt((lat1 - lat2)^2 + (lon1 - lon2)^2)

-----------------------
Part 3: Routing
-----------------------
Given a request location (lat, lon):

1. Find the nearest datacenter with available capacity.
2. If the nearest is full, check the next nearest, and so on.
3. Return:
   - the selected datacenter id
   - the path (list of datacenter ids checked in order)

-----------------------
Constraints / Edge Cases:
-----------------------
- If no datacenters exist, return None
- If all datacenters are full, return None
- If multiple datacenters are at the same distance, choose the one with the smaller id
- Capacity must be enforced (increment load when selected)
"""
import math


"""
Expected Output:
Test 1: {'datacenter': 'dc1', 'path': ['dc1']}
Test 2: {'datacenter': 'dc3', 'path': ['dc1', 'dc3']}
Test 3: {'datacenter': 'dc2', 'path': ['dc1', 'dc3', 'dc2']}
Test 4: {'datacenter': 'dc2', 'path': ['dc1', 'dc3', 'dc2']}
Test 5: None
"""
def run_test(router):
    # Register datacenters
    router.register("dc1", 10, 10, capacity=1)
    router.register("dc2", 20, 20, capacity=2)
    router.register("dc3", 15, 15, capacity=1)

    # First request (should go to dc1 - closest)
    result1 = router.route(12, 12)
    print("Test 1:", result1)

    # Second request (dc1 now full → should go to dc3)
    result2 = router.route(12, 12)
    print("Test 2:", result2)

    # Third request (dc3 now full → should go to dc2)
    result3 = router.route(12, 12)
    print("Test 3:", result3)

    # Fourth request (dc1 & dc3 full, dc2 still has capacity)
    result4 = router.route(12, 12)
    print("Test 4:", result4)

    # Fifth request (all full → should return None)
    result5 = router.route(12, 12)
    print("Test 5:", result5)



"""
Solution
"""
class DataCenter:
    def __init__(self, id, latitude, longitude, capacity):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.capacity = capacity
        self.current_load = 0

class Router:
    def __init__(self):
        self.data_centers = {}

    def register(self, id, latitude, longitude, capacity):
        self.data_centers[id] = DataCenter(id, latitude, longitude, capacity)

    def distance(self, latitude_1, longitude_1, latitude_2, longitude_2):
        return math.sqrt( (latitude_1 - latitude_2) ** 2 + (longitude_1 - longitude_2) ** 2 )

    def route(self, request_latitude, request_longitude):
        if not self.data_centers:
            return None

        candidates = []
        for dc in self.data_centers.values():
            dist = self.distance(request_latitude, request_longitude, dc.latitude, dc.longitude)
            candidates.append((dc.id, dist, dc))

        candidates.sort(key=lambda x: (x[1], x[0]))

        path = []
        for candidate in candidates:
            path.append(candidate[0])
            if candidate[2].current_load < candidate[2].capacity:
                candidate[2].current_load += 1
                return candidate[0], path

        return None

router = Router()
run_test(router)