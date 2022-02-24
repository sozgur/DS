/** product: calculate the product of an array of numbers. */

function product(nums, i = 0) {
  if (i > nums.length - 1) return 1;
  return nums[i] * product(nums, i + 1);
}

/** longest: return the length of the longest word in an array of words. */

function longest(words, i = 0, longOne = 0) {
  if (i > words.length - 1) return longOne;
  if (words[i].length > longOne) {
    longOne = words[i].length;
  }
  return longest(words, i + 1, longOne);
}

/** everyOther: return a string with every other letter. */

function everyOther(str, i = 0, l = []) {
  if (i > str.length - 1) return;
  l.push(str[i]);
  everyOther(str, i + 2, l);
  return l.join("");
}

/** isPalindrome: checks whether a string is a palindrome or not. */

function isPalindrome(str, l = 0, r = str.length - 1) {
  if (l >= r) return true;
  if (str[l] !== str[r]) return false;
  return isPalindrome(str, l + 1, r - 1);
}

/** findIndex: return the index of val in arr (or -1 if val is not present). */

function findIndex(arr, val, i = 0) {
  if (i > arr.length - 1) return -1;
  if (arr[i] === val) return i;
  return findIndex(arr, val, i + 1);
}

/** revString: return a copy of a string, but in reverse. */

function revString(str, idx = 0, revStr = "") {
  if (str.length === revStr.length) return revStr;
  revStr += str[str.length - 1 - idx];
  return revString(str, idx + 1, revStr);
}

/** gatherStrings: given an object, return an array of all of the string values. */

function gatherStrings(obj, stValList = []) {
  const values = Object.values(obj);
  for (val of values) {
    if (typeof val === "string") {
      stValList.push(val);
    } else if (typeof val === "object") {
      gatherStrings(val, stValList);
    }
  }
  return stValList;
}

/** binarySearch: given a sorted array of numbers, and a value,
 * return the index of that value (or -1 if val is not present). */

function binarySearch(arr, val, l = 0, r = arr.length - 1) {
  if (l > r) {
    return -1;
  }
  const mid = Math.floor((l + r) / 2);
  if (arr[mid] === val) {
    return mid;
  } else if (arr[mid] > val) {
    return binarySearch(arr, val, (l = l), (r = mid - 1));
  } else {
    return binarySearch(arr, val, (l = mid + 1), (r = r));
  }
}

module.exports = {
  product,
  longest,
  everyOther,
  isPalindrome,
  findIndex,
  revString,
  gatherStrings,
  binarySearch,
};
