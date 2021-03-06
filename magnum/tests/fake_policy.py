# Copyright (c) 2012 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


policy_data = """
{
    "context_is_admin":  "role:admin",
    "admin_or_owner":  "is_admin:True or project_id:%(project_id)s",
    "default": "rule:admin_or_owner",
    "admin_api": "rule:context_is_admin",

    "bay:create": "",
    "bay:delete": "",
    "bay:detail": "",
    "bay:get": "",
    "bay:get_all": "",
    "bay:update": "",

    "baymodel:create": "",
    "baymodel:delete": "",
    "baymodel:detail": "",
    "baymodel:get": "",
    "baymodel:get_all": "",
    "baymodel:update": "",

    "cluster:create": "",
    "cluster:delete": "",
    "cluster:detail": "",
    "cluster:get": "",
    "cluster:get_all": "",
    "cluster:update": "",

    "clustertemplate:create": "",
    "clustertemplate:delete": "",
    "clustertemplate:detail": "",
    "clustertemplate:get": "",
    "clustertemplate:get_all": "",
    "clustertemplate:update": "",
    "clustertemplate:publish": "",

    "certificate:create": "",
    "certificate:get": "",

    "magnum-service:get_all": "",
    "stats:get_all": ""
}
"""
