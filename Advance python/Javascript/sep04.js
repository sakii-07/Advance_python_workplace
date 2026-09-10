// // console.log("Hello");


// // let employees = [
// //     {id:101,name:"sakshi",salary:12345},
// //     {id:102,name:"supriya",salary:12345},
// //     {id:103,name:"gayatri",salary:12345},
// //     {id:104,name:"divya",salary:12345},
// //     {id:105,name:"amruta",salary:12345}
// // ]

// // console.log(employees);

// // empFound = employees.find((emp)=> emp.name == 'divya')

// // console.log(empFound);

// // empFound = {...empFound, salary : 11223344}

// // console.log(empFound);

// // employees = employees.filter((emp)=>emp.name!="divya")

// // console.log(employees);

// // employees = [...employees, empFound]

// // console.log(employees);

// // employees = employees.map((emp)=>{
// //     if (emp.name == "sakshi"){
// //         return {...emp, salary:112233}
// //     }
// //     return emp
// // })

// // console.log(employees);


// // crud operation on object

let employees = [
    {
        id: 1,
        name: "Sakshi",
        department: "IT",
        salary: 50000
    },
    {
        id: 2,
        name: "Rahul",
        department: "HR",
        salary: 45000
    },
    {
        id: 3,
        name: "Priya",
        department: "Finance",
        salary: 55000
    }
];

// // create
// let newemployee = {
//     id:4,
//     name:"Divya",
//     department:"Test",
//     salary:60000
// }
// employees = [...employees,newemployee]
// console.log(employees);


// let ar1 = [1,2,3,4]
// let ar2 = [6,5,7,8]

// let ar3 = [...ar1, ...ar2]
// console.log(ar3);

// console.log();

// read 
let emp = employees.find((emp)=>(emp.name == "Sakshi"))
console.log(emp);

// update
let employee = employees.map((emp)=>{
    if (emp.name == "Sakshi"){
        return {... emp, salary:20000}
    }
    return emp
})

console.log(employee);

// fitler
employees = employees.filter((emp)=>emp.name !="Sakshi")
console.log(employees);


