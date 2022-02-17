const LinkedList = require("./linked-list");
const { reverseInPlace }= require("./reverse-in-place");

describe("test reverse in place", function() {
  it("appends node and reverse in place", function() {
    let lst = new LinkedList();
    lst.push(5);
    lst.push(10);
    lst.push(15);

    // let rlst = reverseInPlace(lst)
    // expect(rlst.length).toBe(3);
    // expect(rlst.val).toBe(15);
    // expect(rlst.next.next.val).toBe(5);
 
  });
});
