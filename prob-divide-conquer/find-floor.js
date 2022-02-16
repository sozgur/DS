function findFloor(arr, num, low = 0, high = arr.length - 1) {
    if (low > high) return -1;
    if (num > arr[high]) return arr[high];

    let mid = Math.floor((low + high) / 2);

    if (arr[mid] === num) return arr[mid];
    if (arr[mid] < num && arr[mid + 1] > num) return arr[mid];

    if (arr[mid] > num) {
        return findFloor(arr, num, low, mid - 1);
    }

    return findFloor(arr, num, mid + 1, high);
}

module.exports = findFloor;
