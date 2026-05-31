# 🌳 Realidad Aumentada - Árbol 3D (Unity + Vuforia)

Aplicación móvil de realidad aumentada desarrollada en Unity y Vuforia Engine.

La aplicación reconoce una imagen llamada `Arbol.jpg` y despliega un modelo 3D de un árbol sobre ella utilizando seguimiento por Image Target.

Este proyecto complementa el juego Puzzle 3x3 desarrollado en Python.

## ⚙️ Tecnologías utilizadas

* Unity 2022.3.25f1 LTS
* Vuforia Engine 11.2.4
* Android
* Modelo 3D (.glb)

---

## 🚀 Funcionamiento

La aplicación utiliza reconocimiento visual mediante Vuforia.

**Proceso**

1. Abrir la aplicación móvil.
2. Apuntar la cámara hacia `Arbol.jpg`.
3. Vuforia detecta el marcador.
4. El modelo 3D del árbol se renderiza sobre la imagen.

---

## 📁 Recursos principales

```text
unity/
├── Assets/
├── Packages/
├── ProjectSettings/
└── README.md
```

**Recursos utilizados**

* `Arbol.jpg`
* `arbol_materiales_editables.glb`
* materiales y texturas del modelo 3D

---

## 🔧 Configuración detectada

* Image Target: `Arbol`
* Seguimiento mediante Vuforia Image Target
* Plataforma objetivo: Android
* Identificador:

```text
com.JoseVuforia1.RealidadAumentada
```

---

## 🌐 Relación con el juego Python

Esta aplicación forma parte de una experiencia complementaria.

El juego Puzzle 3x3 muestra la imagen `Arbol.jpg` al ganar. Esa misma imagen es utilizada aquí como marcador de realidad aumentada para visualizar el árbol tridimensional.

> Puzzle resuelto → imagen mostrada → escaneo móvil → árbol 3D.

---

## ▶️ Abrir proyecto

1. Abrir Unity Hub.
2. Seleccionar el proyecto.
3. Abrir `Assets/Scenes/SampleScene.unity`.
4. Verificar que Vuforia esté instalado.
5. Ejecutar o compilar para Android.
