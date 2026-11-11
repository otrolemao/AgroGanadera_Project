# AgroGanadera - Sistema de Gestión de Ganado

## 📝 Descripción del Proyecto
AgroGanadera es una plataforma web desarrollada en Django para la gestión de un campo ganadero dedicado a la crianza y venta de terneros. El sistema permite clasificar el ganado por raza y administrar la información detallada de cada animal, incluyendo su disponibilidad para la venta. 

Este proyecto corresponde a la Evaluación Sumativa 3 (Hito 3) de la asignatura Programación Back End.

## 🚀 Tecnologías Utilizadas
- **Backend:** Python 3, Django 5
- **Base de Datos:** SQLite (Desarrollo) / MySQL (Producción)
- **Frontend:** HTML5, Bootstrap 5, Django Template Language (DTL)
- **Control de Versiones:** Git y GitHub

## 🏗️ Arquitectura del Proyecto
El proyecto cumple con la arquitectura MVT (Modelo-Vista-Template) y consta de dos modelos relacionados (1:N):
- **Modelo Padre (`Raza`):** Administrado exclusivamente desde el Django Admin.
- **Modelo Hijo (`Ternero`):** Gestionado mediante un CRUD web completo con Vistas Basadas en Clases (CBVs).

## 🛠️ Instalación y Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/otrolemao/AgroGanadera_Project.git
   cd AgroGanadera_Project