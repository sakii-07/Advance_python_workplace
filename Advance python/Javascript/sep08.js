// const user = {
//     name: "Sakshi",
//     address: {
//         city: "Pune"
//     }
// };

// const copy = { ...user };

// copy.name = "Rahul";
// copy.address.city = "Mumbai";

// console.log(user);
// console.log(copy);


// function rest(...nums){
//     console.log(nums);
    
// }

// rest(1,2,3,4,5,6,7)


// const user = {
//     name: "Sakshi",
//     role: "Developer",
//     salary: 50000
// };

// const updatedUser = {    
//      salary: 70000,         
//     role: "Senior Developer",
//     salary: 90000,
//     age:22,
//     ...user      //  name: "Sakshi",role: "Developer",salary: 50000
// };

// console.log(updatedUser);

// function test(a, b, ...rest) {
//     console.log(a);
//     console.log(b);
//     console.log(rest);
// }

// const numbers = [10, 20, 30, 40, 50,34,34,24];

// test(...numbers);

// let b = document.querySelector('body')
// let colors = ['red','pink','brown','orange','yellow','green','blue']
// let index = 0
// function change(){
//     if (colors.length-1 == index){
//         index = 0
//     }
//     index++
//     b.style.backgroundColor = colors[index]
// }
// setInterval(change,100)

// let head = document.getElementById("head")


// function change(){
//     if (head.innerHTML == "Welcome to JS"){
//         head.innerHTML = "Document object model"
//         head.style.backgroundColor = "red"
//     }else if(head.innerHTML == "Document object model"){
//         head.innerHTML = "adfhdjg gsjfg sddfh"
//         head.style.backgroundColor = "orange"
//     }else{
//         head.innerHTML = "Welcome to JS"
//         head.style.backgroundColor = "yellow"
//     }
// }