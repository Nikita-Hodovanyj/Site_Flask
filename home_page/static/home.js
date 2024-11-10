
// alert("dhskj")
let commentButton = document.querySelector(".comment")


commentButton.addEventListener(
    type = "click",
    listener = function(event){
        event.preventDefault()
        document.querySelector(".appearances").style.display = "block"
        document.querySelector(".home").style.display = "none"
        console.log("jhgfhjgfhj")
    }
)