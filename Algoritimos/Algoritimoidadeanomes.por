programa {
  funcao inicio() {
    inteiro idade, anos, meses, dias
    escreva("DIGITE QUANTOS ANOS VOCE VIVEU: ")
    leia(anos)
    escreva("DIGITE QUANTOS MESES VOCE VIVEU: ")
    leia(meses)
    escreva("DIGITE QUANTOS DIAS VOCE VIVEU: ")
    leia(dias)
    idade = (anos * 365) + (meses * 30) + dias
    escreva("A SUA IDADE EXPRESSADAS EM DIAS E: ", idade)
    
  }
}
