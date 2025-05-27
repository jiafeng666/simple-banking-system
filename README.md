# simple-banking-system

## Features
- Users can create a new bank account with a name and starting balance 
- Users can deposit money to their accounts 
- Users can withdraw money from their accounts 
- Users are not allowed to overdraft their accounts 
- Users can transfer money to other accounts in the same banking system 
- Save and load system state to CSV 

## Setup & Run

1. Clone the repository (or copy files):
```bash
git clone https://github.com/yourusername/simple-banking-system.git
cd simple-banking-system
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
venv\\Scripts\\activate   # Windows
```

3. Run tests:
```bash
python -m unittest discover -v
```