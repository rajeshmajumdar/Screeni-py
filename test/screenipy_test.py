'''
 *  Project             :   Screenipy
 *  Author              :   Pranjal Joshi
 *  Created             :   29/04/2021
 *  Description         :   Automated Test Script for Screenipy
'''

import pytest
import sys
import os
import numpy as np
import pandas as pd
import configparser
import requests
import json

sys.path.append(os.path.abspath('../src'))
from screenipy import *
import classes.ConfigManager as ConfigManager


def test_if_release_version_increamented():
    r = requests.get("https://api.github.com/repos/pranjal-joshi/Screeni-py/releases/latest")
    last_release = float(r.json()['tag_name'])
    assert float(VERSION) > last_release

# Generate default configuration if not exist
def test_generate_default_config(mocker, capsys):
    mocker.patch('builtins.input',side_effect=['\n'])
    with pytest.raises(SystemExit):
        ConfigManager.tools.setConfig(ConfigManager.parser,default=True)
    out, err = capsys.readouterr()
    assert err == ''

def test_option_0(mocker):
    try:
        mocker.patch('builtins.input',side_effect=['0', TEST_STKCODE,'y'])
        main(testing=True)
        assert len(screenResults) == 1
    except StopIteration:
        pass

def test_option_1(mocker):
    try:
        mocker.patch('builtins.input',side_effect=['1','y'])
        main(testing=True)
        assert len(screenResults) > 0
    except StopIteration:
        pass

def test_option_2(mocker):
    try:
        mocker.patch('builtins.input',side_effect=['2','y'])
        main(testing=True)
        assert len(screenResults) > 0
    except StopIteration:
        pass

def test_option_3(mocker):
    try:
        mocker.patch('builtins.input',side_effect=['3','y'])
        main(testing=True)
        assert len(screenResults) > 0
    except StopIteration:
        pass

def test_option_4(mocker):
    try:
        mocker.patch('builtins.input',side_effect=['4','7','y'])
        main(testing=True)
        assert len(screenResults) > 0
    except StopIteration:
        pass

def test_option_5(mocker):
    try:
        mocker.patch('builtins.input',side_effect=['5','30','70'])
        main(testing=True)
        assert len(screenResults) > 0
    except StopIteration:
        pass

def test_option_6(mocker, capsys):
    try:
        mocker.patch('builtins.input',side_effect=[
            '5',
            str(ConfigManager.period),
            str(ConfigManager.daysToLookback),
            str(ConfigManager.duration),
            str(ConfigManager.minLTP),
            str(ConfigManager.maxLTP),
            str(ConfigManager.volumeRatio),
            str(ConfigManager.consolidationPercentage),
            'y',
            'y',
        ])
        with pytest.raises((SystemExit, configparser.DuplicateSectionError)):
            main(testing=True)
        out, err = capsys.readouterr()
        assert err == 0 or err == ''
    except StopIteration:
        pass

def test_option_7():
    ConfigManager.tools.getConfig(ConfigManager.parser)
    assert ConfigManager.duration != None
    assert ConfigManager.period != None
    assert ConfigManager.consolidationPercentage != None

def test_option_8(mocker):
    try:
        mocker.patch('builtins.input',side_effect=['8'])
        main(testing=True)
        assert len(screenResults) > 0
    except StopIteration:
        pass

def test_option_10(mocker, capsys):
    try:
        mocker.patch('builtins.input',side_effect=['10'])
        with pytest.raises(SystemExit):
            main(testing=True)
        out, err = capsys.readouterr()
        assert err == ''
    except StopIteration:
        pass

def test_ota_updater():
    try:
        OTAUpdater.checkForUpdate(proxyServer, VERSION)
        assert ("exe" in OTAUpdater.checkForUpdate.url or "bin" in OTAUpdater.checkForUpdate.url)
    except StopIteration:
        pass