package com.draeger.smartcoffee.application.port.in;

public record RebuildResultDto(int eventsReplayed, long elapsedMs) {}
