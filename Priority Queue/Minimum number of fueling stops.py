def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        currentfuel=startFuel
        stops=0
        max_heap=[]
        for station in stations:
            position=station[0]
            fuel=station[1]

            while currentfuel<position:
                if len(max_heap)==0:
                    return -1
                max_fuel=heappop(max_heap)
                currentfuel+=(-max_fuel)
                stops+=1
            heappush(max_heap,-fuel)

        while currentfuel<target:
            if len(max_heap)==0:
                return -1
            max_fuel=heappop(max_heap)
            currentfuel+=(-max_fuel)
            stops+=1
        return stops
