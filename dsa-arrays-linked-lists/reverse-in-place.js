const LinkedList = require("./linked-list");

function reverseInPlace(l) {
    let node = null
    let currentNode = l.head

    while(currentNode) {
       
       let nextNode = currentNode.next
       currentNode.next = node
       node = currentNode    
       currentNode = nextNode      
    }
    
    return node
}

const l = new LinkedList([1,2,3])
const rl = reverseInPlace(l)

module.exports = {reverseInPlace}