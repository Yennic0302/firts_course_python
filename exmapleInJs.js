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

console.log(array);
console.log(Object.keys(obj));

let number = "6.7";
let number2 = "6";

console.log(parseFloat(number) + parseInt(number2));

function search(num) {
  find: {
    for (var i of [0, 1, 2, 3, 4]) {
      if (i === num) {
        console.log("Match found: " + i);
        break find;
      }
    } // else part after the loop:
    console.log("No match found!");
  }
  // after loop and else
}

let myText = "hola mundo como estan mi nombre es yender";
let result = [];

for (let i = 0; i < myText.length; i++) {
  if (result.length == 0) result[0] = [myText[i], 0];
  let isInResult = true;
  els: {
    for (let e = 0; e < result.length; e++) {
      if (result[e][0] == myText[i]) {
        isInResult = false;
        break els;
      }
    }
  }
  if (isInResult) result.push([myText[i], 0]);

  for (let a = 0; a < result.length; a++) {
    if (result[a][0] == myText[i]) result[a][1] = result[a][1] + 1;
  }
}

console.log(result);

let numbs = [1, 2, 34, 4, 5];

let numbsTimes2 = numbs.map((e) => e * 2);
console.log(numbsTimes2);

myOperation = "12.03839/2*100/10";

console.log(eval(myOperation));
