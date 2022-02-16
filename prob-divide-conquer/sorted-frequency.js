function sortedFrequency(arr, num) {
    let anyIndx = findAnyIndx(arr, num);
    if (anyIndx === -1) {
        return -1;
    }

    let [left, right] = [anyIndx, anyIndx];
    let total = 0;

    // Calculate left side
    while (left > 0) {
        if (arr[left - 1] === num) {
            total++;
            left--;
        } else {
            break;
        }
    }

    // Calculate right side
    while (right < arr.length - 1) {
        if (arr[right + 1] === num) {
            total++;
            right++;
        } else {
            break;
        }
    }

    return total + 1;
}

function findAnyIndx(arr, num) {
    let [left, right] = [0, arr.length - 1];

    while (left <= right) {
        let middle = Math.floor((left + right) / 2);
        if (arr[middle] === num) {
            return middle;
        } else if (arr[middle] > num) {
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }
    return -1;
}

module.exports = sortedFrequency;
