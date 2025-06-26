---
title: Nome do Personagem
aliases: ["Apelido", "Título", "Nome Alternativo"]
tags:
  - personagens
  - #raça/espécie
  - #facção/grupo
  - #status/vivo
cssclasses: character-page
---

```dataview
TABLE WITHOUT ID
  file.link as "Personagem",
  join(aliases) as "Também conhecido como",
  join(tags) as "Tags"
WHERE file = this.file
```

# `= this.title`

> [!abstract]+ Resumo Executivo
> Breve descrição do personagem em 1-2 frases que capture sua essência

![[imagem-personagem.webp|400]]

## 📋 Informações Básicas

| Campo | Informação |
|-------|------------|
| **Nome Completo** | Nome Completo do Personagem |
| **Títulos/Apelidos** | Lista de títulos e apelidos conhecidos |
| **Raça/Espécie** | [[Raça]] |
| **Gênero** | Masculino/Feminino/Outro |
| **Idade** | XX anos (aparente/real) |
| **Status** | 🟢 Vivo / 🔴 Morto / ❓ Desconhecido |

## 🗓️ Cronologia

### Nascimento
- **Data**: DD/MM/AAAA ou Era/Período
- **Local**: [[Local de Nascimento]]
- **Circunstâncias**: Detalhes relevantes sobre o nascimento

### Morte
> [!danger]- Informações sobre a Morte
> - **Data**: DD/MM/AAAA
> - **Local**: [[Local da Morte]]
> - **Causa**: Como morreu
> - **Circunstâncias**: Contexto da morte

## 🏛️ Afiliações e Grupos

### Organizações Atuais
- **[[Nome da Organização]]** - *Posição/Cargo*
  - Desde: Data de entrada
  - Responsabilidades: Lista de funções

### Organizações Anteriores
- **[[Organização Anterior]]** - *Ex-Posição*
  - Período: Data início - Data fim
  - Motivo da saída: Razão

## ⚔️ Feitos e Conquistas

### Feitos Notáveis
> [!success]+ Grande Conquista
> Descrição detalhada de um feito importante

- **Nome do Feito**: Breve descrição
- **Nome do Feito 2**: Breve descrição

### Batalhas e Conflitos
- **[[Nome da Batalha]]** (AAAA) - Papel desempenhado
- **[[Conflito Importante]]** (AAAA) - Resultado

## 👥 Relacionamentos

### Família
```dataview
TABLE WITHOUT ID
  link(rows.file.link) as "Membro",
  rows.relacao as "Relação"
FROM #personagens 
WHERE contains(familia, this.file.name)
GROUP BY true
```

- **Pai**: [[Nome do Pai]]
- **Mãe**: [[Nome da Mãe]]
- **Irmãos**: [[Irmão 1]], [[Irmã 2]]
- **Cônjuge**: [[Nome do Cônjuge]]
- **Filhos**: [[Filho 1]], [[Filha 2]]

### Aliados e Amigos
- **[[Nome do Aliado]]** - Natureza da relação
- **[[Amigo Próximo]]** - Como se conheceram

### Inimigos e Rivais
- **[[Nome do Inimigo]]** - Motivo da inimizade
- **[[Rival]]** - História do conflito

## 🎯 Personalidade e Características

### Traços de Personalidade
- **Virtudes**: Corajoso, Leal, Inteligente
- **Defeitos**: Teimoso, Impulsivo, Orgulhoso
- **Medos**: Lista de medos ou fobias
- **Motivações**: O que move o personagem

### Aparência Física
- **Altura**: X,XX m
- **Peso**: XX kg
- **Cor dos Olhos**: Cor
- **Cor do Cabelo**: Cor
- **Marcas Distintivas**: Cicatrizes, tatuagens, etc.

## 🛡️ Habilidades e Poderes

### Habilidades Mundanas
- **Combate**: Nível de habilidade
- **Diplomacia**: Nível de habilidade
- **Conhecimento**: Áreas de especialização

### Poderes Especiais
> [!magic]+ Poder Único
> Descrição detalhada de um poder especial

- **Nome do Poder**: Descrição
- **Limitações**: O que limita esse poder

## 📚 História e Background

### Infância e Juventude
Narrativa sobre os primeiros anos de vida do personagem.

### Vida Adulta
Principais eventos que moldaram o personagem.

### Eventos Recentes
O que está acontecendo atualmente na vida do personagem.

## 🗣️ Citações Memoráveis

> "Frase icônica do personagem que define sua personalidade"
> — Contexto onde foi dita

> "Outra frase importante"
> — Outro contexto relevante

## 📖 Notas e Observações

### Curiosidades
- Fato interessante 1
- Fato interessante 2

### Notas do Autor
Espaço para anotações pessoais sobre o desenvolvimento do personagem.

---

## 🔗 Links Relacionados

```dataview
LIST
FROM [[]] OR outgoing([[]])
WHERE file != this.file
SORT file.name ASC
```

### Locais Importantes
- [[Local 1]] - Conexão com o personagem
- [[Local 2]] - Significado especial

### Eventos Relacionados
- [[Evento Histórico]] - Participação do personagem
- [[Batalha Importante]] - Papel desempenhado

---
*Última atualização: `= date(now)`*

**Tags**: `= join(this.file.tags, " • ")`