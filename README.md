# Tech-Bank RIWI-G2 - Manual de Usuario

## Tabla de contenidos
1. [Introducción](#introducción)
2. [Requisitos del sistema](#requisitos-del-sistema)
3. [Inicio del programa](#inicio-del-programa)
4. [Autenticación](#autenticación)
5. [Menú principal](#menú-principal)
6. [Operaciones disponibles](#operaciones-disponibles)
7. [Guía paso a paso](#guía-paso-a-paso)
8. [Validaciones y límites](#validaciones-y-límites)
9. [Historial de operaciones](#historial-de-operaciones)
10. [Preguntas frecuentes](#preguntas-frecuentes)

---

## Introducción

Tech-Bank RIWI-G2 es un simulador de cajero automático (ATM) que permite realizar operaciones bancarias básicas de forma segura y práctica. Fue desarrollado como parte del programa RIWI G2.

### Características principales:
- Autenticación segura mediante PIN
- Consultar saldo disponible
- Retirar dinero con límites diarios
- Depositar dinero en la cuenta
- Historial detallado de todas las operaciones
- Validaciones de seguridad y límites bancarios

---

## Requisitos del sistema

- **Python 3.7** o superior
- Sistema operativo: Windows, macOS o Linux
- Terminal o línea de comandos
- Acceso a los archivos del programa

---

## Inicio del programa

### Paso 1: Ejecuta el programa
```bash
python3 main.py
```

### Resultado esperado:
```
...: Bievenidos al cajero automatico TechBank Riwi Digital:...
Ingrese el pin: 
```

---

## Autenticación

Al iniciar el programa, se te pedirá que ingreses el **PIN de tu cuenta**.

### Detalles importantes:
- **PIN correcto:** `1234`
- **Número de intentos:** 3
- **Bloqueo:** Si fallas 3 veces, el acceso se deniega automáticamente

### Proceso de autenticación:

```
Ingrese el pin: 1234
¡Contraseña correcta! Acceso concedido.

¿Cuantas operaciones quieres realizar?: 
```

Luego, debes indicar **cuántas operaciones deseas realizar** en esta sesión.

---

## Menú principal

Una vez autenticado, se mostrará el menú principal:

```
========================================
                 Menu
========================================
Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: 
```

### Opciones disponibles:
| Opción | Descripción |
|--------|------------|
| **1** | Consultar saldo actual de tu cuenta |
| **2** | Retirar dinero del cajero |
| **3** | Depositar dinero en tu cuenta |

---

## Operaciones disponibles

### 1 - Consultar Saldo

**Qué hace:** Muestra el dinero disponible en tu cuenta.

**Ejemplo de uso:**
```
Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: 1
Tu saldo es de:  1000
```

**Información registrada:** Esta operación se guarda en el historial.

---

### 2 - Retirar Dinero

**Qué hace:** Te permite extraer dinero de tu cuenta con las siguientes restricciones:
- No puede exceder tu saldo actual
- No puede superar el límite diario de retiro ($500)

**Ejemplo de uso:**
```
Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: 2
Ingrese el monto a Retirar: 200
Has retirado 200. Tu nuevo saldo es 800.
```

**Límites:**
- Límite diario: **$500**
- Máximo por retiro: Tu saldo actual
- Retiros acumulados hoy: Se rastrea automáticamente

---

### 3 - Depositar Dinero

**Qué hace:** Permite agregar dinero a tu cuenta bancaria.

**Ejemplo de uso:**
```
Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: 3
Ingrese el monto a Depositar: 500
 Su Deposito fue exitoso, su nuevo saldo es: 1500
```

**Notas:**
- No hay límite máximo de depósito
- El depósito se acredita inmediatamente
- Aparecerá en el historial de operaciones

---

## Guía paso a paso

### Ejemplo completo de una sesión:

**Paso 1: Iniciar programa**
```bash
python3 main.py
```

**Paso 2: Ingresar PIN**
```
...: Bievenidos al cajero automatico TechBank Riwi Digital:...
Ingrese el pin: 1234
¡Contraseña correcta! Acceso concedido.
```

**Paso 3: Indicar número de operaciones**
```
¿Cuantas operaciones quieres realizar?: 3
```

**Paso 4: Primera operación - Consultar saldo**
```
========================================
                 Menu
========================================
Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: 1
Tu saldo es de:  1000

¿Quieres continuar con las operaciones, 1 para si o 2 para no: 
1
```

**Paso 5: Segunda operación - Retirar dinero**
```
========================================
                 Menu
========================================
Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: 2
Ingrese el monto a Retirar: 300
Has retirado 300. Tu nuevo saldo es 700.

¿Quieres continuar con las operaciones, 1 para si o 2 para no: 
1
```

**Paso 6: Tercera operación - Depositar dinero**
```
========================================
                 Menu
========================================
Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: 3
Ingrese el monto a Depositar: 500
 Su Deposito fue exitoso, su nuevo saldo es: 1200

¿Quieres continuar con las operaciones, 1 para si o 2 para no: 
2
```

**Paso 7: Historial final**
```
========================================
                         HISTORIAL DE OPERACIONES
========================================
 Operacion 1---- consultar
  Monto:                $.00
  Saldo:           $1000.00
 Operacion 2---- Retirar
  Monto:             $300.00
  Saldo:             $700.00
 Operacion 3---- Depositar
  Monto:             $500.00
  Saldo:            $1200.00
```

---

## Validaciones y límites

### Límites de la cuenta:

| Aspecto | Límite | Descripción |
|--------|--------|-------------|
| **Saldo inicial** | $1,000 | Dinero disponible al comenzar |
| **Límite diario de retiro** | $500 | Máximo a retirar por día |
| **Saldo mínimo** | $0 | No puedes quedarte con saldo negativo |
| **Intentos de PIN** | 3 | Máximo de intentos antes de bloqueo |

### Mensajes de error comunes:

#### "Contraseña incorrecta. Inténtalo de nuevo."
- **Causa:** Ingresaste un PIN incorrecto
- **Solución:** Verifica el PIN e intenta nuevamente. Tienes 2 intentos restantes

#### "Has agotado tus intentos. Acceso denegado."
- **Causa:** Fallaste los 3 intentos de PIN
- **Solución:** Debes ejecutar el programa nuevamente

#### "Monto excede el saldo en cuenta"
- **Causa:** Intentaste retirar más dinero del que tienes
- **Solución:** Ingresa un monto menor o igual a tu saldo actual

#### "Se ha superado el límite máximo de retiro permitido. su tope diario es de 500"
- **Causa:** La suma de tus retiros hoy supera $500
- **Solución:** Espera hasta el día siguiente o retira menos dinero

#### "Opcion invalida"
- **Causa:** Ingresaste un número diferente a 1, 2 o 3
- **Solución:** Selecciona una opción válida del menú

#### "Entrada no válida. Por favor, ingresa un número entero."
- **Causa:** Ingresaste texto en lugar de números
- **Solución:** Usa solo números cuando se te solicite

---

## Historial de operaciones

### Qué es:
El historial es un registro de todas las operaciones que realizaste durante tu sesión.

### Información registrada:
- **Tipo de operación:** Consultar, Retirar o Depositar
- **Monto:** Dinero movido (0 para consultas)
- **Saldo:** Tu saldo después de la operación

### Visualización:
Se muestra automáticamente al final de la sesión cuando cierras el programa.

### Formato:
```
========================================
                    HISTORIAL DE OPERACIONES
========================================
 Operacion 1---- [TIPO]
  Monto:     $[CANTIDAD]
  Saldo:     $[SALDO ACTUAL]
```

---

## Preguntas frecuentes

### ¿Cuál es el PIN inicial?
**R:** El PIN por defecto es `1234`

### ¿Qué sucede si olvido el PIN?
**R:** El programa actual no tiene recuperación de PIN. Después de 3 intentos fallidos, debes reiniciar el programa.

### ¿Puedo retirar dinero sin límite?
**R:** No. Hay dos límites:
1. No puedes retirar más de lo que tienes en tu saldo
2. No puedes retirar más de $500 en un día

### ¿Se reinicia el límite diario de retiros?
**R:** En la versión actual, no. El límite se acumula durante toda la sesión. Para una nueva sesión con límite "nuevo", necesitarías reiniciar el programa.

### ¿Puedo hacer depósitos sin límite?
**R:** Sí, no hay límite máximo de depósito. Solo asegúrate de ingresar montos válidos.

### ¿Se guardan las operaciones después de cerrar?
**R:** En la versión actual, el historial se muestra solo al final de la sesión. No se guarda de forma permanente en archivo.

### ¿Qué pasa si quiero pausar mi sesión?
**R:** En cada operación, se te pregunta si deseas continuar:
```
¿Quieres continuar con las operaciones, 1 para si o 2 para no:
```
Responde `2` para terminar tu sesión.

### ¿Puedo cambiar el PIN?
**R:** En la versión actual, no hay opción para cambiar el PIN. Este está configurado en el código como `1234`.

### ¿Qué hago si veo un error inesperado?
**R:** 
1. Verifica que estés usando Python 3.7 o superior
2. Asegúrate de ingresar solo números cuando se solicita dinero
3. Reinicia el programa si algo se congela

---

## Consejos de uso

**Siempre verifica tu saldo** antes de realizar un retiro
**Lee los mensajes** del programa cuidadosamente
**Sé cuidadoso con los montos** para evitar errores
**Revisa el historial** al final de tu sesión para confirmar las operaciones
**Responde correctamente** a los prompts (1 para sí, 2 para no)

---

## Soporte

Si tienes problemas no cubiertos en este manual, verifica:
- Que estés ejecutando Python 3.7+
- Que todos los archivos del programa estén en la misma carpeta
- Que tengas permisos para ejecutar scripts de Python

---

**Versión:** 1.0  
**Última actualización:** Marzo 2026  
**Desarrollado por:** RIWI G2
