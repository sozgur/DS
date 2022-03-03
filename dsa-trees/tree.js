/** TreeNode: node for a general tree. */

class TreeNode {
  constructor(val, children = []) {
    this.val = val;
    this.children = children;
  }
}

class Tree {
  constructor(root = null) {
    this.root = root;
  }

  /** sumValues(): add up all of the values in the tree. */

  sumValues() {
    let total = 0;
    if (this.root === null) {
      return total;
    }
    const stack = [this.root];
    while (stack.length > 0) {
      const node = stack.pop();
      total += node.val;
      if (node.children.length > 0) {
        stack.push(...node.children);
      }
    }
    return total;
  }

  /** countEvens(): count all of the nodes in the tree with even values. */

  countEvens() {
    let numberOfEven = 0;
    if (this.root === null) {
      return 0;
    }
    const stack = [this.root];
    while (stack.length > 0) {
      const node = stack.pop();
      if (node.val % 2 === 0) {
        numberOfEven++;
      }
      if (node.children.length > 0) {
        stack.push(...node.children);
      }
    }
    return numberOfEven;
  }

  /** numGreater(lowerBound): return a count of the number of nodes
   * whose value is greater than lowerBound. */

  numGreater(lowerBound) {
    let totalNumber = 0;
    if (this.root === null) {
      return 0;
    }
    const stack = [this.root];
    while (stack.length > 0) {
      const node = stack.pop();
      if (node.val > lowerBound) {
        totalNumber++;
      }
      if (node.children.length > 0) {
        stack.push(...node.children);
      }
    }
    return totalNumber;
  }
}

module.exports = { Tree, TreeNode };
