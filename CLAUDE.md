# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the application (http://localhost:8080)
./gradlew bootRun

# Run with remote debug on port 5005
DEBUG=true ./gradlew bootRun

# Run tests
./gradlew test

# Run a single test class
./gradlew test --tests "com.draeger.smartcoffee.SomeTest"

# Build without running
./gradlew build
```

## Stack

- **Spring Boot 4.0.3**, Java 24, Gradle

## Architecture

Hexagonal (Ports & Adapters) with Event Sourcing + CQRS. Every state change is an immutable `DomainEvent`; aggregate state is rebuilt by replaying the event stream.

```
domain/        — Pure domain: CoffeeMachine aggregate, DomainEvent subclasses, CoffeeType enum
application/   — Commands (records), port interfaces (in/out), command & query services
adapter/in/    — REST controllers + request DTOs
adapter/out/   — InMemoryEventStore, InMemoryEventSourcedRepository
```

### Event Sourcing Flow

1. Controller receives HTTP request → creates Command record
2. `CoffeeMachineCommandService` loads aggregate via `CoffeeMachineRepository`
3. Repository calls `EventStore.loadEvents(aggregateId)` and replays them through `CoffeeMachine.reconstitute()`
4. Service calls `aggregate.handle(command)` → returns new `DomainEvent`
5. Event is appended to `EventStore`

### CQRS — Query side

`CoffeeMachineQueryService` reads all events from the store and builds projections on-the-fly (no read model / materialized view). Caffeine alert logic: users with ≥3 `DOUBLE_ESPRESSO` events in the last 2 hours trigger an alert.

### Domain Model

- `CoffeeMachine` — aggregate root; state: `id`, `name`, `beansAvailable`; `MAX_BEANS_CAPACITY = 60`
- `CoffeeType` enum — `ESPRESSO(10)`, `DOUBLE_ESPRESSO(20)`, `AMERICANO(5)`, `HOT_WATER(0)` (bean costs)
- Events: `MachineRegistered`, `CoffeeProduced`, `BeansRefilled` — all extend `DomainEvent`
- `InsufficientBeansException` — thrown by aggregate; caught in controller → HTTP 409

### Ports (Interfaces)

| Interface | Location | Purpose |
|---|---|---|
| `CoffeeMachineCommandUseCase` | `application/port/in/` | register, produce, refill |
| `CoffeeMachineQueryUseCase` | `application/port/in/` | get machines, projections |
| `EventStore` | `application/port/out/` | append/load events |
| `CoffeeMachineRepository` | `application/port/out/` | load aggregate |

### REST API

| Method | Path | Description |
|---|---|---|
| GET | `/api/machines` | List all machines |
| POST | `/api/machines/{id}/produce-coffee` | `{coffeeType, user}` |
| POST | `/api/machines/{id}/refill` | `{beansToAdd, user}` |
| GET | `/api/projections/bean-levels` | Bean levels per machine |
| GET | `/api/projections/user-stats` | Cups per user, broken down by type |
| GET | `/api/projections/caffeine-alerts` | Users exceeding the caffeine threshold |

### Startup

`DataInitializer` registers 3 machines on startup: "OR Machine 1" (60 beans), "OR Machine 2" (60 beans), "Doctors' Lounge" (40 beans). Each emits a `MachineRegistered` event logged as JSON.

### Frontend

Static HTML served from `src/main/resources/static/`:
- `index.html` — landing page
- `operations.html` — command UI (dispense coffee, refill beans)
- `projections.html` — query UI (bean levels, user stats, caffeine alerts; auto-refreshes every 3 s)
