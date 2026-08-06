console.log("hii")


// Types of js:
//         1. Inline
//         2. Internal
//         3. External


/* 1. Inline JavaScript
JavaScript code is written directly inside an HTML element using an event attribute.
Suitable for small tasks like button clicks.
Not recommended for large projects because it mixes HTML and JavaScript.

2. Internal JavaScript
JavaScript code is written inside the <script> tag in the same HTML file.
The <script> tag is usually placed inside the <head> or just before the closing </body> tag.

3. External JavaScript
JavaScript code is stored in a separate .js file.
The file is linked to the HTML page using the <script src=""> tag. */

document.write()

var num1 = 30
console.log(num1)

num1 = 40 // reinitialize
console.log(num1)

var num1 = 70 // redeclare
console.log(num1)

const pi = 3.14

// var -- reassign and redeclare
// let -- reassign, not redeclare
// const -- not reassign, not redeclare

// | Event           | Description                                  |
// | --------------- | -------------------------------------------- |
// | `onclick`       | Triggered when an element is clicked.        |
// | `ondblclick`    | Triggered when an element is double-clicked. |
// | `onmousedown`   | Mouse button is pressed.                     |
// | `onmouseup`     | Mouse button is released.                    |
// | `onmousemove`   | Mouse pointer moves over an element.         |
// | `onmouseover`   | Mouse enters an element.                     |
// | `onmouseout`    | Mouse leaves an element.                     |
// | `onmouseenter`  | Mouse enters an element (doesn't bubble).    |
// | `onmouseleave`  | Mouse leaves an element (doesn't bubble).    |
// | `oncontextmenu` | Right-click menu opens.                      |
// | `onwheel`       | Mouse wheel is scrolled.                     |
