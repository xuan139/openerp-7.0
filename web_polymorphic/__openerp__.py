# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Augustin Cisterne-Kaas <augustin.cisterne-kaas@elico-corp.com>
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
{'name': 'Web Polymorphic',
 'version': '0.1',
 'category': 'Web',
 'depends': ['web'],
 'author': 'Elico Corp',
 'license': 'AGPL-3',
 'website': 'https://www.elico-corp.com',
 'description': """
Add a new widget named "polymorphic"
The polymorphic field allow to dynamically store an id linked to any model in
OpenERP instead of the usual fixed one in the view definition

E.g:

<field name="model" invisible="1" />
<field name="object_id" widget="polymorphic" polymorphic="model" />
""",
 'js': [
     'static/src/js/view_form.js'
 ],
 'installable': True,
 'application': False}
