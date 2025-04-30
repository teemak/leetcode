/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isCompleteTree = function(root) {
     if (!root) return false

  let q = [root]
  let seenNull = false

  while (q.length > 0) {
    let node = q.shift()

    if (!node) {
      seenNull = true
    } else {
      if (seenNull) {
        return false
      }
      q.push(node.left)
      q.push(node.right)
    }

  }

  return true
};
    