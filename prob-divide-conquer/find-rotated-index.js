function findRotatedIndex(arr, num) {
    let pivot = findPivot(arr);
    if (pivot === 0) {
        return binarySearch(arr, 0, arr.length - 1);
    } else {
        if (binarySearch(arr, num, 0, pivot - 1) !== -1) {
            return binarySearch(arr, num, 0, pivot - 1);
        } else {
            return binarySearch(arr, num, pivot, arr.length - 1);
        }
    }
}

function binarySearch(arr, num, start, end) {
    while (start <= end) {
        let middle = Math.floor((start + end) / 2);
        if (arr[middle] < num) {
            start = middle + 1;
        } else if (arr[middle] > num) {
            end = middle - 1;
        } else {
            return middle;
        }
    }
    return -1;
}

function findPivot(arr) {
    if (arr[0] < arr[arr.length - 1] || arr.length === 1) {
        return 0;
    }
    let [left, right] = [0, arr.length - 1];

    while (left <= right) {
        let middle = Math.floor((left + right) / 2);
        if (arr[middle] > arr[middle + 1]) {
            return middle + 1;
        } else if (arr[middle] < arr[left]) {
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }
}

module.exports = findRotatedIndex;
