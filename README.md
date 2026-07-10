# NN: Zero to Hero

Implementación desde cero de los componentes fundamentales del deep learning (desde un motor de autodiferenciación hasta un modelo de lenguaje tipo GPT), con el objetivo de entender a profundidad qué sucede matemática y computacionalmente dentro de una red neuronal, más allá de usar frameworks como PyTorch como caja negra.

## Motivación

La mayoría de la práctica moderna de ML se apoya en frameworks de alto nivel que abstraen backpropagation, optimización y arquitecturas complejas. Este repositorio documenta el proceso inverso: construir cada pieza desde los fundamentos matemáticos (cálculo, álgebra lineal, probabilidad) para entender exactamente qué hace `.backward()`, cómo se propaga un gradiente, y por qué las arquitecturas modernas están diseñadas como están.

## Contenido

### [`micrograd-from-scratch/`](./micrograd-from-scratch)
Motor de autodiferenciación (autograd) implementado en Python puro.

- Clase `Value` con soporte para operaciones aritméticas y funciones de activación (tanh)
- Backpropagation vía aplicación recursiva de la regla de la cadena, con ordenamiento topológico del grafo computacional
- Visualización del grafo computacional con Graphviz
- Construcción incremental: `Neuron` → `Layer` → `MLP`
- Ciclo de entrenamiento completo: forward pass, cálculo de loss, backward pass, actualización de parámetros vía gradient descent

### `makemore/` *(en progreso)*
Modelos de lenguaje a nivel de carácter, construidos con complejidad creciente:

- Modelo de bigramas (baseline estadístico)
- Perceptrón multicapa (MLP)
- Mejoras de inicialización, activaciones y normalización (BatchNorm)
- Arquitectura tipo WaveNet (convoluciones causales)

### `nanogpt/` *(próximamente)*
Transformer implementado desde cero, replicando la arquitectura de GPT.

## Stack

- Python puro para las primeras implementaciones (sin frameworks de ML)
- NumPy / PyTorch conforme aumenta la complejidad de las arquitecturas
- Jupyter Notebooks con documentación inline
- Graphviz para visualización de grafos computacionales
- `uv` para gestión de entorno y dependencias

## Sobre el código

Los notebooks priorizan la implementación funcional sobre la exposición extensa, con comentarios puntuales que marcan las etapas clave de cada proceso (forward pass, backward pass, actualización de parámetros), en lugar de celdas de explicación extendida. El objetivo de cada notebook es que el código mismo sea la evidencia de comprensión: cada línea fue escrita entendiendo su propósito matemático, no copiada de una referencia.

## Créditos

Este trabajo está inspirado en la estructura pedagógica del curso Neural Networks: Zero to Hero de Andrej Karpathy. Las implementaciones, explicaciones y ejercicios adicionales en este repositorio son elaboración propia como parte de mi proceso de aprendizaje autodirigido en fundamentos de deep learning.