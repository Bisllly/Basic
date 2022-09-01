console.log("Hello World");
const a = "const"
let b = "let"
var c = "var"

const name = "OngDev";
var number = 1;
const ongdev = {
    firstName: "Ong", 
    lastName: "Dev",
    age: 26,
    male: true,
};
let undefinedTest;
let nullTest = null; 

// Data Types
// String
// Number
// Object
// Boolean
// Null, undefined

// Condition

// if else
if (ongdev.age == 26) {
 console.log(ongdev.age == 26)
} else if (ongdev.age == 27) {
 console.log("dung roi ahihi")
} else {
 console.log("dung nua ahihi do ngok")
}

// switch case 
switch (ongdev.age) {
    case 26:
        console.log("ong dev 26")
        break;
    case 27: 
        console.log("ong dev 27")
        break;
    default:
        console.log("dung nua ahihi do ngok")
        break;
}

console.log(name);
console.log(number);
console.log(object);
console.log({object, undefinedTest, nullTest})

// Function
function showObjectInfo() { 
    console.log({object, undefinedTest, nullTest})
}
showObjectInfo( )