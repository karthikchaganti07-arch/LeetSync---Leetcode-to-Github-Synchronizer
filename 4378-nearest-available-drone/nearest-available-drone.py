class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target
        min_distance = float("inf")
        nearest_index = -1
        for i, (x, y, r) in enumerate(drones):
            distance = abs(x - tx) + abs(y - ty)
            if distance <= r and distance < min_distance:
                min_distance = distance
                nearest_index = i
        return nearest_index