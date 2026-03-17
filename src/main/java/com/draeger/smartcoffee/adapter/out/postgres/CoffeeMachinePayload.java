package com.draeger.smartcoffee.adapter.out.postgres;

import java.time.Instant;

record CoffeeMachinePayload(String name, int beansAvailable, Instant lastMaintenance) {}
