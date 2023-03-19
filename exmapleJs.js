let saludo = "el pepe";

console.log(saludo.indexOf("pe") > -1);

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
