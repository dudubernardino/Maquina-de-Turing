<h1 align="center">
<br>
Máquina de Turing
</h1>

<p align="center">💻 Um algoritmo que simula a execução de uma máquina de Turing</p>

<p align="center">
  <a href="http://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License MIT">
  </a>
</p>

<hr />

## Desenvolvedores

Estudantes de Ciência da Computação da UECE - Universidade Estadual do Ceará

- 👨‍💻 [**Eduardo de Moura Bernardino**](https://github.com/dudubernardino)
- 👨‍💻 [**Vinícius Linhares Alves de Oliveira**](https://github.com/ViniciusLinharesAO)
- 👨‍💻 [**Raimundo Angeliano Gonçalves de Sousa**](https://github.com/Angelo768)

## Sobre

Programa baseado em [python-turing](https://github.com/ronaldosvieira/python-turing#2)

Este programa foi desenvolvido de modo a simular o processamento de uma Máquina de Turing Determinística. Foi desenvolvido na linguagem Python 3 e requer um arquivo com as configurações desejadas para a execução da máquina.

## Como Executar

1. Clone este repositório `https://github.com/dudubernardino/Maquina-de-Turing`
2. Informe a configuração da MT num arquivo txt.<br />
3. Execute `python3 maquina_turing.py`<br />

## Exemplo

- Utilize o arquivo `config.txt` para inserir a definição formal da Máquina de Turing

```
  alfabeto:a,b
  alfabet0_aux:A,B
  estados:q0,q1,q2,q3,q4
  trans_q0:[#,#,DIR,q0];[a,A,DIR,q1];[B,B,DIR,q3];[' ',' ',DIR,q4]
  trans_q1:[b,B,ESQ,q2];[a,a,DIR,q1];[B,B,DIR,q1]
  trans_q2:[A,A,DIR,q0];[a,a,ESQ,q2];[B,B,ESQ,q2]
  trans_q3:[B,B,DIR,q3];[' ',' ',DIR,q4]
  trans_q4:[[]]
  estado_inicial:q0
  simbolo_inicial:#
```

- Mantenha a sintaxe apresentada no config.txt, utilizando DIR e ESQ para o movimento do cabeçote e ' ' para o simbolo branco, com o espaçamento adequado.

- Para executar a máquina, vá até o arquivo maquina.py e use a função run para escolher uma cadeia a ser analisada.

```
  turing = turing(alfabeto,estados,estado_inicial,alfabeto_aux,simbolo_inicial,' ')
  turing.run("ab")
  turing.run("aabb")
  turing.run("aaab")
  turing.run("aaaabbbb")
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
