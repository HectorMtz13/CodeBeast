import asyncio
# Definir una función asincrónica que simula una tarea
async def tarea(nombre):
    print(f"{nombre} inicia")
    await asyncio.sleep(2)
    print(f"{nombre} termina")
# Ejecutar las tareas de forma concurrente
async def main():
    await asyncio.gather(# Ejecutar las tareas de forma concurrente
        tarea("Tarea 1"),
        tarea("Tarea 2")
    )
asyncio.run(main()) # Ejecutar la función principal