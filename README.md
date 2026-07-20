# 📦 Smart Inventory

Smart Inventory is a personal inventory management system currently under active development. The goal of the project is to evolve from a simple console application into a complete bakery management solution with a modern architecture, persistent data storage, and eventually a mobile application.

The project follows a version-based roadmap, where each release introduces new features while maintaining clean, modular, and scalable code.

---

## 🚀 Current Version

**Version:** v0.3

This version introduces persistent JSON storage, improved business logic, duplicate product detection, product editing, and a more robust inventory management workflow while maintaining a clean Object-Oriented architecture.

---

## ✨ Features

### 📦 Product Management

- ➕ Create new products
- ✏️ Modify existing products
- 🔍 Search products by name
- 📋 Display complete inventory
- 🚫 Duplicate product detection
- 🏷️ Automatic internal code generation
- 💰 Automatic suggested sale price for purchased products

### 📊 Inventory Management

- 📦 Register stock entries
- 💰 Register product sales
- 📉 Automatic stock updates
- 📈 Inventory value calculation

### 🗂️ Product Categories

- 🛒 Purchased products (barcode)
- 🏭 Manufactured products (internal code)
- ⚖️ Loose products (unit or kilogram)

### ✅ Validations

- Required fields
- Positive values
- Stock validation
- Valid product categories
- Valid unit types
- Duplicate barcode detection
- Duplicate product detection
- Cost cannot exceed sale price

### 💾 Persistence

- JSON storage
- Automatic save on exit
- Automatic load on startup

### 🧱 Architecture

- Object-Oriented Programming (OOP)
- Service layer
- Separation of responsibilities
- Modular project structure
- Prepared for future SQLite migration

---

## 🛠️ Technologies

- Python 3
- Object-Oriented Programming (OOP)
- JSON

---

## 📁 Project Structure

```text
Bakery_management_system/
│
├── docs/
│   └── design.md
│
├── src/
│   ├── config/
│   ├── core/
│   ├── models/
│   ├── services/
│   ├── storage/
│   └── ui/
│
├── tests/
│
├── .gitignore
└── README.md
```

---

## 🎯 Project Roadmap

- ✅ **v0.1** — Console application using OOP
- ✅ **v0.2** — JSON data persistence
- ✅ **v0.3** — Business logic improvements, duplicate detection and product editing
- 🔄 **v0.4** — SQLite database integration
- 🎯 **v1.0** — First complete inventory management system
- 📱 **v2.0** — Mobile-friendly application
- 🤖 **v3.0** — AI-powered features and automation

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📌 Long-Term Vision

Smart Inventory is intended to become a complete management system for a small bakery business, including inventory control, sales, purchasing, pricing, and business management tools.

The project is being developed incrementally, with each version serving as the foundation for the next. The next major milestone is replacing JSON persistence with SQLite while keeping the existing architecture intact.

---

## 👨‍💻 Author

Created by **Tor3k** as a long-term personal software development project.