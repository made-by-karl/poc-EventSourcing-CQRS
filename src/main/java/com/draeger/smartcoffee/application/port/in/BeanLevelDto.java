package com.draeger.smartcoffee.application.port.in;

import java.util.UUID;

public record BeanLevelDto(UUID id, String name, int beansAvailable, int cupsProduced) {
}
