package com.draeger.smartcoffee.application.command;

import java.util.UUID;

public record RefillBeansCommand(UUID machineId, int beansToAdd, String user) {
}
