class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #the maximum number of rooms that have simulataneous meetings
        #whenever we start a meeting we open a room
        #so that gives us count of open room
        #stopping a meeting closes a room and decrements the count of open rooms
        #so we sort the times and separate from start and end
        #intervals = [[1,2],[4,8],[5,6], [3,7]]
        start_time = [i[0] for i in intervals] #[1,3,4,5]
        end_time = [i[1] for i in intervals] #[2,6,7,8]

        start_time.sort() #[1,3,4,5]
        end_time.sort() #[2,6,7,8]
        #i=4
        #j=1
        #start_time[i]<end_time[j]: 5<6:T
        #count_rooms = 3
        #min_rooms = 3
        count_rooms = 0
        min_rooms = float('-inf')

        i = j = 0
        while i<len(start_time) and j<len(end_time):
            if start_time[i]<end_time[j]:
                count_rooms += 1
                min_rooms = max(count_rooms, min_rooms)
                i += 1
            else:
                #end_time is earlier than current start time
                count_rooms -= 1
                j += 1

        return min_rooms
 