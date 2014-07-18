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

import boto

from cdn.provider import base


class ServiceController(base.ServiceBase):

    def __init__(self, driver):
        super(ServiceController, self).__init__()

        self.client = driver.client
        self.current_customer = self.client.get_current_customer()

        self.provider_resp = base.ProviderResponse("cloudfront")

    def update(self, service_name, service_json):
        print("update services")

    def create(self, service_name, service_json):
        try:
            for origin in service_json["origins"]:
                # Create the origins for this domain:
                aws_origin = self.origin.CustomOrigin(
                    dns_name=origin["origin"],
                    http_port=origin["port"],
                    https_port=origin["ssl"],
                    origin_protocol_policy="match-viewer")
                distribution = self.client.create_distribution(
                    origin=aws_origin,
                    enabled=True,
                    comment='Comment')

            return self.provider_resp.created(distribution.id)

    except cloudfront.exception:
            return self.provider_resp.failed("failed to create service")
        except Exception:
            return self.provider_resp.failed("failed to create service")

    def delete(self, distribution.id):
        try:
            self.client.delete_distribution(distribution.id)

            return self.provider_resp.deleted(distribution.id)
        except Exception:
            return self.provider_resp.failed("failed to delete service")
