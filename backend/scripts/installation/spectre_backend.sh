#!/bin/bash
# SPDX-FileCopyrightText: © 2024 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later

# cloning enables backend development inside the container
# sparse-checkout means we only take what's necessary from the repo

# don't checkout HEAD when clone is complete
git clone --no-checkout https://github.com/jcfitzpatrick12/spectre.git
cd spectre

# Update the working directory only with the backend folder
git sparse-checkout set backend/src backend/pyproject.toml
# Update the working directory
# git checkout main
git checkout rest-api

# install dependencies (in editable mode)
cd backend
pip install --upgrade pip
pip install -e .

# install spectre-core via git clone for easier development
git clone https://github.com/jcfitzpatrick12/spectre-core.git
git checkout v0.0.5
cd spectre-core
pip install -e .
