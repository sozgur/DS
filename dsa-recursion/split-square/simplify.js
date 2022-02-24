function simplify(s) {
    if (typeof s === "number") {
        return s;
    }

    s = s.map(simplify);

    if (Number.isInteger(s[0]) && s.every((q) => q === s[0])) {
        return s[0];
    } else {
        return s;
    }
}
