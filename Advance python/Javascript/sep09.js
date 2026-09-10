let database = [
    {email:"sakshi@gmail.com",password:"123"},
    {email:"supriya@gmail.com",password:"123"},
    {email:"gayatri@gmail.com",password:"123"},
]

let formJs = document.getElementById("frm")
formJs.style.border = "2px solid black"
formJs.style.width = "20%"
formJs.style.padding = "20px"
formJs.style.margin = "100px auto"
formJs.style.borderRadius = "20px"

let emJS = document.getElementById("em")
emJS.style.width="260px"
emJS.style.border="2px solid black"
emJS.style.borderRadius="5px"
emJS.style.padding = "5px"
emJS.style.fontSize="20px"

let psJS = document.getElementById("ps")
psJS.style.width="260px"
psJS.style.border="2px solid black"
psJS.style.padding = "5px"
psJS.style.borderRadius="5px"
psJS.style.fontSize="20px"

let btn = document.getElementById("btn")
btn.style.border = "2px solid black"
btn.style.borderRadius = "10px"
btn.style.padding = "5px 20px"
btn.style.marginLeft = "100px"
btn.style.fontSize="20px"

function validateLogin(){
    let emailJS = document.getElementById("em").value ;
    let passwdJS = document.getElementById("ps").value ;
    
    let userFound = database.find((user)=>user.email == emailJS && user.password == passwdJS)

    if (userFound){
        window.open("success.htm")
    }else{
        alert("Invalid Creditials")
    }
    
}