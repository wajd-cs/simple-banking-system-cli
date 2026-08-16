<div align="center">

# Simple Banking System (CLI)

**A command-line banking application built in Python as an applied project for core Python and object-oriented programming fundamentals — encapsulation, inheritance, and polymorphism.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-4479A1?style=for-the-badge&logo=codeium&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-2EA44F?style=for-the-badge)

</div>

---

## Table of Contents
- [Overview](#overview)
- [Class Diagram](#class-diagram)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Skills Demonstrated](#skills-demonstrated)
- [Author](#author)

---

## Overview

A menu-driven, command-line banking system where users can create accounts, log in, and manage their money — deposits, withdrawals, balance checks, and a timestamped transaction history. Built specifically as an applied project to practice core Python fundamentals and object-oriented programming: encapsulated account data, class inheritance, and method overriding.

## Class Diagram

```mermaid
classDiagram
    class BankAccount {
        -float __balance
        -str __account_number
        -str __owner_name
        -list __transactions
        +deposit(amount)
        +withdraw(amount)
        +get_balance()
        +get_transactions()
    }
    class SavingAccount {
        +get_balance()
    }
    BankAccount <|-- SavingAccount
```

**How to read it:** `BankAccount` encapsulates all account data as private attributes (double-underscore name-mangled in Python) and only exposes them through controlled methods like `deposit()` and `withdraw()`, which validate input before changing the balance. `SavingAccount` inherits from `BankAccount` and overrides `get_balance()` — calling `super().get_balance()` to reuse the parent's logic while adding its own behavior on top, a direct example of inheritance and polymorphism.

## Key Features

- Create multiple accounts of two types: standard `BankAccount` or `SavingAccount`
- Login system that routes to a per-account menu
- Deposit and withdraw funds with validation (rejects zero, negative, or insufficient-balance operations)
- Timestamped transaction history logged for every deposit and withdrawal
- Defensive input handling — invalid (non-numeric) amounts are caught and re-prompted instead of crashing

## Tech Stack

`Python` · `Object-Oriented Programming` · `Exception Handling` · `CLI Design`

## Skills Demonstrated

- **Encapsulation** — protecting account data with private attributes and controlled access methods
- **Inheritance & Polymorphism** — `SavingAccount` extending `BankAccount` and overriding its behavior
- **Input Validation & Error Handling** — using `try`/`except` to gracefully handle invalid user input
- **State Management** — tracking multiple accounts and their transaction histories in memory
- **CLI/UX Design** — structuring a clear, menu-driven text interface for a multi-step user flow

## Author

**Wajd Sameer Al Luhaybi**
Computer Science Student | Data Analysis & Software Development

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/wajd-al-luhaibi-9194a1396)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:wajdalharbics@gmail.com)
