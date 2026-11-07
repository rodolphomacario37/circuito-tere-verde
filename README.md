# Circuito Terê Verde - Back-End MVP

## 1. Dados de Identificação
- **Estudante**: Rodolpho Laurindo Macário Lins (06015421)
- **Curso**: Análise e Desenvolvimento de Sistemas (ADS) - UNIFESO
- **Polo de Origem**: Teresópolis

## 2. Escolha da Situação-Problema
- **Desafio**: Situação-Problema #1 - Circuito Terê Verde (Teresópolis).
- **Contexto**: Teresópolis é cercada por três unidades de conservação (Parque Nacional da Serra dos Órgãos, Parque Estadual dos Três Picos e Parque Natural Municipal Montanhas de Teresópolis). O turismo ecológico e montanhismo sofrem com a falta de centralização e atualização em tempo real sobre interdições de trilhas por riscos climáticos e horários de funcionamento.

## 3. Descrição do MVP
Desenvolvimento de uma API RESTful em Python e Django com o objetivo de centralizar os dados dos parques, trilhas e pontos turísticos, permitindo que administradores mantenham a disponibilidade atualizada e que visitantes consultem informações públicas confiáveis em tempo real.

---

## 4. Escopo do Produto

### Dentro do Escopo (MVP)
- Centralização de catálogo de atrativos turísticos e unidades de conservação.
- Cadastro e consulta detalhada de trilhas ecológicas (extensão em km, tempo estimado e nível de dificuldade).
- Gestão de disponibilidade operacional (status de aberta, fechada ou em manutenção temporária).
- API RESTful padronizada com payloads em formato JSON para integração com Front-End/Mobile.
- Automação de testes unitários para validação das regras de dados.

### Fora do Escopo (Evoluções Futuras)
- Sistema de venda e pagamento de ingressos online (Pix/Cartão).
- Emissão e controle de certificados ou vouchers de visitação.
- Sistema de recomendação automatizada com Inteligência Artificial.
- Aplicativo mobile nativo (o foco desta etapa é o Back-End).
- Avaliações e comentários públicos com moderação de conteúdo.

---

## 5. Especificação de Requisitos

### Requisitos Funcionais (RF)
- **RF01 - Consulta de Atrativos**: O sistema deve permitir que visitantes listem todos os parques e atrativos naturais cadastrados.
- **RF02 - Detalhamento do Atrativo**: O sistema deve permitir a consulta detalhada de um atrativo específico e suas trilhas associadas.
- **RF03 - Cadastro de Atrativos**: O sistema deve permitir o cadastro de novos pontos turísticos com nome, parque, horários e status operacional.
- **RF04 - Gestão de Trilhas**: O sistema deve permitir cadastrar, listar e atualizar trilhas vinculadas aos atrativos.
- **RF05 - Controle de Disponibilidade**: O sistema deve permitir alterar o status de funcionamento de uma trilha (aberto/fechado/manutenção) em tempo real.

### Requisitos Não-Funcionais (RNF)
- **RNF01 - Padrão Arquitetural**: O Back-End deve operar no padrão RESTful, utilizando os métodos HTTP adequados (`GET`, `POST`, `PUT`, `DELETE`).
- **RNF02 - Formato de Dados**: A comunicação de entrada e saída deve ser realizada estritamente no formato JSON.
- **RNF03 - Desempenho**: As consultas públicas devem responder com tempo de resposta inferior a 2 segundos em condições normais de uso.
- **RNF04 - Confiabilidade e Testes**: A aplicação deve possuir suíte de testes unitários automatizados cobrindo a criação e o relacionamento dos modelos.

---

## 6. Endpoints da API

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/atrativos/` | Lista todos os atrativos naturais |
| `POST` | `/api/atrativos/` | Cadastra um novo atrativo |
| `GET` | `/api/atrativos/<id>/` | Exibe detalhes de um atrativo específico |
| `PUT` | `/api/atrativos/<id>/` | Atualiza dados do atrativo |
| `DELETE` | `/api/atrativos/<id>/` | Remove um atrativo |
| `GET` | `/api/trilhas/` | Lista todas as trilhas cadastradas |
| `POST` | `/api/trilhas/` | Cadastra uma nova trilha vinculada a um atrativo |
| `GET` | `/api/trilhas/<id>/` | Exibe detalhes de uma trilha específica |
| `PUT` | `/api/trilhas/<id>/` | Atualiza status operacional e dados da trilha |

---

## 7. Instruções para Executar Localmente

### Pré-requisitos
- Python 3.8 ou superior
- Git instalado

### Passo a passo

1. Clone este repositório:
```bash
git clone [https://github.com/rodolphomacario37/circuito-tere-verde.git](https://github.com/rodolphomacario37/circuito-tere-verde.git)
cd circuito-tere-verde