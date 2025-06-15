"""
Question:  
Leetcode 853 - Car Fleet

There are `n` cars traveling to a destination called `target`, and you are given:
- `position[i]`: the starting position of the i-th car
- `speed[i]`: the speed of the i-th car

Each car moves at constant speed. A car **cannot pass** another car, but it may **catch up and form a fleet**, moving at the same speed as the slowest car in that group.

Return the number of **car fleets** that will arrive at the destination.

---

Approach: Sorting + Stack

- Pair up each car’s `(position, speed)` and sort the cars by **position in descending order** (i.e., closer to the destination first).
- For each car, compute the **time** it will take to reach the target: `(target - position) / speed`.
- Use a **stack** to track fleets:
    - If the current car's time to reach is **greater** than the fleet on top of the stack, it **cannot catch up** and forms a new fleet → push to stack.
    - Otherwise, it joins the fleet in front → do nothing.

Why this works:
- By processing cars from **closest to target to farthest**, we simulate each car seeing the car ahead and deciding whether it can catch up.
- The stack keeps the latest fleet arrival times.

Time Complexity: O(n log n) — for sorting the cars  
Space Complexity: O(n) — for the stack

Test Case:
Input: target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]  
Output: 3
"""

class Solution:
    def carFleet(self, target, position, speed):
        # Zip position and speed, then sort by position (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)

        stack = []
        for pos, spd in cars:
            time = float(target - pos) / spd

            # If current car takes longer, it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
                # else: current car joins previous fleet, no push needed

        return len(stack)
