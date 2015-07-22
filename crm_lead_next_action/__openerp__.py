# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Yannick Vaucher (Camptocamp)
#    Contributor:
#    Copyright 2011 Camptocamp SA
#    Donors:
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Next action in leads',
    'version': '1.0',
    'maintainer': 'Camptocamp',
    'category': 'Generic Modules/Others',
    'complexity': 'easy',
    'description':
'''
Adding next action fields to make it easier to use in crm

This module adds:

- Next action and next action fields in crm lead
- Next action and next action fields in crm email wizard
''',
    'author': 'Camptocamp',
    'website': 'http://www.camptocamp.com',
    'depends' : ['base','crm'],
    'data' : [
        'crm_lead_view.xml',
        'crm_send_email_view.xml'
    ],
    'demo' : [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3'
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: