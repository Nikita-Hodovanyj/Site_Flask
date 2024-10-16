
// alert("dhskj")
let commentButton = document.querySelector(".comment")


commentButton.addEventListener(
    type = "click",
    listener = function(event){
        event.preventDefault()
        document.querySelector(".appearances").style.display = "flex"
    }
)