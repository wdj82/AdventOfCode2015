import parens from './input.js';

function calcHeight(parens) {
    let height = 0;
    for (let i = 0; i < parens.length; i++) {
        if (parens[i] === '(') {
            height += 1;
        } else {
            height -= 1;
        }
    }
    return height;
}

function enterBasement(parens) {
    let height = 0;
    for (let i = 0; i < parens.length; i++) {
        if (parens[i] === '(') {
            height += 1;
        } else {
            height -= 1;
        }
        if (height === -1) {
            return i + 1;
        }
    }
    return null;
}

console.log(calcHeight(parens));
console.log(enterBasement(parens));
