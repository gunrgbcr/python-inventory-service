# E-Commerce Inventory Manager

An object-oriented inventory and order management system in Python, written as a course project ("Matamazon"). It registers customers and suppliers, keeps a product catalog, places and removes orders with stock checks, and saves and reloads system state, all driven by a command-line script.

## Features
* **Entity Management:** Registers customers and suppliers with type checks and non-negative integer IDs, and rejects a duplicate ID within each type. A customer, supplier or product cannot be removed while an order still references it.
* **Product Catalog:** Adds a product only for a registered supplier, and updates an existing product (name, price, stock) only when the supplier ID matches. Prices and stock must be non-negative.
* **Order Processing:** Rejects an order for an unknown product, an unknown customer, or more units than are in stock. Otherwise it reduces stock, computes the total as quantity × unit price, and assigns sequential order IDs starting at 1. Removing an order returns its quantity to stock.
* **Product Search:** Case-insensitive substring match on product name, with an optional maximum price (inclusive). Out-of-stock items are excluded and results are sorted by price, ascending.
* **Data Persistence:**
    * Exports customers, suppliers and products to a text file, one object per line in its printed form, and reloads a system from such a file. Orders are not included.
    * Exports all orders as JSON, grouped by the city of the supplier of each ordered product.

---

## Usage
```bash
python3 matamazon.py -l <matamazon_log> [-s <matamazon_system>] [-o <output_file>] [-os <out_matamazon_system>]
```
* `-l` (required): log file of commands, one per line: `register`, `add` / `update`, `order`, `remove`, `search`.
* `-s`: system file to load before the log is processed.
* `-o`: file for the JSON order export (printed to standard output if omitted).
* `-os`: file to export the final system state to.

## Requirements
* Python 3.6+ (standard library only; no third-party dependencies).
