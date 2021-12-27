__author__ = "Wren J. R. (uberfastman)"
__email__ = "uberfastman@uberfastman.dev"

import logging
import warnings
from pathlib import Path

import pytest
from dotenv import load_dotenv

from yfpy.logger import get_logger
from yfpy.models import Game, StatCategories
from yfpy.utils import prettify_data

logger = get_logger(__name__)

# Suppress YahooFantasySportsQuery debug logging
logging.getLogger("yfpy.query").setLevel(level=logging.INFO)

# Ignore resource warnings from unittest module
warnings.simplefilter("ignore", ResourceWarning)

# load python-dotenv to parse environment variables
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

"""
TEST SAVING AND LOADING FANTASY GAME DATA
"""


@pytest.mark.integration
def test_get_all_yahoo_fantasy_game_keys(yahoo_query, yahoo_data, game_code, game_key, show_log_output):
    """Retrieve all Yahoo fantasy football game keys.
    """
    query_result_data = yahoo_data.save(game_code + "-game_keys",
                                        yahoo_query.get_all_yahoo_fantasy_game_keys)
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    loaded_result_data = yahoo_data.load(game_code + "-game_keys")
    if show_log_output:
        logger.info(f"{prettify_data(loaded_result_data)}\n----------\n")

    assert query_result_data == loaded_result_data


@pytest.mark.integration
def test_get_game_key_by_season(yahoo_query, season, game_key, show_log_output):
    """Retrieve specific game key by season.
    """
    query_result_data = yahoo_query.get_game_key_by_season(season=season)
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    assert query_result_data == game_key


@pytest.mark.integration
def test_get_current_game_info(yahoo_query, yahoo_data, data_dir, season, game_key, show_log_output):
    """Retrieve game info for current fantasy season.
    """
    query_result_data = yahoo_data.save("current-game-info", yahoo_query.get_current_game_info)
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    loaded_result_data = yahoo_data.load("current-game-info", Game)
    if show_log_output:
        logger.info(prettify_data(loaded_result_data))

    assert query_result_data == loaded_result_data


@pytest.mark.integration
def test_get_current_game_metadata(yahoo_query, yahoo_data, data_dir, season, game_key, show_log_output):
    """Retrieve game metadata for current fantasy season.
    """
    query_result_data = yahoo_data.save("current-game-metadata", yahoo_query.get_current_game_metadata)
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    loaded_result_data = yahoo_data.load("current-game-metadata", Game)
    if show_log_output:
        logger.info(prettify_data(loaded_result_data))

    assert query_result_data == loaded_result_data


@pytest.mark.integration
def test_get_game_info_by_game_id(yahoo_query, yahoo_data, data_dir, season, game_key, show_log_output):
    """Retrieve game info for specific game by id.
    """
    new_data_dir = data_dir / str(season)
    query_result_data = yahoo_data.save(str(game_key) + "-game-info",
                                        yahoo_query.get_game_info_by_game_id,
                                        params={"game_id": game_key}, new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    loaded_result_data = yahoo_data.load(str(game_key) + "-game-info", Game, new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(loaded_result_data))

    assert query_result_data == loaded_result_data


@pytest.mark.integration
def test_get_game_metadata_by_game_id(yahoo_query, yahoo_data, data_dir, season, game_key, show_log_output):
    """Retrieve game metadata for specific game by id.
    """
    new_data_dir = data_dir / str(season)
    query_result_data = yahoo_data.save(str(game_key) + "-game-metadata",
                                        yahoo_query.get_game_metadata_by_game_id,
                                        params={"game_id": game_key}, new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    loaded_result_data = yahoo_data.load(str(game_key) + "-game-metadata", Game, new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(loaded_result_data))

    assert query_result_data == loaded_result_data


@pytest.mark.integration
def test_get_league_key(yahoo_query, yahoo_data, data_dir, season, game_key, league_id, show_log_output):
    """Retrieve league key for selected league.
    """
    query_result_data = yahoo_query.get_league_key()
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    assert query_result_data == game_key + ".l." + league_id


@pytest.mark.integration
def test_get_game_weeks_by_game_id(yahoo_query, yahoo_data, data_dir, season, game_key, show_log_output):
    """Retrieve all valid weeks of a specific game by id.
    """
    new_data_dir = data_dir / str(season)
    query_result_data = yahoo_data.save(str(game_key) + "-game-weeks",
                                        yahoo_query.get_game_weeks_by_game_id,
                                        params={"game_id": game_key}, new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    loaded_result_data = yahoo_data.load(str(game_key) + "-game-weeks", new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(loaded_result_data))

    assert query_result_data == loaded_result_data


@pytest.mark.integration
def test_get_game_stat_categories_by_game_id(yahoo_query, yahoo_data, data_dir, season, game_key, show_log_output):
    """Retrieve all valid stat categories of a specific game by id.
    """
    new_data_dir = data_dir / str(season)
    query_result_data = yahoo_data.save(str(game_key) + "-game-stat_categories",
                                        yahoo_query.get_game_stat_categories_by_game_id,
                                        params={"game_id": game_key}, new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    loaded_result_data = yahoo_data.load(str(game_key) + "-game-stat_categories", StatCategories,
                                         new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    assert query_result_data == loaded_result_data


@pytest.mark.integration
def test_get_game_position_types_by_game_id(yahoo_query, yahoo_data, data_dir, season, game_key, show_log_output):
    """Retrieve all valid position types for specific game by id.
    """
    new_data_dir = data_dir / str(season)
    query_result_data = yahoo_data.save(str(game_key) + "-game-position_types",
                                        yahoo_query.get_game_position_types_by_game_id,
                                        params={"game_id": game_key}, new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    loaded_result_data = yahoo_data.load(str(game_key) + "-game-position_types", new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(loaded_result_data))

    assert query_result_data == loaded_result_data


@pytest.mark.integration
def test_get_game_roster_positions_by_game_id(yahoo_query, yahoo_data, data_dir, season, game_key, show_log_output):
    """Retrieve all valid roster positions for specific game by id.
    """
    new_data_dir = data_dir / str(season)
    query_result_data = yahoo_data.save(str(game_key) + "-game-roster_positions",
                                        yahoo_query.get_game_roster_positions_by_game_id,
                                        params={"game_id": game_key}, new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(query_result_data))

    loaded_result_data = yahoo_data.load(str(game_key) + "-game-roster_positions",
                                         new_data_dir=new_data_dir)
    if show_log_output:
        logger.info(prettify_data(loaded_result_data))

    assert query_result_data == loaded_result_data
