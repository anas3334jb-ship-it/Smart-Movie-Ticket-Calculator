# Smart Movie Ticket Calculator

A clean, robust, and beginner-friendly Python script that calculates movie ticket prices based on age, student status, and weekday promotions. 

This project demonstrates core programming logic using **pure conditional statements (`if-elif-else`)** and **arithmetic operators**, completely built **without using loops** while featuring advanced input validation to prevent runtime crashes.

---

### Features & Logic
* **Dynamic Pricing:** Standard ticket pricing with automated tier calculation.
* **Age-Based Discounts & Tiers:** 
  * Children (<= 12 years): **50% discount**
  * Seniors (>= 65 years): **30% discount**
  * Standard Adults (13 - 64 years)
* **Student Concession:** Special **20% discount** for students within the standard adult age bracket.
* **Weekday Special:** An additional **$2 off** applied automatically on weekdays (when weekday status is True).
* **Bulletproof Validation:** Handles invalid text entries, decimals, negative numbers, and incorrect boolean/student inputs gracefully without crashing.

---

### How to Run
1. Make sure you have Python installed on your system.
2. Copy the final script code into a file named `movie_ticket_calculator.py`.
3. Open your terminal or command prompt and run:
   ```bash
   python movie_ticket_calculator.py
