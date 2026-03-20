# Smart Coffee — OR Coffee Machine

A demo application illustrating **Event Sourcing** and **CQRS** in a medical device context:
a smart coffee machine in an Operating Room that must document every dispensing event for compliance.

## Requirements

- Java 24
- Docker (for the database)

## Starting the application

```bash
./gradlew bootRun
```

The application starts on **http://localhost:8080**.

On startup, three machines are registered automatically and their `MachineRegistered` events
are logged as JSON:

```
INFO  EVENT: {"eventType":"MachineRegistered","aggregateId":"...","name":"OR Machine 1","initialBeans":60,...}
INFO  EVENT: {"eventType":"MachineRegistered","aggregateId":"...","name":"OR Machine 2","initialBeans":60,...}
INFO  EVENT: {"eventType":"MachineRegistered","aggregateId":"...","name":"Doctors' Lounge","initialBeans":40,...}
```

## Using the application

Open **http://localhost:8080** for the landing page, which links to both UIs.

### Coffee Terminal — `http://localhost:8080/operations.html`

The command side. Select a machine, enter a username, pick a coffee type, and click **Dispense Coffee**.
Each dispense appends a `CoffeeProduced` event to the log:

```
INFO  EVENT: {"eventType":"CoffeeProduced","machineId":"...","coffeeType":"DOUBLE_ESPRESSO","user":"mueller","beansConsumed":2,"beansAvailableAfter":58,...}
```

Use the **Refill Beans** section to replenish a machine. If a machine runs out of beans,
the terminal shows an error and the API returns `409 Conflict`.

### Controlling Dashboard — `http://localhost:8080/projections.html`

The query side. Refreshes automatically every 3 seconds.

| Section | What it shows |
|---|---|
| Bean Levels | Current bean count and total cups produced per machine |
| User Statistics | Total cups and breakdown by coffee type per user |
| Caffeine Alert | Warning banner when a user has had ≥ 3 Double Espressos in the last 2 hours |

### Reset the database for a clean start

To reset the data remove the postgres volume. The application will rebuild the database with initial values.

```bash
docker compose down -v && docker compose up -d
```

## Architecture

The application follows **Hexagonal Architecture (Ports & Adapters)**:

- **Domain** — `CoffeeMachine` aggregate, `DomainEvent` hierarchy, business rules
- **Application** — use case interfaces (ports), command/query services
- **Adapters** — REST controllers (in), database event store (out)

Every state change is stored as an immutable event (`CoffeeProduced`, `BeansRefilled`, …).
The aggregate is always rebuilt by replaying these events.

```
Command → load events → reconstitute aggregate → handle → append new event
Query   → scan event stream → build projection on the fly
```

## REST API

| Method | Path | Description |
|---|---|---|
| `GET` | `/api/machines` | List all machines |
| `POST` | `/api/machines/{id}/produce-coffee` | Dispense a coffee |
| `POST` | `/api/machines/{id}/refill` | Refill beans |
| `GET` | `/api/projections/bean-levels` | Bean level projection |
| `GET` | `/api/projections/user-stats` | User statistics projection |
| `GET` | `/api/projections/caffeine-alerts` | Active caffeine alerts |

**Produce coffee request body:**
```json
{ "coffeeType": "DOUBLE_ESPRESSO", "user": "smith" }
```

**Refill request body:**
```json
{ "beansToAdd": 20, "user": "bob" }
```

## Debug mode

Start with remote debugging enabled on port 5005:

```bash
DEBUG=true ./gradlew bootRun
```

## Running tests

```bash
./gradlew test
```

## Generating the presentation

The `presentation/` directory contains the slide deck "Facts over State" (`facts-over-state.pptx`).
You can regenerate it in two ways:

### Option A: Docker (no Python installation needed)

**Prerequisites:** Docker

```bash
cd presentation
docker build -t smart-coffee-slides .
docker run --rm -v "$(pwd):/presentation" smart-coffee-slides
```

### Option B: Run directly with Python

**Prerequisites:** Python 3, `python-pptx` package

```bash
pip install python-pptx
python3 presentation/scripts/generate_presentation.py
```
