// Constante tem que ter seu valor atribuido quando são declaradas:
        const constLocalGeral = 10;
        // Um bloco de código sem função específica:
        {
            // Atribuindo valor pelo usuário
            const constLocalBloco = window.prompt("Informe um valor: ");
            alert(constLocalBloco);
            alert(constLocalGeral);
        }
        /*
            Erro!! Constantes assim como variáveis declaradas com 'let',
            tem escopo de bloco.
        */
        alert(constLocalBloco);

        // Erro! Tentando alterar o valor de uma constante.
        constLocalGeral = 20;