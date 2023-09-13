var submitButton =  document.querySelector("#submitButton")
// Validar campo de nome
function validarNome(){
    var nome = document.querySelector('#nome')
    var erroNome = document.querySelector("#span-error-nome")
    var labelNome = document.querySelector("#label-nome")
    if (/[@!#$%^&*()/\\0-9]/.test(nome.value)){
        labelNome.style.color = "red"
        nome.style.borderColor = "red"
        erroNome.textContent = "O nome do aluno não pode conter números ou caracteres especiais."
        submitButton.disabled = true
    }
    else {
        labelNome.style.color = "black"
        nome.style.border = "var(--bs-border-width) solid var(--bs-border-color)"
        erroNome.textContent = ""
        submitButton.disabled = false
    }
}

// Validação do campo de sobrenome
function validarSobrenome(){
    var sobrenome = document.querySelector('#sobrenome')
    var erroSobrenome = document.querySelector("#span-error-sobrenome")
    var labelSobrenome = document.querySelector("#label-sobrenome")
    if (/[@!#$%^&*()/\\0-9]/.test(sobrenome.value)){
        labelSobrenome.style.color = "red"
        sobrenome.style.borderColor = "red"
        erroSobrenome.textContent = "O sobrenome do aluno não pode conter números ou caracteres especiais."
        submitButton.disabled = true
    }
    else {
        labelSobrenome.style.color = "black"
        sobrenome.style.border = "var(--bs-border-width) solid var(--bs-border-color)"
        erroSobrenome.textContent = ""
        submitButton.disabled = false
    }
}

// Validação do campo de email
function validarEmail(){
    var email = document.querySelector("#email")
    var labelEmail = document.querySelector("#label-email")
    var erroEmail = document.querySelector("#span-error-email")

    usuario = email.value.substring(0, email.value.indexOf("@"))
    dominio = email.value.substring(email.value.indexOf("@")+1, email.value.length)

    if ((usuario.length >=1) && (dominio.length >=3) && (usuario.search("@")==-1) &&
        (dominio.search("@")==-1) && (usuario.search(" ")==-1) && (dominio.search(" ")==-1) &&
        (dominio.search(".")!=-1) && (dominio.indexOf(".") >=1)&& (dominio.lastIndexOf(".") < dominio.length - 1)) 
    {
        // email válida
        email.style.border = "var(--bs-border-width) solid var(--bs-border-color)"
        labelEmail.style.color = "black"
        erroEmail.textContent = ""
    }
    else {
        // email invalido
        email.style.borderColor = "red"
        labelEmail.style.color = "red"
        erroEmail.textContent = "Email Inválido"
    }
}

// Validação do campo de senha
function validarSenha(){
    // VALIDAÇÃO DO CAMPO DE SENHA
    // 1. DEVE CONTER NO MINIMO 8 CARACTERES
    // 2. DEVE CONTER PELO MENOS UM NUMERO
    // 3. DEVE CONTER PELO MENOS UMA LETRA MAIUSCULA
    var senha = document.querySelector("#senha")
    var labelSenha = document.querySelector("#label-senha")
    var erroSenha = document.querySelector("#span-error-senha")
    var msnError = ""               

    // validação
    if (senha.value.length < 8){
        msnError += "\nO Campo de senha deve conter no minimo 8 caracteres."
        senha.style.borderColor = "red"
        labelSenha.style.color = "red"
    }
    else if (!(/[0-9]/.test(senha.value))){
        msnError += "\nO Campo de senha deve conter pelo menos um numero."
        senha.style.borderColor = "red"
        labelSenha.style.color = "red"
    }
    else if (!(/[A-Z]/.test(senha.value))) {
        msnError += "\nO Campo de senha deve conter pelo menos uma letra maiuscula."
        senha.style.borderColor = "red"
        labelSenha.style.color = "red"
    }
    else {
        msnError = ""
        senha.style.border = "var(--bs-border-width) solid var(--bs-border-color)"
        labelSenha.style.color = "black"
    }

    erroSenha.textContent = msnError               

}

// Validação do campo de confirmação de senha 
function validarSenhaConfirm() {
    // VALIDAÇÃO DO CAMPO DE CONFIRMAÇÃO DE SENHA                                                                                                                                                  
    var senhaConfirm = document.querySelector("#senha-confirm")
    var senha = document.querySelector("#senha")
    var labelSenhaConfirm = document.querySelector("#label-senha-confirm")
    var erroSenhaConfirm = document.querySelector("#span-error-senha-confirm")

    if (senhaConfirm.value !== senha.value) {
        erroSenhaConfirm.textContent = "\nAs duas senhas não conferem."
        senhaConfirm.style.borderColor = "red"
        labelSenhaConfirm.style.color = "red"
    }
    else {
        erroSenhaConfirm.textContent = ""
        senhaConfirm.style.border = "var(--bs-border-width) solid var(--bs-border-color)"
        labelSenhaConfirm.style.color = "var(--bs-body-color)"
    }
}

// Validar datas de inicio e de fim do curso
function validarData(){
    var ingresso = document.querySelector("#ingresso")
    var conclusao = document.querySelector("#conclusao")

    // Se a data de ingresso for maior do que a data de conclusão, datas invalidas
    var dataIngressoList = ingresso.value.split("-") 
    var dataConclusaoList = conclusao.value.split("-") 

    // Se o ano ou o dia ou o mes da conclusão for maior que o ingresso as datas são válidas
    if (
        (dataConclusaoList[0] > dataIngressoList[0]) ||
        (dataConclusaoList[1] > dataIngressoList[1]) ||
        (dataConclusaoList[2] > dataIngressoList[2])
        )
        {
            // Data válida
            ingresso.style.border = "var(--bs-border-width) solid var(--bs-border-color)"
            conclusao.style.border = "var(--bs-border-width) solid var(--bs-border-color)"
            submitButton.disabled = false
        }
    else {
        // data inválida
        ingresso.style.borderColor = "red"
        conclusao.style.borderColor = "red"
        submitButton.disabled = true
    }
}

document.querySelector("#nome").addEventListener("keyup", validarNome)
document.querySelector("#sobrenome").addEventListener("keyup", validarSobrenome)
document.querySelector("#email").addEventListener("blur", validarEmail)
document.querySelector("#senha").addEventListener("blur", validarSenha)
document.querySelector("#senha-confirm").addEventListener("blur", validarSenhaConfirm)