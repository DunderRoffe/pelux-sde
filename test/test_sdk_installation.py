#
# Copyright (C) 2017 Pelagicore AB
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0
#

import pytest
import os

@pytest.fixture(scope="class")
def vagrant():
    os.system("NO_GUI=1 vagrant up")
    yield
    os.system("vagrant destroy -f")

@pytest.mark.usefixtures("vagrant")
class Test(object):

    def test_is_a_sane_ubuntu_system(self):
        self.__run_test_script_inside_vm("check_is_ubuntu.py")

    PATH_ON_VM_TO_TEST_SCRIPTS = "/vagrant/test/scripts"
    def __run_test_script_inside_vm(self, script_name, script_args=""):
        script_exec_result = os.system("vagrant ssh -c \"python3 {}/{} {}\"".format(self.PATH_ON_VM_TO_TEST_SCRIPTS,
                                                                                    script_name,
                                                                                    script_args))
        assert script_exec_result == 0
