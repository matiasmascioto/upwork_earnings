"""
Upwork Earnings
"""

import logging.config
import pandas as pd
import yaml

from datetime import datetime
from pathlib import Path

from helpers.helper_functions import timing


@timing
def main_function(config, logger):
    """ Main function """
    logger.info("Main function")

    # Read input data
    df = pd.read_csv(**config["input"])

    # Data exploration
    logger.info(f"DataFrame shape: {df.shape}")

    # Delete withdrawal rows
    row_filter = ~df["Type"].isin(["Withdrawal", "Withdrawal Fee"])
    df = df.loc[row_filter, :]

    # Re-sample and export results
    folder_path = Path(config["output"]["folder_path"])
    for rule, period in config["periods"]:
        file_path = Path(folder_path, f"upwork_by_{period}.csv")
        resampled_df = df.resample(rule).sum()
        resampled_df.to_csv(file_path, **config["output"]["csv"])

    logger.info("Script finished")


if __name__ == "__main__":
    config = yaml.load(open("upwork_earnings.yml"))

    config["logs"]["handlers"]["file"]["filename"] = datetime.now().strftime(
        config["logs"]["handlers"]["file"]["filename"]
    )
    logging.config.dictConfig(config["logs"])
    logger = logging.getLogger(__name__)

    try:
        main_function(config, logger)
    except Exception:
        logger.exception("Exception occurred", exc_info=True)
