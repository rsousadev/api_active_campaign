#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""      
    Documento de integração Python API's
    
"""

__author__ = "Ricardo Sousa"
__copyright__ = "Free"
__credits__ = "Ricardo De Maria Sousa"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ricardo Sousa"
__email__ = "ricardo.dmsousa@gmail.com"
__status__ = "Production"

import re
import sys
import time
from datetime import datetime
from granatum import granatum
from active_campaign import contacts
from e_notas import emitir_nfe
from memberkit import adiciona_um_aluno

nome = 'Ricardo Sousa'
num_tel = '123123132121'
email = 'ricardo.dmsousa@gmail.com'


nome = re.sub(r"(\w)([A-Z])", r"\1 \2", nome)


"""Inserir contato Active Campaign """

inserir_contato = contacts.Contact()
inserir_contato.insert_contact_in_list(inserir_contato.insert_contact(email_validar, nome, num_tel))
inserir_contato.insert_tag_contact()

