let chat=document.getElementById("chat")
let usermsg=document.getElementById("message")
let reselem=document.getElementsByClassName("responce")[0]
let user=document.getElementsByClassName("user-meaage")[0]
let chatting=document.getElementById("chat-window")
chatting.scrollTop = chatting.scrollHeight;

chat.addEventListener("submit",async (e)=>{
    e.preventDefault()
    console.log("hi")
    let msg=usermsg.value.trim()
    if(msg !== ""){
        console.log(msg)
        let user=document.createElement("div")
        user.className="user-message"
        user.innerText=msg
        chatting.appendChild(user)
        usermsg.value=""
    }

    try {
        const responce= await fetch("/chat",
            {
                method:"POST",
                headers: {
                    "Content-Type": "application/json",
                  },
                  body:JSON.stringify({"message":msg})

            }

        )    
        let data=await responce.json()
        console.log("Hi is"+data.responce)
        let a=data.responce
        console.log("hi man")
        if(data){
             let data=document.createElement("div")
             data.className="response"
             data.innerText=a
             chatting.appendChild(data)
        }

       
        msg.value = '';



    } 
    catch (error) {
        console.log(error)
        
    }

})