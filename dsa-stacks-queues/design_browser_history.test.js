const BrowserHistory = require("./design_browser_history");

describe("Test Browser History", function () {
  it("will add some history and work back and forward", function () {
    browser = new BrowserHistory("google.com");
    browser.visit("leetcode.com");
    browser.visit("facebook.com");
    expect(browser.back(2)).toBe("google.com");
    expect(browser.back(5)).toBe("google.com");
    expect(browser.forward(1)).toBe("leetcode.com");
    expect(browser.forward(4)).toBe("facebook.com");
    expect(browser.back(1)).toBe("leetcode.com");
    browser.visit("ebay.com");
    expect(browser.forward(1)).toBe("ebay.com");
  });
});
