class BrowserHistory {
    constructor(homepage) {
        this.history = [];
        this.future = [];
        this.history.push(homepage);
    }

    visit(url) {
        this.history.push(url);
        this.future = [];
    }

    back(steps) {
        while (steps > 0 && this.history.length > 1) {
            const page = this.history.pop();
            this.future.push(page);
            steps--;
        }
        return this.history[this.history.length - 1];
    }

    forward(steps) {
        while (steps > 0 && this.future.length > 0) {
            const page = this.future.pop();
            this.history.push(page);
            steps--;
        }
        return this.history[this.history.length - 1];
    }
}

module.exports = BrowserHistory;
