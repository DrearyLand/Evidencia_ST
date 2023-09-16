# Evidencia_ST


## Descripción
Este es un juego de memoria de números en el que se deben emparejar las fichas para revelar los pares. El objetivo es destapar todas las fichas emparejadas con la menor cantidad de toques.

## Cambios Realizados

### Conteo de Toques
- Se agregó un contador de toques (`tap_count`) para llevar un registro del número de toques realizados por el jugador.
- El contador se muestra en la esquina inferior izquierda de la pantalla y se actualiza en tiempo real.

### Detección de Fichas Reveladas
- Se implementó la detección de fichas reveladas mediante la función `all_tiles_revealed`.
- Cuando todas las fichas han sido destapadas, se muestra un mensaje de felicitación en la pantalla.

### Ajustes para Cumplir con Flake8
- Se realizaron ajustes en el código para asegurarse de que cumpla con los estándares de linting de Flake8.

## Instrucciones para Jugar
1. Haz clic en dos fichas para destaparlas. Si son iguales, permanecerán destapadas; de lo contrario, se ocultarán nuevamente.
2. El objetivo es destapar todas las fichas emparejadas con la menor cantidad de toques posible.
3. Observa el contador de toques en la esquina inferior izquierda para llevar un registro de tus movimientos.
4. Cuando todas las fichas estén destapadas, verás un mensaje de felicitación.
