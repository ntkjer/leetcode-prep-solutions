class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        free_rooms = list() 
        intervals.sort(key = lambda x: x[0])
        free_rooms.append(intervals[0][1])

        for interval in intervals[1:]:
            if interval[0] >= free_rooms[0]:
                heappop(free_rooms)

            heappush(free_rooms, interval[1])

        return len(free_rooms)