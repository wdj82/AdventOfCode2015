import input from './input.js';

const strings = input.split('\n');

function isNice(string) {
    let vowelCount = 0;
    let hasDoubleLetter = false;
    for (let i = 0; i < string.length; i++) {
        const char = string[i];
        const nextChar = string[i + 1];
        const twoChars = char + nextChar;

        if (nextChar && (twoChars === 'ab' || twoChars === 'cd' || twoChars === 'pq' || twoChars === 'xy')) {
            return false;
        }
        if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
            vowelCount += 1;
        }
        if (char === nextChar) {
            hasDoubleLetter = true;
        }
    }
    return hasDoubleLetter && vowelCount >= 3;
}

function isNiceRegex(string) {
    const pairs = string.match(/([a-z][a-z])[a-z]*\1/)?.length;
    const repeat = string.match(/([a-z])[a-z]\1/)?.length;
    return repeat > 0 && pairs > 0;
}

function getNiceCount(strings) {
    return strings.reduce((count, string) => (isNiceRegex(string) ? count + 1 : count), 0);
}

console.log(getNiceCount(strings));
