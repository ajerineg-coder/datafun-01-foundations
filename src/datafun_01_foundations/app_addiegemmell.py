"""app_addiegemmell.py - Project script.

Author: Addie Gemmell
Date: 2026-01

  Practice key Python skills related to:
    - imports
    - logging
    - variables
    - type hints
    - global constants
    - f-strings
    - functions
    - main function
    - conditional execution guard

OBS:
  This is your file to practice and customize.
  Find the TODO comments, and as you complete each task, remove the TODO note.

"""
# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
import statistics
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("P01", level="INFO")


# === DECLARE GLOBAL CONSTANTS ===

# All these global variables are CONSTANT, they do NOT change when the program runs.
# By convention, constants are named in UPPERCASE_WITH_UNDERSCORES.
# The following illustrates variables that hold these common types:
#    str, int, float, bool, list of strings.
# `Final` is added to indicate these variables should not be reassigned.
# Examples:

MY_ANALYTICS_COMPANY: Final[str] = "DataFun Analytics"
MY_EMPLOYEE_COUNT: Final[int] = 150
MY_UNDERSTANDING: Final[str] = "Getting there slowly"
MY_STRESS_LEVEL: Final[int] = 10
MY_HUNGER_LEVEL: Final[float] = 7.4
HAVING_FUN: Final[bool] = True
FAVORITE_FOODS: Final[list[str]] = ["Pizza", "Sandwiches", "Sushi"]

# See the other file for examples.

# REQ: Strings must be in quotes and items are separated by commas,
# REQ: The list is wrapped in square brackets. (See the other file for examples.)


# === DECLARE A FUNCTION TO FORMAT THE INFORMATION ===


def get_summary() -> str:
    """Get a formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string (starts with f and wrapped in triple quotes).
    """
    # all of the global variables you declared above, each on its own line,
    # labeled clearly with descriptive text.
    # See the other file for an example. Remember to start the string with an f!
    summary: str = f"""
    Custom Information:
        Company name: {MY_ANALYTICS_COMPANY}
        Employee count: {MY_EMPLOYEE_COUNT}
        My understanding: {MY_UNDERSTANDING}
        My stress level: {MY_STRESS_LEVEL}
        My hunger level: {MY_HUNGER_LEVEL}
        Having fun: {HAVING_FUN}
        Favorite foods: {FAVORITE_FOODS}

    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DECLARE A FUNCTION TO FORMAT DESCRIPTIVE STATISTICS ===


def get_statistics() -> str:
    """Get a formatted summary showing descriptive statistics.

    Arguments: None (nothing is passed in the parentheses).

    Returns: - a formatted multi-line string.
    """
    # Initialize sample data - snowfall measurements in inches.
    # REQ: Vary ONE of the sample data values.
    # See how the statistics change when you do.

    snowfall_inches: list[float] = [2.5, 3.5, 5.8, 5.5, 6.5]

    total: float = sum(snowfall_inches)
    count: int = len(snowfall_inches)

    minimum: float = min(snowfall_inches) if count > 0 else 0.0
    maximum: float = max(snowfall_inches) if count > 0 else 0.0

    average: float = statistics.mean(snowfall_inches) if count > 0 else 0.0
    standard_deviation: float = statistics.stdev(snowfall_inches) if count > 1 else 0.0

    summary: str = f"""
    Descriptive Statistics for Snowfall (inches):
        Total snowfall: {total:.2f} inches
        Count of measurements: {count}
        Minimum snowfall: {minimum:.2f}
        Maximum snowfall: {maximum:.2f}
        Average snowfall: {average:.2f} inches
        Standard deviation: {standard_deviation:.2f}
    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None.

    Returns: None.
    """
    # Log a header for the application.
    LOG.info("=================")
    log_header(LOG, "Foundations of Professional Python")
    LOG.info("=================")

    # Log start of main processing.
    LOG.info("START main()..................")

    # Call functions to get formatted strings and log them.
    summary: str = get_summary()
    LOG.info(summary)

    stats: str = get_statistics()
    LOG.info(stats)

    # Log end of main processing.
    LOG.info("END main()..................")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# OBS: This is just standard Python boilerplate.

if __name__ == "__main__":
    main()
