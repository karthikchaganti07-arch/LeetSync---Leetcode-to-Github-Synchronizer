class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start

        dist = sum(distance[start:destination])
        total = sum(distance)
        c = total -dist
        return min(dist, c)