#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#


import roslib; roslib.load_manifest('test_rosbag')

import rospy
from test_rosbag.msg import *

import rosbag

def generate_data():
    bag = rosbag.Bag("test/migrated_explicit_gen3.bag", "w")
    m = MigratedExplicit(None, 17, 58.2, "aldfkja", 82)
    bag.write("migrated_explicit", m, roslib.rostime.Time())
    bag.close()

    bag = rosbag.Bag("test/migrated_implicit_gen3.bag", "w")
    m = MigratedImplicit(None, MigratedExplicit(None, 17, 58.2, "aldfkja", 82), "kljene", 16.32, 34)
    bag.write("migrated_implicit", m, roslib.rostime.Time())
    bag.close()

    bag = rosbag.Bag("test/migrated_mixed_gen3.bag", "w")
    m = MigratedMixed(None, MigratedImplicit(None, MigratedExplicit(None, 17, 58.2, "aldfkja", 82), "kljene", 16.32, 34), 59)
    bag.write("migrated_mixed", m, roslib.rostime.Time())
    bag.close()

    bag = rosbag.Bag("test/partially_migrated_gen3.bag", "w")
    m = PartiallyMigrated(40, MigratedExplicit(None, 17, 58.2, "aldfkja", 82), "radasdk")
    bag.write("partially_migrated", m, roslib.rostime.Time())
    bag.close()

    bag = rosbag.Bag("test/renamed_gen3.bag", "w")
    m = Renamed3(2.17, [8, 2, 5, 1])
    bag.write("renamed", m, roslib.rostime.Time())
    bag.close()

    bag = rosbag.Bag("test/converged_gen3.bag", "w")
    m = Converged([1.2, 3.4, 5.6, 7.8], [SimpleMigrated(11), SimpleMigrated(22), SimpleMigrated(33), SimpleMigrated(44)])
    bag.write("converged", m, roslib.rostime.Time())
    bag.close()
        
if __name__ == '__main__':
    generate_data()
