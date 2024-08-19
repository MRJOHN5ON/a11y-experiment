# a11y-experiment
# Selenium Accessibility Testing

## Overview

This repository provides a setup for running Selenium-based accessibility tests on a webpage. It includes a script that automates interactions with a webpage and performs accessibility checks using `axe-selenium-python`.

## Prerequisites

- Python 3
- pip (Python package installer)

## Setup Instructions

1. **Create a Virtual Environment**

   Open your terminal and run:
   ```bash
   python3 -m venv env
2. **Activate the Virtual Environment**

Activate the virtual environment with:

```bash
source env/bin/activate
```
3. **Install Dependencies**

With the virtual environment activated, install the required packages:

```bash
pip install selenium
pip install webdriver_manager
pip install axe-selenium-python
```

## Script
The repository includes a script for performing accessibility checks. Save the code to a file named `ally.py`


## Running the Script
Run the script using:

```bash

python ally.py
```
## Main Violation
The following key accessibility issue was found:

**Color Contrast**
<br>
- Description: Ensures the contrast between foreground and background colors meets WCAG 2 AA contrast ratio thresholds.
- Issue: An element on the page has insufficient color contrast. The foreground color (#ffffff) and background color (#ffa370) have a contrast ratio of 1.95, while the expected ratio is 4.5:1.
- Impact: Serious
- Help: Color Contrast Guidelines
- "HelpUrl": "https://dequeuniversity.com/rules/axe/3.1/color-contrast?application=axeAPI"
- Example: The "Submit" button does not meet the required contrast ratio. Here's the HTML for the problematic element:
```html

<button type="submit" class="section__submit-btn">Submit</button>
```
Contribution
I’m interested in improving this testing setup. If you have suggestions or can enhance the script to cover incomplete checks or address the main violations, please fork this repository and submit a pull request.
