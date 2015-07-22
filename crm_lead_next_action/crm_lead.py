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
from osv import osv, fields

class CRMLead(osv.osv):
    _inherit = "crm.lead"
    # make sure we have date_action and title_action in the CRMLead
    _columns = {
       'date_action': fields.date('Next Action Date'),
       'title_action': fields.char('Next Action', size=64),
    }

CRMLead()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: