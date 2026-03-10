package com.draeger.smartcoffee.application.port.in;

import java.util.UUID;

public record MachineDto(UUID id, String name, int beansAvailable) {
}
