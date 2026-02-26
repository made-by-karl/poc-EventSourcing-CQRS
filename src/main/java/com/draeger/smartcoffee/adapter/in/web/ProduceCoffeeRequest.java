package com.draeger.smartcoffee.adapter.in.web;

import com.draeger.smartcoffee.domain.model.CoffeeType;

public record ProduceCoffeeRequest(CoffeeType coffeeType, String user) {
}
