let saludo = "el pepe";
console.log(saludo.indexOf("pe") > -1);

console.log(saludo.slice(2, 5));
let obj = {
  target: {
    name: "pepe",
    value: "marisol",
  },
};

let state = {};

let setState = (obj) => {
  state = { ...state, [obj.target.name]: obj.target.value };
};

setState(obj);

console.log(state);

let array = ["banana", "apple", "watermelon", "pear"];
let numb = [1, 2, 45, 63, 9, 67, 3, 2, 3];
let newArray = array.filter((el) => el != "apple");
let a = array.slice(1, 3);

let set = new Set(array);

console.log();
console.log(array);
console.log(Object.keys(obj));

let number = "6.7";
let number2 = "6";

console.log(parseFloat(number) + parseInt(number2));
