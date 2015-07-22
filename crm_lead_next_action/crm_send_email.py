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
from tools.translate import _

class CRMSendEmail(osv.osv_memory):
    _inherit = "mail.compose.message"
    _columns = {
       'date_action': fields.date('Next Action Date'),
       'title_action': fields.char('Next Action', size=64),
    }

    def send_mail(self, cr, uid, ids, context=None):
        """ Override to add write date_action and title_action """
        if context is None:
            context = {}

        hist_obj = self.pool.get('mail.message')
        to_return = super(CRMSendEmail, self).send_mail(cr, uid, ids, context=context)

        if context.get('default_model') == 'crm.lead' and context.get('default_res_id'):
            model = context.get('default_model')
            case_pool = self.pool.get(model)
            res_id = context.get('default_res_id')

            for obj in self.browse(cr, uid, ids, context=context):
                if context.get('mail', 'new') not in ['new', 'forward']:
                    hist = hist_obj.browse(cr, uid, res_id, context=context)
                    res_id = hist.res_id
                    model = hist.model
                case = case_pool.browse(cr, uid, res_id, context=context)
                if obj.date_action:
                    values = {'date_action': obj.date_action}
                    case_pool.write(cr, uid, [case.id], values, context=context)
                if obj.title_action:
                    values = {'title_action': obj.title_action}
                    case_pool.write(cr, uid, [case.id], values, context=context)

        return to_return

CRMSendEmail()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: