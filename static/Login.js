let chatbot=document.getElementById("chatbot")
let custombox=document.getElementById("chatbot-info")

chatbot.addEventListener("change",()=>{
    console.log("Hi")
    if(chatbot.value==="Custom"){
        custombox.style.display="block"
    }else{
        custombox.style.display="none"
    }
})
