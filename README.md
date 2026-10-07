# harness-gate-demo

Demo pública, con **código sintético**, de la compuerta de merge del *Harness IA Gobernado* de Quind.

La rama `main` está protegida por un *ruleset* de GitHub, sin actores con bypass, ni siquiera el dueño del repo:

- todo cambio entra por pull request;
- el check **`harness/verify`** debe estar en verde y sobre la última versión de la rama;
- no se permite force-push ni borrar la rama.

## Qué produce `harness/verify`

El verificador corre **fuera de GitHub**, en un ambiente efímero: contenedor gVisor o tarea de AWS Fargate sin credenciales.

1. Toma snapshots inmutables de la base y del head del PR.
2. Ejecuta herramientas deterministas (Betterleaks, Opengrep, Ruff, OSV-Scanner y Trivy) y, en otro contenedor, las pruebas del repo.
3. Decide con una política OPA *fail-closed*. Bloquea si hay:
   - secretos nuevos;
   - hallazgos nuevos de severidad alta;
   - regresiones en las pruebas;
   - pruebas nuevas que no se ejecutaron;
   - falta de evidencia.
4. Publica el resultado como estado del commit, junto con un resumen de la evidencia en el PR.

Los agentes de IA trabajan en un sandbox sin credenciales de Git; un publicador aparte abre el PR. Nadie, ni humano ni agente, puede fusionar sin el check.

> En producción el estado lo publica una GitHub App dedicada y el ruleset exige además la aprobación humana (CODEOWNERS). En esta demo hay 0 aprobaciones obligatorias porque el repo tiene un solo mantenedor.
