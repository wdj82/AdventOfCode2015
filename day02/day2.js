import input from './input.js';

// const input = `2x3x4
// 1x1x10`;

const inputArray = input.split('\n');

function getSquareFeetWrapping(dimensions) {
    return dimensions.reduce((total, present) => {
        const [length, width, height] = present.split('x');
        const side1 = length * width;
        const side2 = width * height;
        const side3 = height * length;
        const slack = Math.min(side1, side2, side3);
        return total + 2 * (side1 + side2 + side3) + slack;
    }, 0);
}

function getFeetRibbon(dimensions) {
    return dimensions.reduce((total, present) => {
        // get the dimensions, convert to numbers and sort them
        const sides = present
            .split('x')
            .map(Number)
            .sort((a, b) => a - b);
        const smallestPerimeter = sides[0] + sides[0] + sides[1] + sides[1];
        const volume = sides[0] * sides[1] * sides[2];
        return total + smallestPerimeter + volume;
    }, 0);
}

console.log(getSquareFeetWrapping(inputArray));
console.log(getFeetRibbon(inputArray));
