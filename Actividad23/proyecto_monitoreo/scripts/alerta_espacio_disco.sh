#!/bin/bash

THRESHOLD=80

PARTITIONS=$(df -h | grep '^/dev/' | awk '{print $1}')

for PART in $PARTITIONS; do
    USAGE=$(df -h | grep $PART | awk '{print $5}' | sed 's/%//g')
    if [ $USAGE -ge $THRESHOLD ]; then
    echo "Alerta: La partición $PART está al $USAGE% de uso."
    # Aquí podrías agregar envío de correo o notificación
    fi
done