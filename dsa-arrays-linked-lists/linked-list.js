/** Node: node for a singly linked list. */

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

/** LinkedList: chained together nodes. */

class LinkedList {
  constructor(vals = []) {
    this.head = null;
    this.tail = null;
    this.length = 0;

    for (let val of vals) this.push(val);
  }

  _get(idx) {
    if(!this.head) {
      throw new Error("List is empty")
    } else {
      if (idx < 0) {
        throw new Error("index is not valid")
      }
      let currentNode = this.head
      while(idx > 0){
        idx--
        currentNode = currentNode.next
        if (!currentNode) {
          throw new Error("index is not valid")
        }
      }
      return currentNode
    }

  }

  /** push(val): add new value to end of list. */

  push(val) {
    const newNode = new Node(val)
    if(!this.head) {
      this.head = newNode
      this.tail = newNode
    } else {
      this.tail.next = newNode
      this.tail = newNode
    }
    this.length++
  }

  /** unshift(val): add new value to start of list. */

  unshift(val) {
    const newNode = new Node(val)
    if(!this.head) {
      this.head = newNode
      this.tail = newNode
    } else {
      newNode.next = this.head
      this.head = newNode
    }
    this.length++
  }

  /** pop(): return & remove last item. */

  pop() {
    if(!this.head) {
      throw new Error("List is empty")
    } else {
      const removeValue  = this.tail.val
      if(this.tail === this.head) { 
        this.head = null
        this.tail = null
      } else {
        let currentNode = this.head
        while(currentNode.next.next) {
          currentNode = currentNode.next
        }
        currentNode.next = null
        this.tail = currentNode
      }
      this.length--
      return removeValue 
    }

  }

  /** shift(): return & remove first item. */

  shift() {
    if(!this.head) {
      throw new Error("List is empty")
    } else {
      const removeValue = this.head.val
      if(this.tail === this.head) { 
        this.head = null
        this.tail = null
      } else {
        this.head = this.head.next
      }
      this.length--
      return removeValue
    }

  }

  /** getAt(idx): get val at idx. */

  getAt(idx) {
    return this._get(idx).val
  }

  /** setAt(idx, val): set val at idx to val */

  setAt(idx, val) {
    this._get(idx).val = val
  }

  /** insertAt(idx, val): add node w/val before idx. */

  insertAt(idx, val) {
    const newNode = new Node(val)
    if(idx === 0) {
      if(this.length === 0) {
        this.head = newNode
        this.tail = newNode
      } else {
        newNode.next = this.head
        this.head = newNode
      }
    } else {
      const prevNode = this._get(idx-1)
      const temp = prevNode.next
      prevNode.next = newNode
      newNode.next = temp
      if(!temp) {
        this.tail = newNode
      }
    }
    this.length++
    
  }

  /** removeAt(idx): return & remove item at idx, */

  removeAt(idx) {
    if(idx > this.length-1 || idx < 0) {
      throw new Error("index is not valid")
    }

    const removeNode = this._get(idx)

    // this is head
    if (idx === 0) {
      this.head = removeNode.next
      this.length--
      if(this.length === 0) {
        this.tail = null
      }
      return removeNode.val
    }
    
    // this is tail
    if (idx === this.length - 1) {
      const prevNode = this._get(idx-1)
      prevNode.next = null
      this.tail = prevNode
      this.length--
      return removeNode.val
    } 

    const prevNode = this._get(idx-1)
    prevNode.next = removeNode.next
    removeNode.next = null
    this.length--
    return removeNode.val

  }

  /** average(): return an average of all values in the list */

  average() {
    if (this.length === 0) return 0
    let currentNode = this.head
    let totalVal = 0
    while(currentNode) {
      totalVal += currentNode.val
      currentNode = currentNode.next
    }
    return totalVal/this.length
  }
}

module.exports = LinkedList;
