package com.draeger.smartcoffee.application.port.in;

import java.util.Map;

public record UserStatsDto(String user, int totalCups, Map<String, Integer> byType) {
}
