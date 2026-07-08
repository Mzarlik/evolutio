En el paradigma del SDLC Agéntico (ASDLC), la IA evoluciona desde un simple copiloto de autocompletado de código hacia un sistema de múltiples agentes (MAS) autónomos, capaces de planificar, interactuar con herramientas, ejecutar pipelines y corregir sus propios errores de manera coordinada.  

En este ecosistema, los roles de arquitectura de TI tradicionales no son reemplazados, sino que se transforman en agentes supervisores (que actúan como orquestadores y toman decisiones críticas) y subagentes especialistas (que ejecutan tareas técnicas acotadas). El ser humano asume la responsabilidad de definir el contexto organizativo, establecer las reglas de autoridad (guardrails) y dar la aprobación final.  

A continuación se detalla cómo se distribuyen estos roles como agentes y subagentes en cada una de las fases del ciclo de vida del desarrollo:

1. Fase de Planificación (Planning)
Agente Supervisor: Orquestador de Arquitectura Empresarial (Enterprise Architect Agent)

Se encarga de alinear los objetivos de negocio de alto nivel con la infraestructura existente de la corporación. Define el alcance general de las iniciativas y automatiza la creación de epopeyas de arquitectura (Enabler Epics).  

Subagente de Análisis de Viabilidad y Portafolio: Escanea los repositorios, wikis internas y bases de datos lógicas para determinar si la funcionalidad propuesta ya existe en otro departamento, evitando la duplicidad de costes y sistemas.  

Subagente de Contexto y Estimación: Analiza los datos de velocidad histórica de los trenes ágiles y los recursos financieros consumidos para proyectar un presupuesto inicial y una línea de tiempo preliminar para el proyecto.  

2. Fase de Análisis (Analysis)
Agente Supervisor: Orquestador de Soluciones (Solutions Architect Agent)

Actúa como el nexo que traduce las necesidades del negocio en especificaciones lógicas y flujos de integración técnicos.  

Subagente de Redacción del SRS (Software Requirements Specification): Toma las solicitudes en lenguaje natural del equipo de negocio y genera la documentación técnica detallada, asegurando que todos los requisitos funcionales y de calidad estén estructurados formalmente.  

Subagente Analizador de Integración de APIs: Lee de manera autónoma los contratos de APIs, esquemas de bases de datos de terceros y diagramas lógicos existentes en la corporación para documentar los mecanismos de comunicación compatibles (ej. gRPC o REST).  

Subagente de Estimación de Costes (FinOps): Evalúa el posible consumo financiero del diseño (procesamiento cloud, volumen de tokens de IA, almacenamiento) y simula el retorno de inversión (ROI) antes de escribir una sola línea de código.  

3. Fase de Diseño (Design)
Agente Supervisor: Diseñador Técnico de Software (Software Architect Agent)

Decide la estructura anatómica del sistema (por capas, microservicios, hexagonal o monolito) y el modelado de datos.  

Subagente de Modelado UML y Flujos: Genera esquemas lógicos de bases de datos, diagramas de clases orientados a objetos y estructuras de llamadas asíncronas basadas en eventos.  

Subagente Evaluador de Trade-offs: Compara de manera autónoma diferentes patrones de diseño (creacionales, estructurales y de comportamiento) y presenta una comparativa de rendimiento (latencia, consistencia, memoria) argumentando cuál es la mejor configuración arquitectónica para el proyecto.  

4. Fase de Desarrollo (Development / Programación)
Agente Supervisor: Orquestador de Desarrollo de Software (Software Developer Agent)

Supervisa la implementación práctica del código, asegurando la consistencia y reduciendo los cuellos de botella iniciales.  

Subagente Generador de Plantillas (Boilerplate): Provee las configuraciones básicas, dependencias estándar y la infraestructura modular reutilizable siguiendo las "Rutas Doradas" (Golden Paths) autorizadas por la empresa.  

Subagente de Refactorización y Modernización Incremental: Identifica partes obsoletas en sistemas heredados (legacy) y aplica progresivamente patrones como el del "higo estrangulador" para migrar la lógica hacia nuevos componentes aislados.  

