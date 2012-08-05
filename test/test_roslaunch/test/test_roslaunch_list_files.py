#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2011, Willow Garage, Inc.
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
# Revision $Id: test_roslaunch_command_line_online.py 6411 2009-10-02 21:32:01Z kwc $

PKG = 'test_roslaunch'
NAME = 'test_roslaunch_list_files'
import roslib; roslib.load_manifest(PKG)

import os
import signal
import sys 
import time
import unittest
import roslib.packages

import rostest

from subprocess import Popen, PIPE, check_call, call

class TestListFiles(unittest.TestCase):

    def setUp(self):
        pass

    def test_list_files(self):
        cmd = 'roslaunch'

        # check error behavior
        p = Popen([cmd, '--files'], stdout = PIPE)
        o, e = p.communicate()
        self.assert_(p.returncode != 0, "Should have failed w/o file argument. Code: %d" % (p.returncode))

        d = os.path.join(roslib.packages.get_pkg_dir('test_roslaunch'), 'test', 'xml')
        
        p = Popen([cmd, '--files', 'test_roslaunch', 'test-valid.xml'], stdout = PIPE)
        o, e = p.communicate()
        self.assert_(p.returncode == 0, "Return code nonzero for list files! Code: %d" % (p.returncode))
        self.assertEquals(os.path.join(d, 'test-valid.xml'), o.strip())

        print "check 1", o
        
        p = Popen([cmd, '--files', 'test_roslaunch', 'test-env.xml'], stdout = PIPE)
        o, e = p.communicate()
        self.assert_(p.returncode == 0, "Return code nonzero for list files! Code: %d" % (p.returncode))
        self.assertEquals(set([os.path.join(d, 'test-env.xml'), os.path.join(d, 'test-env-include.xml')]),
                          set([x.strip() for x in o.split() if x.strip()]))

        print "check 2", o

if __name__ == '__main__':
    rostest.run(PKG, NAME, TestListFiles, sys.argv)
