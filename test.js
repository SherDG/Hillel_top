let str = "Привіт";
let str2 = 'Одинарні лапки також дозволяються';
let phrase = `так можна вставляти ${str2}`;

// console.log(str);
// console.log(phrase);


// typeof undefined // "undefined"

// console.log(typeof 4) // "number"

// console.log(typeof 10n) // "bigint"

var check = false;
// console.log(typeof check) // "boolean"

// // typeof "foo" // "string"

// // typeof Symbol("id") // "symbol"

// // typeof Math // "object"  (1)

// console.log(typeof null) // "object"  (2)

// typeof alert // "function"  (3)

var array = ['Name', 'Test', 'Check', 4, [1,2,2]]
// console.log(array[0]);

var json = {
    name: "Test",
    age: 42
};
// console.log(json);

let s = 'мій_' + 'рядок' + 2;
// console.log(s);

let s1 = '1' + 2;
// console.log(s1);

let x = 2
x--;
// console.log(x);
// let year = 2015
// let additionalCondition = 2

// if (year == 2015 || additionalCondition === 1 && year == 2012 || additionalCondition === 2) {
//     console.log( "Це правильно!" );
//     console.log( "Ви такий розумний!" );
//     if(additionalCondition == 2){
//         console.log( "Це правильно2!" );
//         console.log( "Ви такий розумний2!" );
//     }
//   }
// else if(year == 2022){
//     console.log( "Це точно!" );
// }
// else{
//     console.log( "Спробуйте ще!" );
// };

for (let i = 0; i < 3; i++) { // показується 0, далі 1, потім 2
    console.log( "Спробуйте ще !" + i );
  }
