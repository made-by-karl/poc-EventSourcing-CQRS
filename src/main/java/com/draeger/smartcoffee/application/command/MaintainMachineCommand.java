package com.draeger.smartcoffee.application.command;

import java.util.UUID;

public record MaintainMachineCommand(UUID machineId, String user) {
}
