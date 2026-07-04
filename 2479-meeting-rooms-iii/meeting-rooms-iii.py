class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        numOfMeetings=[0]*n
        emptyRooms=[i for i in range(n)]
        roomFilledTill=[]
        
        for startTime,endTime in meetings:
            roomNo=-1
            while roomFilledTill and roomFilledTill[0][0]<=startTime:
                _,rno=heapq.heappop(roomFilledTill)
                heapq.heappush(emptyRooms,rno)
            if emptyRooms:
                roomNo=heapq.heappop(emptyRooms)
                heapq.heappush(roomFilledTill,[endTime,roomNo])
            else:
                earliestFreeTime,roomNo=heapq.heappop(roomFilledTill)
                heapq.heappush(roomFilledTill,[earliestFreeTime-startTime+endTime,roomNo])
            #print(startTime,':',endTime,'\n',roomNo,'\n',emptyRooms,'\n',roomFilledTill,'\n','\n','\n')
            numOfMeetings[roomNo]+=1
        maxMeetings=max(numOfMeetings)
        for i in range(n):
            if maxMeetings==numOfMeetings[i]:
                return i
            