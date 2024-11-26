const myObject = {
    property: 'Value!',
    otherProperty: 77,
    "obnoxious property": function()
    {
        console.log("Doing stuff!");
    }
}


function Player(name, marker){
    this.name = name;
    this.marker = marker;
}

console.log(myObject.property); // This will print: 'Value!'
myObject["obnoxious property"](); // Prints: Doing stuff!
const player = new Player('steve', 'X');
console.log(player.name); // Prints: steve

// PROTOTYPE EXAMPLES
function Food(name, type) {
    this.name = name; // Name of the food
    this.type = type; // Type of food (e.g., fruit, vegetable, dessert)
}
 
// Add a method to the prototype to describe the food
Food.prototype.describe = function() {
    console.log(`The ${this.name} is a type of ${this.type}.`);
};


// Create two food items
const apple = new Food("Apple", "Fruit");
const carrot = new Food("Carrot", "Vegetable");

// Call the shared method
apple.describe(); // Outputs: The Apple is a type of Fruit.
carrot.describe(); // Outputs: The Carrot is a type of Vegetable.

// wtf