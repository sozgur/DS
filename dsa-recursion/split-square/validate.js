function validate(s) {
    if (s === 0 || s === 1) {
        return true;
    }

    if (Array.isArray(s) && s.length === 4) {
        return s.every(validate);
    }

    return false;
}
