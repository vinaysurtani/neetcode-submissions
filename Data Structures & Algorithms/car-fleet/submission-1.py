class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p,s) for p,s in zip(position, speed)],reverse=True)
        print(cars)
        curtime = 0
        fleet = 0
        for car in cars:
            time = (target - car[0])/car[1]
            if curtime < time:
                fleet += 1
                curtime = time
        return fleet