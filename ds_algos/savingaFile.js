const twoSumClosest = (nums, target) => {
    // O(nlogn) 
    const sorted = nums.sort((a, b) => a - b)
    // initialize the two pointers

    let l = 0;
    let r = sorted.length - 1; 
    let min = Infinity;

    // while left pointer is less than right pointer (l and r meet in the middle)
    while (l <= r) {
        // initialize a sum to left and right elements
        const sum = sorted[l] + sorted[r];
        // initialize a measure of the distance between our sum and target
        // NOTE - the sign is super important for how we move our pointers
        const distance = target - sum
        // the return condition 
        if (Math.abs(distance) < min && Math.abs(distance) >= 0) { // <-- Is distance between  0 and min?
        // If it is, reassign min and closestSum
        min = Math.abs(distance)
        closestSum = sum
        // Additionally, if the min is 0, return closestSum immediately
        if (min === 0) return closestSum;
        }
        // If sum is less that target, increase left
        if (distance > 0) { 
        l++;
        // else decrease right!
        } else {
        r--;
        }
    }
    return closestSum
};

// console.log(twoSumClosest([2,-2,1], 4))
// console.log(twoSumClosest([2, -3, -6, 7, 4], 3))
console.log(twoSumClosest([3, 1, 4, 3], 6))

module.exports = {twoSumClosest};