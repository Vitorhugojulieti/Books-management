// //selecionando os campos 
// const username = document.querySelector("#username");
// const email = document.querySelector("#email");
// const cpf = document.querySelector("#cpf");
// const telefone = document.querySelector("#telefone");
// const password1 = document.querySelector("#password1");
// const password2 = document.querySelector("#password2");
// const formCad = document.querySelector("#formCad");
// //selecionando msgs
// const msgEmail = document.querySelector("#msgEmail");
// const msgCpf = document.querySelector("#msgCpf");
// const msgTelefone = document.querySelector("#msgCpf");
// const msgSenha1 = document.querySelector("#msgCpf");
// const msgSenha2 = document.querySelector("#msgCpf");
// //regex
// const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
// const senhaRegex = /^.{8,}$/;
// const cpfRegex = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/;
// const telefoneRegex = /^\d{2,3}[\s.-]?\d{3,4}[\s.-]?\d{4}$/;
// //cores
// const corTrue = "green";
// const corFalse = "red";


// //modificar para alterar classe do campo e msg
// function setColor(msg, bool){
//     if(bool){
//         msg.style.color = corTrue;
//     }else{
//         msg.style.color = corFalse;
//     }
// }

// function validaCampo(campo,pMsg,regex,nomeCampo){
//     if(!regex.test(campo.value)){
//         if(nomeCampo === "senha"){
//             pMsg.innerText = "Senha deve conter no minimo 8 caracteres";
//             setColor(pMsg,false);
//         }else{
//             pMsg.innerText = "Campo " + nomeCampo+" invalido!"
//             setColor(pMsg,false);
//         }
//     }else{
//         pMsg.innerText = "";
//         setColor(pMsg,true);
//     }
// }


// formCad.addEventListener("submit",(e)=>{
//     //evitar envio do formulario
//     e.preventDefault();
//     //validacao dos campos
//     validaCampo(email,msgEmail,emailRegex,"e-mail");
//     validaCampo(password1,msgCpf,senhaRegex,"senha");

//     if(password1.value !== password2.value){
//         //chamar funcao para erro e estilo
//         setColor(msgSenha2,false);
//         msgSenha2.innerText = "Senhas não são iguais!";
//     }else{
//         setColor(msgSenha2,true);
//         msgSenha2.innerText = "";
//     }
//     //forcar envio do formulario
//     //e.Submit();
// })