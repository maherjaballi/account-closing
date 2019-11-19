# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_account_cutoff_base = fields.Boolean(string='Account Cutoff Base',
        help='This module contains models, fields and menu entries that are used by \n'
              'other cut-off modules ; it doesnt provide useful features by itself. You \n'
              'need to install other cut-off modules to get the useful features: \n'
              '* the module *account_cutoff_prepaid* will manage prepaid cut-offs based on \n'
               ' start date and end date, \n'
              '* the module *account_cutoff_accrual_picking* will manage the accruals based \n'
               ' on the status of the pickings. \n'
             '-This installs the module account_cutoff_base.')
    
    module_account_cutoff_prepaid = fields.Boolean(string='Account Cutoff Prepaid',
        help='This module allows you to easily compute the prepaid revenue and prepaid expenses and to generate \n'
               'the related cutoff journal items. It uses the **Start Date** and **End Date** fields of journal entries \n' 
               '(copied from the same fields of invoice lines). \n')

    module_account_invoice_start_end_dates = fields.Boolean(string='Account Invoice Start End Dates',
        help='This module adds the fields *Start Date* and *End Date* on invoice lines. When you validate the invoice,  \n'
              'the information is copied from invoice lines to account move lines (if you enabled the grouping option on the related journal,  \n'
              'Odoo will not group invoice lines that have different start/end dates). \n'
              'It also adds an option *Must Have Start and End Dates* on the product form (in the *Accounting* tab) ; if you enable this option, you  \n'
              'will get an error message if you try to validate an invoice that constains such a product on one of its lines and doesnt have start/ \n'
              'end dates on that line. \n'
              'If you use this module, you may also be interested in 2 other modules: \n'

             ' * the module *sale_start_end_dates* from the sale-workflow OCA project: this module adds the fields *Start Date* and *End Date* on sale \n'
             'order lines and copies the information from sale order lines to invoice lines. \n'

             'the module *account_cutoff_prepaid* '
              '(same repository): this module allows easy computation of prepaid expenses and prepaid revenues. \n')
    
    module_account_multicurrency_revaluation = fields.Boolean(string='Account Multicurrency Revaluation',
        help='This module was written to extend the functionality of the accounting module to \n'
              'support the multicurrency and to allow you to generate automatically \n'
              'revaluation journal entries. \n'
             '-This installs the module account_multicurrency_revaluation.')


   