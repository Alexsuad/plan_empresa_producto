---
trigger: always_on
---


# Regla — Seguridad, gobierno y aprobaciones

Requieren aprobación explícita del usuario:

- borrar archivos o carpetas;
- modificar `.env`;
- tocar secretos, tokens o claves;
- cambiar arquitectura general;
- usar MCP;
- crear código productivo;
- mover documentos fuente;
- modificar masivamente archivos Markdown.

Si la aprobación es ambigua, pedir al usuario que escriba exactamente:

`Aprobado`

o:

`Aprobado: <acción concreta>`

No ejecutar acciones sensibles con respuestas ambiguas.