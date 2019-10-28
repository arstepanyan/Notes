"""
Consider a coodrinate system for the Milky Way, in which Earth is at (0, 0, 0).
Model stars as points, and assume distances are in light years.
The Milky Way consists of approximately 10^12 stars, and their coordinates are stored in a file.

How would you compte the k stars which are closest to Earth?
"""

import math
import heapq


class Star:
    def __inint__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    # def __lt__(self, star):
    #     return self.distance < star.distance


# Time = O(n log k), Extra Space = O(k)
def k_closest(stars, k):
    max_heap = []
    for el in stars:
        heapq.heappush(max_heap, (-el.distance, el))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    # Return the distance as well for debugging
    return [((star[1].x, star[1].y, star[1].z), round(star[1].distance, 2)) for star in max_heap]


if __name__ == "__main__":
    import random

    x_coord = random.sample(range(100), 10)
    y_coord = random.sample(range(100), 10)
    z_coord = random.sample(range(100), 10)

    stars = []
    for (x, y, z) in zip(x_coord, y_coord, z_coord):
        star = Star()
        star.x, star.y, star.z = x, y, z
        stars.append(star)

    # Print the distances
    for star in stars:
        print(round(star.distance, 2))

    k_closest = k_closest(stars, 3)
    print(k_closest)
