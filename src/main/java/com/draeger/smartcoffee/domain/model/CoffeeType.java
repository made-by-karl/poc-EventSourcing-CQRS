package com.draeger.smartcoffee.domain.model;

public enum CoffeeType {
    ESPRESSO(10),
    DOUBLE_ESPRESSO(20),
    AMERICANO(5),
    HOT_WATER(0);

    private final int beansRequired;

    CoffeeType(int beansRequired) {
        this.beansRequired = beansRequired;
    }

    public int getBeansRequired() {
        return beansRequired;
    }
}
