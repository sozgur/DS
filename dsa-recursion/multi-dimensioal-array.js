function realSize(arrays) {
  let total = 0;
  for (let e of arrays) {
    if (Array.isArray(e) && e.length > 0) {
      total += realSize(e);
    } else if (Number.isInteger(e)) {
      total += 1;
    }
  }
  return total;
}

// const realSize = arr => arr.reduce((a, e) => a + (Array.isArray(e) ? realSize(e) : 1), 0);
