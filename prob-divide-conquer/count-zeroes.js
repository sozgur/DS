function countZeroes(arr) {
    let firstZeroIdx = findFirstZeroIndx(arr, 0, arr.length - 1);

    if (firstZeroIdx === -1) {
        return 0;
    }

    return arr.length - firstZeroIdx;
}

function findFirstZeroIndx(arr, left = 0, right = arr.length - 1) {
    while (left <= right) {
        let middle = Math.floor((left + right) / 2);

        if ((middle === 0 || arr[middle - 1] === 1) && arr[middle] === 0) {
            return middle;
        } else if (arr[middle] === 1) {
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }
    return -1;
}

module.exports = countZeroes;
