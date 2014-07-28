# Copyright (c) 2014 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mock
import unittest

from oslo.config import cfg

from cdn.manager.default import driver
from cdn.manager.default import services


class DefaultManagerDriverTests(unittest.TestCase):
    @mock.patch('cdn.storage.base.driver.StorageDriverBase')
    @mock.patch('cdn.provider.base.driver.ProviderDriverBase')
    def setUp(self, mock_storage, mock_provider):
        conf = cfg.ConfigOpts()
        self.driver = driver.DefaultManagerDriver(conf,
                                                  mock_storage,
                                                  mock_provider)

    def test_services_controller(self):
        sc = self.driver.services_controller

        self.assertIsInstance(sc, services.DefaultServicesController)
