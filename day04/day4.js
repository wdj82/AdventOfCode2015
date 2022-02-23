import md5 from 'blueimp-md5';

const secretKey = `iwrupvqb`;

let num = 0;
let hash = md5(secretKey + 0);
while (hash.slice(0, 6) != '000000') {
    num += 1;
    hash = md5(secretKey + num);
}

console.log(num);
