# Pharmacy Management System

## Overview

The **Pharmacy Management System** is a Python-based desktop application that helps manage pharmacy inventory, sales, and user authentication. It provides a graphical user interface (GUI) built using `Tkinter` and utilizes `SQLite3` as the database. The system allows users to add, update, delete, and search medicines while maintaining user authentication for secure access.

## Features

### Pharmacy Management System (med.py)

- Add, Update, Delete, and Search medicines
- Stores medicine information including reference number, company name, type, expiry date, price, and quantity
- SQLite3 database integration
- Real-time data fetching and display
- Interactive GUI with `Tkinter` and `PIL` for image handling

### User Authentication (auth.py / login system)

- Secure user sign-up and sign-in functionality
- Uses `SHA-256` password hashing for security
- Additional password protection for extra security layer
- Stores user credentials in `datasheet.json`

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- Required Python libraries:
  ```bash
  pip install tkinter pillow sqlite3 json hashlib
  ```

### Clone the Repository

```bash
git clone https://github.com/yourusername/pharmacy-management.git
cd pharmacy-management
```

### Running the Application

1. Run the authentication system (Sign In/Sign Up):
   ```bash
   python check2.py
   ```
2. After signing in, the pharmacy management system will open automatically.
   ```bash
   python med.py
   ```

## Database Structure (SQLite3)

The `pharmacy.db` database contains tables like:

- `pharma`
  - `Ref_no` (Primary Key)
  - `Med_name`
  - `Company_name`
  - `Type_med`
  - `Lot_no`
  - `Issue_date`
  - `Exp_date`
  - `Uses`
  - `Side_effects`
  - `Warning`
  - `Dosage`
  - `Price`
  - `Quantity`

## Usage

1. **Sign Up:** Register a new user.
2. **Sign In:** Log in with registered credentials.
3. **Manage Medicines:** Add, update, delete, and search medicines.
4. **Security:** Additional password required for access.


## Future Enhancements

- Implement role-based access control (Admin, Pharmacist, Customer)
- Add sales tracking and invoice generation
- Cloud-based database integration
- Mobile app version



