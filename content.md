# Intro

### Git

* Es un software local
* Herramienta CLI
* Permite version de controles

### Github

* Servidor cloud
* Funciona principalmente como una interfaz grafica
* Facilita colaboracion entre muchos
* Permite CI/CD
    * CI:
        * Plan de integracion de features
        * Code : Evaluar el codigo desarrolado
        * Construir: Compilar y dejar todo para ser usado por algun host
    * CD:
        * Release: Enviar Build a la locacion remota
        * Deploy: Reconfigurar y relanzar los proyectos  con los nuevos feature
        * Operar: Mantener el proyecto a flote
        * Measure: Metricas de la calidad del codigo y operacion.

### Componentes principales

* Workflows : Proceso automatizado que contiene varios Jobs
  * Event : Actividad que ejecuta un workflow
    * Esto puede suceder a través de un API REST
  ```yaml
    name: hola-mundo # Nombre del Workflow
    on: [push]
  ```
* Job: Es un conjunto de tareas o steps que viven dentro de un workflow
    ```
    name: hola-mundo
    on: [push]
    jobs:
        hola-mundo:
          runs-on: ubuntu-latest  
    ```
* Steps: Acciones que corren dentro de nuestro flujo
    ```
    name: hola-mundo
    on: [push]
    jobs:
        hola-mundo:
          runs-on: ubuntu-latest
    steps: 
        - name: Public IP
          id : ip
          uses: hayutem/public-ip@v1.3
        - name: Hola Mundo
          run: echo Hola mundo desde ${{steps.ip.output.ipv4}} 
    ```
* Runner : Servidor donde corren los jobs
* Actions:  





