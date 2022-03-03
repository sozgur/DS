/** BinaryTreeNode: node for a general tree. */

class BinaryTreeNode {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

class BinaryTree {
  constructor(root = null) {
    this.root = root;
  }

  /** minDepth(): return the minimum depth of the tree -- that is,
   * the length of the shortest path from the root to a leaf. */

  minDepth() {
    if (!this.root) return 0;

    function minDepthHelper(node) {
      if (!node.left && !node.right) {
        return 1;
      }
      if (node.right && !node.left) return minDepthHelper(node.right) + 1;
      if (node.left && !node.right) return minDepthHelper(node.left) + 1;
      return (
        Math.min(minDepthHelper(node.left), minDepthHelper(node.right)) + 1
      );
    }

    return minDepthHelper(this.root);
  }

  /** maxDepth(): return the maximum depth of the tree -- that is,
   * the length of the longest path from the root to a leaf. */

  maxDepth() {
    if (!this.root) return 0;

    function helperMaxDepth(node) {
      if (!node.right && !node.left) return 1;
      if (!node.right && node.left) return helperMaxDepth(node.left) + 1;
      if (!node.left && node.right) return helperMaxDepth(node.right) + 1;
      return (
        Math.max(helperMaxDepth(node.left), helperMaxDepth(node.right)) + 1
      );
    }

    return helperMaxDepth(this.root);
  }

  /** maxSum(): return the maximum sum you can obtain by traveling along a path in the tree.
   * The path doesn't need to start at the root, but you can't visit a node more than once. */

  maxSum() {
    let result = 0;
    function helperMaxSum(node) {
      if (node === null) return 0;
      const leftSum = helperMaxSum(node.left);
      const rightSum = helperMaxSum(node.right);
      result = Math.max(result, leftSum + rightSum + node.val);
      return Math.max(0, leftSum + node.val, rightSum + node.val);
    }
    helperMaxSum(this.root);
    return result;
  }

  /** nextLarger(lowerBound): return the smallest value in the tree
   * which is larger than lowerBound. Return null if no such value exists. */

  nextLarger(lowerBound) {
    let largerNum = null;

    function helperFindLarger(node) {
      if (node === null) return largerNum;
      if (node.val > lowerBound && largerNum) {
        largerNum = Math.min(node.val, largerNum);
      } else if (node.val > lowerBound && !largerNum) {
        largerNum = node.val;
      }

      helperFindLarger(node.left);
      helperFindLarger(node.right);
      return largerNum;
    }
    helperFindLarger(this.root);
    return largerNum;
  }

  /** Further study!
   * areCousins(node1, node2): determine whether two nodes are cousins
   * (i.e. are at the same level but have different parents. ) */

  areCousins(node1, node2) {
    if (this.root === node1 || this.root === node2) return false;

    function helperFindLevelAndParent(
      nodeToFind,
      currentNode,
      level = 0,
      data = { level: 0, parent: null }
    ) {
      if (currentNode.left === nodeToFind || currentNode.right === nodeToFind) {
        data.level = level + 1;
        data.parent = currentNode;
        return data;
      }
      if (currentNode.left !== null) {
        helperFindLevelAndParent(nodeToFind, currentNode.left, level + 1, data);
      }
      if (currentNode.right !== null) {
        helperFindLevelAndParent(
          nodeToFind,
          currentNode.right,
          level + 1,
          data
        );
      }
      return data;
    }
    // data: {level, parent}
    const data1 = helperFindLevelAndParent(node1, this.root);
    const data2 = helperFindLevelAndParent(node2, this.root);
    if (
      data1 &&
      data2 &&
      data1.level === data2.level &&
      data1.parent !== data2.parent
    ) {
      return true;
    }
    return false;
  }

  /** Further study!
   * serialize(tree): serialize the BinaryTree object tree into a array. */

  static serialize(tree) {
    const result = [];
    function helperTraverseBST(node) {
      if (node !== null) {
        result.push(node.val);
        helperTraverseBST(node.left);
        helperTraverseBST(node.right);
      } else {
        result.push(null);
      }
    }
    helperTraverseBST(tree.root);
    return result;
  }

  /** Further study!
   * deserialize(arr): deserialize array into a BinaryTree object. */

  static deserialize(arr) {
    if (arr.length < 0) {
      return null;
    }
    function buildTree() {
      const val = arr.shift();
      if (val === null) return null;

      const node = new BinaryTreeNode(val);
      node.left = buildTree();
      node.right = buildTree();
      return node;
    }

    const root = buildTree();
    return new BinaryTree(root);
  }

  /** Further study!
   * lowestCommonAncestor(node1, node2): find the lowest common ancestor
   * of two nodes in a binary tree. */

  lowestCommonAncestor(node1, node2, currentNode=this.root) {
    // base case 1: empty tree
    if (currentNode === null) return null;

    // base case 2: root is one of the target nodes
    if (currentNode === node1 || currentNode === node2) return currentNode;

    // recursively search the left sub-tree
    const left = this.lowestCommonAncestor(node1, node2, currentNode.left);

    // recursively search the right sub-tree
    const right = this.lowestCommonAncestor(node1, node2, currentNode.right);
    

    // if neither left nor right is null, currentNode is the ancestor
    if (left !== null && right !== null) return currentNode;
    
    // if one node is not null, return it
    if (left !== null || right !== null) return left || right;
    
    // left and right are both null, return null
    if (left === null && right === null) return null;
  }
}

module.exports = { BinaryTree, BinaryTreeNode };
