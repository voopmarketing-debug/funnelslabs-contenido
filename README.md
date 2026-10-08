# Funnels Labs — contenido

Agente y skill para crear carruseles de Instagram/LinkedIn con la marca Funnels Labs, y los carruseles ya publicados.

- `.claude/agents/carruseles-funnels-labs.md` — el agente.
- `.claude/skills/carruseles-funnels-labs/` — guía de marca, copy, plantillas y script de render.
- `carruseles/<tema>/` — cada carrusel: `carrusel.html`, `slide-NN.png`, `caption.md`, `img/`.

## Crear un carrusel

En Claude Code, dentro de este repo:

> usa el agente carruseles-funnels-labs para hacer un carrusel sobre …

## Volver a exportar los PNG

```bash
npm install
npm run render -- carruseles/<tema>/carrusel.html
```
