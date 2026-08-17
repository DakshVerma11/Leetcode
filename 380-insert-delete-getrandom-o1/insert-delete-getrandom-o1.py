class RandomizedSet:
        def __init__(self):
            self.nums = []
            self.index = {}

        def insert(self, val: int) -> bool:
            if val in self.index:
                return False

            self.index[val] = len(self.nums)
            self.nums.append(val)

            return True

        def remove(self, val: int) -> bool:
            if val not in self.index:
                return False

            idx = self.index[val]
            last_val = self.nums[-1]

            # Move last element into the position of val
            self.nums[idx] = last_val
            self.index[last_val] = idx

            # Remove last element
            self.nums.pop()
            del self.index[val]

            return True

        def getRandom(self) -> int:
            return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()