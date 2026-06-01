# PCS Automation Library

A Python automation library for interacting with the **PCS Maintenance** application through keyboard-driven workflows.

This library uses PyAutoGUI to automate common maintenance tasks such as:

* Selecting models
* Managing options
* Updating pricing
* Adding paint and interior groups
* Navigating PCS menus
* Validating existing records

## Features

* Window focusing and activation
* Automated menu navigation
* Model selection and validation
* Option creation and maintenance
* Invoice and MSRP price management
* Paint group management
* Interior group management
* Reusable navigation helper functions

## Requirements

### Python Packages

Install the required dependencies:

```bash
pip install pyautogui pygetwindow pyperclip
```

### Supported Environment

* Windows
* PCS Maintenance application
* Keyboard shortcuts enabled in PCS

## Quick Start

```python
from pcs_automation import *

focus_pcs()

select_model("ABC", "2025")

select_option(
    option="PKG1",
    name="Premium Package",
    category="PKG",
    invoice=1200,
    msrp=1500
)
```

## Core Functions

### Window Management

#### `focus_pcs()`

Activates and maximizes the PCS Maintenance window.

```python
focus_pcs()
```

---

## Navigation Functions

### `refresh()`

Refreshes the current PCS screen.

```python
refresh()
```

### `back(i=1)`

Navigates back one or more screens.

```python
back()
back(3)
```

### `tab(i=1)`

Moves focus forward using the Tab key.

```python
tab()
tab(5)
```

### `close()`

Closes the current dialog window.

```python
close()
```

### `options()`

Opens the Options menu.

```python
options()
```

## Record Management

### `add()`

Triggers PCS Add action.

### `copy()`

Triggers PCS Copy action.

### `delete()`

Deletes the selected record.

### `ok()`

Confirms the current action.

## Model Functions

### `select_model(model_code, year, down=1)`

Selects a model and opens the Options screen.

#### Example

```python
select_model(
    model_code="ABC",
    year="2025"
)
```

### `check_model(model_code)`

Verifies that the currently selected model matches the supplied model code.

Returns:

```python
True
False
```

## Option Functions

### `select_option(option, name, category, invoice, msrp)`

Selects an option and creates it if it does not exist.

#### Example

```python
select_option(
    option="PKG1",
    name="Premium Package",
    category="PKG",
    invoice=1200,
    msrp=1500
)
```

### `add_option(option, name, category, invoice, msrp)`

Creates a new option record.

### `check_option(option, name, category, invoice, msrp)`

Verifies option existence and pricing.

## Pricing Functions

### `price()`

Opens the pricing screen.

### `check_price(invoice, msrp, down=1)`

Validates invoice and MSRP values.

### `add_price(invoice, msrp, correct_screen=False, differential=False)`

Creates a new price record.

#### Differential Pricing

```python
add_price(
    invoice=1000,
    msrp=1200,
    differential=True
)
```

### `add_price_compare(invoice, msrp)`

Compares existing pricing and updates when necessary.

## Paint Groups

### `paint_group()`

Opens the Paint Group screen.

### `add_paints(paints)`

Adds paint codes to the EXT1 paint group.

#### Example

```python
add_paints([
    "RED",
    "BLK",
    "WHT"
])
```

## Interior Groups

### `add_interiors(interiors)`

Adds interior codes to the INT1 interior group.

#### Example

```python
add_interiors([
    "LEATHER",
    "CLOTH"
])
```

## Notes

* PCS screen layouts and keyboard shortcuts must remain consistent.
* Timing delays are implemented using `time.sleep()` and may require adjustment depending on system performance.
* The library assumes the PCS Maintenance window title contains:

```text
PCS Maintenance
```

* Clipboard validation relies on `pyperclip`.

## Limitations

* Windows only.
* UI automation is sensitive to PCS layout changes.
* Running the automation while actively using the keyboard or mouse may interfere with execution.
* No built-in error handling for missing windows or unexpected dialogs.

## Future Improvements

* Configurable wait times
* Logging support
* Exception handling
* Screen-state validation
* Unit tests
* Configurable PCS window title detection
