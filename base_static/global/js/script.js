//FORMAT INPUT expenseValue
function formatCurrency(value) {
    const numericValue = value.replace(/[^0-9]/g, ''); // Remove caracteres não numéricos
    const integerPart = numericValue.slice(0, -2); // Obtém a parte inteira (removendo os dois últimos dígitos)
    const decimalPart = numericValue.slice(-2); // Obtém a parte decimal (dois últimos dígitos)
    let formattedValue = '';
    for (let i = 0; i < integerPart.length; i++) {
      formattedValue += integerPart[i];
      if ((integerPart.length - i - 1) % 3 === 0 && i !== integerPart.length - 1) {
        formattedValue += '.';
      }
    }
    formattedValue += ',' + decimalPart;
    // Adiciona o símbolo do real e retorna o valor formatado
    return 'R$ ' + formattedValue;
  }

  const valorInput = document.getElementById('id_valor_total')
  valorInput.addEventListener('input', ()=>{
    const valorOriginal = valorInput.value
    const valorAtualizado = valorOriginal.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});
    console.log(valorAtualizado)
    valorInput.value = valorAtualizado
    console.log('teste')
  })
