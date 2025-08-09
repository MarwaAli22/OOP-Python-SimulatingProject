# 🐍 ITI Python Final Task

This repository contains the final project for the **Python course** as part of the **ITI scholarship program**.  
The project demonstrates **Object-Oriented Programming (OOP)** concepts in Python by simulating a simple **office management system** with employees, cars, and email validation.

---

## 📂 Project Structure

- **`story.py`**  
  Contains the main classes and logic:
  - `Person`: Base class for basic attributes and behaviors (sleep, eat, buy).
  - `Employee`: Inherits from `Person`, adds work-related methods (work, drive, refuel, send email).
  - `Office`: Manages employees (hire, fire, check lateness, reward, deduct).
  - `Car`: Simulates car behavior (run, stop) with fuel and velocity handling.

- **`email_validator.py`**  
  Contains the email validation function

---

## 🛠 Features & OOP Concepts

### 1. **Email Validation** (`email_validator.py`)
A standalone function `email_validation(email: str)` that:
- Checks if the email is not empty.
- Ensures the email starts with an alphabetic character.
- Prevents spaces in the email.
- Validates the format (e.g., `example@email.com`).

This function is **imported and used** inside the `Employee` class to ensure valid emails before assigning them to employees.

---

### 2. **Class: `Person`**
Base class representing a general person.
- **Attributes:** `name`, `money`, `mood`, `healthRate`
- **Methods:**
  - `sleep(hours)` → changes mood based on hours slept.
  - `eat(meals)` → adjusts health rate based on meal count.
  - `buy(item_count)` → deducts money when buying items.

---

### 3. **Class: `Employee` (inherits from `Person`)**
Represents an employee with extra attributes and behaviors.
- **Extra Attributes:** `id`, `car`, `email`, `salary`, `distanceToWork`, `targetHour`
- **Extra Methods:**
  - `work(hours)` → updates mood based on working hours.
  - `drive()` → uses the `Car` object to simulate driving.
  - `refuel(gasAmount)` → refuels the car.
  - `send_mail(body, to)` → sends an email if the employee has a valid email.

**Key OOP concept:**  
- **Inheritance** from `Person` to reuse common attributes and methods.
- **Composition**: Employee "has-a" `Car` object.

---

### 4. **Class: `Office`**
Manages a collection of employees.
- **Attributes:** `name`, `employees` (dictionary), `employees_num` (class variable)
- **Methods:**
  - `hire(...)` → adds a new employee.
  - `fire(id)` → removes an employee.
  - `get_all_employees()` / `get_employee(id)` → retrieves employee info.
  - `check_lateness(...)` → checks if an employee is late based on car speed and distance.
  - `reward(id, amount)` / `deduct(id, amount)` → updates employee money.
  - `change_emps_num(num)` → updates total number of employees (class method).

**Key OOP concepts:**  
- **Static methods** (`calculate_lateness`) for utility calculations.
- **Class methods** (`change_emps_num`) to modify class-level data.

---

### 5. **Class: `Car`**
Represents a car assigned to an employee.
- **Attributes:** `name`, `fuelRate`, `velocity`, `distance`
- **Methods:**
  - `run(distance, velocity)` → simulates driving until fuel or distance runs out.
  - `stop()` → stops the car.

**Key OOP concept:**  
- Encapsulation of car behavior inside its own class.

---

## 💡 OOP Principles Used
- **Encapsulation** → Grouping related attributes and methods inside classes.
- **Inheritance** → `Employee` inherits from `Person`.
- **Composition** → `Employee` has a `Car`.
- **Polymorphism** → Methods like `sleep()` and `work()` change behavior based on input.
- **Static & Class Methods** → For operations not tied to a specific object instance.

---
