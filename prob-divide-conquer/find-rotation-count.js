function findRotationCount(arr) {
    if (arr.lenght === 1 || arr[0] < arr[arr.length - 1]) {
        return 0;
    }

    let [start, end] = [0, arr.length - 1];

    while (start <= end) {
        mid = Math.floor((start + end) / 2);
        if (arr[mid] < arr[mid - 1]) {
            return mid;
        } else if (arr[start] <= arr[mid]) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
}

module.exports = findRotationCount;
