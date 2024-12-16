#!/bin/bash

echo "Fecha y hora: $(date)"
echo "----------------------------------------"

echo "Tiempo de actividad del sistema:"
uptime
echo "----------------------------------------"

echo "Uso de CPU y procesos:"
top -b -n1 | head -15
echo "----------------------------------------"

echo "Uso de memoria:"
free -hm
echo "----------------------------------------"

echo "Estadísticas de E/S:"
vmstat 1 5
echo "----------------------------------------"

echo "Uso de disco:"
df -h
echo "----------------------------------------"

echo "Procesos con mayor consumo de memoria:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
echo "----------------------------------------"

echo "Estadísticas de red:"
ss -tuna
echo "----------------------------------------"

echo "Fin del reporte"