5. Fase de Pruebas (Testing / QA)
Agente Supervisor: Orquestador de Calidad y Verificación (QA Agent)

Se asegura de que el software entregado coincida exactamente con las especificaciones acordadas en el SRS y funcione de forma segura bajo estrés.  

Subagente de Generación y Ejecución de Pruebas: Redacta casos de prueba unitarios, simula interacciones de usuario final y evalúa escenarios extremos (edge cases) de forma autónoma.  

Subagente Auditor de Seguridad y DevSecOps: Escanea el código en busca de credenciales e información confidencial hardcodeada (SCA, SAST), verifica la integridad del manifiesto SBOM y valida que las imágenes de contenedores Docker no introduzcan vulnerabilidades críticas.  

6. Fase de Despliegue (Deployment)
Agente Supervisor: Orquestador de Infraestructura y Plataformas (Platform Architect Agent)

Garantiza el ciclo continuo de entrega y empaquetado seguro en entornos cloud o híbridos.  

Subagente Validador de IaC (Infraestructura como Código): Evalúa los scripts de aprovisionamiento de terraform o cloudformation antes del despliegue, bloqueando la compilación si detecta que se van a crear servicios o buckets con acceso público no autorizado.  

Subagente de Despliegue y Orquestación: Gestiona la instalación en los entornos de producción reales de manera controlada (ej. despliegues tipo canario), asegurando la compatibilidad con el hardware subyacente.  

7. Fase de Mantenimiento (Maintenance)
Agente Supervisor: Ingeniero de Resiliencia SRE (AI SRE Agent)

Mantiene la salud operativa global del sistema en tiempo real y mitiga las incidencias antes de que afecten al negocio.  

Subagente de Análisis y Correlación de Anomalías (AIOps): Monitoriza las trazas, métricas y logs del sistema. Si detecta un pico de latencia anormal, lo asocia de forma inteligente con los últimos despliegues, identifica la causa raíz y propone una solución de emergencia.  

Subagente de Parches y Actualizaciones de Dependencias: Busca constantemente nuevas alertas de vulnerabilidad publicadas (CVEs) en la industria y abre de manera automática solicitudes de combinación (Upgrade PRs) con dependencias actualizadas sin romper el sistema.  

Patrones de Coordinación de la Red de Agentes
Para que estos agentes y subagentes colaboren de manera fluida y sin colisionar en sus tareas, se aplican patrones lógicos específicos en el diseño del sistema:  

Patrón Orquestador-Trabajador (Supervisor-Worker): El agente supervisor (por ejemplo, el Solutions Architect Agent) analiza los requerimientos globales, los divide en tareas más pequeñas y las distribuye simultáneamente a los subagentes expertos (como el FinOps y el analista de APIs).  

Patrón de Retroalimentación (Critic-Refiner): El subagente generador de código escribe el código de la solución, mientras que el subagente de auditoría de DevSecOps lo examina de manera exhaustiva en busca de fallos de seguridad. El código se perfecciona recursivamente en un bucle cerrado hasta que cumple los umbrales de seguridad definidos.  

Patrón de Enrutador y Clasificador (Router-Classifier): Un ticket reportado por un usuario llega al sistema, y el agente enrutador, leyendo la documentación de la arquitectura interna de la empresa, redirige el problema al subagente experto en la infraestructura de bases de datos o de APIs correspondiente.  

El Rol Humano en el Ciclo Agéntico
Aunque los agentes ejecuten la mayor parte del trabajo mecánico e informático en minutos, el criterio humano sigue siendo indispensable. Los ingenieros y arquitectos humanos actúan como directores estratégicos (humans on the loop):  

Gobiernan los límites: Definen qué herramientas y repositorios puede modificar activamente cada agente y con qué presupuesto.  

Toman decisiones de negocio y éticas: Definen el análisis de riesgos aceptables para la organización, deciden sobre el lanzamiento del producto y validan las decisiones creativas que la tecnología no puede automatizar.