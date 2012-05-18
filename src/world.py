#! usr/bin/env python
# 
#  APM - Another Python Mud
#  Copyright (C) 2012  bdubyapee (BWP) p h i p p s b @ g m a i l . c o m
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
# Filename: world.py
# 
# File Description: Contains configuration data


import os

# Directory Configuration values
homeDir = 'c:\\apm'
dataDir = os.path.join(homeDir, 'data')
logDir = os.path.join(dataDir, 'log')
helpDir = os.path.join(dataDir, 'help')
playerDir = os.path.join(dataDir, 'players')
raceDir = os.path.join(dataDir, 'races')
areaDir = os.path.join(dataDir, 'areas')
commandDir = os.path.join(dataDir, 'commands')


# Generic Configurables
allownewCharacters = True
