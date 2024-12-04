const SEARCH = document.getElementById('search');
const TABELA_USUARIOS = document.getElementById('tabela-usuarios');

SEARCH.addEventListener('keyup', () => {
    let expressao = SEARCH.value.toLowerCase();

    // if (expressao.length <= 2) {
    //     // Se for, exibe todas as linhas e retorna
    //     for (let linha of TABELA_DADOS.getElementsByTagName('tr')) {
    //         linha.style.display = ''; // Mostra todas as linhas
    //     }
    //     return; // Sai da função
    // }

    // pesquisa o valor digitado dentro do id tabela dados nas linhas que estão envolvidas com <tr>
    let linhas = TABELA_USUARIOS.getElementsByTagName('tr');

    console.log(linhas);
    for(let posicao in linhas){
        if (true === isNaN(posicao)){
            continue;
        }
        // transforma todas as letras em minusculas 
        let conteudodalinha = linhas[posicao].innerHTML.toLowerCase();

         // mostra as linhas que tem o conteudo do usuario
        if(true === conteudodalinha.includes(expressao)) { 
            linhas[posicao].style.display = '';           
        } 
         // oculta as outras linhas que não tem o que o usuario digitou
        else{
            linhas[posicao].style.display = 'none';
        }
    }
});