function add(s1, s2) {
    if (Number.isInteger(s1) && Number.isInteger(s2)) {
        return s1 | s2;
    }

    if (Number.isInteger(s1)) {
        s1 = [s1, s1, s1, s1];
    }

    if (Number.isInteger(s2)) {
        s2 = [s2, s2, s2, s2];
    }

    return [
        add(s1[0], s2[0]),
        add(s1[1], s2[1]),
        add(s1[2], s2[2]),
        add(s1[3], s2[3]),
    ];
}

let s1 = [0, [1, 1, 1, 1], [0, 0, 0, 0], 1];
let s2 = [1, [1, 0, 1, [0, [0, 0, 0, 0], 1, 1]], [1, 0, 1, 0], 1];

const r = add(s1, s2);
r;
