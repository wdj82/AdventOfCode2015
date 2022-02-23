import input from './input.js';

const symbols = { '^': { x: 0, y: -1 }, v: { x: 0, y: 1 }, '<': { x: -1, y: 0 }, '>': { x: 1, y: 0 } };

function navigateHouses(directions) {
    let x = 0;
    let y = 0;
    const houses = new Set();
    houses.add([x, y].toString());
    for (let i = 0; i < directions.length; i++) {
        const { x: deltaX, y: deltaY } = symbols[directions[i]];
        x += deltaX;
        y += deltaY;
        houses.add([x, y].toString());
    }
    console.log(houses.size);
}

function navigateHousesWithRoboSanta(directions) {
    let santaX = 0;
    let santaY = 0;
    let roboX = 0;
    let roboY = 0;
    const houses = new Set();
    houses.add([santaX, santaY].toString());
    for (let i = 0; i < directions.length; i += 2) {
        const { x: santaDeltaX, y: santaDeltaY } = symbols[directions[i]];
        santaX += santaDeltaX;
        santaY += santaDeltaY;
        houses.add([santaX, santaY].toString());
        const { x: roboDeltaX, y: roboDeltaY } = symbols[directions[i + 1]];
        roboX += roboDeltaX;
        roboY += roboDeltaY;
        houses.add([roboX, roboY].toString());
    }
    console.log(houses.size);
}

//navigateHouses(input);
navigateHousesWithRoboSanta(input);
